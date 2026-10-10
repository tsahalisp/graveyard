#!/usr/bin/env python3
"""bootstrap.py — Phase 7. An interval on every number the firm reports.

Constitution §5 missing organ #2: "UNCERTAINTY ON EVERY NUMBER: bootstrap
confidence intervals on backtest metrics; a sharpe without an interval invites
overconfidence."

WHAT THIS FIXES AND WHAT IT DOES NOT
  This measures SAMPLING uncertainty: how much a metric would move if the same
  strategy were run over a different draw of the same process. One series, one
  question — "how firmly do we know this number?"

  It does NOT touch SELECTION bias. Trying 1,006 parameter cells and reporting
  the best one is a different failure, and validate.py's rising noise ceiling
  is what answers it. Conflating the two is a classic error: a tight CI on a
  cherry-picked cell is a confident wrong answer. BOTH gates, or neither.

WHY BLOCKS, NOT IID
  Daily returns are autocorrelated and volatility clusters. Resampling them one
  at a time destroys that structure and reports intervals that are too narrow —
  the very overconfidence the organ exists to kill. So we resample contiguous
  BLOCKS (circular, so every observation gets equal weight). Block length is
  swept (5/10/20 days by default) and the WIDEST interval is reported, matching
  the house precedent from the ES audit. If the three disagree a lot, the
  dependence structure matters and the result deserves a second look.

  Block length is a judgement call, not a fact. It is reported alongside every
  interval so the reader can see what was assumed.

THE DECISION-FACING NUMBER
  The firm's gates read "sharpe > 0.3 in both halves". `prob_above` reports the
  share of bootstrap draws that clear the bar. A "CONFIRMED" whose interval
  straddles its own gate is not a confirmation — it is a coin flip with a
  verdict stapled to it, and `gate_report` says so in words.
"""
import numpy as np
import pandas as pd

DEFAULT_BLOCKS = (5, 10, 20)
DEFAULT_N_BOOT = 2000


def _check(r: pd.Series, stat: str = "sharpe") -> np.ndarray:
    if not isinstance(r, pd.Series):
        raise TypeError("returns must be a pd.Series of periodic net returns")
    x = r.dropna().to_numpy(dtype=float)
    if len(x) < 30:
        raise ValueError(f"need >=30 observations to bootstrap, got {len(x)}")
    # A constant series has zero variance, so mean/sd explodes instead of erroring:
    # test_paired_difference caught this returning a Sharpe of 7e14 on a flat
    # difference series. Degenerate input gets refused, not scaled.
    #
    # The refusal is SCALE-DEPENDENT and must not apply to every stat: a mean is
    # perfectly well defined on a constant series, and eventgate.py needs an
    # interval on a mean. Refusing there would reject valid input.
    if _SCALE_DEPENDENT.get(stat, True):
        sd = float(x.std(ddof=1))
        if sd < 1e-12:
            raise ValueError(f"series is constant (sd < 1e-12); {stat} is undefined")
    return x


def _resample(x: np.ndarray, block: int, n_boot: int, rng) -> np.ndarray:
    """Circular block bootstrap -> (n_boot, n) matrix of resampled series."""
    n = len(x)
    if not 1 <= block <= n:
        raise ValueError(f"block must be in [1, {n}], got {block}")
    n_blocks = int(np.ceil(n / block))
    starts = rng.integers(0, n, size=(n_boot, n_blocks))
    offs = np.arange(block)
    idx = (starts[:, :, None] + offs[None, None, :]) % n      # circular wrap
    return x[idx.reshape(n_boot, -1)[:, :n]]


