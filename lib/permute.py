"""Whole-procedure permutation test.

The register permutes DATA INSIDE a test. That measures whether one cell beats
chance. It does not measure what actually sinks a research programme: that the
cell was CHOSEN from many. This module puts the choosing inside the null.

    You hand it the entire search. It reruns the entire search on permuted
    data B times. The p-value is the rank of your real best against B best-of-
    search values drawn from data with the signal removed.

Enforcement is at the boundary, on purpose (CLAUDE.md 2026-10-02): a caller
cannot report a number without declaring its alternative, cannot run too few
permutations, and cannot hide how many variants it tried -- every variant is
written to a jsonl, so N is a measured fact and not something anyone remembers
to write down.

    from permute import Search, whole_procedure_test, shuffle_labels

    s = Search("cal1", variants, evaluate)       # evaluate(data, variant)->float
    r = whole_procedure_test(data, s, shuffle_labels("dow"), B=1000,
                             alternative="greater")
    print(r)
"""
from __future__ import annotations
import json, math, pathlib, time
import numpy as np
import pandas as pd

MIN_B = 200


class Search:
    """The WHOLE search: every variant you would have tried, and the pick.

    `evaluate` must be pure in `data` -- it may not read anything the permuter
    did not permute, or the null is not a null.
    """

    def __init__(self, name, variants, evaluate, select=max, log_dir=None):
        if not variants:
            raise ValueError("a search with no variants is not a search")
        self.name, self.variants, self.evaluate, self.select = \
            name, list(variants), evaluate, select
        self.log_dir = pathlib.Path(log_dir) if log_dir else None
        self.n_evaluated = 0

    def run(self, data, tag="real"):
        stats, rows = [], []
        for v in self.variants:
            x = self.evaluate(data, v)
            x = float("-inf") if x is None or (isinstance(x, float) and math.isnan(x)) else float(x)
            stats.append(x)
            rows.append({"tag": tag, "variant": str(v), "stat": x})
        self.n_evaluated += len(self.variants)
        if self.log_dir:
            self.log_dir.mkdir(parents=True, exist_ok=True)
            with open(self.log_dir / f"{self.name}.variants.jsonl", "a") as f:
                for r in rows:
                    f.write(json.dumps(r) + "\n")
        best = self.select(stats)
        return best, self.variants[stats.index(best)]


# ---------------------------------------------------------------- permuters
def shuffle_labels(*cols):
    """Permute conditioning COLUMNS across rows, leaving the market untouched.

    The right null for a calendar or regime claim: prices, ranges, dependence
    and volatility clustering are all exactly preserved; only the claimed link
    between the label and the outcome is destroyed.
    """
    def f(df, rng):
        out = df.copy()
        perm = rng.permutation(len(out))
        for c in cols:
            out[c] = out[c].values[perm]
        return out
    f.__name__ = f"shuffle_labels({','.join(cols)})"
    return f


def shuffle_sessions(rng_cols=None):
    """Permute whole session rows. Destroys cross-session ordering, keeps each
    session's internal shape. Use for a claim about session sequence."""
    def f(df, rng):
        return df.iloc[rng.permutation(len(df))].reset_index(drop=True)
    f.__name__ = "shuffle_sessions"
    return f


