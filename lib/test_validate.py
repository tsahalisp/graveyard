"""Two-sided checks for validate.py, portfolio.py, costs.py.
Each tool must stay quiet on noise AND catch a planted effect. Exit 0 = all pass."""
import sys, pathlib, math
import numpy as np, pandas as pd
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from validate import (walk_forward, sharpe, psr, expected_max_sr, deflated_sharpe,
                      pbo_cscv, max_drawdown, bootstrap_drawdown, size_for_drawdown)
from portfolio import inverse_vol_weights, combine, stats
from costs import CONTRACTS

R = []
def check(name, cond, detail=""):
    R.append(bool(cond)); print(f"  {'PASS' if cond else 'FAIL'}  {name}  {detail}")

rng = np.random.default_rng(42)

print("walk-forward")
n = 2000; x = rng.normal(size=n)
fit = lambda X, y: np.polyfit(X[:, 0], y, 1)
pred = lambda m, X: np.polyval(m, X[:, 0])
y_real = 0.3 * x + rng.normal(size=n)
p = walk_forward(x[:, None], y_real, fit, pred, min_train=250, step=50)
ok = ~np.isnan(p); c_real = np.corrcoef(p[ok], y_real[ok])[0, 1]
check("finds a planted slope out of sample", c_real > 0.2, f"corr {c_real:+.3f}")
y_noise = rng.normal(size=n)
p = walk_forward(x[:, None], y_noise, fit, pred, min_train=250, step=50)
c_noise = np.corrcoef(p[ok], y_noise[ok])[0, 1]
check("stays near zero on noise", abs(c_noise) < 0.08, f"corr {c_noise:+.3f}")
seen = []
def spy_fit(X, y): seen.append(len(y)); return fit(X, y)
walk_forward(x[:, None], y_real, spy_fit, pred, min_train=250, step=50)
check("each fit sees only rows before its test block", seen == list(range(250, n, 50)))
check("warm-up rows are NaN", np.isnan(p[:250]).all())

print("PSR / deflated Sharpe")
T = 252; reps = 3000
null_psr = np.array([psr(rng.normal(0, 1, T)) for _ in range(reps)])
fp = (null_psr > 0.95).mean()
check("PSR false-positive rate ~5% on a zero-SR null", 0.035 < fp < 0.065, f"{fp:.3f}")
N = 50; T2 = 500
maxes = [max(sharpe(rng.normal(0, 1, T2)) for _ in range(N)) for _ in range(300)]
emp, theo = float(np.mean(maxes)), expected_max_sr(N, 1 / (T2 - 1))
check("E[max SR] formula matches simulation (N=50)", abs(emp - theo) / theo < 0.10, f"sim {emp:.4f} vs formula {theo:.4f}")
best_noise = []
for _ in range(200):
    trials = [rng.normal(0, 1, T2) for _ in range(N)]
    best_noise.append(deflated_sharpe(max(trials, key=sharpe), N))
fp_dsr = (np.array(best_noise) > 0.95).mean()
check("DSR rejects the best of 50 noise strategies", fp_dsr < 0.08, f"pass rate {fp_dsr:.3f}")
real = rng.normal(0.25, 1, T2)
check("DSR keeps a strong planted strategy (SR 0.25/period)", deflated_sharpe(real, N) > 0.95, f"{deflated_sharpe(real, N):.3f}")

print("PBO (CSCV)")
# PBO from ONE noise search ranges ~0.1-0.9 (measured 2026-10-06: 200 draws, mean
# 0.482, sd 0.198). It holds in expectation, so test the mean of 100 draws (SE ~0.02,
# bound +/-0.12 = 6 SE) and never read a single PBO alone.
pb = [pbo_cscv(rng.normal(0, 1, (1000, 20)), S=10)[0] for _ in range(100)]
check("PBO averages ~0.5 across noise searches", 0.38 < np.mean(pb) < 0.62, f"mean {np.mean(pb):.2f}, range {min(pb):.2f}-{max(pb):.2f}")
M = rng.normal(0, 1, (1000, 20))
M2 = M.copy(); M2[:, 7] += 0.2
pbo_real, _ = pbo_cscv(M2, S=10)
check("PBO ~0 when one variant is really better", pbo_real < 0.1, f"{pbo_real:.2f}")

print("drawdown & sizing")
check("max_drawdown on a hand example", max_drawdown([1, -2, 1, -3, 4]) == 4.0)
check("max_drawdown counts a loss from the start", max_drawdown([-2, 1]) == 2.0)
pnl = rng.normal(5, 100, 750)
q1, _ = bootstrap_drawdown(pnl, B=800, seed=1)
q2, _ = bootstrap_drawdown(2 * pnl, B=800, seed=1)
check("bootstrap drawdown scales linearly with size", abs(q2 / q1 - 2) < 1e-9, f"{q2 / q1:.6f}")
check("95th-pct drawdown >= realised drawdown is typical", q1 >= 0.8 * max_drawdown(pnl), f"q95 {q1:.0f} vs realised {max_drawdown(pnl):.0f}")
units, _ = size_for_drawdown(pnl, 5000, B=800, seed=1)
check("size_for_drawdown hits the budget", abs(units * q1 - 5000) < 1e-6, f"{units:.2f} units")

