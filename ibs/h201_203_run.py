#!/usr/bin/env python3
"""H201-H203 (registered 4062e7b). One run each."""
import json, math, pathlib, sys
import numpy as np, pandas as pd, yfinance as yf
HERE = pathlib.Path(__file__).resolve().parent; G = HERE.parent
sys.path.insert(0, str(G.parent / "firm"))
import bootstrap  # noqa: E402
OUT = HERE / "results"
if any((OUT / f"h20{k}_results.json").exists() for k in (1, 2, 3)):
    sys.exit("results exist: one run per ID")
N_TESTS = 193; COST, STRESS = 0.0001, 0.0005

ff = pd.read_csv(G / "phase3/data/F-F_Research_Data_Factors.csv", skiprows=4, nrows=1200)
ff = ff[ff.iloc[:, 0].astype(str).str.strip().str.len() == 6]
ff.columns = ["ym", "mkt", "smb", "hml", "rf"]; ff["ym"] = ff.ym.astype(str).str.strip(); ff["rf"] = ff.rf.astype(float) / 100
RFM = dict(zip(ff.ym, ff.rf)); LAST_RF = ff.rf.iloc[-1]


def rf_for(idx):
    ym = idx.strftime("%Y%m"); dim = pd.Series(1, index=idx).groupby(ym).transform("sum")
    return pd.Series([RFM.get(m, LAST_RF) for m in ym], index=idx) / dim


def load(t):
    if t == "SPY":
        d = pd.read_csv(OUT / "spy_yf_2026-10-08.csv", index_col=0, parse_dates=True)
        return d[["High", "Low", "Close", "adjClose"]]
    r = yf.download(t, start="1998-01-01", end="2026-10-08", auto_adjust=False, progress=False)
    a = yf.download(t, start="1998-01-01", end="2026-10-08", auto_adjust=True, progress=False)
    r.columns = [c[0] if isinstance(c, tuple) else c for c in r.columns]; a.columns = [c[0] if isinstance(c, tuple) else c for c in a.columns]
    d = pd.DataFrame({"High": r.High, "Low": r.Low, "Close": r.Close, "adjClose": a.Close}).dropna()
    d.to_csv(OUT / f"{t.lower()}_yf_2026-10-08.csv"); return d


def ibs_pos(d, allow=None):
    ibs = ((d.Close - d.Low) / (d.High - d.Low)).where(d.High > d.Low, 0.5)
    p, s = 0, []
    for i, v in enumerate(ibs):
        ok = True if allow is None else bool(allow.iloc[i])
        if p == 0 and v < 0.2 and ok: p = 1
        elif p == 1 and v > 0.8: p = 0
        s.append(p)
    return pd.Series(s, index=d.index)


def sleeve(d, pos, cost, rf):
    ret = d.adjClose.pct_change().fillna(0.0)
    held = pos.shift(1).fillna(0); tr = pos.diff().abs().fillna(pos.iloc[0])
    return held * ret + (1 - held) * rf - tr * cost - rf, held, ret


def sh(x): return float(x.mean() / x.std(ddof=1) * math.sqrt(252)) if x.std(ddof=1) > 0 else 0.0


def mdd(t): c = (1 + t).cumprod(); return float((c / c.cummax() - 1).min())


def blo(x):
    rep = bootstrap.gate_report(x, gate=0.5, periods=252); return rep.get("ci", {}).get("lo", rep.get("lo"))


