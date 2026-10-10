#!/usr/bin/env python3
"""H198 (Williams %R(2)) and H199 (252-day high, hold 21d) on SPY. Registered ae550fb. One run each.
Same data file, costs, rf, halves and gates as H195."""
import json, math, pathlib, sys
import numpy as np, pandas as pd
HERE = pathlib.Path(__file__).resolve().parent; G = HERE.parent
sys.path.insert(0, str(G.parent / "firm"))
import bootstrap  # noqa: E402
OUT = HERE / "results"
if (OUT / "h198_results.json").exists() or (OUT / "h199_results.json").exists():
    sys.exit("results exist: one run per ID")
N_TESTS = 190; COST, STRESS = 0.0001, 0.0005

px = pd.read_csv(OUT / "spy_yf_2026-10-08.csv", index_col=0, parse_dates=True)
px = px[px.index >= "1993-02-01"]
H, L, C, TR = px.High, px.Low, px.Close, px.adjClose
ret = TR.pct_change().fillna(0.0)
ff = pd.read_csv(G / "phase3/data/F-F_Research_Data_Factors.csv", skiprows=4, nrows=1200)
ff = ff[ff.iloc[:, 0].astype(str).str.strip().str.len() == 6]
ff.columns = ["ym", "mkt", "smb", "hml", "rf"]; ff["ym"] = ff.ym.astype(str).str.strip(); ff["rf"] = ff.rf.astype(float) / 100
rfm = dict(zip(ff.ym, ff.rf)); ym = px.index.strftime("%Y%m"); last_rf = ff.rf.iloc[-1]
dim = pd.Series(1, index=px.index).groupby(ym).transform("sum")
rf = pd.Series([rfm.get(m, last_rf) for m in ym], index=px.index) / dim

# H195 position, for the overlap report only
ibs = ((C - L) / (H - L)).where(H > L, 0.5)
p, s = 0, []
for v in ibs:
    if p == 0 and v < 0.2: p = 1
    elif p == 1 and v > 0.8: p = 0
    s.append(p)
pos195 = pd.Series(s, index=px.index)


def pos_wr2():
    hh = H.rolling(2).max(); ll = L.rolling(2).min()
    wr = (-100 * (hh - C) / (hh - ll)).where(hh > ll, -50.0)
    p, s = 0, []
    for i in range(len(C)):
        w = wr.iloc[i]
        if p == 0 and w < -90: p = 1
        elif p == 1 and (C.iloc[i] > H.iloc[i - 1] or w > -30): p = 0
        s.append(p)
    return pd.Series(s, index=px.index)


def pos_hi252():
    prior_max = C.shift(1).rolling(252).max()
    p, left, s = 0, 0, []
    for i in range(len(C)):
        if p == 1:
            left -= 1
            if left == 0: p = 0
        elif not np.isnan(prior_max.iloc[i]) and C.iloc[i] > prior_max.iloc[i]:
            p, left = 1, 21
        s.append(p)
    return pd.Series(s, index=px.index)


def strat(pos, cost):
    held = pos.shift(1).fillna(0); trades = pos.diff().abs().fillna(pos.iloc[0])
    return held * ret + (1 - held) * rf - trades * cost - rf, held


def sh(x): return float(x.mean() / x.std(ddof=1) * math.sqrt(252)) if x.std(ddof=1) > 0 else 0.0


def mdd(t): c = (1 + t).cumprod(); return float((c / c.cummax() - 1).min())


def blo(x):
    rep = bootstrap.gate_report(x, gate=0.5, periods=252); return rep.get("ci", {}).get("lo", rep.get("lo"))


mid = px.index[len(px) // 2]; spy_ex = ret - rf
out = {}
for hid, pos, pred in (("H198", pos_wr2(), "pass gates 1-2; H2 0.6-0.9; gate 4 borderline; overlap with H195 >60%"),
                       ("H199", pos_hi252(), "FAIL gate 4; H2 Sharpe below SPY")):
    ex, held = strat(pos, COST); exs, _ = strat(pos, STRESS)
    h1, h2 = ex[ex.index < mid], ex[ex.index >= mid]; s1, s2 = exs[exs.index < mid], exs[exs.index >= mid]
    Y2 = len(h2) / 252; bar = math.sqrt(2 * math.log(N_TESTS)) / math.sqrt(Y2)
    lo, lo_s = blo(h2), blo(s2)
    n_tr = int((pos.diff() == 1).sum())
    r = {"id": hid, "split": str(mid.date()), "trades": n_tr, "exposure": float(held.mean()),
         "sharpe_h1": sh(h1), "sharpe_h2": sh(h2), "sharpe_full": sh(ex), "boot_lo_h2": lo, "g3_bar": bar,
         "spy_sharpe_h2": sh(spy_ex[h2.index]), "mdd_h2": mdd(h2 + rf[h2.index]), "spy_mdd_h2": mdd(ret[h2.index]),
         "stress": {"sharpe_h1": sh(s1), "sharpe_h2": sh(s2), "boot_lo_h2": lo_s},
         "avg_trade_gross": float((held * ret).sum() / max(n_tr, 1)),
         "overlap_with_H195_in_market_days": float(((held == 1) & (pos195.shift(1) == 1)).sum() / max((held == 1).sum(), 1)),
         "corr_daily_with_H195": float(ex.corr(strat(pos195, COST)[0]))}
    g = {"1_both_halves": r["sharpe_h1"] > 0.5 and r["sharpe_h2"] > 0.5, "2_boot_lo": lo is not None and lo > 0,
         "3_bar": r["sharpe_h2"] > bar,
         "4_long_only": r["sharpe_h2"] >= r["spy_sharpe_h2"] and abs(r["mdd_h2"]) <= 0.6 * abs(r["spy_mdd_h2"]),
         "5_stress": r["stress"]["sharpe_h1"] > 0.5 and r["stress"]["sharpe_h2"] > 0.5 and lo_s is not None and lo_s > 0}
    r["gates"] = g; r["VERDICT"] = "CONFIRMED" if all(g.values()) else "NOT CONFIRMED"; r["prediction"] = pred
    (OUT / f"{hid.lower()}_results.json").write_text(json.dumps(r, indent=1, default=float)); out[hid] = r
print(json.dumps(out, indent=1, default=float))
