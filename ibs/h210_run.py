#!/usr/bin/env python3
"""H210 (registered, see HYPOTHESES.md). One run. Reuses H208/H209 helpers by exec of that runner's prefix."""
import json, math, pathlib, sys
import numpy as np, pandas as pd
HERE = pathlib.Path(__file__).resolve().parent
if (HERE / "results" / "h210_results.json").exists():
    sys.exit("results exist: one run per ID")
src = (HERE / "h208_209_run.py").read_text().split("res = {}")[0]
src = src.replace('sys.exit("results exist: one run per ID")', 'pass')
g = {"__file__": str(HERE / "h208_209_run.py"), "__name__": "h210"}; exec(src, g)
load, ibs_pos, rf_for, sh, mdd, blo, trades = (g[k] for k in ("load", "ibs_pos", "rf_for", "sh", "mdd", "blo", "trades"))
cluster_drop, win_payoff, OUT, COST, STRESS = g["cluster_drop"], g["win_payoff"], g["OUT"], g["COST"], g["STRESS"]

spy = load("SPY"); s = spy[(spy.index >= "1993-02-01") & (spy.index <= "2026-10-07")]
vx = pd.read_csv(OUT / "vix_yf_2026-10-10.csv", index_col=0, parse_dates=True).vix   # saved by the H209 run
med = vx.rolling(252).median()
high = (vx > med).reindex(s.index).ffill().fillna(False).astype(bool); vix_t = vx.reindex(s.index).ffill()
rf = rf_for(s.index); ret = s.adjClose.pct_change().fillna(0.0)
p = ibs_pos(s)
# weight fixed at entry for the whole trade
w_entry = pd.Series(np.where(high, 1.5, 0.5), index=s.index)
w = w_entry.where((p == 1) & (p.shift(1).fillna(0) == 0)).ffill().where(p == 1).fillna(0.0)   # weight while in position (as of close t)
held_w = w.shift(1).fillna(0.0)
turn = (w - w.shift(1).fillna(0.0)).abs()


def book(cost):
    return held_w * (ret - rf) - turn * cost


ex, exs = book(COST), book(STRESS)
held1 = p.shift(1).fillna(0); tr1 = p.diff().abs().fillna(p.iloc[0])
e195 = held1 * (ret - rf) - tr1 * COST
mid = ex.index[len(ex) // 2]
h1, h2 = ex[ex.index < mid], ex[ex.index >= mid]; s1, s2 = exs[exs.index < mid], exs[exs.index >= mid]
bar = math.sqrt(2 * math.log(197)) / math.sqrt(len(h2) / 252)
lo, lo_s = blo(h2), blo(s2)
spy_ex = ret - rf
r = {"id": "H210", "n_tests": 197, "split": str(mid.date()),
     "sharpe_h1": sh(h1), "sharpe_h2": sh(h2), "sharpe_full": sh(ex), "boot_lo_h2": lo, "g3_bar": bar,
     "spy_sharpe_h2": sh(spy_ex[h2.index]), "mdd_h2": mdd(h2 + rf[h2.index]), "spy_mdd_h2": mdd(ret[h2.index]),
     "mdd_full": mdd(ex + rf), "h195_mdd_full_same_code": mdd(e195 + rf),
     "stress": {"sharpe_h1": sh(s1), "sharpe_h2": sh(s2), "boot_lo_h2": lo_s},
     "h195_sharpe_h2_same_code": sh(e195[e195.index >= mid]), "h195_sharpe_full_same_code": sh(e195),
     "avg_gross_exposure": float(held_w.mean()), "h195_exposure": float(held1.mean()),
     "entries_high": int(((p == 1) & (p.shift(1) == 0) & high).sum()), "entries_low": int(((p == 1) & (p.shift(1) == 0) & ~high).sum()),
     "median_vix_high_entries": float(vix_t[(p == 1) & (p.shift(1) == 0) & high].median()),
     "median_vix_low_entries": float(vix_t[(p == 1) & (p.shift(1) == 0) & ~high].median()),
     "cluster_drop_year": cluster_drop(ex.values, ex.index.year.values)}
tl = trades(s, p); we = [1.5 if high.loc[d] else 0.5 for d, _ in tl]
r["win_payoff_weighted"] = win_payoff(np.array([x[1] * k for x, k in zip(tl, we)]))
gates = {"1_both_halves": r["sharpe_h1"] > 0.5 and r["sharpe_h2"] > 0.5, "2_boot_lo": lo is not None and lo > 0,
         "3_bar": r["sharpe_h2"] > bar,
         "4_long_only": r["sharpe_h2"] >= r["spy_sharpe_h2"] and abs(r["mdd_h2"]) <= 0.6 * abs(r["spy_mdd_h2"]),
         "5_stress": r["stress"]["sharpe_h1"] > 0.5 and r["stress"]["sharpe_h2"] > 0.5 and lo_s is not None and lo_s > 0}
r["gates"] = gates
r["improvement_criterion"] = r["sharpe_h2"] >= r["h195_sharpe_h2_same_code"] + 0.10
r["VERDICT"] = "ADOPT" if all(gates.values()) and r["improvement_criterion"] else "NOT AN IMPROVEMENT"
r["prediction"] = "passes 1,2,5; H2 0.80-0.95; DD worse than H195; G4 fails; NOT AN IMPROVEMENT"
(OUT / "h210_results.json").write_text(json.dumps(r, indent=1, default=float))
print(json.dumps(r, indent=1, default=float))
