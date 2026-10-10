"""Phase 0: portfolio-level evaluation (2026-10-06).

Sleeves are judged together, not one at a time. Weights are computed from a
TRAILING window and applied from the NEXT period (shift(1)), so a weight can
never use the return it is applied to.
"""
import numpy as np
import pandas as pd


def inverse_vol_weights(R: pd.DataFrame, window=63, min_periods=None):
    """Naive risk parity: weight_j proportional to 1 / trailing vol_j, rows sum to 1.
    First usable row is NaN by construction (lagged one period)."""
    mp = min_periods or window
    vol = R.rolling(window, min_periods=mp).std()
    w = 1.0 / vol.replace(0, np.nan)
    w = w.div(w.sum(axis=1), axis=0)
    return w.shift(1)


def vol_target(r: pd.Series, target_ann=0.10, window=63, periods=252, cap=2.0):
    """Scale a return series to a target annual vol using trailing vol, lagged."""
    vol = r.rolling(window).std() * np.sqrt(periods)
    lev = (target_ann / vol).clip(upper=cap).shift(1)
    return r * lev, lev


def combine(R: pd.DataFrame, W: pd.DataFrame):
    """Portfolio return = sum of lagged weights x sleeve returns (rows with no
    weights yet are dropped, not zero-filled)."""
    W = W.reindex_like(R)
    ok = W.notna().all(axis=1)
    return (R[ok] * W[ok]).sum(axis=1)


def stats(r: pd.Series, periods=252):
    r = pd.Series(r).dropna()
    mu, sd = r.mean(), r.std(ddof=1)
    c = (1 + r).cumprod()
    mdd = (c / c.cummax() - 1).min()
    return dict(n=len(r), ann_ret=mu * periods, ann_vol=sd * np.sqrt(periods),
                sharpe_ann=(mu / sd * np.sqrt(periods)) if sd > 0 else 0.0,
                max_dd=float(mdd))


def report(R: pd.DataFrame, W: pd.DataFrame, periods=252):
    """Per-sleeve stats, correlation matrix and the combined book."""
    rows = {c: stats(R[c], periods) for c in R}
    rows["PORTFOLIO"] = stats(combine(R, W), periods)
    return pd.DataFrame(rows).T, R.corr()
