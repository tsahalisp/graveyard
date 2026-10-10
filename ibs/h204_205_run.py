#!/usr/bin/env python3
"""H204 (IBS overnight/intraday decomposition, diagnostic) + H205 (IBS overnight-only), registered 99a43ae. One run."""
import json, math, pathlib, sys
import numpy as np, pandas as pd
HERE = pathlib.Path(__file__).resolve().parent; G = HERE.parent; FIRM = G.parent / "firm"
sys.path.insert(0, str(FIRM))
import bootstrap  # noqa: E402
OUT = HERE / "results"
if any((OUT / f"h20{k}_results.json").exists() for k in (4, 5)):
    sys.exit("results exist: one run per ID")
N_TESTS = 194; COST, STRESS = 0.0001, 0.0005
rng = np.random.default_rng(204)

# ---------- SPY data and H195 position (identical to h195_h196_run.py)
d = pd.read_csv(OUT / "spy_yf_2026-10-08.csv", index_col=0, parse_dates=True)
d = d[d.index >= "1993-02-01"]
ibs = ((d.Close - d.Low) / (d.High - d.Low)).where(d.High > d.Low, 0.5)
p, pos = 0, []
for v in ibs:
    if p == 0 and v < 0.2: p = 1
    elif p == 1 and v > 0.8: p = 0
    pos.append(p)
pos = pd.Series(pos, index=d.index); held = pos.shift(1).fillna(0)
cc = d.adjClose.pct_change()
on = d.adjOpen / d.adjClose.shift(1) - 1
idr = d.adjClose / d.adjOpen - 1
chk = float(((1 + on) * (1 + idr) - 1 - cc).abs().max())
mid = d.index[len(d) // 2]

ff = pd.read_csv(G / "phase3/data/F-F_Research_Data_Factors.csv", skiprows=4, nrows=1200)
ff = ff[ff.iloc[:, 0].astype(str).str.strip().str.len() == 6]
ff.columns = ["ym", "mkt", "smb", "hml", "rf"]; ff["ym"] = ff.ym.astype(str).str.strip(); ff["rf"] = ff.rf.astype(float) / 100
RFM = dict(zip(ff.ym, ff.rf)); ym = d.index.strftime("%Y%m")
rf = pd.Series([RFM.get(m, ff.rf.iloc[-1]) for m in ym], index=d.index) / pd.Series(1, index=d.index).groupby(ym).transform("sum")


def sboot_ci(x, block=10, n=5000):
    x = np.asarray(x, float); T = len(x); means = np.empty(n); pr = 1 / block; ar = np.arange(T)
    for k in range(n):
        starts = rng.random(T) < pr; starts[0] = True
        bid = np.cumsum(starts) - 1                     # block number of each slot
        first = np.flatnonzero(starts)                  # slot where each block starts
        origin = rng.integers(T, size=len(first))       # random origin of each block
        idx = (origin[bid] + ar - first[bid]) % T
        means[k] = x[idx].mean()
    return [float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))]


def legs(mask, o, i, c, boot=False):
    o, i, c = o[mask].dropna(), i[mask].dropna(), c[mask].dropna()
    lo_, li_ = np.log1p(o).sum(), np.log1p(i).sum()
    r = {"days": int(len(o)), "mean_on_bp": float(o.mean() * 1e4), "mean_id_bp": float(i.mean() * 1e4),
         "mean_cc_bp": float(c.mean() * 1e4), "sum_log_on": float(lo_), "sum_log_id": float(li_),
         "on_share_of_log": float(lo_ / (lo_ + li_)) if (lo_ + li_) != 0 else None,
         "hit_on": float((o > 0).mean()), "hit_id": float((i > 0).mean())}
    if boot:
        r["ci_on_bp"] = [v * 1e4 for v in sboot_ci(o.values)]
        r["ci_id_bp"] = [v * 1e4 for v in sboot_ci(i.values)]
    return r


H = held == 1
res4 = {"id": "H204", "start": str(d.index[0].date()), "end": str(d.index[-1].date()), "split": str(mid.date()),
        "identity_max_abs_err": chk, "spy": {}}
for name, rmask in (("full", d.index >= d.index[0]), ("h1", d.index < mid), ("h2", d.index >= mid)):
    m = pd.Series(rmask, index=d.index) & on.notna()
    res4["spy"][name] = {"held": legs(m & H, on, idr, cc, boot=True), "all": legs(m, on, idr, cc),
                         "flat": legs(m & ~H, on, idr, cc)}

# ---------- ES replication (H197 data and day filter)
b = pd.read_csv(FIRM / "data/es_1m_continuous.csv")
ts = pd.to_datetime(b.ts_utc, utc=True).dt.tz_convert("America/New_York")
b["date"] = ts.dt.date; b["mod"] = ts.dt.hour * 60 + ts.dt.minute
b = b[(b["mod"] >= 570) & (b["mod"] <= 959)]
g = b.groupby("date")
day = pd.DataFrame({"H": g.high.max(), "L": g.low.min(), "n": g.size(), "has959": g["mod"].max() == 959,
                    "has570": g["mod"].min() == 570, "nctr": g.contract.nunique()})