def common(hid, ex, exs, rf, spy_ret, gate4_fn, pred, extra):
    mid = ex.index[len(ex) // 2]
    h1, h2 = ex[ex.index < mid], ex[ex.index >= mid]; s1, s2 = exs[exs.index < mid], exs[exs.index >= mid]
    Y2 = len(h2) / 252; bar = math.sqrt(2 * math.log(N_TESTS)) / math.sqrt(Y2)
    lo, lo_s = blo(h2), blo(s2)
    spy_ex = (spy_ret - rf)
    r = {"id": hid, "start": str(ex.index[0].date()), "end": str(ex.index[-1].date()), "split": str(mid.date()),
         "sharpe_h1": sh(h1), "sharpe_h2": sh(h2), "sharpe_full": sh(ex), "boot_lo_h2": lo, "g3_bar": bar,
         "spy_sharpe_h2": sh(spy_ex[h2.index]), "spy_sharpe_full": sh(spy_ex),
         "mdd_h2": mdd(h2 + rf[h2.index]), "spy_mdd_h2": mdd(spy_ret[h2.index]),
         "stress": {"sharpe_h1": sh(s1), "sharpe_h2": sh(s2), "boot_lo_h2": lo_s},
         "cagr_full": float((1 + ex + rf).prod() ** (252 / len(ex)) - 1),
         "spy_cagr_full": float((1 + spy_ret).prod() ** (252 / len(ex)) - 1), **extra}
    g = {"1_both_halves": r["sharpe_h1"] > 0.5 and r["sharpe_h2"] > 0.5, "2_boot_lo": lo is not None and lo > 0,
         "3_bar": r["sharpe_h2"] > bar, "4": gate4_fn(r),
         "5_stress": r["stress"]["sharpe_h1"] > 0.5 and r["stress"]["sharpe_h2"] > 0.5 and lo_s is not None and lo_s > 0}
    r["gates"] = g; r["VERDICT"] = "CONFIRMED" if all(g.values()) else "NOT CONFIRMED"; r["prediction"] = pred
    (OUT / f"{hid.lower()}_results.json").write_text(json.dumps(r, indent=1, default=float))
    return r


spy = load("SPY"); spy = spy[spy.index >= "1993-02-01"]
res = {}
long_only = lambda r: r["sharpe_h2"] >= r["spy_sharpe_h2"] and abs(r["mdd_h2"]) <= 0.6 * abs(r["spy_mdd_h2"])

# ---- H201: 4-ETF book
data = {t: load(t) for t in ("SPY", "QQQ", "IWM", "DIA")}
start = max(d.index[0] for d in data.values()) + pd.Timedelta(days=1)
idx = data["SPY"].index
for d in data.values(): idx = idx.intersection(d.index)
idx = idx[idx >= start]
rf = rf_for(idx)
sl, sls, helds = [], [], []
for t, d in data.items():
    d = d.loc[idx]; p = ibs_pos(d)
    e, h, _ = sleeve(d, p, COST, rf); es, _, _ = sleeve(d, p, STRESS, rf)
    sl.append(e); sls.append(es); helds.append(h)
book, books = sum(sl) / 4, sum(sls) / 4
spy_ret = data["SPY"].loc[idx].adjClose.pct_change().fillna(0.0)
res["H201"] = common("H201", book, books, rf, spy_ret, long_only, "CONFIRMED; H2 0.9-1.3",
                     {"avg_exposure": float(sum(helds).mean() / 4),
                      "sleeve_corr_mean": float(pd.concat(sl, axis=1).corr().values[np.triu_indices(4, 1)].mean())})

# ---- H202: overlay on SPY buy-and-hold
rf = rf_for(spy.index); p = ibs_pos(spy)
ret = spy.adjClose.pct_change().fillna(0.0); held = p.shift(1).fillna(0); tr = p.diff().abs().fillna(p.iloc[0])
ov = (ret - rf) + 0.5 * held * (ret - rf) - 0.5 * tr * COST
ovs = (ret - rf) + 0.5 * held * (ret - rf) - 0.5 * tr * STRESS
res["H202"] = common("H202", ov, ovs, rf, ret,
                     lambda r: r["sharpe_h2"] >= r["spy_sharpe_h2"] and abs(r["mdd_h2"]) <= 1.15 * abs(r["spy_mdd_h2"]),
                     "passes 1,2,4; G3 marginal; H2 Sharpe exceeds SPY by 0.05-0.15", {"avg_leverage": float(1 + 0.5 * held.mean())})

# ---- H203: IBS + 200-day SMA entry filter
sma = spy.Close.rolling(200).mean(); allow = (spy.Close > sma).fillna(False)
p3 = ibs_pos(spy, allow)
e, h, _ = sleeve(spy, p3, COST, rf); es, _, _ = sleeve(spy, p3, STRESS, rf)
res["H203"] = common("H203", e, es, rf, ret, long_only, "not better than H195: H2 within +/-0.15 of 0.93; trades down ~30%",
                     {"trades": int((p3.diff() == 1).sum()), "h195_trades": int((ibs_pos(spy).diff() == 1).sum()),
                      "exposure": float(h.mean())})
print(json.dumps(res, indent=1, default=float))
