#!/usr/bin/env python3
"""H206 (multiple-testing hurdles for H195/H201) + H207 (IBS pre/post 2008), registered 43477aa. One run."""
import json, math, pathlib
from statistics import NormalDist
import numpy as np, pandas as pd
HERE = pathlib.Path(__file__).resolve().parent; G = HERE.parent; OUT = HERE / "results"
if any((OUT / f"h20{k}_results.json").exists() for k in (6, 7)):
    raise SystemExit("results exist: one run per ID")
COST = 0.0001; N = NormalDist()

ff = pd.read_csv(G / "phase3/data/F-F_Research_Data_Factors.csv", skiprows=4, nrows=1200)
ff = ff[ff.iloc[:, 0].astype(str).str.strip().str.len() == 6]
ff.columns = ["ym", "mkt", "smb", "hml", "rf"]; ff["ym"] = ff.ym.astype(str).str.strip(); ff["rf"] = ff.rf.astype(float) / 100
RFM = dict(zip(ff.ym, ff.rf)); LAST = ff.rf.iloc[-1]


def rf_for(idx):
    ym = idx.strftime("%Y%m"); dim = pd.Series(1, index=idx).groupby(ym).transform("sum")
    return pd.Series([RFM.get(m, LAST) for m in ym], index=idx) / dim


def ibs_pos(d):
    ibs = ((d.Close - d.Low) / (d.High - d.Low)).where(d.High > d.Low, 0.5)
    p, s = 0, []
    for v in ibs:
        if p == 0 and v < 0.2: p = 1
        elif p == 1 and v > 0.8: p = 0
        s.append(p)
    return pd.Series(s, index=d.index)


def excess(d, rf):
    pos = ibs_pos(d); ret = d.adjClose.pct_change().fillna(0.0)
    held = pos.shift(1).fillna(0); tr = pos.diff().abs().fillna(pos.iloc[0])
    return held * ret + (1 - held) * rf - tr * COST - rf, held, ret, pos


def load(t):
    d = pd.read_csv(OUT / f"{t.lower()}_yf_2026-10-08.csv", index_col=0, parse_dates=True)
    return d[d.index >= "1993-02-01"] if t == "SPY" else d


def tstats(x, L=10):
    x = np.asarray(x, float); T = len(x); m = x.mean(); z = x - m
    g0 = (z * z).mean(); lrv = g0 + 2 * sum((1 - k / (L + 1)) * (z[:-k] * z[k:]).mean() for k in range(1, L + 1))
    return {"n": T, "years": T / 252, "mean_bp": m * 1e4, "sharpe_ann": m / x.std(ddof=1) * math.sqrt(252),
            "t_plain": m / (x.std(ddof=1) / math.sqrt(T)), "t_nw10": m / math.sqrt(lrv / T)}


H = {"hlz_fixed": 3.0, "bonf_M194": N.inv_cdf(1 - 0.05 / 194), "bonf_M27": N.inv_cdf(1 - 0.05 / 27)}

