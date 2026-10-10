"""Make entry-time knowledge a property of the DATA, not of careful indexing.

Three lookahead bugs in the levels line, all the same shape: a value read from
a numpy array with an index nobody checked against the entry bar. Assertions
did not catch any of them, because an assertion checks a number after the fact
and the bug is in which number got computed.

AsOf fixes it by construction. You build a view at bar i; reading past i raises.
A feature computed from an AsOf view cannot see the future. A feature computed
from the raw arrays is visibly doing something that needs justifying.
"""
import numpy as np

class LookaheadError(IndexError):
    pass

class AsOf:
    """Read-only view of a session's arrays truncated at bar `i` (inclusive)."""
    __slots__ = ("_a", "i", "_name")
    def __init__(self, arrays: dict, i: int, name="session"):
        self._a = arrays; self.i = int(i); self._name = name
    def __getattr__(self, k):
        if k not in self._a:
            raise AttributeError(k)
        return _Slice(self._a[k], self.i, k)
    def at(self, k):
        """scalar value of series k at the entry bar"""
        return self._a[k][self.i]
    def future(self, k, j):
        """EXPLICIT future read -- only legal for outcome measurement, never features."""
        return self._a[k][j]

class _Slice:
    __slots__ = ("_v", "_i", "_k")
    def __init__(self, v, i, k): self._v, self._i, self._k = v, i, k
    def _chk(self, j):
        if isinstance(j, slice):
            stop = j.stop if j.stop is not None else len(self._v)
            if stop > self._i + 1:
                raise LookaheadError(
                    f"{self._k}[{j.start}:{j.stop}] reaches bar {stop-1} "
                    f"but entry is bar {self._i}")
        else:
            jj = j if j >= 0 else len(self._v) + j
            if jj > self._i:
                raise LookaheadError(f"{self._k}[{j}] is bar {jj}, entry is bar {self._i}")
    def __getitem__(self, j):
        self._chk(j); return self._v[j]
    def __len__(self): return self._i + 1
    def all(self): return self._v[:self._i + 1]

# ---------- reporting gates ----------
def mde(sd, n1, n2=None, tcrit=2.87):
    """minimum detectable effect. n2=None -> one-sample."""
    se = sd / np.sqrt(n1) if n2 is None else sd * np.sqrt(1/n1 + 1/n2)
    return tcrit * se

def block_bootstrap_se(groups, stat, B=4000, seed=0):
    """groups: list of arrays/frames, one per independent block (use SESSIONS).
    stat: callable(concatenated) -> float."""
    rng = np.random.default_rng(seed); K = len(groups)
    out = np.empty(B)
    for b in range(B):
        idx = rng.integers(0, K, K)
        out[b] = stat([groups[i] for i in idx])
    return float(out.std(ddof=1)), out

def report_cell(name, stat, *, se, n, mde_, dollars, tcrit=2.87):
    """Refuses to produce a line without a dependence-aware SE, an MDE and a size."""
    for k, v in (("se", se), ("mde", mde_), ("dollars", dollars)):
        if v is None:
            raise ValueError(f"report_cell({name}): '{k}' is required. "
                             "A t-stat without it has misled this project before.")
    t = stat / se
    if abs(stat) < mde_:
        verdict = "cannot tell (under MDE)"
    elif abs(t) > tcrit:
        verdict = "CLEARS"
    else:
        verdict = "fails, and powered to see it"
    return (f"  {name:<28}{n:>8,}{stat:>10.4f}{se:>9.4f}{t:>8.2f}"
            f"{mde_:>9.4f}{dollars:>9.2f}   {verdict}")
