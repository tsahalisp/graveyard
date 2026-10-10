"""Regression test against this project's OWN three lookahead bugs.
Each reproduces the real buggy code. All three must raise."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit("/",1)[0])
from asof import AsOf, LookaheadError, report_cell

n=50
S=dict(H=np.arange(n,dtype=float)+10, L=np.arange(n,dtype=float),
       C=np.arange(n,dtype=float)+5, V=np.ones(n))
i0=10; lvl=12.0
caught=[]

# BUG 1 -- setup_scan.py v1: scan FORWARD for the reclaim, then enter at the touch bar
try:
    v=AsOf(S,i0)
    for j in range(i0,i0+6):
        if v.C[j] < lvl: break        # reads bars i0+1.. while entry is i0
    caught.append(("#1 entry timing: forward reclaim scan, entry at touch bar","NOT CAUGHT"))
except LookaheadError as e:
    caught.append(("#1 entry timing: forward reclaim scan, entry at touch bar",f"caught -- {e}"))

# BUG 2 -- sweep_entry_variants.py: size the stop from the next 6 bars' extreme
try:
    v=AsOf(S,i0)
    ext=v.H[i0:i0+6].max()
    caught.append(("#2 stop sizing from future bars","NOT CAUGHT"))
except LookaheadError as e:
    caught.append(("#2 stop sizing from future bars",f"caught -- {e}"))

# BUG 3 -- setup_scan_v2.py: GROUP MEMBERSHIP decided by the next 5 bars
try:
    v=AsOf(S,i0)
    is_sweep=any(v.C[j] < lvl for j in range(i0,i0+6))   # label needs bar i0+5
    caught.append(("#3 control-group membership from future bars","NOT CAUGHT"))
except LookaheadError as e:
    caught.append(("#3 control-group membership from future bars",f"caught -- {e}"))

# the legal version of each: features from the view, outcome via explicit future()
ok=True
try:
    v=AsOf(S,i0)
    feat=float(v.H.all().max()-lvl)          # legal: bars 0..i0
    outcome=v.future("C",i0+5)-lvl           # legal and EXPLICIT: outcome measurement
except Exception as e:
    ok=False; err=e

print("="*96)
print("REGRESSION TEST vs THIS PROJECT'S OWN THREE LOOKAHEAD BUGS")
print("="*96)
for nm,res in caught: print(f"  {nm:<52}{res[:40]}")
print(f"\n  legal feature + explicit outcome read               {'works' if ok else 'BROKEN: '+str(err)}")

# report_cell refuses incomplete reporting
print()
print("="*96); print("REPORTING GATE -- a t-stat with no MDE, no size, or a naive SE is refused")
print("="*96)
try:
    report_cell("some cell", 0.03, se=0.006, n=29116, mde_=None, dollars=1.2)
    print("  REFUSAL FAILED")
except ValueError as e:
    print(f"  refused: {e}")
print(report_cell("dist_val_prior h15", -0.0508, se=0.0108, n=29116, mde_=0.031, dollars=-3.02))
allcaught=all("caught" in r for _,r in caught)
print(f"\n  ALL THREE HISTORICAL BUGS CAUGHT: {allcaught}")
sys.exit(0 if (allcaught and ok) else 1)