# ---- H206
spy = load("SPY"); rf_s = rf_for(spy.index)
ex195, held195, ret_s, _ = excess(spy, rf_s)
mid195 = spy.index[len(spy) // 2]
data = {t: load(t) for t in ("SPY", "QQQ", "IWM", "DIA")}
start = max(d.index[0] for d in data.values()) + pd.Timedelta(days=1)
idx = data["SPY"].index
for d in data.values(): idx = idx.intersection(d.index)
idx = idx[idx >= start]; rf_b = rf_for(idx)
book = sum(excess(d.loc[idx], rf_b)[0] for d in data.values()) / 4
mid201 = idx[len(idx) // 2]
res6 = {"id": "H206", "hurdles": H, "series": {}}
for name, ex, mid in (("H195", ex195, mid195), ("H201", book, mid201)):
    full, h2 = tstats(ex.values), tstats(ex[ex.index >= mid].values)
    res6["series"][name] = {"split": str(mid.date()), "full": full, "h2": h2,
                            "pass_full": {k: full["t_nw10"] > v for k, v in H.items()},
                            "pass_h2": {k: h2["t_nw10"] > v for k, v in H.items()},
                            "SURVIVES": full["t_nw10"] > H["bonf_M194"],
                            "HOLDOUT_SURVIVES": h2["t_nw10"] > H["bonf_M194"]}
res6["prediction"] = "H195 full SURVIVES, H2 survives; H201 full SURVIVES, H2 FAILS 3.47 (just below); NW t >= plain t for H195"
s6 = res6["series"]
res6["prediction_check"] = {"H195_full": s6["H195"]["SURVIVES"], "H195_h2": s6["H195"]["HOLDOUT_SURVIVES"],
                            "H201_full": s6["H201"]["SURVIVES"], "H201_h2_fails": not s6["H201"]["HOLDOUT_SURVIVES"],
                            "H195_nw_ge_plain": s6["H195"]["full"]["t_nw10"] >= s6["H195"]["full"]["t_plain"]}
(OUT / "h206_results.json").write_text(json.dumps(res6, indent=1, default=float))

# ---- H207
rng = np.random.default_rng(207)


def boot_means(x, n=5000, block=10):
    x = np.asarray(x, float); T = len(x); ar = np.arange(T); out = np.empty(n)
    for k in range(n):
        st = rng.random(T) < 1 / block; st[0] = True
        bid = np.cumsum(st) - 1; first = np.flatnonzero(st); org = rng.integers(T, size=len(first))
        out[k] = x[(org[bid] + ar - first[bid]) % T].mean()
    return out


on = spy.adjOpen / spy.adjClose.shift(1) - 1; idr = spy.adjClose / spy.adjOpen - 1; cc = spy.adjClose.pct_change()
Hd = held195 == 1; ok = on.notna()
eras = {"PRE": (spy.index <= "2007-12-31"), "POST": (spy.index >= "2008-01-01")}
res7 = {"id": "H207", "eras": {}}
draws = {}
for e, m in eras.items():
    m = pd.Series(m, index=spy.index) & ok
    h, a = m & Hd, m
    lo_h, li_h = np.log1p(on[h]).sum(), np.log1p(idr[h]).sum(); lo_a, li_a = np.log1p(on[a]).sum(), np.log1p(idr[a]).sum()
    res7["eras"][e] = {"days": int(m.sum()), "held_days": int(h.sum()),
                       "h195_sharpe": float(ex195[m].mean() / ex195[m].std(ddof=1) * math.sqrt(252)),
                       "held_on_bp": float(on[h].mean() * 1e4), "held_id_bp": float(idr[h].mean() * 1e4), "held_cc_bp": float(cc[h].mean() * 1e4),
                       "held_on_share": float(lo_h / (lo_h + li_h)),
                       "all_on_bp": float(on[a].mean() * 1e4), "all_id_bp": float(idr[a].mean() * 1e4),
                       "all_on_share": float(lo_a / (lo_a + li_a)) if (lo_a + li_a) != 0 else None}
    draws[e] = {"on": boot_means(on[h].values), "id": boot_means(idr[h].values), "cc": boot_means(cc[h].values)}
res7["diff_post_minus_pre_bp"] = {}
for leg in ("on", "id", "cc"):
    dd = (draws["POST"][leg] - draws["PRE"][leg]) * 1e4
    key = {"on": "held_on_bp", "id": "held_id_bp", "cc": "held_cc_bp"}[leg]
    res7["diff_post_minus_pre_bp"][leg] = {"point": res7["eras"]["POST"][key] - res7["eras"]["PRE"][key],
                                           "ci95": [float(np.percentile(dd, 2.5)), float(np.percentile(dd, 97.5))]}
E = res7["eras"]; D = res7["diff_post_minus_pre_bp"]
res7["prediction"] = "held-day legs no era change (CIs incl 0); all-days intraday higher POST; all-days overnight share falls POST"
res7["prediction_check"] = {"held_on_ci_incl_0": D["on"]["ci95"][0] <= 0 <= D["on"]["ci95"][1],
                            "held_id_ci_incl_0": D["id"]["ci95"][0] <= 0 <= D["id"]["ci95"][1],
                            "all_id_higher_post": E["POST"]["all_id_bp"] > E["PRE"]["all_id_bp"],
                            "all_on_share_falls_post": (E["POST"]["all_on_share"] or 0) < (E["PRE"]["all_on_share"] or 0)}
(OUT / "h207_results.json").write_text(json.dumps(res7, indent=1, default=float))
print(json.dumps({"H206": res6, "H207": res7}, indent=1, default=float))
