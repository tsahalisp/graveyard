"""Independent re-implementation of H195 (trade-list loop, not the vectorized runner), plus
reported-not-gated sensitivities. Post-verdict; cannot change the verdict."""
import yfinance as yf, pandas as pd, numpy as np
r = yf.download("SPY", start="1993-01-29", end="2026-10-08", auto_adjust=False, progress=False)
a = yf.download("SPY", start="1993-01-29", end="2026-10-08", auto_adjust=True, progress=False)
r.columns = [c[0] for c in r.columns]; a.columns = [c[0] for c in a.columns]
d = r[r.index >= "1993-02-01"]; tr = a.Close.reindex(d.index); op = a.Open.reindex(d.index)
d.assign(adjClose=tr, adjOpen=op).to_csv("results/spy_yf_2026-10-08.csv")
ibs = np.where(d.High > d.Low, (d.Close - d.Low) / (d.High - d.Low), 0.5)
print("rows", len(d), "H==L days", int((d.High == d.Low).sum()), "first", d.index[0].date(), "last", d.index[-1].date())
trades, inpos = [], False
for i in range(len(d)):
    if not inpos and ibs[i] < 0.2: inpos, ent = True, i
    elif inpos and ibs[i] > 0.8: inpos = False; trades.append((ent, i))
if inpos: trades.append((ent, len(d) - 1))
mid = d.index[len(d) // 2]
R = np.array([tr.iloc[x] / tr.iloc[e] - 1 - 0.0002 for e, x in trades])
E = np.array([d.index[e] >= mid for e, _ in trades])
for nm, m in (("H1", ~E), ("H2", E)):
    x = R[m]; print(nm, "trades", len(x), "mean/trade %.4f" % x.mean(), "win %.3f" % (x > 0).mean(), "compound %.2f" % (np.prod(1 + x) - 1))
hold = [x - e for e, x in trades]; print("trades", len(trades), "median hold", np.median(hold), "max hold", max(hold))
pos = np.zeros(len(d))
for e, x in trades: pos[e + 1:x + 1] = 1
s = pd.Series(tr.pct_change().fillna(0).values * pos, index=d.index)
for nm, x in (("H1", s[s.index < mid]), ("H2", s[s.index >= mid])):
    print(nm, "daily Sharpe (no rf, no cost)", round(x.mean() / x.std() * 252 ** .5, 3))
# sensitivity A: enter at NEXT day's open (no same-close knowledge)
R2 = np.array([tr.iloc[x] / op.iloc[e + 1] - 1 - 0.0002 for e, x in trades if e + 1 <= x])
E2 = np.array([d.index[e] >= mid for e, x in trades if e + 1 <= x])
print("SENS next-open entry: mean/trade all %.4f H2 %.4f win %.3f" % (R2.mean(), R2[E2].mean(), (R2 > 0).mean()))
# sensitivity B: by era
for a0, a1 in ((1993, 2000), (2001, 2008), (2009, 2015), (2016, 2020), (2021, 2026)):
    m = np.array([a0 <= d.index[e].year <= a1 for e, _ in trades])
    print(f"era {a0}-{a1}: n {m.sum()} mean %.4f win %.3f" % (R[m].mean(), (R[m] > 0).mean()))
# sensitivity C: other liquid ETFs, same rule (reported, NOT gated, NOT a new ID)
for t in ("QQQ", "IWM", "DIA"):
    rr = yf.download(t, start="2000-01-01", end="2026-10-08", auto_adjust=False, progress=False)
    aa = yf.download(t, start="2000-01-01", end="2026-10-08", auto_adjust=True, progress=False)
    rr.columns = [c[0] for c in rr.columns]; aa.columns = [c[0] for c in aa.columns]
    ib = np.where(rr.High > rr.Low, (rr.Close - rr.Low) / (rr.High - rr.Low), 0.5); trc = aa.Close.reindex(rr.index)
    tt, ip = [], False
    for i in range(len(rr)):
        if not ip and ib[i] < 0.2: ip, en = True, i
        elif ip and ib[i] > 0.8: ip = False; tt.append((en, i))
    x = np.array([trc.iloc[b] / trc.iloc[e] - 1 - 0.0002 for e, b in tt])
    print(f"{t} 2000+: trades {len(x)} mean %.4f win %.3f" % (x.mean(), (x > 0).mean()))
