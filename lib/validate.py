"""Phase 0 validation toolkit (2026-10-06). Closes the gaps found in the
validation audit: walk-forward, Deflated Sharpe, PBO, bootstrap drawdown sizing.

Every function is checked two ways in test_validate.py: it must stay quiet on
pure noise AND it must find a planted effect. numpy only (no scipy dependency).

Conventions: Sharpe ratios here are PER PERIOD (not annualised) unless a name
says _ann. Kurtosis is RAW (normal = 3). P&L series are ADDITIVE (dollars or
points per period), which is what a futures book is.
"""
from itertools import combinations
from statistics import NormalDist
import math
import numpy as np

_N = NormalDist()
EULER_GAMMA = 0.5772156649015329


# ---------------------------------------------------------------- walk-forward
def walk_forward(X, y, fit, predict, min_train, step, expanding=True):
    """Re-fit every `step` rows on past data only; predict the next block.

    fit(X_train, y_train) -> model ; predict(model, X_test) -> array.
    predict() never receives y, and fit() never receives a row at or after the
    block it is predicting, so lookahead cannot be written through this call.
    Returns an array the length of y: NaN during warm-up, OOS predictions after.
    """
    X = np.asarray(X, float); y = np.asarray(y, float); n = len(y)
    if X.shape[0] != n:
        raise ValueError("X and y length differ")
    if min_train < 2 or step < 1 or min_train >= n:
        raise ValueError("need 2 <= min_train < len(y) and step >= 1")
    out = np.full(n, np.nan)
    for t0 in range(min_train, n, step):
        t1 = min(t0 + step, n)
        lo = 0 if expanding else t0 - min_train
        model = fit(X[lo:t0], y[lo:t0])
        p = np.asarray(predict(model, X[t0:t1]), float)
        if p.shape[0] != t1 - t0:
            raise ValueError("predict returned the wrong number of rows")
        out[t0:t1] = p
    return out


# ------------------------------------------------- probabilistic / deflated SR
def sharpe(x):
    x = np.asarray(x, float); s = x.std(ddof=1)
    return float(x.mean() / s) if s > 0 else 0.0


def _moments(x):
    x = np.asarray(x, float); m = x.mean(); s = x.std(ddof=0)
    z = (x - m) / s
    return float((z ** 3).mean()), float((z ** 4).mean())


def psr(x, sr_star=0.0):
    """Probabilistic Sharpe ratio: P(true SR > sr_star) given the sample,
    allowing for skew and fat tails (Bailey & Lopez de Prado 2012)."""
    x = np.asarray(x, float); T = len(x); sr = sharpe(x); sk, ku = _moments(x)
    den = 1 - sk * sr + (ku - 1) / 4 * sr ** 2
    if den <= 0:
        raise ValueError("non-positive PSR denominator; moments are degenerate")
    return _N.cdf((sr - sr_star) * math.sqrt(T - 1) / math.sqrt(den))


def expected_max_sr(n_trials, var_sr):
    """E[max SR] across n_trials independent zero-skill trials whose sample
    Sharpe ratios have variance var_sr (False Strategy Theorem)."""
    if n_trials < 2:
        return 0.0
    a = _N.inv_cdf(1 - 1 / n_trials); b = _N.inv_cdf(1 - 1 / (n_trials * math.e))
    return math.sqrt(var_sr) * ((1 - EULER_GAMMA) * a + EULER_GAMMA * b)


def deflated_sharpe(x, n_trials, var_sr=None):
    """PSR against the Sharpe you would expect from the BEST of n_trials pure-
    noise attempts. var_sr defaults to 1/(T-1), the null variance of a sample SR.
    Report this next to the permutation p-value; > 0.95 is the usual bar."""
    x = np.asarray(x, float)
    v = var_sr if var_sr is not None else 1.0 / (len(x) - 1)
    return psr(x, expected_max_sr(n_trials, v))


