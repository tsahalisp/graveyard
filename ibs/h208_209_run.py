#!/usr/bin/env python3
"""H208-H209 (registered c6d59bc). One run each."""
import json, math, pathlib, sys
import numpy as np, pandas as pd, yfinance as yf
HERE = pathlib.Path(__file__).resolve().parent; G = HERE.parent
sys.path.insert(0, str(G.parent / "firm")); sys.path.insert(0, str(G / "lib"))
import bootstrap  # noqa: E402
from validate import cluster_drop, win_payoff  # noqa: E402
OUT = HERE / "results"
if any((OUT / f"h20{k}_results.json").exists() for k in (8, 9)):
    sys.exit("results exist: one run per ID")
COST, STRESS = 0.0001, 0.0005
END = "2026-10-08"

ff = pd.read_csv(G / "phase3/data/F-F_Research_Data_Factors.csv", skiprows=4, nrows=1200)
ff = ff[ff.iloc[:, 0].astype(str).str.strip().str.len() == 6]
ff.columns = ["ym", "mkt", "smb", "hml", "rf"]; ff["ym"] = ff.ym.astype(str).str.strip(); ff["rf"] = ff.rf.astype(float) / 100
RFM = dict(zip(ff.ym, ff.rf)); LAST_RF = ff.rf.iloc[-1]


def rf_for(idx):
    ym = idx.strftime("%Y%m"); dim = pd.Series(1, index=idx).groupby(ym).transform("sum")
    return pd.Series([RFM.get(m, LAST_RF) for m in ym], index=idx) / dim


def load(t):
    f = OUT / f"{t.lower()}_yf_2026-10-08.csv"
    if f.exists():
        d = pd.read_csv(f, index_col=0, parse_dates=True); return d[["High", "Low", "Close", "adjClose"]]
    r = yf.download(t, start="1998-01-01", end=END, auto_adjust=False, progress=False)
    a = yf.download(t, start="1998-01-01", end=END, auto_adjust=True, progress=False)
    r.columns = [c[0] if isinstance(c, tuple) else c for c in r.columns]; a.columns = [c[0] if isinstance(c, tuple) else c for c in a.columns]
    d = pd.DataFrame({"High": r.High, "Low": r.Low, "Close": r.Close, "adjClose": a.Close}).dropna()
    d.to_csv(f); return d


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


def trades(d, pos, cost=COST):
    """List of (entry_date, net return) for each completed trade."""
    out, ent = [], None
    for i in range(1, len(pos)):
        if pos.iloc[i] == 1 and pos.iloc[i - 1] == 0: ent = i
        elif pos.iloc[i] == 0 and pos.iloc[i - 1] == 1 and ent is not None:
            out.append((d.index[ent], d.adjClose.iloc[i] / d.adjClose.iloc[ent] - 1 - 2 * cost)); ent = None
    return out


def sh(x): return float(x.mean() / x.std(ddof=1) * math.sqrt(252)) if len(x) > 2 and x.std(ddof=1) > 0 else 0.0


def mdd(t): c = (1 + t).cumprod(); return float((c / c.cummax() - 1).min())


def blo(x):
    rep = bootstrap.gate_report(x, gate=0.5, periods=252); return rep.get("ci", {}).get("lo", rep.get("lo"))


