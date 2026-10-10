"""Two-sided validation of permute.py: it must clear a known null AND catch a
known-real planted effect. The register has never had the second kind of test.
Exit 0 = both pass."""
import sys, pathlib, numpy as np, pandas as pd
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from permute import Search, whole_procedure_test, shuffle_labels

rng = np.random.default_rng(1)
N = 4000
df = pd.DataFrame({"ret": rng.normal(0, 20, N), "dow": rng.integers(0, 5, N),
                   "regime": rng.integers(0, 3, N)})

VARIANTS = [(d, r) for d in range(5) for r in range(3)]     # 15-cell search


def evaluate(data, v):
    d, r = v
    m = (data.dow == d) & (data.regime == r)
    x = data.ret[m]
    return np.nan if len(x) < 30 else x.mean() / (x.std(ddof=1) / np.sqrt(len(x)))


def check(name, data, expect_small):
    s = Search(name, VARIANTS, evaluate)
    res = whole_procedure_test(data, s, shuffle_labels("dow", "regime"),
                               B=400, alternative="greater")
    print(res)
    naive = res["real"]
    ok = (res["p"] < 0.01) if expect_small else (res["p"] > 0.05)
    print(f"  naive t of the winning cell = {naive:+.3f} "
          f"-- a 2.0 threshold would call it {'SIGNIFICANT' if naive > 2 else 'null'}")
    print(f"  {'PASS' if ok else 'FAIL'}: expected p "
          f"{'< 0.01' if expect_small else '> 0.05'}, got {res['p']:.4f}\n")
    return ok

print("=" * 66)
print("TEST 1 -- PURE NOISE. The best of 15 cells must NOT survive.")
print("=" * 66)
ok1 = check("noise", df, expect_small=False)

print("=" * 66)
print("TEST 2 -- PLANTED EFFECT (+6 on dow=2 & regime=1). Must survive.")
print("=" * 66)
d2 = df.copy()
d2.loc[(d2.dow == 2) & (d2.regime == 1), "ret"] += 6.0
ok2 = check("planted", d2, expect_small=True)

print("both:", "PASS" if (ok1 and ok2) else "FAIL")

# --- CAL-3 regression: a permuter that touches nothing must RAISE, not return p=1
print("=" * 66)
print("TEST 3 -- DEGENERATE NULL. A no-op permuter must raise, not pass silently.")
print("=" * 66)
from permute import shuffle_sessions
try:
    whole_procedure_test(df, Search("degen", VARIANTS, evaluate),
                         shuffle_sessions(), B=400, alternative="greater")
    print("  FAIL: no-op permuter returned a p-value instead of raising\n")
    sys.exit(1)
except ValueError as e:
    assert "DEGENERATE NULL" in str(e), e
    print(f"  raised as required: {str(e)[:90]}...")
    print("  PASS\n")
print("all three: PASS")
sys.exit(0 if (ok1 and ok2) else 1)
