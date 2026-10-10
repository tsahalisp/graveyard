#!/usr/bin/env python3
"""H200 Williams %R(2) replication on ES RTH bars (registered after ae550fb; see HYPOTHESES H200). One run."""
import json, math, pathlib, sys
import numpy as np, pandas as pd
HERE = pathlib.Path(__file__).resolve().parent
FIRM = HERE.parent.parent / "firm"
sys.path.insert(0, str(FIRM))
import bootstrap  # noqa: E402
OUT = HERE / "results"; OUT.mkdir(exist_ok=True)
if (OUT / "h200_results.json").exists():
    sys.exit("results exist: one run per ID")
POINT = 50.0; COST, STRESS = 29.48, 40.0

b = pd.read_csv(FIRM / "data/es_1m_continuous.csv")
ts = pd.to_datetime(b.ts_utc, utc=True).dt.tz_convert("America/New_York")
b["date"] = ts.dt.date; b["mod"] = ts.dt.hour * 60 + ts.dt.minute
b = b[(b["mod"] >= 570) & (b["mod"] <= 959)]
g = b.groupby("date")
day = pd.DataFrame({"H": g.high.max(), "L": g.low.min(), "n": g.size(),
                    "has959": g["mod"].max() == 959, "nctr": g.contract.nunique()})
last = b[b["mod"] == 959].set_index("date")
day["C"] = last.close; day["ctr"] = last.contract
keep = day[(day.has959) & (day.n >= 380) & (day.nctr == 1)].copy()
excluded = int(len(day) - len(keep))
keep.index = pd.to_datetime(keep.index)
same = keep.ctr.eq(keep.ctr.shift(1))
ret = (keep.C / keep.C.shift(1) - 1).where(same, 0.0).fillna(0.0)
rolls = int((~same).sum() - 1)
hh = keep.H.rolling(2).max(); ll = keep.L.rolling(2).min()
wr = (-100 * (hh - keep.C) / (hh - ll)).where(hh > ll, -50.0)
p, pos = 0, []
for i in range(len(keep)):
    w = wr.iloc[i]
    if p == 0 and w < -90: p = 1
    elif p == 1 and (keep.C.iloc[i] > keep.H.iloc[i - 1] or w > -30): p = 0
    pos.append(p)
pos = pd.Series(pos, index=keep.index)
held = pos.shift(1).fillna(0)
chg = pos.diff().abs().fillna(pos.iloc[0])
notional = keep.C * POINT


def strat(cost_rt):
    return held * ret - chg * (cost_rt / 2) / notional


def sh(x):
    return float(x.mean() / x.std(ddof=1) * math.sqrt(252)) if x.std(ddof=1) > 0 else 0.0


def mdd(x):
    c = (1 + x).cumprod(); return float((c / c.cummax() - 1).min())


def lo(x):
    rep = bootstrap.gate_report(x, gate=0.5, periods=252)
    return rep.get("ci", {}).get("lo", rep.get("lo")), rep


r, rs = strat(COST), strat(STRESS)
mid = keep.index[len(keep) // 2]
h1, h2 = r[r.index < mid], r[r.index >= mid]
lo_r, rep = lo(r); lo_s, _ = lo(rs)
n_tr = int((pos.diff() == 1).sum() + (pos.iloc[0] == 1))
res = {"id": "H200", "days": len(keep), "excluded_days": excluded, "rolls": rolls,
       "start": str(keep.index[0].date()), "end": str(keep.index[-1].date()), "split": str(mid.date()),
       "trades": n_tr, "exposure": float(held.mean()),
       "sharpe_full": sh(r), "sharpe_h1": sh(h1), "sharpe_h2": sh(h2), "boot_lo_full": lo_r,
       "stress_mean_daily": float(rs.mean()), "stress_boot_lo": lo_s, "stress_sharpe": sh(rs),
       "bh_sharpe": sh(ret), "mdd": mdd(r), "bh_mdd": mdd(ret),
       "net_usd_per_contract": float((r * notional).sum()),
       "avg_trade_gross_pct": float((held * ret).sum() / max(n_tr, 1))}
gates = {"R1_ci": lo_r is not None and lo_r > 0,
         "R2_halves": res["sharpe_h1"] > 0.5 and res["sharpe_h2"] > 0.5,
         "R3_stress": res["stress_mean_daily"] > 0 and lo_s is not None and lo_s > 0,
         "R4_long_only": res["sharpe_full"] >= res["bh_sharpe"] and abs(res["mdd"]) <= 0.6 * abs(res["bh_mdd"])}
res["gates"] = gates
res["VERDICT"] = "REPLICATES" if all(gates.values()) else "DOES NOT REPLICATE"
res["prediction"] = "R1-R3 pass; R4 borderline (DD ratio 0.55-0.65)"
(OUT / "h200_results.json").write_text(json.dumps(res, indent=1, default=float))
print(json.dumps(res, indent=1, default=float))