def circular_block(col, block):
    """Rotate one column by a random offset in whole blocks. Preserves
    within-block dependence; the session-aware variant the 2026-10-01 handoff
    asks for when rows are intraday bars rather than sessions."""
    def f(df, rng):
        out = df.copy(); n = len(out)
        k = int(rng.integers(0, max(1, n // block))) * block
        out[col] = np.roll(out[col].values, k)
        return out
    f.__name__ = f"circular_block({col},{block})"
    return f


# ------------------------------------------------------------------- the test
class Result(dict):
    def __str__(self):
        g = self
        return (f"\n  WHOLE-PROCEDURE PERMUTATION TEST -- {g['search']}\n"
                f"  permuter        : {g['permuter']}\n"
                f"  variants/search : {g['n_variants']}   "
                f"total evaluations: {g['n_evaluations']:,}\n"
                f"  alternative     : {g['alternative']}\n"
                f"  real best       : {g['real']:+.4f}   (variant {g['real_variant']})\n"
                f"  null best       : mean {g['null_mean']:+.4f}  sd {g['null_sd']:.4f}  "
                f"p95 {g['null_p95']:+.4f}  max {g['null_max']:+.4f}\n"
                f"  B               : {g['B']}\n"
                f"  p               : {g['p']:.4f}   "
                f"(resolution floor {1/(g['B']+1):.4f})\n"
                + (f"  WARNING  null sd {g['null_sd1']:.3f} is well under 1.0 for a "
                   f"t-statistic -- the permuter has little to destroy (an imbalanced\n"
                   f"           signal does this; CAL-3). The test is EASIER to pass than "
                   f"it looks; read p as a lower bound.\n" if g.get("weak_null") else "")
                + f"  --> {g['verdict']}\n"
                f"  runtime {g['seconds']:.1f}s\n")


def whole_procedure_test(data, search: Search, permuter, B=1000, seed=7,
                         alternative=None, alpha=0.01):
    """Rerun `search` on B permuted copies of `data`. Returns a Result.

    alternative is REQUIRED. H153's gate 6 and the register's gate 2 were both
    two-sided and marked PASS on results significantly WORSE than the null; the
    caller states the direction of the claim or gets nothing.
    """
    if alternative not in ("greater", "less"):
        raise ValueError("alternative must be 'greater' or 'less' -- state the "
                         "direction of the claim (CLAUDE.md 2026-10-02)")
    if B < MIN_B:
        raise ValueError(f"B={B} gives a p-value floor of {1/(B+1):.3f}; "
                         f"minimum is {MIN_B}")
    t0 = time.time()
    sel = max if alternative == "greater" else min
    search.select = sel
    real, real_v = search.run(data, tag="real")
    rng = np.random.default_rng(seed)
    null = np.array([search.run(permuter(data, rng), tag=f"perm{i}")[0]
                     for i in range(B)])
    # A null whose spread is ~0 is not a null: the permuter did not touch what
    # the statistic reads. `shuffle_sessions` does exactly this to any row-wise
    # statistic (CAL-3, 2026-10-03) and silently returned p=1.0000, which reads
    # like a safe rejection and is in fact a test that never ran.
    spread = float(np.std(null, ddof=1))
    scale = max(abs(float(np.mean(null))), 1e-9)
    if spread < 1e-6 * max(scale, 1.0) or len(np.unique(np.round(null, 9))) < 3:
        raise ValueError(
            f"DEGENERATE NULL: {B} permutations produced {len(np.unique(np.round(null,9)))} "
            f"distinct values (sd={spread:.3e}). The permuter "
            f"'{getattr(permuter,'__name__','?')}' does not alter anything this "
            f"statistic reads, so the test did not run. Pick a permuter that "
            f"breaks the link your claim asserts.")

    ge = (null >= real) if alternative == "greater" else (null <= real)
    p = (1 + int(ge.sum())) / (B + 1)
    return Result(search=search.name, permuter=getattr(permuter, "__name__", "?"),
                  n_variants=len(search.variants), n_evaluations=search.n_evaluated,
                  alternative=alternative, real=real, real_variant=str(real_v),
                  null_mean=float(null.mean()), null_sd=float(null.std(ddof=1)),
                  null_p95=float(np.percentile(null, 95 if alternative == "greater" else 5)),
                  null_max=float(null.max() if alternative == "greater" else null.min()),
                  B=B, p=p, alpha=alpha, seconds=time.time() - t0,
                  null=null,
                  null_p99=float(np.percentile(null, 99 if alternative == "greater" else 1)),
                  null_sd1=float(np.std(null, ddof=1)),
                  weak_null=bool(len(search.variants) == 1
                                 and float(np.std(null, ddof=1)) < 0.80),
                  verdict=("SURVIVES the whole-procedure null" if p < alpha
                           else "INDISTINGUISHABLE from the search itself"))