print("portfolio")
idx = pd.bdate_range("2015-01-01", periods=2520)
Rt = pd.DataFrame({"a": rng.normal(0.0004, 0.01, 2520), "b": rng.normal(0.0004, 0.01, 2520)}, index=idx)
W = inverse_vol_weights(Rt, window=63)
check("weights are lagged (first window+1 rows NaN)", W.iloc[:63].isna().all().all() and W.iloc[63:].notna().all().all())
sa = stats(Rt["a"])["sharpe_ann"]; sb = stats(Rt["b"])["sharpe_ann"]; sp = stats(combine(Rt, W))["sharpe_ann"]
check("two independent equal sleeves combine to ~sqrt(2) x Sharpe", 1.15 < sp / ((sa + sb) / 2) < 1.75, f"{sp:.2f} vs {(sa + sb) / 2:.2f}")

print("costs")
mes, es = CONTRACTS["MES"], CONTRACTS["ES"]
check("MES fees round trip = 2 x 1.11", abs(mes.round_trip(0) - 2.22) < 1e-9, f"{mes.round_trip(0):.2f}")
check("ES fees round trip = 2 x 2.24 (IBKR stated total)", abs(es.round_trip(0) - 4.48) < 1e-9, f"{es.round_trip(0):.2f}")
check("MES 1-tick round trip = 2.22 + 2.50", abs(mes.round_trip(1) - 4.72) < 1e-9, f"{mes.round_trip(1):.2f}")

print("standard verdict rows (2026-10-10)")
from validate import cluster_drop, win_payoff, bounce_check
# cluster_drop: all profit in one month -> flags; spread profit -> does not
months = np.repeat(np.arange(24), 20)
pnl = rng.normal(-0.1, 1, 480); pnl[months == 7] += 4.0   # losing book rescued by one month
cd = cluster_drop(pnl, months)
check("cluster_drop finds the planted month and the sign flip", cd["top_cluster"] == 7 and cd["sign_flips"], f"top {cd['top_cluster']} share {cd['top_share']:.2f}")
cd2 = cluster_drop(rng.normal(0.3, 1, 480), months)
check("cluster_drop stays quiet on an even edge", not cd2["sign_flips"] and cd2["top_share"] < 0.25, f"share {cd2['top_share']:.2f}")
# win_payoff: the 80%-favourite example (8 x +0.15, 2 x -0.85) loses
wp = win_payoff([0.15] * 8 + [-0.85] * 2)
check("win_payoff: 80% win rate, payoff 0.18 is negative", wp["win_rate"] == 0.8 and wp["edge_wr"] < 0 and abs(wp["expectancy"] + 0.05) < 1e-12, f"breakeven {wp['breakeven_wr']:.2f}")
wp2 = win_payoff([2.0] * 4 + [-1.0] * 6)
check("win_payoff: 40% win rate, payoff 2 is positive", wp2["edge_wr"] > 0 and wp2["expectancy"] > 0, f"edge {wp2['edge_wr']:+.3f}")
# bounce_check: random-walk mid, trades alternate randomly at bid/ask -> bounce
mid = 100 * np.exp(np.cumsum(rng.normal(0, 1e-4, 5000)))
side = rng.choice([-1, 1], 5000); trade = mid + side * 0.01
bc = bounce_check(trade, mid)
check("bounce_check flags pure bid-ask bounce", bc["looks_like_bounce"], f"ac trade {bc['ac_trade']:+.3f}, mid {bc['ac_mid']:+.3f}")
r = np.zeros(5000); e = rng.normal(0, 1e-4, 5000)
for t in range(1, 5000): r[t] = -0.3 * r[t - 1] + e[t]
mid2 = 100 * np.exp(np.cumsum(r))
bc2 = bounce_check(mid2, mid2)
check("bounce_check does not call real mid reversion a bounce", bc2["reversion_on_mids"] and not bc2["looks_like_bounce"], f"ac mid {bc2['ac_mid']:+.3f}")

print("Lo (2002) annualisation (2026-10-10)")
from validate import lo_annualize
iid = rng.normal(0.0005, 0.01, 20000)
lo1 = lo_annualize(iid)
check("lo_annualize ~ sqrt(q) on iid returns", abs(lo1["ratio_to_sqrt_q"] - 1) < 0.05, f"ratio {lo1['ratio_to_sqrt_q']:.3f}")
e = rng.normal(0, 0.01, 20000); ar = np.zeros(20000)
for t in range(1, 20000): ar[t] = 0.2 * ar[t - 1] + e[t]
lo2 = lo_annualize(ar + 0.0005)
theory = 1 / math.sqrt((1 + 0.2) / (1 - 0.2))   # long-q limit for AR(1), rho=0.2
check("lo_annualize shrinks sqrt(q) under positive AR(1)", lo2["ratio_to_sqrt_q"] < 0.9 and abs(lo2["ratio_to_sqrt_q"] - theory) < 0.05, f"ratio {lo2['ratio_to_sqrt_q']:.3f} vs theory {theory:.3f}")

print(f"\n{sum(R)}/{len(R)} passed")
sys.exit(0 if all(R) else 1)
