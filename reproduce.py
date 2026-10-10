#!/usr/bin/env python3
"""Reproduce the two headline confirmations from public data, in one command.

    pip install -r requirements.txt && python reproduce.py

H195: IBS on SPY, 1993-02-01 to 2026-10-07.
H208: the same rule, unchanged, on 15 ETFs it was never tuned on, 1999-01-04 to 2026-10-07.
Rule: buy at the close when IBS = (C-L)/(H-L) < 0.2; sell at the first close with IBS > 0.8.
Costs 1 bp per side (stress 5 bp). Sharpe on excess returns over the Fama-French risk-free rate.
Prices come from Yahoo Finance via yfinance, so later dividend re-adjustments can move the
third decimal. The registered numbers are printed beside yours."""
import math, pathlib, sys
import numpy as np, pandas as pd, yfinance as yf
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "lib"))
import bootstrap  # noqa: E402

END = "2026-10-08"; COST, STRESS = 0.0001, 0.0005
REG = {"H195": {"sharpe_h1": None, "sharpe_h2": 0.93, "n": 188}, "H208": {"sharpe_h1": 0.836, "sharpe_h2": 1.113, "n": 195}}

ff = pd.read_csv(HERE / "data/F-F_Research_Data_Factors.csv", skiprows=4, nrows=1200)
ff = ff[ff.iloc[:, 0].astype(str).str.strip().str.len() == 6]
ff.columns = ["ym", "mkt", "smb", "hml", "rf"]; ff["ym"] = ff.ym.astype(str).str.strip(); ff["rf"] = ff.rf.astype(float) / 100
RFM = dict(zip(ff.ym, ff.rf)); LAST = ff.rf.iloc[-1]


def rf_for(idx):
    ym = idx.strftime("%Y%m"); dim = pd.Series(1, index=idx).groupby(ym).transform("sum")
    return pd.Series([RFM.get(m, LAST) for m in ym], index=idx) / dim


def load(t, start="1993-01-29"):
    r = yf.download(t, start=start, end=END, auto_adjust=False, progress=False)
    a = yf.download(t, start=start, end=END, auto_adjust=True, progress=False)
    for d in (r, a): d.columns = [c[0] if isinstance(c, tuple) else c for c in d.columns]
    return pd.DataFrame({"High": r.High, "Low": r.Low, "Close": r.Close, "adjClose": a.Close}).dropna()


def ibs_pos(d):
    ibs = ((d.Close - d.Low) / (d.High - d.Low)).where(d.High > d.Low, 0.5)
    p, out = 0, []
    for v in ibs:
        if p == 0 and v < 0.2: p = 1
        elif p == 1 and v > 0.8: p = 0
        out.append(p)
    return pd.Series(out, index=d.index)


def sleeve(d, cost, rf):
    p = ibs_pos(d); ret = d.adjClose.pct_change().fillna(0.0)
    held = p.shift(1).fillna(0); tr = p.diff().abs().fillna(p.iloc[0])
    return held * ret + (1 - held) * rf - tr * cost - rf


def sh(x): x = x.dropna(); return float(x.mean() / x.std(ddof=1) * math.sqrt(252))


def mdd(x): c = (1 + x.dropna()).cumprod(); return float((c / c.cummax() - 1).min())


def report(name, ex, exs, rf, spy_ret):
    ex = ex.dropna(); exs = exs.loc[ex.index]; mid = ex.index[len(ex) // 2]
    h1, h2 = ex[ex.index < mid], ex[ex.index >= mid]; s1, s2 = exs[exs.index < mid], exs[exs.index >= mid]
    bar = math.sqrt(2 * math.log(REG[name]["n"])) / math.sqrt(len(h2) / 252)
    lo = bootstrap.gate_report(h2, gate=0.5, periods=252); lo = lo.get("ci", {}).get("lo", lo.get("lo"))
    los = bootstrap.gate_report(s2, gate=0.5, periods=252); los = los.get("ci", {}).get("lo", los.get("lo"))
    spy_h2 = (spy_ret - rf).loc[h2.index]
    g = {"1 both halves > 0.5": sh(h1) > 0.5 and sh(h2) > 0.5, "2 holdout bootstrap lower bound > 0": lo > 0,
         f"3 H2 Sharpe > noise bar {bar:.3f}": sh(h2) > bar,
         "4 beats SPY (H2 Sharpe >=, DD <= 0.6x)": sh(h2) >= sh(spy_h2) and abs(mdd(h2 + rf.loc[h2.index])) <= 0.6 * abs(mdd(spy_ret.loc[h2.index])),
         "5 survives 5 bp/side": sh(s1) > 0.5 and sh(s2) > 0.5 and los > 0}
    print(f"\n{name}  {ex.index[0].date()} to {ex.index[-1].date()}, split {mid.date()}")
    print(f"  Sharpe H1 {sh(h1):.3f}  H2 {sh(h2):.3f}   (registered H2 {REG[name]['sharpe_h2']})")
    print(f"  SPY H2 Sharpe {sh(spy_h2):.3f}; max DD H2 {mdd(h2 + rf.loc[h2.index]):.1%} vs SPY {mdd(spy_ret.loc[h2.index]):.1%}")
    for k, v in g.items(): print(f"  {'PASS' if v else 'FAIL'}  {k}")
    print("  VERDICT:", "CONFIRMED" if all(g.values()) else "NOT CONFIRMED")


spy = load("SPY"); spy = spy[spy.index >= "1993-02-01"]
rf = rf_for(spy.index); spy_ret = spy.adjClose.pct_change().fillna(0.0)
report("H195", sleeve(spy, COST, rf), sleeve(spy, STRESS, rf), rf, spy_ret)

U = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY", "EFA", "EEM", "TLT", "GLD"]
idx = spy.index[spy.index >= "1999-01-04"]; rf2 = rf.loc[idx]
E, ES = {}, {}
for t in U:
    d = load(t, "1998-01-01"); d = d.loc[d.index.intersection(idx)].iloc[1:]
    E[t] = sleeve(d, COST, rf2.loc[d.index]).reindex(idx); ES[t] = sleeve(d, STRESS, rf2.loc[d.index]).reindex(idx)
    print(f"  {t:5s} net Sharpe {sh(E[t]):.2f}")
report("H208", pd.DataFrame(E).mean(axis=1), pd.DataFrame(ES).mean(axis=1), rf2, spy_ret.loc[idx])
