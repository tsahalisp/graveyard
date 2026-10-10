#!/usr/bin/env python3
"""H195 (IBS on SPY) and H196 (Turnaround Tuesday), registered in commit 43d7f5a.
One run each. Run: ~/polytail/firm/.venv/bin/python h195_h196_run.py"""
import io, json, math, pathlib, sys
import numpy as np, pandas as pd
import yfinance as yf

HERE = pathlib.Path(__file__).resolve().parent
G = HERE.parent
sys.path.insert(0, str(G.parent / "firm"))
import bootstrap  # noqa: E402

OUT = HERE / "results"; OUT.mkdir(exist_ok=True)
N_TESTS = 188
COST, STRESS = 0.0001, 0.0005          # per side

if (OUT / "h195_results.json").exists() or (OUT / "h196_results.json").exists():
    sys.exit("results exist: one run per ID")

raw = yf.download("SPY", start="1993-01-29", end="2026-10-08", auto_adjust=False, progress=False)
adj = yf.download("SPY", start="1993-01-29", end="2026-10-08", auto_adjust=True, progress=False)
raw.columns = [c[0] if isinstance(c, tuple) else c for c in raw.columns]
adj.columns = [c[0] if isinstance(c, tuple) else c for c in adj.columns]
px = pd.DataFrame({"H": raw.High, "L": raw.Low, "C": raw.Close, "TR": adj.Close}).dropna()
px = px[px.index >= "1993-02-01"]
ret = px.TR.pct_change().fillna(0.0)

# risk-free: monthly FF RF spread over that month's trading days; months after the file end use the last value
ff = pd.read_csv(G / "phase3/data/F-F_Research_Data_Factors.csv", skiprows=4, nrows=1200)
ff = ff[ff.iloc[:, 0].astype(str).str.strip().str.len() == 6]
ff.columns = ["ym", "mkt", "smb", "hml", "rf"]
ff["ym"] = ff.ym.astype(str).str.strip(); ff["rf"] = ff.rf.astype(float) / 100
rfm = dict(zip(ff.ym, ff.rf))
ym = px.index.strftime("%Y%m")
last_rf = ff.rf.iloc[-1]
days_in_m = pd.Series(1, index=px.index).groupby(ym).transform("sum")
rf = pd.Series([rfm.get(m, last_rf) for m in ym], index=px.index) / days_in_m
rf_filled_months = sorted(set(m for m in ym if m not in rfm))

ibs = ((px.C - px.L) / (px.H - px.L)).where(px.H > px.L, 0.5)


def pos_ibs():
    p, s = 0, []
    for v in ibs:
        if p == 0 and v < 0.2:
            p = 1
        elif p == 1 and v > 0.8:
            p = 0
        s.append(p)
    return pd.Series(s, index=px.index)          # position held from this close to the next close


def pos_tt():
    d = px.index
    s = pd.Series(0, index=d)
    c = px.C
    for i in range(1, len(d)):
        if d[i].weekday() == 0 and c.iloc[i] < c.iloc[i - 1]:
            s.iloc[i] = 1                           # buy Monday close, hold to next trading day's close
    return s


def strat(pos, cost):
    held = pos.shift(1).fillna(0)                   # earn the return of the day after the decision
    trades = pos.diff().abs().fillna(pos.iloc[0])
    r = held * ret + (1 - held) * rf - trades * cost
    return r - rf, held, int((pos.diff() == 1).sum())


def sh(x):
    return float(x.mean() / x.std(ddof=1) * math.sqrt(252)) if x.std(ddof=1) > 0 else 0.0


def mdd(total):
    c = (1 + total).cumprod()
    return float((c / c.cummax() - 1).min())


mid = px.index[len(px) // 2]
spy_ex = ret - rf
res_all = {}
for hid, pos, pred in (("H195", pos_ibs(), "FAIL; full Sharpe >0, second half 0.2-0.7, fails gate 3 and/or 4"),
                       ("H196", pos_tt(), "FAIL gate 4: Sharpe below SPY 2010-2026, drawdown condition passes")):
    ex, held, n_tr = strat(pos, COST)
    exs, _, _ = strat(pos, STRESS)
    h1, h2 = ex[ex.index < mid], ex[ex.index >= mid]
    s1, s2 = exs[exs.index < mid], exs[exs.index >= mid]
    Y2 = len(h2) / 252
    bar = math.sqrt(2 * math.log(N_TESTS)) / math.sqrt(Y2)
    rep = bootstrap.gate_report(h2, gate=0.5, periods=252)
    lo = rep.get("ci", {}).get("lo", rep.get("lo"))
    rep_s = bootstrap.gate_report(s2, gate=0.5, periods=252)
    lo_s = rep_s.get("ci", {}).get("lo", rep_s.get("lo"))
    tot2 = (h2 + rf[h2.index]); spy2 = ret[h2.index]
    r = {"id": hid, "start": str(px.index[0].date()), "end": str(px.index[-1].date()), "split": str(mid.date()),
         "trades": n_tr, "exposure": float(held.mean()),
         "sharpe_h1": sh(h1), "sharpe_h2": sh(h2), "sharpe_full": sh(ex), "boot_lo_h2": lo,
         "g3_bar": bar, "spy_sharpe_h2": sh(spy_ex[h2.index]), "mdd_h2": mdd(tot2), "spy_mdd_h2": mdd(spy2),
         "stress": {"sharpe_h1": sh(s1), "sharpe_h2": sh(s2), "boot_lo_h2": lo_s},
         "cagr_full": float((1 + ex + rf).prod() ** (252 / len(ex)) - 1),
         "avg_trade_gross": float(ret[held == 1].sum() / max(n_tr, 1)),
         "rf_months_filled_from_last": rf_filled_months}
    g = {"1_both_halves": r["sharpe_h1"] > 0.5 and r["sharpe_h2"] > 0.5,
         "2_boot_lo": lo is not None and lo > 0,
         "3_bar": r["sharpe_h2"] > bar,
         "4_long_only": r["sharpe_h2"] >= r["spy_sharpe_h2"] and abs(r["mdd_h2"]) <= 0.6 * abs(r["spy_mdd_h2"]),
         "5_stress": r["stress"]["sharpe_h1"] > 0.5 and r["stress"]["sharpe_h2"] > 0.5 and lo_s is not None and lo_s > 0}
    r["gates"] = g
    r["VERDICT"] = "CONFIRMED" if all(g.values()) else "NOT CONFIRMED"
    r["prediction"] = pred
    (OUT / f"{hid.lower()}_results.json").write_text(json.dumps(r, indent=1, default=float))
    res_all[hid] = r
print(json.dumps(res_all, indent=1, default=float))