# ------------------------------------------------------------------ PBO / CSCV
def pbo_cscv(M, S=10):
    """Probability of backtest overfitting via combinatorially symmetric cross-
    validation (Bailey, Borwein, Lopez de Prado, Zhu 2015).

    M: T x N array, column j = per-period P&L of variant j (the WHOLE search).
    Splits rows into S blocks; for every half/half split picks the in-sample
    best variant and records its out-of-sample rank. PBO = share of splits
    where that pick lands at or below the OOS median. ~0.5 = pure selection luck.
    One search gives a NOISY PBO (0.08-0.92 across 40 pure-noise draws, mean 0.49);
    report it with the permutation p and DSR, never as the deciding number.
    """
    M = np.asarray(M, float); T, N = M.shape
    if S % 2 or S < 4 or N < 2:
        raise ValueError("S must be even and >= 4, N >= 2")
    blocks = np.array_split(np.arange(T), S)
    lam = []
    for ins in combinations(range(S), S // 2):
        i_idx = np.concatenate([blocks[k] for k in ins])
        o_idx = np.concatenate([blocks[k] for k in range(S) if k not in ins])
        sr_is = np.array([sharpe(M[i_idx, j]) for j in range(N)])
        sr_os = np.array([sharpe(M[o_idx, j]) for j in range(N)])
        best = int(np.argmax(sr_is))
        rank = (sr_os < sr_os[best]).sum() + 0.5 * ((sr_os == sr_os[best]).sum() - 1) + 1
        w = rank / (N + 1)
        lam.append(math.log(w / (1 - w)))
    lam = np.array(lam)
    return float((lam <= 0).mean()), lam


# ------------------------------------------------------ drawdown & sizing
def max_drawdown(pnl):
    """Largest peak-to-trough fall of the cumulative ADDITIVE P&L (>= 0).
    The peak includes the starting point (0) before the first period."""
    c = np.concatenate([[0.0], np.cumsum(np.asarray(pnl, float))])
    return float((np.maximum.accumulate(c) - c).max())


def bootstrap_drawdown(pnl, block=20, B=4000, q=0.95, seed=0):
    """Circular-block bootstrap of the P&L path -> distribution of max drawdown.
    Keeps losing streaks together (block) instead of shuffling trades one by one,
    which is why it is not the retail 'Monte Carlo' reshuffle. Returns the q-th
    percentile and the full draw."""
    x = np.asarray(pnl, float); n = len(x); rng = np.random.default_rng(seed)
    nb = math.ceil(n / block); out = np.empty(B)
    for b in range(B):
        starts = rng.integers(0, n, nb)
        idx = (starts[:, None] + np.arange(block)[None, :]).ravel()[:n] % n
        out[b] = max_drawdown(x[idx])
    return float(np.quantile(out, q)), out


def size_for_drawdown(pnl_per_unit, max_dd_dollars, **kw):
    """Units to trade so the bootstrapped q-percentile drawdown stays inside
    max_dd_dollars. pnl_per_unit is the P&L of ONE contract/share-block."""
    dd_q, _ = bootstrap_drawdown(pnl_per_unit, **kw)
    if dd_q <= 0:
        raise ValueError("bootstrapped drawdown is zero; check the P&L series")
    return max_dd_dollars / dd_q, dd_q


# ------------------------------------------- standard verdict rows (2026-10-10)
# From Discord review 2 (fully hedged, th, 2026-09-27). Each one is a row that
# every verdict table now reports.

def cluster_drop(pnl, clusters):
    """Recompute total and mean P&L with each cluster removed (a month, a settlement
    window, one event). Returns the cluster whose removal hurts most, the totals with
    and without it, and whether removing that one cluster flips the sign.
    A result that lives in one cluster is an anecdote, not an edge."""
    x = np.asarray(pnl, float); g = np.asarray(clusters)
    total = float(x.sum()); rows = []
    for c in np.unique(g):
        rest = x[g != c]
        rows.append((float(x[g == c].sum()), c, float(rest.sum()), float(rest.mean()) if len(rest) else float("nan")))
    best_sum, worst_c, total_wo, mean_wo = max(rows, key=lambda r: r[0] if total >= 0 else -r[0])
    return {"total": total, "n_clusters": len(rows), "top_cluster": worst_c, "top_cluster_pnl": best_sum,
            "top_share": best_sum / total if total else float("nan"), "total_without_top": total_wo,
            "mean_without_top": mean_wo, "sign_flips": (total > 0) != (total_wo > 0)}


def win_payoff(trade_pnl):
    """Win rate AND payoff, never one without the other. breakeven_wr = the win rate
    this payoff needs to make money; edge_wr = win rate minus that. An 80% win rate
    with 0.17 payoff is a losing system."""
    x = np.asarray(trade_pnl, float); w, l = x[x > 0], x[x < 0]
    wr = len(w) / len(x) if len(x) else float("nan")
    aw = float(w.mean()) if len(w) else 0.0; al = float(-l.mean()) if len(l) else 0.0
    be = al / (aw + al) if (aw + al) > 0 else float("nan")
    return {"n": int(len(x)), "win_rate": wr, "avg_win": aw, "avg_loss": al,
            "payoff": aw / al if al > 0 else float("inf"), "breakeven_wr": be,
            "edge_wr": wr - be, "expectancy": float(x.mean()) if len(x) else float("nan")}


def bounce_check(trade_px, mid_px, lag=1):
    """Bid-ask bounce test for short-horizon reversion. Lag-`lag` autocorrelation of
    returns computed from TRADE prices vs from MID prices on the same timestamps.
    Pure bounce makes trade-price returns negatively autocorrelated while mids show
    nothing. If the 'reversion' disappears on mids, fading it pays the spread for no
    information."""
    def ac(p):
        r = np.diff(np.log(np.asarray(p, float)))
        return float(np.corrcoef(r[:-lag], r[lag:])[0, 1])
    a_t, a_m = ac(trade_px), ac(mid_px); n = len(trade_px) - 1 - lag
    se = 1 / math.sqrt(n)
    return {"ac_trade": a_t, "ac_mid": a_m, "se": se,
            "reversion_on_trades": a_t < -2 * se, "reversion_on_mids": a_m < -2 * se,
            "looks_like_bounce": a_t < -2 * se and a_m > -2 * se}


# ------------------------------- Lo (2002) autocorrelation-adjusted Sharpe (2026-10-10)
def lo_annualize(x, q=252, max_lag=10):
    """Annual Sharpe the Lo (2002, FAJ, eq. 17) way instead of SR * sqrt(q):
    SR_q = eta(q) * SR, eta(q) = q / sqrt(q + 2 * sum_{k=1}^{q-1} (q-k) rho_k).
    rho_k beyond max_lag is taken as 0 (estimating hundreds of lags is noise).
    Positive autocorrelation -> eta < sqrt(q) -> sqrt(q) OVERSTATES the annual Sharpe.
    From Discord review 2 (fully hedged posted Lo 2002)."""
    x = np.asarray(x, float); z = x - x.mean(); v = (z * z).mean()
    rho = [float((z[:-k] * z[k:]).mean() / v) for k in range(1, max_lag + 1)]
    s = q + 2 * sum((q - k) * r for k, r in enumerate(rho, start=1) if k < q)
    eta = q / math.sqrt(s) if s > 0 else float("nan")
    sr = sharpe(x)
    return {"rho": rho, "eta": eta, "sr_lo": sr * eta, "sr_sqrt_q": sr * math.sqrt(q),
            "ratio_to_sqrt_q": eta / math.sqrt(q)}