l9 = b[b["mod"] == 959].set_index("date"); f0 = b[b["mod"] == 570].set_index("date")
day["C"] = l9.close; day["ctr"] = l9.contract; day["O"] = f0.open
keep = day[(day.has959) & (day.n >= 380) & (day.nctr == 1)].copy(); keep.index = pd.to_datetime(keep.index)
same = keep.ctr.eq(keep.ctr.shift(1))
eibs = ((keep.C - keep.L) / (keep.H - keep.L)).where(keep.H > keep.L, 0.5)
p, ep = 0, []
for v in eibs:
    if p == 0 and v < 0.2: p = 1
    elif p == 1 and v > 0.8: p = 0
    ep.append(p)
eheld = pd.Series(ep, index=keep.index).shift(1).fillna(0) == 1
valid = same & keep.has570
eon = (keep.O / keep.C.shift(1) - 1).where(valid); eid = (keep.C / keep.O - 1).where(valid)
ecc = (keep.C / keep.C.shift(1) - 1).where(valid)
res4["es"] = {"start": str(keep.index[0].date()), "end": str(keep.index[-1].date()),
              "dropped_roll_or_no_open": int((~valid).sum()),
              "held": legs(eheld & valid, eon, eid, ecc, boot=True), "all": legs(valid, eon, eid, ecc),
              "flat": legs(~eheld & valid, eon, eid, ecc)}
s_ = res4["spy"]["full"]["held"]; e_ = res4["es"]["held"]
res4["prediction"] = "overnight share of held-day log return >50% (55-75%); overnight CI excludes 0; intraday positive with CI incl 0; ES same signs"
res4["prediction_check"] = {"on_share_gt_50": s_["on_share_of_log"] is not None and s_["on_share_of_log"] > 0.5,
                            "on_share_in_55_75": s_["on_share_of_log"] is not None and 0.55 <= s_["on_share_of_log"] <= 0.75,
                            "on_ci_excl_0": s_["ci_on_bp"][0] > 0, "id_pos": s_["mean_id_bp"] > 0,
                            "id_ci_incl_0": s_["ci_id_bp"][0] <= 0 <= s_["ci_id_bp"][1],
                            "es_same_signs": (e_["mean_on_bp"] > 0) == (s_["mean_on_bp"] > 0)
                            and (e_["mean_id_bp"] > 0) == (s_["mean_id_bp"] > 0)}
(OUT / "h204_results.json").write_text(json.dumps(res4, indent=1, default=float))

# ---------- H205: overnight-only on H195 held days
INTRA = 6.5 / 24   # share of the day's rf earned in cash while flat intraday (convention, disclosed)


def h205(cost):
    tot = pd.Series(np.where(H, on.fillna(0) + INTRA * rf - 2 * cost, rf), index=d.index)
    return tot - rf


def sh(x): return float(x.mean() / x.std(ddof=1) * math.sqrt(252)) if x.std(ddof=1) > 0 else 0.0


def mdd(t): c = (1 + t).cumprod(); return float((c / c.cummax() - 1).min())


def blo(x):
    rep = bootstrap.gate_report(x, gate=0.5, periods=252); return rep.get("ci", {}).get("lo", rep.get("lo"))


ex, exs = h205(COST), h205(STRESS)
h1, h2 = ex[ex.index < mid], ex[ex.index >= mid]; s1, s2 = exs[exs.index < mid], exs[exs.index >= mid]
bar = math.sqrt(2 * math.log(N_TESTS)) / math.sqrt(len(h2) / 252)
lo, lo_s = blo(h2), blo(s2); ret = cc.fillna(0.0); spy_ex = ret - rf
r = {"id": "H205", "split": str(mid.date()), "held_days": int(H.sum()), "sharpe_h1": sh(h1), "sharpe_h2": sh(h2),
     "sharpe_full": sh(ex), "boot_lo_h2": lo, "g3_bar": bar, "spy_sharpe_h2": sh(spy_ex[h2.index]),
     "mdd_h2": mdd(h2 + rf[h2.index]), "spy_mdd_h2": mdd(ret[h2.index]),
     "stress": {"sharpe_h1": sh(s1), "sharpe_h2": sh(s2), "boot_lo_h2": lo_s},
     "cagr_full": float((1 + ex + rf).prod() ** (252 / len(ex)) - 1), "intraday_rf_fraction": INTRA}
r["gates"] = {"1_both_halves": r["sharpe_h1"] > 0.5 and r["sharpe_h2"] > 0.5, "2_boot_lo": lo is not None and lo > 0,
              "3_bar": r["sharpe_h2"] > bar,
              "4_long_only": r["sharpe_h2"] >= r["spy_sharpe_h2"] and abs(r["mdd_h2"]) <= 0.6 * abs(r["spy_mdd_h2"]),
              "5_stress": r["stress"]["sharpe_h1"] > 0.5 and r["stress"]["sharpe_h2"] > 0.5 and lo_s is not None and lo_s > 0}
r["VERDICT"] = "CONFIRMED" if all(r["gates"].values()) else "NOT CONFIRMED"
r["prediction"] = "passes 1,2 at 1bp; FAILS 5 (stress); gate 4 Sharpe below SPY"
(OUT / "h205_results.json").write_text(json.dumps(r, indent=1, default=float))
print(json.dumps({"H204": res4, "H205": r}, indent=1, default=float))