def common(hid, ntests, ex, exs, rf, spy_ret, pred, extra):
    mid = ex.index[len(ex) // 2]
    h1, h2 = ex[ex.index < mid], ex[ex.index >= mid]; s1, s2 = exs[exs.index < mid], exs[exs.index >= mid]
    Y2 = len(h2) / 252; bar = math.sqrt(2 * math.log(ntests)) / math.sqrt(Y2)
    lo, lo_s = blo(h2), blo(s2)
    spy_ex = spy_ret - rf
    r = {"id": hid, "n_tests": ntests, "start": str(ex.index[0].date()), "end": str(ex.index[-1].date()), "split": str(mid.date()),
         "sharpe_h1": sh(h1), "sharpe_h2": sh(h2), "sharpe_full": sh(ex), "boot_lo_h2": lo, "g3_bar": bar,
         "spy_sharpe_h2": sh(spy_ex[h2.index]), "spy_sharpe_full": sh(spy_ex),
         "mdd_h2": mdd(h2 + rf[h2.index]), "spy_mdd_h2": mdd(spy_ret[h2.index]),
         "stress": {"sharpe_h1": sh(s1), "sharpe_h2": sh(s2), "boot_lo_h2": lo_s},
         "cagr_full": float((1 + ex + rf).prod() ** (252 / len(ex)) - 1),
         "spy_cagr_full": float((1 + spy_ret).prod() ** (252 / len(ex)) - 1),
         "cluster_drop_year": cluster_drop(ex.values, ex.index.year.values), **extra}
    g = {"1_both_halves": r["sharpe_h1"] > 0.5 and r["sharpe_h2"] > 0.5, "2_boot_lo": lo is not None and lo > 0,
         "3_bar": r["sharpe_h2"] > bar,
         "4_long_only": r["sharpe_h2"] >= r["spy_sharpe_h2"] and abs(r["mdd_h2"]) <= 0.6 * abs(r["spy_mdd_h2"]),
         "5_stress": r["stress"]["sharpe_h1"] > 0.5 and r["stress"]["sharpe_h2"] > 0.5 and lo_s is not None and lo_s > 0}
    r["gates"] = g; r["VERDICT"] = "CONFIRMED" if all(g.values()) else "NOT CONFIRMED"; r["prediction"] = pred
    (OUT / f"{hid.lower()}_results.json").write_text(json.dumps(r, indent=1, default=float))
    return r


res = {}
spy = load("SPY")
# ---------------- H208
U = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY", "EFA", "EEM", "TLT", "GLD"]
EQ = U[:13]
data = {t: load(t) for t in U}
idx = spy.index[(spy.index >= "1999-01-04") & (spy.index <= "2026-10-07")]
rf = rf_for(idx)
E, ES, per = {}, {}, {}
for t, d in data.items():
    d = d.loc[d.index.intersection(idx)]
    d = d.iloc[1:]  # enters on 2nd trading day
    p = ibs_pos(d); r_ = rf.loc[d.index]
    e, h, _ = sleeve(d, p, COST, r_); es, _, _ = sleeve(d, p, STRESS, r_)
    E[t], ES[t] = e.reindex(idx), es.reindex(idx)
    tl = [x[1] for x in trades(d, p)]
    per[t] = {"start": str(d.index[0].date()), "net_sharpe": sh(e), "trades": len(tl),
              "mean_per_trade": float(np.mean(tl)) if tl else None, "exposure": float(h.mean())}
Edf, ESdf = pd.DataFrame(E), pd.DataFrame(ES)
book, books = Edf.mean(axis=1, skipna=True), ESdf.mean(axis=1, skipna=True)
spy_ret = spy.loc[idx].adjClose.pct_change().fillna(0.0)
# H201 book for correlation
d4 = {t: load(t) for t in ("SPY", "QQQ", "IWM", "DIA")}
i4 = idx
for d in d4.values(): i4 = i4.intersection(d.index)
i4 = i4[i4 >= max(d.index[0] for d in d4.values()) + pd.Timedelta(days=1)]
b4 = sum(sleeve(d.loc[i4], ibs_pos(d.loc[i4]), COST, rf.loc[i4])[0] for d in d4.values()) / 4
eq_sub, ne_sub = Edf[EQ].mean(axis=1, skipna=True), Edf[["TLT", "GLD"]].mean(axis=1, skipna=True)
res["H208"] = common("H208", 195, book, books, rf, spy_ret,
                     "CONFIRMED; H2 0.8-1.2; >=11/13 equity ETFs positive; TLT, GLD < 0.3; corr with H201 0.5-0.75",
                     {"per_etf": per, "n_equity_positive": int(sum(per[t]["net_sharpe"] > 0 for t in EQ)),
                      "corr_with_h201_book": float(book.loc[i4].corr(b4)),
                      "equity_subbook_sharpe": sh(eq_sub.dropna()), "tlt_gld_subbook_sharpe": sh(ne_sub.dropna())})

# ---------------- H209
s = spy[(spy.index >= "1993-02-01") & (spy.index <= "2026-10-07")]
vx = yf.download("^VIX", start="1990-01-01", end=END, auto_adjust=False, progress=False)
vx.columns = [c[0] if isinstance(c, tuple) else c for c in vx.columns]
vx = vx.Close.dropna(); vx.to_frame("vix").to_csv(OUT / "vix_yf_2026-10-10.csv")
med = vx.rolling(252).median()
vix_t = vx.reindex(s.index).ffill(); high = (vx > med).reindex(s.index).ffill().fillna(False).astype(bool)
rf2 = rf_for(s.index)
p195 = ibs_pos(s)
tr195 = trades(s, p195)
rows = [(dt, r_, bool(high.loc[dt]), float(vix_t.loc[dt])) for dt, r_ in tr195]
td = pd.DataFrame(rows, columns=["dt", "r", "high", "vix"]); td["rn"] = td.r / (td.vix / 100 / math.sqrt(252))
rng = np.random.default_rng(209)
H_, L_ = td[td.high].r.values, td[~td.high].r.values
diffs = [rng.choice(H_, len(H_)).mean() - rng.choice(L_, len(L_)).mean() for _ in range(5000)]


def reg(x):
    return {"n": int(len(x)), "mean_per_trade": float(x.r.mean()), "win_rate": float((x.r > 0).mean()),
            "vol_norm_mean": float(x.rn.mean())}


diag = {"HIGH": reg(td[td.high]), "LOW": reg(td[~td.high]),
        "diff_high_minus_low": float(H_.mean() - L_.mean()),
        "diff_ci95": [float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))]}
p9 = ibs_pos(s, high)
e, h, _ = sleeve(s, p9, COST, rf2); es, _, _ = sleeve(s, p9, STRESS, rf2)
e195, _, _ = sleeve(s, p195, COST, rf2)
tr9 = [x[1] for x in trades(s, p9)]
res["H209"] = common("H209", 196, e, es, rf2, s.adjClose.pct_change().fillna(0.0),
                     "diag: HIGH mean > LOW (CI excl 0), vol-norm within 30%; strategy NOT CONFIRMED, H2 within +/-0.2 of 0.93, fails G3 or G4",
                     {"diagnostic": diag, "trades": len(tr9), "h195_trades": len(tr195), "exposure": float(h.mean()),
                      "win_payoff": win_payoff(np.array(tr9)), "h195_sharpe_full_same_code": sh(e195),
                      "h195_sharpe_h2_same_code": sh(e195[e195.index >= e.index[len(e) // 2]])})
print(json.dumps(res, indent=1, default=float))