def sharpe_of(x: np.ndarray, periods: int) -> np.ndarray:
    sd = x.std(axis=-1, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        s = np.where(sd > 0, x.mean(axis=-1) / sd * np.sqrt(periods), 0.0)
    return s


def ann_return_of(x: np.ndarray, periods: int) -> np.ndarray:
    n = x.shape[-1]
    return np.exp(np.log1p(x).sum(axis=-1) * (periods / n)) - 1.0


def max_dd_of(x: np.ndarray) -> np.ndarray:
    eq = np.cumprod(1.0 + x, axis=-1)
    return (1.0 - eq / np.maximum.accumulate(eq, axis=-1)).max(axis=-1)


_STATS = {
    "sharpe": lambda x, p: sharpe_of(x, p),
    "ann_return": lambda x, p: ann_return_of(x, p),
    "max_dd": lambda x, p: max_dd_of(x),
    # "mean" exists for eventgate.py: small-market event data needs an interval
    # on a mean edge metric (CLV and friends), not on a Sharpe. `periods` is
    # ignored -- a per-event mean has no annualisation.
    "mean": lambda x, p: x.mean(axis=1),
}

# Which stats blow up on a zero-variance series and must therefore refuse it.
# A mean does not; a Sharpe does.
_SCALE_DEPENDENT = {"sharpe": True, "ann_return": False, "max_dd": False, "mean": False}


def ci(r: pd.Series, stat: str = "sharpe", periods: int = 252, alpha: float = 0.05,
       blocks=DEFAULT_BLOCKS, n_boot: int = DEFAULT_N_BOOT, seed: int = 0) -> dict:
    """Widest percentile interval across the swept block lengths.

    Returns point, lo, hi, width, the block that produced it, and the per-block
    intervals so a disagreement between blocks is visible rather than averaged
    away.
    """
    if stat not in _STATS:
        raise ValueError(f"unknown stat {stat!r}; have {sorted(_STATS)}")
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")
    x = _check(r, stat)
    fn = _STATS[stat]
    point = float(fn(x[None, :], periods)[0])
    rng = np.random.default_rng(seed)
    per_block, widest = {}, None
    for b in blocks:
        draws = fn(_resample(x, b, n_boot, rng), periods)
        lo, hi = np.percentile(draws, [100 * alpha / 2, 100 * (1 - alpha / 2)])
        per_block[b] = {"lo": float(lo), "hi": float(hi), "width": float(hi - lo)}
        if widest is None or hi - lo > widest[1]["width"]:
            widest = (b, per_block[b])
    b, w = widest
    return {"stat": stat, "point": point, "lo": w["lo"], "hi": w["hi"],
            "width": w["width"], "block": b, "n_boot": n_boot, "n_obs": len(x),
            "alpha": alpha, "per_block": per_block}


def prob_above(r: pd.Series, threshold: float, stat: str = "sharpe", periods: int = 252,
               block: int = 10, n_boot: int = DEFAULT_N_BOOT, seed: int = 0) -> float:
    """Share of bootstrap draws in which `stat` clears `threshold`."""
    if stat not in _STATS:
        raise ValueError(f"unknown stat {stat!r}")
    x = _check(r, stat)
    rng = np.random.default_rng(seed)
    draws = _STATS[stat](_resample(x, block, n_boot, rng), periods)
    return float((draws > threshold).mean())


def gate_report(r: pd.Series, gate: float = 0.3, periods: int = 252, **kw) -> dict:
    """The decision-facing call: does the interval actually clear the gate?"""
    c = ci(r, "sharpe", periods, **{k: v for k, v in kw.items() if k != "block"})
    p = prob_above(r, gate, "sharpe", periods, block=c["block"])
    if c["lo"] > gate:
        v, why = "CLEARS", f"whole {int((1-c['alpha'])*100)}% interval sits above the {gate} gate"
    elif c["hi"] < gate:
        v, why = "FAILS", f"whole interval sits below the {gate} gate"
    else:
        v, why = "STRADDLES", (f"interval spans the {gate} gate — the point estimate "
                               f"{c['point']:.2f} is not distinguishable from the bar")
    return {**c, "gate": gate, "prob_above_gate": p, "gate_verdict": v, "why": why}


def pretty(c: dict, label: str = "") -> str:
    g = ""
    if "gate_verdict" in c:
        g = f"  gate {c['gate']:.2f} -> {c['gate_verdict']} (P={c['prob_above_gate']:.0%})"
    return (f"{label:<22} {c['stat']:<11} {c['point']:+6.2f}  "
            f"[{c['lo']:+6.2f}, {c['hi']:+6.2f}]  width {c['width']:.2f} "
            f"(block {c['block']}, n={c['n_obs']}){g}")
