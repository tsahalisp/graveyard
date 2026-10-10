# VERDICTS — Track B strategy graveyard

Every tested idea ends here with an autopsy: what was claimed, what the data
said, why it lived or died. Same format as ../VERDICTS.md (Track A).

## H1. Cross-sectional momentum 12-1 on megacaps — NOT CONFIRMED (2026-07-03)

```
TRAIN <=2018    ret +1.2%  sharpe 0.21  maxDD 11.8%  hit 52.4%  n=2264
HOLDOUT >=2019  ret +0.3%  sharpe 0.09  maxDD 26.1%  hit 52.0%  n=1885
Gate: ann>0 AND sharpe>0.30 in both halves -> FAILED on sharpe, both halves.
```

Autopsy: the signal is THERE — both halves positive, hit rate 52% both, and
the effect landed inside our pre-registered 0-6%/yr expectation — but far
too weak to deploy. This matches the literature exactly: momentum is weakest
in megacaps, and our cross-section is thin (quintiles of 18 names from 89).
Holdout maxDD 26% is consistent with the known momentum crashes (Mar 2020,
Nov 2020 vaccine rotation — winners/losers flip violently).

What would change the verdict (candidates for a future H2+, not promises):
- Broader universe: 500+ mid/small caps where the anomaly historically lives
  (needs point-in-time membership data to be honest about survivorship).
- Crypto cross-sectional momentum on the 14 majors (thin, but different market).

Process note: gate was set before data; both halves were positive and it
would have been easy to rationalize a pass. We did not. The verdict is the
decision.

Phase 5 addendum (2026-07-03, validate.py): the NOT CONFIRMED verdict got
stronger under interrogation. Walk-forward folds: +0.30, -0.08, +0.59, -0.50,
+0.70 — no consistency; fold4 (2020-2023) is the momentum-crash era bleeding.
Parameter grid (16 cells, lookback 126-315 x reb 10-63): everything between
-0.08 and 0.16, flat weakness, no plateau. Noise ceiling: best of 16 pure-noise
tries over 16y ~ sharpe 0.58; our best cell = 0.16. The entire neighborhood is
indistinguishable from luck. H1 stays buried.

## H2. 5-day cross-sectional reversal on megacaps — NOT CONFIRMED (2026-07-03)

```
GROSS  train +3.3% sharpe 0.57 | holdout +1.5% sharpe 0.20
NET    train -4.3% sharpe -0.68 | holdout -6.2% sharpe -0.58
Cost wall measured: 7.6%/yr at 10bps x weekly full-book rotation.
```

Autopsy: the pre-registered prediction hit exactly — the anomaly exists
(gross positive both halves; liquidity provision is real) and transaction
costs eat it whole. This is the classic reversal result since the 1990s:
the edge belongs to whoever already sits at the market-making layer with
sub-bp costs, not to anyone paying retail spreads. No parameter tweak fixes
a 7.6%/yr toll on a 3%/yr edge.

Lesson banked: ALWAYS compute annual turnover x cost BEFORE building a
strategy. This one was knowable-dead from arithmetic alone; we ran it to
see the wall measured, and now the number is on file.

## H3. Crypto 90-7 momentum on 13 majors — NOT CONFIRMED (2026-07-03)

```
TRAIN <=2021   ret +6.5%  sharpe +0.39  maxDD 43.9%   (passes gate alone)
HOLDOUT >=2022 ret -6.7%  sharpe -0.22  maxDD 41.9%   (sign flip)
Gate: both halves > 0 and sharpe > 0.30 -> FAILED in holdout.
```

Autopsy: regime-dependent, not robust. Momentum among crypto majors worked
through the 2017-2021 narrative-bull era and INVERTED post-2022 (maturing
market, more mean-reversion between majors, ETF-era flows). Had we split
anywhere inside the bull years, this would have "confirmed" — the declared
2022 split (one full bear cycle in holdout) did its job. Also registered as
underpowered (13 survivors, 4L/4S) — even the train-half pass is weak evidence.

Firm scoreboard after three hypotheses: 0 confirmed, 3 honest burials
(thin edge, cost wall, regime flip) — three DIFFERENT ways strategies die,
each now recognizable on sight.

## H4. Crypto momentum, powered universe (52 names) — NOT CONFIRMED (2026-07-03)

```
TRAIN <=2024   ret +2.9%  sharpe 0.24  maxDD 44.8%
HOLDOUT >=2025 ret +0.4%  sharpe 0.13  maxDD 26.4%
Gate: >0 and sharpe>0.30 both halves -> FAILED on sharpe, both halves.
```

Autopsy: with 4x the cross-section, crypto momentum shows the same H1
signature — directionally positive everywhere, nowhere near deployable.
Between H3 (regime flip) and H4 (powered, weak), cross-sectional momentum
in crypto majors+mids is now thoroughly dead to us at retail costs.

INSTRUMENT INCIDENT during H4 (worth more than the verdict): first run
printed +984%/yr with 883,758% vol — Yahoo ticker-reuse seams (TIA $0.01 ->
$7,149 "overnight" when Celestia took the ticker; ARB/OP pre-launch junk;
AAVE's LEND migration). The quality gate had a crypto blind spot (cliff
check was equity-only). Fixed permanently: >900%/day = seam = FAIL, and 7
symbols' histories truncated past their last seam. House rule 2 vindicated
again: audit the instrument before believing any number it prints.

## H6. Time-series trend on megacaps (6m) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  +5.0%  sharpe +0.55  maxDD 16.0%
HOLDOUT (last 35%)  ret  +1.8%  sharpe +0.25  maxDD 18.1%
FULL                ret  +3.9%  sharpe +0.46  vol  9.3%
Neighborhood best cell +0.63  vs  noise ceiling 0.69  (N=49 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.55, holdout sh 0.25 vs bar 0.3). No edge after 10bps costs.

## H7. Risk-parity 12-1 momentum on megacaps - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  -0.1%  sharpe +0.03  maxDD 14.6%
HOLDOUT (last 35%)  ret  +2.0%  sharpe +0.24  maxDD 16.4%
FULL                ret  +0.6%  sharpe +0.12  vol  8.9%
Neighborhood best cell +0.14  vs  noise ceiling 0.70  (N=58 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.03, holdout sh 0.24 vs bar 0.3). No edge after 10bps costs.

## H8. Low-volatility anomaly on megacaps - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  -9.1%  sharpe -0.94  maxDD 66.0%
HOLDOUT (last 35%)  ret  -9.7%  sharpe -0.67  maxDD 52.3%
FULL                ret  -9.3%  sharpe -0.81  vol 11.3%
Neighborhood best cell -0.74  vs  noise ceiling 0.71  (N=67 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.94, holdout sh -0.67 vs bar 0.3). No edge after 10bps costs.

## H9. Time-series trend on crypto majors (3m, weekly) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret +18.7%  sharpe +0.59  maxDD 90.8%
HOLDOUT (last 35%)  ret  +1.1%  sharpe +0.24  maxDD 58.5%
FULL                ret +12.2%  sharpe +0.49  vol 55.9%
Neighborhood best cell +0.74  vs  noise ceiling 0.71  (N=76 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.59, holdout sh 0.24 vs bar 0.4). No edge after 10bps costs.

## H10. Risk-parity momentum on crypto majors - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  -9.7%  sharpe -0.64  maxDD 66.1%
HOLDOUT (last 35%)  ret  -4.1%  sharpe -0.08  maxDD 52.9%
FULL                ret  -7.8%  sharpe -0.38  vol 17.2%
Neighborhood best cell -0.17  vs  noise ceiling 0.72  (N=85 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.64, holdout sh -0.08 vs bar 0.4). No edge after 10bps costs.

## H11. Short-horizon reversal on crypto majors (5d) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret -14.2%  sharpe -0.78  maxDD 81.6%
HOLDOUT (last 35%)  ret -27.3%  sharpe -0.75  maxDD 83.7%
FULL                ret -19.0%  sharpe -0.73  vol 24.8%
Neighborhood best cell -0.05  vs  noise ceiling 0.73  (N=91 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.78, holdout sh -0.75 vs bar 0.4). No edge after 10bps costs.

## H12. Low-volatility tilt on crypto majors - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret -10.4%  sharpe -0.55  maxDD 74.9%
HOLDOUT (last 35%)  ret -22.0%  sharpe -0.79  maxDD 83.0%
FULL                ret -14.7%  sharpe -0.65  vol 21.0%
Neighborhood best cell -0.44  vs  noise ceiling 0.73  (N=100 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.55, holdout sh -0.79 vs bar 0.4). No edge after 10bps costs.

## H13. Fast cross-sectional momentum on crypto (63d) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  -1.4%  sharpe +0.01  maxDD 42.6%
HOLDOUT (last 35%)  ret +13.4%  sharpe +0.62  maxDD 20.0%
FULL                ret  +3.5%  sharpe +0.27  vol 20.8%
Neighborhood best cell +0.27  vs  noise ceiling 0.74  (N=109 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.01, holdout sh 0.62 vs bar 0.4). No edge after 10bps costs.

## H14. Fast time-series trend on megacaps (3m) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  +1.4%  sharpe +0.18  maxDD 31.8%
HOLDOUT (last 35%)  ret  -0.3%  sharpe +0.01  maxDD 23.4%
FULL                ret  +0.8%  sharpe +0.13  vol 10.4%
Neighborhood best cell +0.13  vs  noise ceiling 0.76  (N=118 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.18, holdout sh 0.01 vs bar 0.3). No edge after 10bps costs.

## H15. Overnight 1-day reversal megacaps - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret -32.2%  sharpe -4.01  maxDD 97.9%
HOLDOUT (last 35%)  ret -35.2%  sharpe -3.51  maxDD 91.2%
FULL                ret -33.3%  sharpe -3.78  vol 10.5%
Neighborhood best cell -1.04  vs  noise ceiling 0.76  (N=122 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -4.01, holdout sh -3.51 vs bar 0.3). No edge after 10bps costs.

## H16. Long-horizon 12-1 momentum with 1-month skip equity - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  +0.2%  sharpe +0.07  maxDD 16.3%
HOLDOUT (last 35%)  ret  +2.2%  sharpe +0.24  maxDD 19.4%
FULL                ret  +0.9%  sharpe +0.14  vol 10.5%
Neighborhood best cell +0.19  vs  noise ceiling 0.77  (N=131 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.07, holdout sh 0.24 vs bar 0.3). No edge after 10bps costs.

## H17. Crypto 1-month XS momentum weekly rebal - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret +14.7%  sharpe +0.74  maxDD 26.0%
HOLDOUT (last 35%)  ret  -6.1%  sharpe +0.04  maxDD 55.1%
FULL                ret  +7.0%  sharpe +0.38  vol 29.2%
Neighborhood best cell +0.54  vs  noise ceiling 0.76  (N=140 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.74, holdout sh 0.04 vs bar 0.4). No edge after 10bps costs.

## H18. 2-day crypto cross-sectional reversal - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret -13.5%  sharpe -0.67  maxDD 81.1%
HOLDOUT (last 35%)  ret -13.5%  sharpe -0.26  maxDD 74.2%
FULL                ret -13.5%  sharpe -0.45  vol 25.3%
Neighborhood best cell -0.24  vs  noise ceiling 0.76  (N=146 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.67, holdout sh -0.26 vs bar 0.4). No edge after 10bps costs.

## H19. Funding carry: long crowded-short crypto (7d) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  +8.5%  sharpe +0.49  maxDD 30.8%
HOLDOUT (last 35%)  ret  -1.6%  sharpe -0.03  maxDD 26.4%
FULL                ret  +4.9%  sharpe +0.34  vol 18.7%
Neighborhood best cell +0.42  vs  noise ceiling 0.77  (N=152 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.49, holdout sh -0.03 vs bar 0.4). No edge after 10bps costs.

## H20. Funding carry: long crowded-long crypto (7d) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret -14.2%  sharpe -0.63  maxDD 81.5%
HOLDOUT (last 35%)  ret -12.1%  sharpe -0.77  maxDD 59.8%
FULL                ret -13.5%  sharpe -0.66  vol 18.8%
Neighborhood best cell -0.39  vs  noise ceiling 0.77  (N=158 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.63, holdout sh -0.77 vs bar 0.4). No edge after 10bps costs.

## H21. Time-series funding: long each crowded-short name (14d) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret -24.7%  sharpe -0.47  maxDD 98.3%
HOLDOUT (last 35%)  ret -12.8%  sharpe -0.17  maxDD 83.3%
FULL                ret -20.7%  sharpe -0.37  vol 40.7%
Neighborhood best cell -0.34  vs  noise ceiling 0.77  (N=164 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.47, holdout sh -0.17 vs bar 0.4). No edge after 10bps costs.

## H22. Equity 1-day micro-reversal (tight universe) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret -31.1%  sharpe -4.60  maxDD 97.5%
HOLDOUT (last 35%)  ret -33.3%  sharpe -3.89  maxDD 89.3%
FULL                ret -31.9%  sharpe -4.28  vol  8.9%
Neighborhood best cell -0.99  vs  noise ceiling 0.79  (N=168 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -4.60, holdout sh -3.89 vs bar 0.3). No edge after 10bps costs.

## H23. Equity 1-month XS momentum (monthly horizon) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  -4.4%  sharpe -0.60  maxDD 41.1%
HOLDOUT (last 35%)  ret  -4.1%  sharpe -0.39  maxDD 32.1%
FULL                ret  -4.3%  sharpe -0.51  vol  8.0%
Neighborhood best cell -0.31  vs  noise ceiling 0.79  (N=177 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.60, holdout sh -0.39 vs bar 0.3). No edge after 10bps costs.

## H24. Crypto 6-month XS momentum (long horizon) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  -4.8%  sharpe -0.25  maxDD 52.1%
HOLDOUT (last 35%)  ret  -1.8%  sharpe +0.03  maxDD 45.6%
FULL                ret  -3.8%  sharpe -0.12  vol 18.0%
Neighborhood best cell +0.26  vs  noise ceiling 0.78  (N=186 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.25, holdout sh 0.03 vs bar 0.4). No edge after 10bps costs.

## H25. Equity annual time-series trend (monthly rebal) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret  +7.7%  sharpe +0.74  maxDD 18.3%
HOLDOUT (last 35%)  ret  +5.2%  sharpe +0.59  maxDD 20.7%
FULL                ret  +6.8%  sharpe +0.69  vol 10.3%
Neighborhood best cell +0.76  vs  noise ceiling 0.80  (N=195 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - passes the raw gate but the best neighborhood cell (0.76) is UNDER the noise ceiling (0.80) at N=195 cumulative tests: indistinguishable from the luckiest of that many tries. The multiple-testing bar did its job.

## H26. Crypto 2-week reversal (weekly rebal) - NOT CONFIRMED (2026-07-12)

```
TRAIN  (first 65%)  ret -21.1%  sharpe -0.87  maxDD 91.4%
HOLDOUT (last 35%)  ret -12.9%  sharpe -0.14  maxDD 75.9%
FULL                ret -18.3%  sharpe -0.50  vol 30.7%
Neighborhood best cell -0.15  vs  noise ceiling 0.79  (N=204 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.87, holdout sh -0.14 vs bar 0.4). No edge after 10bps costs.

## H28. Crypto 2-week XS reversal weekly rebal - NOT CONFIRMED (2026-07-13)

```
TRAIN  (first 65%)  ret  -4.2%  sharpe -0.29  maxDD 47.8%
HOLDOUT (last 35%)  ret  -6.0%  sharpe -0.12  maxDD 34.6%
FULL                ret  -4.8%  sharpe -0.19  vol 17.8%
Neighborhood best cell +0.02  vs  noise ceiling 0.80  (N=222 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.29, holdout sh -0.12 vs bar 0.4). No edge after 10bps costs.

## H29. Crypto 6-month time-series trend monthly rebal - NOT CONFIRMED (2026-07-13)

```
TRAIN  (first 65%)  ret +37.2%  sharpe +0.82  maxDD 79.4%
HOLDOUT (last 35%)  ret  -7.5%  sharpe +0.01  maxDD 72.7%
FULL                ret +19.5%  sharpe +0.60  vol 55.7%
Neighborhood best cell +0.79  vs  noise ceiling 0.80  (N=231 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.82, holdout sh 0.01 vs bar 0.4). No edge after 10bps costs.

## H30. Crypto 90-5 vol-scaled momentum biweekly rebal - NOT CONFIRMED (2026-07-13)

```
TRAIN  (first 65%)  ret  -1.6%  sharpe -0.03  maxDD 40.5%
HOLDOUT (last 35%)  ret  +7.1%  sharpe +0.42  maxDD 43.6%
FULL                ret  +1.4%  sharpe +0.17  vol 18.0%
Neighborhood best cell +0.38  vs  noise ceiling 0.80  (N=240 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.03, holdout sh 0.42 vs bar 0.4). No edge after 10bps costs.

## H31. Equity annual vol-scaled momentum monthly rebal - NOT CONFIRMED (2026-07-13)

```
TRAIN  (first 65%)  ret  -0.1%  sharpe +0.03  maxDD 14.6%
HOLDOUT (last 35%)  ret  +2.0%  sharpe +0.24  maxDD 16.4%
FULL                ret  +0.6%  sharpe +0.12  vol  8.9%
Neighborhood best cell +0.14  vs  noise ceiling 0.82  (N=249 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.03, holdout sh 0.24 vs bar 0.3). No edge after 10bps costs.

## H32. Equity 3-day XS reversal semi-weekly rebal - NOT CONFIRMED (2026-07-14)

```
TRAIN  (first 65%)  ret  -7.9%  sharpe -1.11  maxDD 61.1%
HOLDOUT (last 35%)  ret -12.2%  sharpe -1.39  maxDD 51.2%
FULL                ret  -9.4%  sharpe -1.21  vol  7.9%
Neighborhood best cell -0.24  vs  noise ceiling 0.82  (N=258 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -1.11, holdout sh -1.39 vs bar 0.3). No edge after 10bps costs.

## H33. Equity 6-month XS momentum weekly rebal tighter book - NOT CONFIRMED (2026-07-14)

```
TRAIN  (first 65%)  ret  +0.0%  sharpe +0.05  maxDD 25.6%
HOLDOUT (last 35%)  ret  +0.8%  sharpe +0.13  maxDD 21.7%
FULL                ret  +0.3%  sharpe +0.08  vol 10.3%
Neighborhood best cell +0.09  vs  noise ceiling 0.82  (N=267 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.05, holdout sh 0.13 vs bar 0.3). No edge after 10bps costs.

## H34. Crypto 1-month time-series trend weekly rebal - NOT CONFIRMED (2026-07-14)

```
TRAIN  (first 65%)  ret +60.7%  sharpe +1.09  maxDD 65.0%
HOLDOUT (last 35%)  ret  -9.9%  sharpe -0.01  maxDD 63.5%
FULL                ret +31.3%  sharpe +0.77  vol 55.4%
Neighborhood best cell +1.04  vs  noise ceiling 0.81  (N=276 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.09, holdout sh -0.01 vs bar 0.4). No edge after 10bps costs.

## H35. Equity 6m vol-scaled momentum monthly rebal - NOT CONFIRMED (2026-07-14)

```
TRAIN  (first 65%)  ret  -0.4%  sharpe -0.01  maxDD 22.1%
HOLDOUT (last 35%)  ret  -4.5%  sharpe -0.40  maxDD 30.4%
FULL                ret  -1.9%  sharpe -0.17  vol  8.9%
Neighborhood best cell +0.08  vs  noise ceiling 0.83  (N=285 cells, 16y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.01, holdout sh -0.40 vs bar 0.3). No edge after 10bps costs.

## H36. Crypto 1-month XS momentum 2-day skip weekly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret +13.8%  sharpe +0.84  maxDD 27.2%
HOLDOUT (last 35%)  ret  -3.1%  sharpe +0.07  maxDD 44.5%
FULL                ret  +7.6%  sharpe +0.42  vol 24.1%
Neighborhood best cell +0.54  vs  noise ceiling 0.82  (N=294 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.84, holdout sh 0.07 vs bar 0.4). No edge after 10bps costs.

## H37. Crypto 9-month time-series trend monthly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret +37.3%  sharpe +0.81  maxDD 96.5%
HOLDOUT (last 35%)  ret -17.7%  sharpe -0.38  maxDD 84.2%
FULL                ret +14.8%  sharpe +0.53  vol 55.7%
Neighborhood best cell +0.80  vs  noise ceiling 0.82  (N=303 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.81, holdout sh -0.38 vs bar 0.4). No edge after 10bps costs.

## H38. Crypto 60d vol-scaled momentum biweekly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret  -0.7%  sharpe +0.03  maxDD 34.7%
HOLDOUT (last 35%)  ret +14.1%  sharpe +0.70  maxDD 26.4%
FULL                ret  +4.3%  sharpe +0.32  vol 17.9%
Neighborhood best cell +0.50  vs  noise ceiling 0.82  (N=312 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.03, holdout sh 0.70 vs bar 0.4). No edge after 10bps costs.

## H39. Crypto 2-week XS reversal 12-side weekly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret  -5.9%  sharpe -0.33  maxDD 56.0%
HOLDOUT (last 35%)  ret  -7.0%  sharpe -0.09  maxDD 39.5%
FULL                ret  -6.3%  sharpe -0.19  vol 21.5%
Neighborhood best cell +0.02  vs  noise ceiling 0.82  (N=321 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.33, holdout sh -0.09 vs bar 0.4). No edge after 10bps costs.

## H40. Crypto 30-2 XS momentum tri-daily rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret +10.5%  sharpe +0.66  maxDD 31.0%
HOLDOUT (last 35%)  ret  +1.6%  sharpe +0.21  maxDD 47.6%
FULL                ret  +7.3%  sharpe +0.41  vol 23.8%
Neighborhood best cell +0.49  vs  noise ceiling 0.82  (N=330 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.66, holdout sh 0.21 vs bar 0.4). No edge after 10bps costs.

## H41. Crypto short-window low-vol bi-weekly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret -17.8%  sharpe -0.96  maxDD 88.5%
HOLDOUT (last 35%)  ret -39.6%  sharpe -1.24  maxDD 94.7%
FULL                ret -26.2%  sharpe -1.05  vol 25.8%
Neighborhood best cell -0.88  vs  noise ceiling 0.83  (N=339 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.96, holdout sh -1.24 vs bar 0.4). No edge after 10bps costs.

## H42. Equity 3-week XS reversal weekly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret  -3.5%  sharpe -0.38  maxDD 38.2%
HOLDOUT (last 35%)  ret  -8.4%  sharpe -0.77  maxDD 42.2%
FULL                ret  -5.3%  sharpe -0.53  vol  9.4%
Neighborhood best cell -0.27  vs  noise ceiling 0.84  (N=348 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.38, holdout sh -0.77 vs bar 0.3). No edge after 10bps costs.

## H43. Equity 9-month XS momentum 2-week skip weekly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret  +0.8%  sharpe +0.13  maxDD 17.7%
HOLDOUT (last 35%)  ret  -1.3%  sharpe -0.05  maxDD 27.6%
FULL                ret  +0.0%  sharpe +0.06  vol 10.6%
Neighborhood best cell +0.21  vs  noise ceiling 0.84  (N=357 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.13, holdout sh -0.05 vs bar 0.3). No edge after 10bps costs.

## H44. Crypto 45-day time-series trend weekly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret +49.4%  sharpe +0.96  maxDD 77.7%
HOLDOUT (last 35%)  ret  -8.5%  sharpe +0.02  maxDD 67.3%
FULL                ret +25.8%  sharpe +0.69  vol 56.0%
Neighborhood best cell +1.01  vs  noise ceiling 0.83  (N=366 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.96, holdout sh 0.02 vs bar 0.4). No edge after 10bps costs.

## H45. Crypto 6-month vol-scaled momentum biweekly rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret  -6.0%  sharpe -0.35  maxDD 62.0%
HOLDOUT (last 35%)  ret +11.3%  sharpe +0.59  maxDD 35.8%
FULL                ret  -0.3%  sharpe +0.07  vol 17.9%
Neighborhood best cell +0.30  vs  noise ceiling 0.83  (N=375 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.35, holdout sh 0.59 vs bar 0.4). No edge after 10bps costs.

## H46. Crypto 3-day XS reversal tri-daily rebal - NOT CONFIRMED (2026-08-05)

```
TRAIN  (first 65%)  ret  -7.6%  sharpe -0.31  maxDD 63.3%
HOLDOUT (last 35%)  ret  -9.2%  sharpe -0.11  maxDD 69.3%
FULL                ret  -8.2%  sharpe -0.21  vol 25.6%
Neighborhood best cell -0.04  vs  noise ceiling 0.83  (N=384 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.31, holdout sh -0.11 vs bar 0.4). No edge after 10bps costs.

## H47. Equity 20d XS momentum 5d skip daily rebal - NOT CONFIRMED (2026-08-22)

```
TRAIN  (first 65%)  ret  -0.9%  sharpe -0.07  maxDD 19.1%
HOLDOUT (last 35%)  ret  -5.2%  sharpe -0.49  maxDD 35.2%
FULL                ret  -2.4%  sharpe -0.24  vol  8.7%
Neighborhood best cell -0.21  vs  noise ceiling 0.85  (N=393 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.07, holdout sh -0.49 vs bar 0.3). No edge after 10bps costs.

## H48. Crypto 2-week time-series trend 2-day rebal - NOT CONFIRMED (2026-08-22)

```
TRAIN  (first 65%)  ret +64.6%  sharpe +1.12  maxDD 52.3%
HOLDOUT (last 35%)  ret  -4.8%  sharpe +0.11  maxDD 62.9%
FULL                ret +35.9%  sharpe +0.83  vol 55.8%
Neighborhood best cell +0.89  vs  noise ceiling 0.84  (N=402 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.12, holdout sh 0.11 vs bar 0.4). No edge after 10bps costs.

## H49. Equity 60d vol-scaled momentum 10d skip 10d rebal - NOT CONFIRMED (2026-08-22)

```
TRAIN  (first 65%)  ret  -3.4%  sharpe -0.42  maxDD 39.1%
HOLDOUT (last 35%)  ret  -1.8%  sharpe -0.12  maxDD 27.9%
FULL                ret  -2.8%  sharpe -0.29  vol  8.7%
Neighborhood best cell -0.14  vs  noise ceiling 0.85  (N=411 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.42, holdout sh -0.12 vs bar 0.3). No edge after 10bps costs.

## H50. Crypto 1-week XS reversal 3-day rebal 20-side - NOT CONFIRMED (2026-08-22)

```
TRAIN  (first 65%)  ret  +0.0%  sharpe +0.00  maxDD  0.0%
HOLDOUT (last 35%)  ret  -6.8%  sharpe -0.31  maxDD 39.3%
FULL                ret  -2.4%  sharpe -0.18  vol 10.5%
Neighborhood best cell +0.36  vs  noise ceiling 0.84  (N=420 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.00, holdout sh -0.31 vs bar 0.4). No edge after 10bps costs.

## H51. Crypto 20d low-vol tilt 10-day rebal - NOT CONFIRMED (2026-08-22)

```
TRAIN  (first 65%)  ret -12.3%  sharpe -0.64  maxDD 77.1%
HOLDOUT (last 35%)  ret -38.1%  sharpe -1.20  maxDD 94.3%
FULL                ret -22.4%  sharpe -0.88  vol 25.1%
Neighborhood best cell -0.82  vs  noise ceiling 0.84  (N=429 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.64, holdout sh -1.20 vs bar 0.4). No edge after 10bps costs.

## H52. Equity 2-week XS reversal weekly rebal - NOT CONFIRMED (2026-08-24)

```
TRAIN  (first 65%)  ret  -3.5%  sharpe -0.37  maxDD 37.0%
HOLDOUT (last 35%)  ret  -7.2%  sharpe -0.66  maxDD 39.0%
FULL                ret  -4.8%  sharpe -0.48  vol  9.4%
Neighborhood best cell +0.21  vs  noise ceiling 0.86  (N=438 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.37, holdout sh -0.66 vs bar 0.3). No edge after 10bps costs.

## H53. Equity 12-1 XS momentum monthly rebal wider book - NOT CONFIRMED (2026-08-24)

```
TRAIN  (first 65%)  ret  +0.1%  sharpe +0.06  maxDD 18.1%
HOLDOUT (last 35%)  ret  +2.9%  sharpe +0.34  maxDD 14.7%
FULL                ret  +1.1%  sharpe +0.17  vol  8.9%
Neighborhood best cell +0.17  vs  noise ceiling 0.86  (N=447 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.06, holdout sh 0.34 vs bar 0.3). No edge after 10bps costs.

## H54. Equity 3-month low-vol monthly rebal - NOT CONFIRMED (2026-08-24)

```
TRAIN  (first 65%)  ret  -7.4%  sharpe -0.75  maxDD 60.7%
HOLDOUT (last 35%)  ret -10.8%  sharpe -0.79  maxDD 53.3%
FULL                ret  -8.6%  sharpe -0.76  vol 11.1%
Neighborhood best cell -0.73  vs  noise ceiling 0.86  (N=456 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.75, holdout sh -0.79 vs bar 0.3). No edge after 10bps costs.

## H55. H55. Equity 40d XS momentum 3d skip 5d rebal tight 15-side - NOT CONFIRMED (2026-08-26)

```
TRAIN  (first 65%)  ret  -2.2%  sharpe -0.22  maxDD 39.3%
HOLDOUT (last 35%)  ret  -5.8%  sharpe -0.50  maxDD 42.7%
FULL                ret  -3.5%  sharpe -0.33  vol  9.4%
Neighborhood best cell -0.07  vs  noise ceiling 0.86  (N=465 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.22, holdout sh -0.50 vs bar 0.3). No edge after 10bps costs.

## H56. H56. Crypto 14-day time-series trend 3-day rebal - NOT CONFIRMED (2026-08-26)

```
TRAIN  (first 65%)  ret +51.9%  sharpe +1.00  maxDD 56.4%
HOLDOUT (last 35%)  ret -16.7%  sharpe -0.17  maxDD 72.1%
FULL                ret +23.1%  sharpe +0.65  vol 55.3%
Neighborhood best cell +0.95  vs  noise ceiling 0.85  (N=474 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.00, holdout sh -0.17 vs bar 0.4). No edge after 10bps costs.

## H57. H57. Equity 90d vol-scaled momentum 2d skip 15d rebal - NOT CONFIRMED (2026-08-26)

```
TRAIN  (first 65%)  ret  -1.2%  sharpe -0.11  maxDD 24.9%
HOLDOUT (last 35%)  ret  -2.2%  sharpe -0.17  maxDD 25.2%
FULL                ret  -1.6%  sharpe -0.14  vol  8.8%
Neighborhood best cell -0.02  vs  noise ceiling 0.86  (N=483 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.11, holdout sh -0.17 vs bar 0.3). No edge after 10bps costs.

## H58. H58. Crypto 4-day XS reversal 2-day rebal 15-side - NOT CONFIRMED (2026-08-26)

```
TRAIN  (first 65%)  ret  -7.7%  sharpe -0.59  maxDD 62.4%
HOLDOUT (last 35%)  ret  -1.9%  sharpe +0.05  maxDD 53.3%
FULL                ret  -5.7%  sharpe -0.24  vol 18.0%
Neighborhood best cell -0.24  vs  noise ceiling 0.85  (N=489 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.59, holdout sh 0.05 vs bar 0.4). No edge after 10bps costs.

## H59. H59. Crypto 30d low-vol 7-day rebal - NOT CONFIRMED (2026-08-26)

```
TRAIN  (first 65%)  ret -18.1%  sharpe -0.98  maxDD 88.9%
HOLDOUT (last 35%)  ret -38.1%  sharpe -1.18  maxDD 94.7%
FULL                ret -25.8%  sharpe -1.03  vol 25.5%
Neighborhood best cell -0.88  vs  noise ceiling 0.85  (N=498 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.98, holdout sh -1.18 vs bar 0.4). No edge after 10bps costs.

## H60. Equity 6m XS momentum 5d skip bi-weekly rebal - NOT CONFIRMED (2026-08-26)

```
TRAIN  (first 65%)  ret  +1.5%  sharpe +0.19  maxDD 25.4%
HOLDOUT (last 35%)  ret  -0.4%  sharpe +0.04  maxDD 26.5%
FULL                ret  +0.8%  sharpe +0.13  vol 12.4%
Neighborhood best cell +0.21  vs  noise ceiling 0.87  (N=507 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.19, holdout sh 0.04 vs bar 0.3). No edge after 10bps costs.

## H61. Crypto 90d low-vol monthly rebal - NOT CONFIRMED (2026-08-26)

```
TRAIN  (first 65%)  ret  -7.7%  sharpe -0.40  maxDD 63.7%
HOLDOUT (last 35%)  ret -22.2%  sharpe -0.79  maxDD 81.9%
FULL                ret -13.1%  sharpe -0.57  vol 20.8%
Neighborhood best cell -0.50  vs  noise ceiling 0.85  (N=516 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.40, holdout sh -0.79 vs bar 0.4). No edge after 10bps costs.

## H62. Equity 2-week XS reversal 20-side weekly rebal - NOT CONFIRMED (2026-08-27)

```
TRAIN  (first 65%)  ret  -2.0%  sharpe -0.23  maxDD 28.8%
HOLDOUT (last 35%)  ret  -6.6%  sharpe -0.70  maxDD 36.2%
FULL                ret  -3.6%  sharpe -0.41  vol  8.2%
Neighborhood best cell +0.21  vs  noise ceiling 0.87  (N=525 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.23, holdout sh -0.70 vs bar 0.3). No edge after 10bps costs.

## H63. Crypto 6-month time-series trend bi-weekly rebal - NOT CONFIRMED (2026-08-27)

```
TRAIN  (first 65%)  ret +59.9%  sharpe +1.06  maxDD 68.3%
HOLDOUT (last 35%)  ret  -3.8%  sharpe +0.10  maxDD 66.9%
FULL                ret +33.9%  sharpe +0.80  vol 55.6%
Neighborhood best cell +0.80  vs  noise ceiling 0.86  (N=534 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.06, holdout sh 0.10 vs bar 0.4). No edge after 10bps costs.

## H64. Equity 40d vol-scaled momentum 5d skip bi-weekly rebal - NOT CONFIRMED (2026-08-27)

```
TRAIN  (first 65%)  ret  -3.0%  sharpe -0.37  maxDD 36.7%
HOLDOUT (last 35%)  ret  -5.2%  sharpe -0.53  maxDD 34.3%
FULL                ret  -3.8%  sharpe -0.43  vol  8.1%
Neighborhood best cell -0.27  vs  noise ceiling 0.87  (N=543 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.37, holdout sh -0.53 vs bar 0.3). No edge after 10bps costs.

## H65. Crypto 21d XS momentum 3d skip weekly rebal tight book - NOT CONFIRMED (2026-08-27)

```
TRAIN  (first 65%)  ret  +6.6%  sharpe +0.40  maxDD 48.6%
HOLDOUT (last 35%)  ret  +8.1%  sharpe +0.39  maxDD 42.0%
FULL                ret  +7.2%  sharpe +0.38  vol 29.3%
Neighborhood best cell +0.38  vs  noise ceiling 0.86  (N=552 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.40, holdout sh 0.39 vs bar 0.4). No edge after 10bps costs.

## H66. Equity 60d low-vol monthly rebal - NOT CONFIRMED (2026-08-27)

```
TRAIN  (first 65%)  ret  -7.2%  sharpe -0.74  maxDD 61.1%
HOLDOUT (last 35%)  ret -11.2%  sharpe -0.83  maxDD 53.2%
FULL                ret  -8.7%  sharpe -0.77  vol 11.0%
Neighborhood best cell -0.75  vs  noise ceiling 0.87  (N=561 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.74, holdout sh -0.83 vs bar 0.3). No edge after 10bps costs.

## H67. Equity 40d XS momentum 7d skip 20d rebal 20-side - NOT CONFIRMED (2026-08-29)

```
TRAIN  (first 65%)  ret  -1.1%  sharpe -0.12  maxDD 27.3%
HOLDOUT (last 35%)  ret  -0.9%  sharpe -0.05  maxDD 18.7%
FULL                ret  -1.0%  sharpe -0.09  vol  7.8%
Neighborhood best cell -0.02  vs  noise ceiling 0.87  (N=570 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.12, holdout sh -0.05 vs bar 0.3). No edge after 10bps costs.

## H68. Crypto 21d time-series trend 5-day rebal - NOT CONFIRMED (2026-08-29)

```
TRAIN  (first 65%)  ret +59.3%  sharpe +1.06  maxDD 72.0%
HOLDOUT (last 35%)  ret  -5.5%  sharpe +0.10  maxDD 68.4%
FULL                ret +32.7%  sharpe +0.78  vol 56.7%
Neighborhood best cell +1.04  vs  noise ceiling 0.86  (N=579 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.06, holdout sh 0.10 vs bar 0.4). No edge after 10bps costs.

## H69. Equity 120d vol-scaled momentum 10d skip 30d rebal - NOT CONFIRMED (2026-08-29)

```
TRAIN  (first 65%)  ret  -0.6%  sharpe -0.04  maxDD 21.9%
HOLDOUT (last 35%)  ret  -2.9%  sharpe -0.25  maxDD 26.1%
FULL                ret  -1.4%  sharpe -0.12  vol  8.6%
Neighborhood best cell +0.04  vs  noise ceiling 0.88  (N=588 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.04, holdout sh -0.25 vs bar 0.3). No edge after 10bps costs.

## H70. Crypto 45-day low-vol 14-day rebal - NOT CONFIRMED (2026-08-29)

```
TRAIN  (first 65%)  ret -16.3%  sharpe -0.89  maxDD 86.1%
HOLDOUT (last 35%)  ret -34.6%  sharpe -1.12  maxDD 92.0%
FULL                ret -23.2%  sharpe -0.96  vol 24.2%
Neighborhood best cell -0.75  vs  noise ceiling 0.86  (N=597 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.89, holdout sh -1.12 vs bar 0.4). No edge after 10bps costs.

## H71. Equity 1-year XS momentum 1-month skip quarterly rebal wide - NOT CONFIRMED (2026-08-31)

```
TRAIN  (first 65%)  ret  -0.8%  sharpe -0.08  maxDD 15.8%
HOLDOUT (last 35%)  ret  -0.2%  sharpe +0.01  maxDD 20.5%
FULL                ret  -0.6%  sharpe -0.05  vol  7.7%
Neighborhood best cell +0.16  vs  noise ceiling 0.88  (N=606 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.08, holdout sh 0.01 vs bar 0.3). No edge after 10bps costs.

## H72. Crypto 10-day time-series trend daily rebal - NOT CONFIRMED (2026-08-31)

```
TRAIN  (first 65%)  ret +54.9%  sharpe +1.02  maxDD 65.1%
HOLDOUT (last 35%)  ret -24.5%  sharpe -0.42  maxDD 79.7%
FULL                ret +20.4%  sharpe +0.61  vol 55.3%
Neighborhood best cell +0.83  vs  noise ceiling 0.87  (N=612 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.02, holdout sh -0.42 vs bar 0.4). No edge after 10bps costs.

## H73. Equity 20-day low-vol bi-weekly rebal - NOT CONFIRMED (2026-08-31)

```
TRAIN  (first 65%)  ret  -8.1%  sharpe -0.87  maxDD 63.9%
HOLDOUT (last 35%)  ret -11.0%  sharpe -0.87  maxDD 55.8%
FULL                ret  -9.1%  sharpe -0.86  vol 10.4%
Neighborhood best cell -0.73  vs  noise ceiling 0.88  (N=621 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.87, holdout sh -0.87 vs bar 0.3). No edge after 10bps costs.

## H74. Crypto 45-day vol-scaled momentum 3-day skip weekly rebal - NOT CONFIRMED (2026-08-31)

```
TRAIN  (first 65%)  ret  +3.2%  sharpe +0.28  maxDD 35.5%
HOLDOUT (last 35%)  ret  +8.0%  sharpe +0.46  maxDD 23.4%
FULL                ret  +4.9%  sharpe +0.35  vol 18.5%
Neighborhood best cell +0.55  vs  noise ceiling 0.87  (N=630 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.28, holdout sh 0.46 vs bar 0.4). No edge after 10bps costs.

## H75. Equity 10-day XS reversal weekly rebal 10-side - NOT CONFIRMED (2026-09-02)

```
TRAIN  (first 65%)  ret  -3.6%  sharpe -0.30  maxDD 40.8%
HOLDOUT (last 35%)  ret  -7.0%  sharpe -0.52  maxDD 38.4%
FULL                ret  -4.8%  sharpe -0.39  vol 11.1%
Neighborhood best cell +0.22  vs  noise ceiling 0.88  (N=639 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.30, holdout sh -0.52 vs bar 0.3). No edge after 10bps costs.

## H76. Crypto 6-month TS trend monthly rebal - NOT CONFIRMED (2026-09-02)

```
TRAIN  (first 65%)  ret +35.5%  sharpe +0.80  maxDD 93.2%
HOLDOUT (last 35%)  ret -14.8%  sharpe -0.25  maxDD 76.9%
FULL                ret +15.2%  sharpe +0.54  vol 55.9%
Neighborhood best cell +0.75  vs  noise ceiling 0.87  (N=648 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.80, holdout sh -0.25 vs bar 0.4). No edge after 10bps costs.

## H77. Equity 60d XS momentum 2d skip 10d rebal - NOT CONFIRMED (2026-09-02)

```
TRAIN  (first 65%)  ret  -1.7%  sharpe -0.19  maxDD 32.2%
HOLDOUT (last 35%)  ret  -2.2%  sharpe -0.16  maxDD 28.0%
FULL                ret  -1.9%  sharpe -0.18  vol  8.7%
Neighborhood best cell -0.08  vs  noise ceiling 0.88  (N=657 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.19, holdout sh -0.16 vs bar 0.3). No edge after 10bps costs.

## H78. Crypto 30d vol-scaled momentum 1d skip weekly rebal - NOT CONFIRMED (2026-09-02)

```
TRAIN  (first 65%)  ret +11.5%  sharpe +0.78  maxDD 29.4%
HOLDOUT (last 35%)  ret +12.2%  sharpe +0.61  maxDD 23.9%
FULL                ret +11.7%  sharpe +0.69  vol 18.6%
Neighborhood best cell +0.71  vs  noise ceiling 0.87  (N=666 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - passes the raw gate but the best neighborhood cell (0.71) is UNDER the noise ceiling (0.87) at N=666 cumulative tests: indistinguishable from the luckiest of that many tries. The multiple-testing bar did its job.

## H79. Crypto 10-day XS reversal 5d rebal 10-side tight book - NOT CONFIRMED (2026-09-02)

```
TRAIN  (first 65%)  ret -11.0%  sharpe -0.56  maxDD 72.6%
HOLDOUT (last 35%)  ret  -4.1%  sharpe +0.05  maxDD 37.4%
FULL                ret  -8.7%  sharpe -0.24  vol 24.7%
Neighborhood best cell -0.05  vs  noise ceiling 0.87  (N=675 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.56, holdout sh 0.05 vs bar 0.4). No edge after 10bps costs.

## H80. Equity 7d XS reversal 3d rebal 15-side - NOT CONFIRMED (2026-09-03)

```
TRAIN  (first 65%)  ret  -2.5%  sharpe -0.25  maxDD 44.5%
HOLDOUT (last 35%)  ret  -7.3%  sharpe -0.65  maxDD 42.2%
FULL                ret  -4.2%  sharpe -0.41  vol  9.3%
Neighborhood best cell -0.23  vs  noise ceiling 0.89  (N=684 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.25, holdout sh -0.65 vs bar 0.3). No edge after 10bps costs.

## H81. Crypto 6-month TS trend biweekly rebal - NOT CONFIRMED (2026-09-03)

```
TRAIN  (first 65%)  ret +48.5%  sharpe +0.94  maxDD 89.8%
HOLDOUT (last 35%)  ret -16.2%  sharpe -0.28  maxDD 78.4%
FULL                ret +21.5%  sharpe +0.63  vol 55.9%
Neighborhood best cell +0.81  vs  noise ceiling 0.87  (N=693 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.94, holdout sh -0.28 vs bar 0.4). No edge after 10bps costs.

## H82. Equity 30d vol-scaled momentum 1d skip weekly rebal - NOT CONFIRMED (2026-09-03)

```
TRAIN  (first 65%)  ret  -5.8%  sharpe -0.76  maxDD 49.6%
HOLDOUT (last 35%)  ret  -5.8%  sharpe -0.58  maxDD 34.7%
FULL                ret  -5.8%  sharpe -0.68  vol  8.2%
Neighborhood best cell -0.43  vs  noise ceiling 0.89  (N=702 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.76, holdout sh -0.58 vs bar 0.3). No edge after 10bps costs.

## H83. Crypto 2-week XS momentum 1d skip weekly rebal tight - NOT CONFIRMED (2026-09-03)

```
TRAIN  (first 65%)  ret  +8.8%  sharpe +0.54  maxDD 42.2%
HOLDOUT (last 35%)  ret  -3.7%  sharpe +0.05  maxDD 56.0%
FULL                ret  +4.2%  sharpe +0.29  vol 24.6%
Neighborhood best cell +0.63  vs  noise ceiling 0.88  (N=711 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.54, holdout sh 0.05 vs bar 0.4). No edge after 10bps costs.

## H84. Crypto 60d low-vol monthly rebal - NOT CONFIRMED (2026-09-03)

```
TRAIN  (first 65%)  ret -10.9%  sharpe -0.58  maxDD 72.5%
HOLDOUT (last 35%)  ret -28.6%  sharpe -0.92  maxDD 87.7%
FULL                ret -17.6%  sharpe -0.72  vol 23.0%
Neighborhood best cell -0.54  vs  noise ceiling 0.88  (N=720 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.58, holdout sh -0.92 vs bar 0.4). No edge after 10bps costs.

## H85. Equity 4d XS reversal 2d rebal 20-side - NOT CONFIRMED (2026-09-04)

```
TRAIN  (first 65%)  ret  -5.5%  sharpe -0.74  maxDD 53.3%
HOLDOUT (last 35%)  ret -14.3%  sharpe -1.60  maxDD 56.5%
FULL                ret  -8.7%  sharpe -1.08  vol  8.1%
Neighborhood best cell -0.60  vs  noise ceiling 0.89  (N=726 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.74, holdout sh -1.60 vs bar 0.3). No edge after 10bps costs.

## H86. Crypto 120d XS momentum 5d skip bi-weekly rebal tight - NOT CONFIRMED (2026-09-04)

```
TRAIN  (first 65%)  ret  -6.9%  sharpe -0.34  maxDD 72.1%
HOLDOUT (last 35%)  ret  +4.0%  sharpe +0.28  maxDD 46.1%
FULL                ret  -3.2%  sharpe -0.06  vol 20.1%
Neighborhood best cell +0.21  vs  noise ceiling 0.88  (N=735 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.34, holdout sh 0.28 vs bar 0.4). No edge after 10bps costs.

## H87. Equity 12m vol-scaled momentum 1m skip quarterly rebal - NOT CONFIRMED (2026-09-04)

```
TRAIN  (first 65%)  ret  -0.6%  sharpe -0.04  maxDD 16.5%
HOLDOUT (last 35%)  ret  -2.9%  sharpe -0.23  maxDD 23.4%
FULL                ret  -1.4%  sharpe -0.12  vol  8.9%
Neighborhood best cell +0.15  vs  noise ceiling 0.89  (N=744 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.04, holdout sh -0.23 vs bar 0.3). No edge after 10bps costs.

## H88. Equity 6m XS momentum 5d skip monthly rebal wide book - NOT CONFIRMED (2026-09-04)

```
TRAIN  (first 65%)  ret  +0.3%  sharpe +0.08  maxDD 14.2%
HOLDOUT (last 35%)  ret  +0.1%  sharpe +0.05  maxDD 20.7%
FULL                ret  +0.2%  sharpe +0.07  vol  8.1%
Neighborhood best cell +0.13  vs  noise ceiling 0.89  (N=753 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.08, holdout sh 0.05 vs bar 0.3). No edge after 10bps costs.

## H89. Crypto 6m XS momentum 10d skip monthly rebal tight - NOT CONFIRMED (2026-09-06)

```
TRAIN  (first 65%)  ret  -6.3%  sharpe -0.36  maxDD 56.4%
HOLDOUT (last 35%)  ret  -4.5%  sharpe -0.11  maxDD 49.9%
FULL                ret  -5.7%  sharpe -0.25  vol 17.5%
Neighborhood best cell +0.18  vs  noise ceiling 0.88  (N=762 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.36, holdout sh -0.11 vs bar 0.4). No edge after 10bps costs.

## H90. Equity annual TS trend quarterly rebal - **RETIRED, NOT CONFIRMED** (confirmed 2026-09-06, retired 2026-09-18, ledger corrected 2026-09-22)

```
TRAIN  (first 65%)  ret  +7.4%  sharpe +0.59  maxDD 33.3%
HOLDOUT (last 35%)  ret  +3.5%  sharpe +0.38  maxDD 25.5%
FULL                ret  +6.0%  sharpe +0.52  vol 12.6%
Neighborhood best cell +0.98  vs  noise ceiling 0.89  (N=771 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> PASS
```

Autopsy: CONFIRMED - cleared >0.3 sharpe in BOTH halves AND beat the rising noise ceiling (0.98 > 0.89 at N=771). First survivor. Next gates before capital: sizing/risk module, bootstrap CIs, survivorship-free re-test.

### LEDGER CORRECTION (2026-09-22)

This entry read **CONFIRMED** for four days after the project had already
retired it, and that stale label was the graveyard's only remaining
confirmation. Corrected here so the count is honest.

`GRAVEYARD-REVIEW.md` (2026-09-18) already found:

> "**H90 is done.** It cleared sharpe > 0.3 in both halves and beat the noise
> ceiling, and it **loses to SPY by 6.2%/yr on a paired test.** Rule 5: the
> verdict is the decision."

H90 passed the gates **in force at its registration**, which is not in dispute
and is not being retroactively denied. What happened is that gate 4 -- BEATS
`spy_buyhold` on a paired difference -- was added to the standard gate set
afterwards, and H90 loses it by 6.2%/yr. Its own autopsy above named three
things required "before capital": a sizing/risk module, bootstrap CIs, and a
survivorship-free re-test. **None of the three was ever run.** H141 has since
demonstrated that the survivorship concern is not hypothetical.

**Consequence, stated plainly: the Graveyard has ZERO hypotheses that survive a
paired test against buy-and-hold.** 145 judged, 0 standing. EdgeBot's
confirmations are a separate project and are not counted here.

That is the project's actual result, and it is a real one: 145 pre-registered
tests, with costs, a rising noise ceiling and a proper benchmark, establishing
that retail-known structures on the most liquid index instruments are empty.

## H91. Crypto 10d low-vol ultra-fast rebal - NOT CONFIRMED (2026-09-06)

```
TRAIN  (first 65%)  ret -12.5%  sharpe -0.59  maxDD 79.8%
HOLDOUT (last 35%)  ret -41.3%  sharpe -1.22  maxDD 95.8%
FULL                ret -23.9%  sharpe -0.86  vol 27.2%
Neighborhood best cell -0.74  vs  noise ceiling 0.88  (N=780 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.59, holdout sh -1.22 vs bar 0.4). No edge after 10bps costs.

## H92. Crypto 90d vol-scaled momentum 7d skip biweekly rebal - NOT CONFIRMED (2026-09-06)

```
TRAIN  (first 65%)  ret  -4.3%  sharpe -0.22  maxDD 43.0%
HOLDOUT (last 35%)  ret  +3.5%  sharpe +0.27  maxDD 50.8%
FULL                ret  -1.6%  sharpe -0.00  vol 17.8%
Neighborhood best cell +0.40  vs  noise ceiling 0.88  (N=789 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.22, holdout sh 0.27 vs bar 0.4). No edge after 10bps costs.

## H93. Equity 90d XS momentum 20d skip 5d rebal 25-side - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret  -2.1%  sharpe -0.27  maxDD 31.7%
HOLDOUT (last 35%)  ret  -1.8%  sharpe -0.17  maxDD 24.9%
FULL                ret  -2.0%  sharpe -0.23  vol  7.5%
Neighborhood best cell -0.05  vs  noise ceiling 0.90  (N=798 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.27, holdout sh -0.17 vs bar 0.3). No edge after 10bps costs.

## H94. Crypto 60d time-series trend 3-day rebal - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret +35.9%  sharpe +0.81  maxDD 88.5%
HOLDOUT (last 35%)  ret  +5.0%  sharpe +0.33  maxDD 65.1%
FULL                ret +24.2%  sharpe +0.67  vol 55.8%
Neighborhood best cell +0.77  vs  noise ceiling 0.88  (N=807 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.81, holdout sh 0.33 vs bar 0.4). No edge after 10bps costs.

## H95. Crypto 15d low-vol tilt 5-day rebal - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret -11.3%  sharpe -0.54  maxDD 74.9%
HOLDOUT (last 35%)  ret -40.5%  sharpe -1.19  maxDD 95.9%
FULL                ret -22.9%  sharpe -0.83  vol 26.9%
Neighborhood best cell -0.82  vs  noise ceiling 0.89  (N=816 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.54, holdout sh -1.19 vs bar 0.4). No edge after 10bps costs.

## H96. Equity 8-day XS reversal 2-day rebal 30-side - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret  -3.0%  sharpe -0.49  maxDD 37.3%
HOLDOUT (last 35%)  ret  -7.6%  sharpe -0.98  maxDD 37.9%
FULL                ret  -4.6%  sharpe -0.69  vol  6.6%
Neighborhood best cell -0.30  vs  noise ceiling 0.90  (N=825 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.49, holdout sh -0.98 vs bar 0.3). No edge after 10bps costs.

## H97. Equity 75d vol-scaled momentum 15d skip weekly rebal - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret  -2.6%  sharpe -0.31  maxDD 38.2%
HOLDOUT (last 35%)  ret  -6.8%  sharpe -0.63  maxDD 37.2%
FULL                ret  -4.1%  sharpe -0.44  vol  8.6%
Neighborhood best cell -0.16  vs  noise ceiling 0.90  (N=834 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.31, holdout sh -0.63 vs bar 0.3). No edge after 10bps costs.

## H98. Crypto 1M Time-Series Trend 7D Rebal - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret +79.2%  sharpe +1.27  maxDD 59.1%
HOLDOUT (last 35%)  ret  -1.7%  sharpe +0.18  maxDD 50.3%
FULL                ret +45.3%  sharpe +0.96  vol 54.6%
Neighborhood best cell +1.04  vs  noise ceiling 0.89  (N=843 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.27, holdout sh 0.18 vs bar 0.4). No edge after 10bps costs.

## H99. Equity 3M Low-Vol Tilt 20D Rebal - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret  -8.6%  sharpe -0.88  maxDD 65.2%
HOLDOUT (last 35%)  ret  -9.3%  sharpe -0.67  maxDD 51.8%
FULL                ret  -8.8%  sharpe -0.78  vol 11.0%
Neighborhood best cell -0.76  vs  noise ceiling 0.90  (N=852 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.88, holdout sh -0.67 vs bar 0.3). No edge after 10bps costs.

## H100. Crypto 60D Vol-Scaled Momentum 3D Skip 5D Rebal - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret  +0.4%  sharpe +0.11  maxDD 38.1%
HOLDOUT (last 35%)  ret +16.7%  sharpe +0.80  maxDD 19.5%
FULL                ret  +5.8%  sharpe +0.41  vol 18.0%
Neighborhood best cell +0.50  vs  noise ceiling 0.89  (N=861 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.11, holdout sh 0.80 vs bar 0.4). No edge after 10bps costs.

## H101. Equity 5D XS Reversal 2D Rebal 30-side - NOT CONFIRMED (2026-09-08)

```
TRAIN  (first 65%)  ret  -4.8%  sharpe -0.80  maxDD 48.0%
HOLDOUT (last 35%)  ret -12.4%  sharpe -1.68  maxDD 53.2%
FULL                ret  -7.5%  sharpe -1.15  vol  6.6%
Neighborhood best cell -0.54  vs  noise ceiling 0.90  (N=867 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.80, holdout sh -1.68 vs bar 0.3). No edge after 10bps costs.

## H102. H102: Equity 1Y XS momentum 1M skip quarterly rebal ultra-wide - NOT CONFIRMED (2026-09-11)

```
TRAIN  (first 65%)  ret  -0.2%  sharpe -0.01  maxDD 13.8%
HOLDOUT (last 35%)  ret  -0.9%  sharpe -0.07  maxDD 19.6%
FULL                ret  -0.5%  sharpe -0.03  vol  6.9%
Neighborhood best cell +0.12  vs  noise ceiling 0.90  (N=876 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.01, holdout sh -0.07 vs bar 0.3). No edge after 10bps costs.

## H103. H103: Crypto 6-day XS reversal daily rebal ultra-wide - NOT CONFIRMED (2026-09-11)

```
TRAIN  (first 65%)  ret  +0.0%  sharpe +0.00  maxDD  0.0%
HOLDOUT (last 35%)  ret  +2.8%  sharpe +0.32  maxDD 25.5%
FULL                ret  +1.0%  sharpe +0.19  vol  6.0%
Neighborhood best cell +0.19  vs  noise ceiling 0.89  (N=882 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.00, holdout sh 0.32 vs bar 0.4). No edge after 10bps costs.

## H104. H104: Equity 6M vol-scaled momentum 10D skip monthly rebal tight - NOT CONFIRMED (2026-09-11)

```
TRAIN  (first 65%)  ret  -0.2%  sharpe +0.01  maxDD 19.4%
HOLDOUT (last 35%)  ret  -0.3%  sharpe +0.02  maxDD 23.5%
FULL                ret  -0.3%  sharpe +0.02  vol  9.1%
Neighborhood best cell +0.02  vs  noise ceiling 0.90  (N=891 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.01, holdout sh 0.02 vs bar 0.3). No edge after 10bps costs.

## H105. H105: Crypto 4-month time-series trend biweekly rebal - NOT CONFIRMED (2026-09-11)

```
TRAIN  (first 65%)  ret +59.0%  sharpe +1.05  maxDD 65.7%
HOLDOUT (last 35%)  ret  -5.0%  sharpe +0.07  maxDD 68.1%
FULL                ret +32.7%  sharpe +0.79  vol 55.7%
Neighborhood best cell +0.79  vs  noise ceiling 0.89  (N=900 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.05, holdout sh 0.07 vs bar 0.4). No edge after 10bps costs.

## H106. H106: Crypto 45-day low-vol tilt 3-week rebal - NOT CONFIRMED (2026-09-11)

```
TRAIN  (first 65%)  ret -16.6%  sharpe -0.91  maxDD 85.6%
HOLDOUT (last 35%)  ret -27.8%  sharpe -0.87  maxDD 86.6%
FULL                ret -20.7%  sharpe -0.86  vol 23.6%
Neighborhood best cell -0.64  vs  noise ceiling 0.89  (N=909 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.91, holdout sh -0.87 vs bar 0.4). No edge after 10bps costs.

## H107. H107: Equity 15d XS reversal 10d rebal 20-side - NOT CONFIRMED (2026-09-12)

```
TRAIN  (first 65%)  ret  -5.4%  sharpe -0.74  maxDD 46.2%
HOLDOUT (last 35%)  ret  -3.1%  sharpe -0.30  maxDD 23.1%
FULL                ret  -4.6%  sharpe -0.56  vol  7.8%
Neighborhood best cell -0.21  vs  noise ceiling 0.91  (N=918 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.74, holdout sh -0.30 vs bar 0.3). No edge after 10bps costs.

## H108. H109: Crypto 45d XS momentum 5d skip 10d rebal 8-side - NOT CONFIRMED (2026-09-12)

```
TRAIN  (first 65%)  ret  -2.4%  sharpe +0.01  maxDD 42.9%
HOLDOUT (last 35%)  ret  -8.9%  sharpe -0.08  maxDD 67.9%
FULL                ret  -4.8%  sharpe -0.03  vol 28.0%
Neighborhood best cell +0.34  vs  noise ceiling 0.89  (N=927 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.01, holdout sh -0.08 vs bar 0.4). No edge after 10bps costs.

## H109. H110: Equity 9m vol-scaled momentum 1m skip monthly rebal - NOT CONFIRMED (2026-09-12)

```
TRAIN  (first 65%)  ret  -0.5%  sharpe -0.02  maxDD 23.7%
HOLDOUT (last 35%)  ret  -3.8%  sharpe -0.31  maxDD 24.9%
FULL                ret  -1.7%  sharpe -0.14  vol  9.2%
Neighborhood best cell +0.07  vs  noise ceiling 0.91  (N=936 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.02, holdout sh -0.31 vs bar 0.3). No edge after 10bps costs.

## H110. H111: Crypto 7d XS reversal 3d rebal 10-side - NOT CONFIRMED (2026-09-12)

```
TRAIN  (first 65%)  ret -10.7%  sharpe -0.49  maxDD 76.1%
HOLDOUT (last 35%)  ret  -1.9%  sharpe +0.12  maxDD 44.8%
FULL                ret  -7.7%  sharpe -0.18  vol 26.1%
Neighborhood best cell -0.00  vs  noise ceiling 0.90  (N=945 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.49, holdout sh 0.12 vs bar 0.4). No edge after 10bps costs.

## H111. Equity 6d XS reversal 3d rebal 25-side - NOT CONFIRMED (2026-09-14)

```
TRAIN  (first 65%)  ret  -4.6%  sharpe -0.69  maxDD 44.8%
HOLDOUT (last 35%)  ret  -7.7%  sharpe -0.93  maxDD 40.0%
FULL                ret  -5.7%  sharpe -0.78  vol  7.1%
Neighborhood best cell -0.35  vs  noise ceiling 0.91  (N=954 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.69, holdout sh -0.93 vs bar 0.3). No edge after 10bps costs.

## H112. Crypto 180d XS momentum 14d skip biweekly rebal 8-side - NOT CONFIRMED (2026-09-14)

```
TRAIN  (first 65%)  ret -10.5%  sharpe -0.47  maxDD 76.7%
HOLDOUT (last 35%)  ret  -1.6%  sharpe +0.06  maxDD 56.2%
FULL                ret  -7.4%  sharpe -0.25  vol 21.8%
Neighborhood best cell +0.23  vs  noise ceiling 0.90  (N=963 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.47, holdout sh 0.06 vs bar 0.4). No edge after 10bps costs.

## H113. Equity 45d vol-scaled momentum 2d skip weekly rebal - NOT CONFIRMED (2026-09-14)

```
TRAIN  (first 65%)  ret  -3.3%  sharpe -0.40  maxDD 41.9%
HOLDOUT (last 35%)  ret  -2.3%  sharpe -0.20  maxDD 25.9%
FULL                ret  -3.0%  sharpe -0.32  vol  8.3%
Neighborhood best cell -0.19  vs  noise ceiling 0.91  (N=972 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.40, holdout sh -0.20 vs bar 0.3). No edge after 10bps costs.

## H114. Equity 20d XS momentum 2d skip weekly rebal 20-side - NOT CONFIRMED (2026-09-14)

```
TRAIN  (first 65%)  ret  -4.1%  sharpe -0.55  maxDD 37.7%
HOLDOUT (last 35%)  ret  -6.0%  sharpe -0.62  maxDD 31.6%
FULL                ret  -4.8%  sharpe -0.57  vol  8.0%
Neighborhood best cell -0.37  vs  noise ceiling 0.91  (N=981 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.55, holdout sh -0.62 vs bar 0.3). No edge after 10bps costs.

## H115. Crypto ultra-short 3-day time-series trend daily rebal - NOT CONFIRMED (2026-09-16)

```
TRAIN  (first 65%)  ret +34.6%  sharpe +0.80  maxDD 69.8%
HOLDOUT (last 35%)  ret -28.7%  sharpe -0.52  maxDD 87.0%
FULL                ret  +7.8%  sharpe +0.41  vol 54.5%
Neighborhood best cell +0.65  vs  noise ceiling 0.90  (N=987 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.80, holdout sh -0.52 vs bar 0.4). No edge after 10bps costs.

## H116. Crypto ultra-short 5d low-vol tilt tri-daily rebal - NOT CONFIRMED (2026-09-16)

```
TRAIN  (first 65%)  ret -19.2%  sharpe -1.04  maxDD 90.9%
HOLDOUT (last 35%)  ret -48.0%  sharpe -1.65  maxDD 97.6%
FULL                ret -30.8%  sharpe -1.28  vol 25.9%
Neighborhood best cell -0.93  vs  noise ceiling 0.90  (N=993 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -1.04, holdout sh -1.65 vs bar 0.4). No edge after 10bps costs.

## H117. Equity 3M vol-scaled momentum 5d skip 10d rebal - NOT CONFIRMED (2026-09-16)

```
TRAIN  (first 65%)  ret  -2.3%  sharpe -0.26  maxDD 36.8%
HOLDOUT (last 35%)  ret  -4.2%  sharpe -0.33  maxDD 28.0%
FULL                ret  -3.0%  sharpe -0.29  vol  9.1%
Neighborhood best cell -0.08  vs  noise ceiling 0.91  (N=1002 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.26, holdout sh -0.33 vs bar 0.3). No edge after 10bps costs.

## H118. Crypto 1-day XS reversal daily rebal ultra-wide - NOT CONFIRMED (2026-09-16)

```
TRAIN  (first 65%)  ret  +0.0%  sharpe +0.00  maxDD  0.0%
HOLDOUT (last 35%)  ret  +1.5%  sharpe +0.20  maxDD 40.4%
FULL                ret  +0.5%  sharpe +0.12  vol  5.7%
Neighborhood best cell +0.14  vs  noise ceiling 0.90  (N=1006 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.00, holdout sh 0.20 vs bar 0.4). No edge after 10bps costs.

## H119. Equity 20d XS reversal 10d rebal 15-side - NOT CONFIRMED (2026-09-17)

```
TRAIN  (first 65%)  ret  -2.8%  sharpe -0.30  maxDD 30.4%
HOLDOUT (last 35%)  ret  -4.7%  sharpe -0.44  maxDD 30.5%
FULL                ret  -3.5%  sharpe -0.35  vol  8.9%
Neighborhood best cell -0.04  vs  noise ceiling 0.91  (N=1015 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.30, holdout sh -0.44 vs bar 0.3). No edge after 10bps costs.

## H120. Crypto 6-month TS trend monthly rebal slow - NOT CONFIRMED (2026-09-17)

```
TRAIN  (first 65%)  ret +47.5%  sharpe +0.94  maxDD 79.5%
HOLDOUT (last 35%)  ret -14.1%  sharpe -0.18  maxDD 84.2%
FULL                ret +22.1%  sharpe +0.64  vol 55.4%
Neighborhood best cell +0.80  vs  noise ceiling 0.90  (N=1024 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.94, holdout sh -0.18 vs bar 0.4). No edge after 10bps costs.

## H121. Equity 9M XS momentum 1M skip monthly rebal tight - NOT CONFIRMED (2026-09-17)

```
TRAIN  (first 65%)  ret  +2.2%  sharpe +0.25  maxDD 19.5%
HOLDOUT (last 35%)  ret  +0.1%  sharpe +0.07  maxDD 27.6%
FULL                ret  +1.5%  sharpe +0.18  vol 12.3%
Neighborhood best cell +0.29  vs  noise ceiling 0.91  (N=1033 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.25, holdout sh 0.07 vs bar 0.3). No edge after 10bps costs.

## H122. Crypto 6M vol-scaled momentum 10d skip biweekly refined - NOT CONFIRMED (2026-09-17)

```
TRAIN  (first 65%)  ret  -6.3%  sharpe -0.44  maxDD 56.4%
HOLDOUT (last 35%)  ret  +0.9%  sharpe +0.15  maxDD 32.4%
FULL                ret  -3.8%  sharpe -0.17  vol 15.9%
Neighborhood best cell +0.17  vs  noise ceiling 0.90  (N=1042 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.44, holdout sh 0.15 vs bar 0.4). No edge after 10bps costs.

## H123. Crypto 30d XS reversal weekly rebal tight 8-side - NOT CONFIRMED (2026-09-17)

```
TRAIN  (first 65%)  ret -22.2%  sharpe -1.01  maxDD 92.9%
HOLDOUT (last 35%)  ret -16.2%  sharpe -0.32  maxDD 66.8%
FULL                ret -20.2%  sharpe -0.67  vol 27.7%
Neighborhood best cell -0.26  vs  noise ceiling 0.90  (N=1051 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -1.01, holdout sh -0.32 vs bar 0.4). No edge after 10bps costs.

## H124. Equity 60d XS reversal monthly rebal medium book - NOT CONFIRMED (2026-09-18)

```
TRAIN  (first 65%)  ret  -1.3%  sharpe -0.11  maxDD 19.7%
HOLDOUT (last 35%)  ret  +0.1%  sharpe +0.06  maxDD 26.1%
FULL                ret  -0.8%  sharpe -0.04  vol  9.8%
Neighborhood best cell -0.04  vs  noise ceiling 0.91  (N=1060 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.11, holdout sh 0.06 vs bar 0.3). No edge after 10bps costs.

## H125. Crypto 1-year time-series trend monthly rebal - NOT CONFIRMED (2026-09-18)

```
TRAIN  (first 65%)  ret +63.5%  sharpe +1.08  maxDD 92.1%
HOLDOUT (last 35%)  ret  -9.8%  sharpe -0.09  maxDD 71.6%
FULL                ret +32.8%  sharpe +0.78  vol 57.0%
Neighborhood best cell +0.78  vs  noise ceiling 0.90  (N=1069 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 1.08, holdout sh -0.09 vs bar 0.4). No edge after 10bps costs.

## H126. Crypto 12-1 XS momentum monthly rebal tight book - NOT CONFIRMED (2026-09-18)

```
TRAIN  (first 65%)  ret  -3.8%  sharpe -0.12  maxDD 65.1%
HOLDOUT (last 35%)  ret  -1.5%  sharpe +0.04  maxDD 37.1%
FULL                ret  -3.0%  sharpe -0.06  vol 19.4%
Neighborhood best cell +0.07  vs  noise ceiling 0.90  (N=1078 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.12, holdout sh 0.04 vs bar 0.4). No edge after 10bps costs.

## H127. Equity 6M low-vol weekly rebal - NOT CONFIRMED (2026-09-18)

```
TRAIN  (first 65%)  ret  -9.2%  sharpe -0.92  maxDD 67.2%
HOLDOUT (last 35%)  ret -10.6%  sharpe -0.75  maxDD 54.3%
FULL                ret  -9.7%  sharpe -0.84  vol 11.4%
Neighborhood best cell -0.78  vs  noise ceiling 0.92  (N=1087 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.92, holdout sh -0.75 vs bar 0.3). No edge after 10bps costs.

## H128. Equity 1M vol-scaled momentum 2d skip tri-daily rebal - NOT CONFIRMED (2026-09-18)

```
TRAIN  (first 65%)  ret  -5.9%  sharpe -0.79  maxDD 48.0%
HOLDOUT (last 35%)  ret  -6.7%  sharpe -0.70  maxDD 33.5%
FULL                ret  -6.1%  sharpe -0.75  vol  8.1%
Neighborhood best cell -0.63  vs  noise ceiling 0.92  (N=1096 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.79, holdout sh -0.70 vs bar 0.3). No edge after 10bps costs.

## H124b. ES opening-range breakout, 09:30-10:00 range, intraday - NOT CONFIRMED (2026-09-18)
- NUMBERING CORRECTION (2026-09-20): registered as H124 on 2026-09-18, colliding with the auto-pipeline's H124 (Equity 60d XS reversal) registered the same day. Renamed H124b here and in VERDICTS.md. Content, date and verdict unchanged; only the label was ambiguous.

```
ES continuous 1-min, 2024-08-25..2026-08-24, 491 eligible sessions (1.95y), 479 trades
costs $27.50/round trip (1 tick slippage/side + $1.25 commission/side), ES not MES

TRAIN   (first 65%, 319 sess)  net  +$10,705.00  sharpe +0.34  maxDD 73.8%
HOLDOUT (last 35%, 172 sess)   net  -$10,927.50  sharpe -0.67  maxDD 64.8%
FULL                           net     -$222.50  sharpe -0.00  maxDD 84.4%  win 46.1%  stops 190

Neighborhood (3x3), best cell +0.39  vs  noise ceiling 1.50 (N=9, 1.95y)   [cumulative N=1015 bar: 2.67]

GATE 1  net>0 AND sharpe>0.5 both halves          -> FAIL (holdout -$10,927, sh -0.67)
GATE 2  holdout 95% CI on sharpe excludes zero    -> FAIL (-0.67 [-3.20, +1.63], P(>0.5)=17%)
GATE 3  best cell clears the noise ceiling        -> FAIL (0.39 vs 1.50)
GATE 4  BEATS spy_buyhold, paired difference      -> FAIL (TIES; ORB -38.0%/yr vs SPY +14.2%/yr,
                                                    diff-sharpe -0.15 [-1.57, +1.21], 491 overlaps)
```

Autopsy: NOT CONFIRMED - all four pre-set gates failed. Train positive, holdout strongly
negative, full sample flat because the two cancel; that is the ordinary shape of a rule fitted
to nothing in particular. No cell in the 3x3 came within a factor of three of the noise ceiling.

Two things worth keeping from this corpse:

1. THE ARITHMETIC MEAN LIED. Mean daily P&L put the full sample at -0.5%/yr, which reads as
   "roughly flat". Compounded on the same $25k notional it is -38.0%/yr. The gap is volatility
   drag against an 84.4% drawdown. Any future intraday verdict reports the geometric figure.

2. THE SAMPLE WAS TOO SHORT AND THAT WAS KNOWN IN ADVANCE. The power note in the registration
   said 1.95 years might fail a good strategy. It did not get the chance to matter here - the
   best cell was 0.39 against a 1.50 bar, so this is a clean fail, not an underpowered one. But
   the ceiling arithmetic stands as a constraint on all future work with this data: at 1.95
   years, the cumulative-cell bar is 2.67, and essentially nothing clears that. More ES history
   is a precondition for intraday research here, not an optimisation.

Provenance: research/orb.py (frozen spec from AUTOMATED-TRADING-RESEARCH.md 2026-09-15),
results in research/results/2026-09-18/. Registered PRE-DATA 2026-09-18; no parameters, windows
or gates were changed after the run.

## H129. Equity 3d XS reversal 3d rebal 10-side - NOT CONFIRMED (2026-09-19)

```
TRAIN  (first 65%)  ret  -8.4%  sharpe -0.83  maxDD 64.9%
HOLDOUT (last 35%)  ret -13.7%  sharpe -1.22  maxDD 55.4%
FULL                ret -10.3%  sharpe -0.98  vol 10.5%
Neighborhood best cell -0.21  vs  noise ceiling 0.92  (N=1105 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.83, holdout sh -1.22 vs bar 0.3). No edge after 10bps costs.

## H130. Crypto 120d XS momentum 7d skip biweekly rebal 6-side - NOT CONFIRMED (2026-09-19)

```
TRAIN  (first 65%)  ret  +2.2%  sharpe +0.21  maxDD 62.0%
HOLDOUT (last 35%)  ret  -8.9%  sharpe -0.11  maxDD 70.8%
FULL                ret  -1.9%  sharpe +0.07  vol 27.4%
Neighborhood best cell +0.28  vs  noise ceiling 0.91  (N=1114 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.21, holdout sh -0.11 vs bar 0.4). No edge after 10bps costs.

## H131. Crypto 6m vol-scaled momentum 14d skip monthly rebal - NOT CONFIRMED (2026-09-19)

```
TRAIN  (first 65%)  ret  -8.1%  sharpe -0.58  maxDD 62.2%
HOLDOUT (last 35%)  ret  -0.3%  sharpe +0.09  maxDD 37.2%
FULL                ret  -5.4%  sharpe -0.27  vol 15.8%
Neighborhood best cell -0.00  vs  noise ceiling 0.91  (N=1123 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.58, holdout sh 0.09 vs bar 0.4). No edge after 10bps costs.

## H132. Equity 6m low-vol quarterly rebal - NOT CONFIRMED (2026-09-19)

```
TRAIN  (first 65%)  ret  -9.4%  sharpe -1.00  maxDD 67.4%
HOLDOUT (last 35%)  ret -10.0%  sharpe -0.71  maxDD 52.3%
FULL                ret  -9.6%  sharpe -0.86  vol 11.1%
Neighborhood best cell -0.81  vs  noise ceiling 0.92  (N=1132 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -1.00, holdout sh -0.71 vs bar 0.3). No edge after 10bps costs.

## H133-ES. ES opening-range breakout, IDENTICAL rule, 16.07-year sample - NOT CONFIRMED (2026-09-20)
- NUMBERING CORRECTION (2026-09-21): the auto-pipeline registered its own H133 (Equity 45d XS reversal) after this one. Renamed H133-ES here and in VERDICTS.md. Content, gates, date and verdict unchanged. Root cause: the pipeline picks the next integer without checking for headers added by hand. See the DUPLICATE-LABELS finding.

Registered PRE-DATA and PRE-PURCHASE in commit fb10369 on 2026-09-20, before the
$31.91 Databento order was placed. All five gates, the roll rule, the cost model
and the reported-but-not-gated diagnostics were fixed in that commit. Nothing
below was chosen after seeing a number.

**Sample.** Databento GLBX.MDP3 `ohlcv-1m`, `ES.FUT` parent, 2010-06-06..2026-09-20.
1,608,271 front-month RTH bars over 4,049 eligible sessions = **16.07 years**.
Rejected: 34 scheduled early closes, 10 sessions with missing minutes, 4 missing
previous close. Front month by daily volume, 66 rolls (quarterly, as ES should
be), 0 volume ties, 0 duplicate timestamps. Provenance in
`data/es_1m_continuous.QUALITY.md`.

**This is 8.25x H124b's sample.** H124b's autopsy blamed 1.95 years. That excuse
is now spent.

### Gates - ALL FOUR FAILED

| gate | requirement | result | |
|---|---|---|---|
| 1 | net>0 AND sharpe>0.5 in BOTH halves | train -$100,382.50 / -0.98; holdout +$32,840.00 / +0.27 | **FAIL** |
| 2 | holdout 95% block-bootstrap CI excludes zero | +0.27 [-0.47, +1.01], P(>0.5)=25.9%, STRADDLES | **FAIL** |
| 3 | best neighborhood cell > 0.5998 (N=18 over 16.07y) | best cell (or630_brk660) = **-0.0848** | **FAIL** |
| 4 | BEATS spy_buyhold on paired difference | **LOSES TO**: -28.94%/yr vs +15.59%/yr, diff-sharpe -0.50 [-0.98, -0.03], 4,047 overlaps | **FAIL** |
| 5 | $40 stress does not sink gates 1-2 | n/a, 1 and 2 already failed. For the record: train -$131,795 / -1.29, holdout +$15,727 / +0.13 | - |

Gate 3 is the decisive one and it is worse than a near miss. **All nine
neighborhood cells are negative**: -0.0848, -0.0948, -0.1117, -0.1642, -0.1654,
-0.1671, -0.2639, -0.2770, -0.2962. The question was never whether ORB clears a
bar that 1,141 prior tests raised. No parameter choice in the registered
neighborhood makes it profitable at all. Max drawdown on the registered cell:
**99.70%**.

Gate 4's interval sits entirely below zero, so this is not a "cannot distinguish"
result. Buying and holding SPY beat this rule by 44.5 percentage points a year,
and the paired difference says that gap is real.

### Finding 1: the arithmetic mean lied again, and in the direction that flatters

| | arithmetic | GEOMETRIC |
|---|---:|---:|
| full | -15.48% | **-29.38%** |
| train | -31.95% | **-36.92%** |
| holdout | **+26.28%** | **-12.90%** |

The holdout shows a **+$32,840 profit and a +26.28% arithmetic annual return, and
still compounds to -12.90% a year.** A reader given only the net P&L and the
arithmetic mean would conclude the holdout worked. It did not. This is the second
consecutive intraday verdict where the arithmetic figure pointed the opposite way
from the geometric one (H124b: -0.5% arithmetic, -38.0% geometric). The standing
rule from H124b's autopsy holds and is now reinforced: **the geometric figure is
the headline, always, and the arithmetic figure is not reported without it.**

### Finding 2: the regime story was pre-empted on purpose

Reported, and registered in advance as NOT gated:

| period | n | net | sharpe | geometric |
|---|---:|---:|---:|---:|
| 2010-2012 | 642 | -$22,218 | -1.45 | -31.47% |
| 2013-2015 | 739 | -$46,355 | -2.40 | -48.70% |
| 2016-2019 | 997 | -$25,115 | -0.69 | -27.36% |
| 2020-2021 | 498 | -$7,295 | -0.20 | -33.49% |
| **2022-2023** | **498** | **+$41,137** | **+0.89** | **+50.64%** |
| 2024-2026 | 675 | -$7,697 | -0.13 | -40.87% |

One window out of six is strongly positive. Without the pre-registration this is
exactly where the story "ORB works in high-volatility regimes, we just need a vol
filter" gets written, and it would have been indistinguishable from an honest
finding. It was fenced off before the data arrived, so it is a diagnostic and not
a result. **2022-2023 does not reopen this hypothesis.** One positive window in
six, chosen after the fact from six tries, is what noise looks like.

### What this cost, and what it bought

$31.91 against the $500 ceiling (first paid research; the $50 cap applied and was
respected). It did not buy a strategy. It bought the elimination of an excuse: the
firm can no longer say "not demonstrated on a short sample" about ORB on ES. On
16 years and 4,049 sessions, with costs the rule's own promoters would call
generous, it loses money in five of six regimes and loses to SPY decisively. That
is a verdict, which is what the money was for.

It also bought a reusable asset: 16.07 years of audited front-month ES minute bars
and a 2010-2026 NYSE session calendar validated against the ICE release. Every
future intraday hypothesis runs on this, at no further cost.

### Upper-bound caveat, stated in advance and still binding

Minute bars cannot resolve within-bar path, so stop fills are flattered. Every
number here is an UPPER bound on the achievable result; the true figures are
worse, not better. Tick data was priced at the same time and is outside the
budget ($77.48 for one year of `mbp-1`, $144.65 for one year of `trades`). This
caveat cannot rescue the verdict - it only deepens it.

### Kill

H133 -> graveyard. H124b stays buried. Per §3 rule 5 and the kill rule registered
in advance: no goalpost moves, no re-cut of the window, no second neighborhood, no
vol filter, no "but 2022-2023". **ORB on ES is closed.** Reopening it requires a
new mechanism argument that survives §1, not a new parameter.

## H133. Equity 45d XS reversal monthly rebal medium book - NOT CONFIRMED (2026-09-20)

```
TRAIN  (first 65%)  ret  -2.5%  sharpe -0.30  maxDD 24.7%
HOLDOUT (last 35%)  ret  -2.1%  sharpe -0.17  maxDD 18.4%
FULL                ret  -2.3%  sharpe -0.24  vol  8.3%
Neighborhood best cell +0.03  vs  noise ceiling 0.92  (N=1141 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.30, holdout sh -0.17 vs bar 0.3). No edge after 10bps costs.

## H134. Equity 20d vol-scaled momentum 1d skip weekly rebal - NOT CONFIRMED (2026-09-20)

```
TRAIN  (first 65%)  ret  -5.2%  sharpe -0.70  maxDD 44.5%
HOLDOUT (last 35%)  ret  -6.7%  sharpe -0.70  maxDD 33.5%
FULL                ret  -5.8%  sharpe -0.70  vol  8.1%
Neighborhood best cell -0.45  vs  noise ceiling 0.92  (N=1150 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.70, holdout sh -0.70 vs bar 0.3). No edge after 10bps costs.

## H135. Crypto 60d XS momentum 5d skip weekly rebal tight book - NOT CONFIRMED (2026-09-20)

```
TRAIN  (first 65%)  ret -10.2%  sharpe -0.27  maxDD 79.7%
HOLDOUT (last 35%)  ret  +7.6%  sharpe +0.38  maxDD 31.0%
FULL                ret  -4.3%  sharpe -0.00  vol 29.4%
Neighborhood best cell +0.31  vs  noise ceiling 0.91  (N=1159 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.27, holdout sh 0.38 vs bar 0.4). No edge after 10bps costs.

### H133 addendum (2026-09-21): independent implementation cross-check via Astral

Not a re-test and not a second shot at the verdict, which is filed. The question
was narrower and worth asking after Amendment A1: **is my backtester producing
these losses through a bug?** Astral is a separate platform with its own engine,
its own data vendor and its own expression language, so it can answer that.

What Astral could NOT do, established before running anything:
- **No futures.** The platform itself suggests SPY as the proxy. So: SPY, not ES.
- **Long-only** (`allow_shorts: false`). The short side of ORB is inexpressible.
- **40,000-bar cap at 1-minute resolution.** It requested 276,515 bars for the
  window asked for and returned `history_capped: true`, collapsing to
  2026-04-29 .. 2026-09-17 = **98 sessions**. Not 16 years, not even H124b's 1.95.
- **Fills on the signal bar's CLOSE** (`fill_price_mode: on_close`), where orb.py
  enters at the NEXT bar's open. This is the *more favourable* model of the two.

Same 98 sessions, long side only, both engines:

| | Astral (SPY, own engine, on_close fills) | mine (ES, long only, next-bar-open fills) |
|---|---:|---:|
| sessions | 98 | 98 |
| trades | 63 | 51 |
| win rate | 38.1% | 41.2% |
| expectancy / trade | -$64.49 | -$136.57 |
| Sharpe | **-2.45** | **-1.61** |
| profit factor | 0.61 | - |

**Agreement on sign, on win rate, and on order of magnitude of Sharpe.** The trade
counts differ (63 vs 51) for an identifiable reason: Astral's rule fires on any bar
in the window and `accumulate: false` only blocks adding while a position is open,
so it can re-enter the same session after a stop-out. orb.py takes one trade per
day by construction. Dollar expectancy is not comparable across a share-based SPY
position and a $50/point ES contract; the sign and the win rate are.

The informative detail: **Astral's more generous fill model produced the WORSE
Sharpe** (-2.45 vs -1.61). If my next-bar-open entry were manufacturing the losses,
the relationship would run the other way. It does not.

What this establishes: two independent implementations, on different data for
different instruments, agree that the long side of this rule loses at roughly a 40%
win rate. The H133 verdict is not an artifact of my code.

What it does NOT establish: anything about 16 years. 98 sessions of a proxy
instrument, one side only. It corroborates the implementation, not the statistics.

**Separate finding worth acting on.** The 40,000-bar cap is per bar-size, so at
`1d` it is ~158 years of daily bars. Astral can therefore replicate the firm's
DAILY strategies over their full history. That is the cross-check Amendment A1
actually calls for -- an independent check on `engine.py` itself -- and it is now
known to be available at no additional data cost. Logged as the next candidate,
not run here.

Astral strategy id 30884, backtest `bt_9cbb89d02ecf63d9`. No orders, no deployment,
no money; backtests only.

### H133 correction (2026-09-21): survivorship-of-days in gate 4. Verdict stands.

Found while calibrating the firm's engine against Astral. Not a re-litigation --
the corrected verdict is the same -- but a real defect in my own filed result,
recorded because rule 5 cuts both ways: the verdict does not move, and neither
does the error get quietly dropped.

**Engine calibration (the reason this was found).** Plain SPY buy-and-hold,
2010-06-07..2026-09-18, firm `engine.py` vs Astral's commercial engine:

| | firm | Astral | gap |
|---|---:|---:|---:|
| annualized (geometric) | +12.74% | +12.68% | 0.06pp |
| annualized vol | 17.03% | 17.01% | 0.02pp |
| Sharpe | +0.790 | +0.787 | 0.003 |
| max drawdown | 34.10% | 34.10% | ~0 |

Agreement to three decimals. The residual return gap (+602.7% vs +596.4% total)
is Astral's 5-bar warmup starting it a week later. **`engine.py` is calibrated on
the benchmark path.** The 0-of-117 graveyard result is not an engine artifact.

**But that number should have been +15.59%,** which is what H133 gate 4 reported.
Chasing the 2.85pp gap found the defect.

`benchmark.compare()` inner-joins, so the STRATEGY's exclusion rules delete days
from the BENCHMARK. ORB excludes sessions with missing minutes -- which is exactly
what a market-wide circuit-breaker halt produces. The 50 sessions it excluded
compounded to **-31.44%** for SPY:

| dropped session | SPY | why ORB excluded it |
|---|---:|---|
| 2020-03-16 | -10.94% | circuit-breaker halt -> missing minutes |
| 2020-03-12 | -9.57% | circuit-breaker halt |
| 2020-03-09 | -7.81% | circuit-breaker halt |
| 2020-03-18 | -5.06% | circuit-breaker halt |
| 2018-12-24 | -2.64% | scheduled early close |

Mean daily return on dropped days **-0.7202%**, on kept days **+0.0629%**. The
strategy's own definition of a tradeable session had silently deleted the
benchmark's five worst days.

**Corrected gate 4.** On a day the rules forbid trading, the strategy is FLAT and
earns zero -- so it is reindexed onto the benchmark's calendar with 0, not dropped:

| | ann strategy | ann benchmark | ann diff | diff-sharpe | verdict |
|---|---:|---:|---:|---:|---|
| as filed (inner join) | -28.94% | +15.59% | -44.54% | -0.501 | LOSES TO |
| **corrected (flat-filled)** | **-28.65%** | **+12.74%** | **-41.39%** | **-0.462** | **LOSES TO** |

**Gate 4 still fails. H133 stays NOT CONFIRMED and stays in the graveyard.** Here
the bias ran against the strategy, so correcting it helped ORB and changed nothing.
That is luck, not soundness: the same mechanism flatters the STRATEGY whenever the
days it skips are bad ones, and it was invisible in the output either way.

**Fix, in `benchmark.py::compare()`.** `benchmark_bars_dropped` is now always
reported; dropping more than 1% of the benchmark's bars inside the window raises a
RuntimeWarning; `fill_flat=True` reindexes a flat strategy onto the benchmark's
calendar. Two regression tests added in `test_benchmark.py::DaySurvivorshipTests`
using a 60-session fixture with one -20% halt day. Suite: **44 pass** (was 42).

**Blast radius, measured not assumed.** All nine near-misses in the graveyard
review are crypto, where the strategy has MORE bars than the benchmark, so the join
trims the strategy -- the opposite direction. Verified directly on H63, the closest
of them: **`benchmark_bars_dropped` = 0**, `n_overlap` 2,884, diff-sharpe +0.542,
which reproduces the logged +0.542 exactly and so also cross-validates
`graveyard_review.py`. **The graveyard review's 117 verdicts are unaffected.**

Separate limitation, disclosed not fixed: a crypto-vs-SPY comparison trims crypto's
4,188 bars to SPY's 2,884 weekdays, so crypto weekend P&L is invisible to the
paired test. Direction of that bias is unknown and it is not this bug.

Astral strategy 30889, backtest `bt_0f38a35443085e14`. Benchmarks only. No search
was run and N is unchanged, because a benchmark and a replication are not
hypotheses.

## H136. Mechanism-diversified portfolio of trend + carry sleeves - NOT CONFIRMED (2026-09-21)

Registered PRE-RESULT with the sleeve rule fixed on mechanism grounds, the
contamination disclosed, and all four gates set before the portfolio was run.

**Why it was worth running.** The firm had spent 1,141 cells hunting for ONE
strategy that beats SPY. That is not how the industry reaches Sharpe > 1. The
identity is `combined = s*sqrt(N)/sqrt(1 + (N-1)*rho)` -- many weak, weakly
correlated sleeves. Measured here, the firm's mechanism-level **rho is +0.037**
(holdout +0.106), which is near-independence and the genuinely scarce ingredient.
The firm's gate had never asked whether a cell ADDS to a book, only whether it
BEATS SPY alone, so a +0.3 sleeve with rho 0.05 was discarded by construction.

### Gates - all four failed

| gate | requirement | result | |
|---|---|---|---|
| 1 | holdout Sharpe>0.5 and net>0 | Sharpe **+0.037**, net +0.0159 | FAIL |
| 2 | holdout CI excludes zero | [-0.856, +0.966] | FAIL |
| 3 | beats firm ceiling N=1,141 over 4.03y = 1.869 | +0.037 | FAIL |
| 4 | BEATS spy_buyhold (fill_flat=True) | **LOSES TO**, -0.04%/yr vs +8.91%/yr, 0 bars dropped | FAIL |

Equal weight: train **+0.349** -> holdout **+0.037**.

### The finding: sleeve Sharpes do not persist

| sleeve | train | holdout |
|---|---:|---:|
| ts_momentum.equ | +0.496 | +0.123 |
| ts_momentum.cry | **+0.524** | **-0.269** |
| funding_carry.cry | **+0.599** | **-0.222** |
| mom_volscaled.cry | -0.286 | -0.325 |
| xsec_momentum.cry | +0.126 | **+0.442** |
| xsec_momentum.equ | -0.039 | +0.285 |
| mom_volscaled.equ | +0.018 | +0.298 |
| funding_ts.cry | **-0.457** | **+0.159** |

Signs flip nearly at random. **Train Sharpe carries no information about holdout
Sharpe here.** So there is no persistently positive component to aggregate. The
diversification machinery worked exactly as the formula predicts -- rho stayed at
+0.106, nothing was lost to correlation -- and multiplied an edge of zero.

This is the cleanest statement of the firm's real problem yet. It is NOT tooling,
NOT budget, NOT the noise ceiling, and NOT the engine (calibrated 2026-09-21
against Astral to three decimals). It is that momentum, reversal, low-vol and
carry on megacap equity and top-50 crypto do not carry an edge that survives out
of sample, because those are the most competed signals on the most competed
markets in existence.

### What the firm's own record says instead

**H27, EdgeBot sports-model CLV edge -- CONFIRMED 2026-09-20. mean CLV +2.44,
t-stat +6.71, 63% beat-close, same sign in both halves, n=399.**

One test, on a small capacity-constrained proprietary book, produced t = 6.71.
1,141 cells on equity and crypto produced a holdout Sharpe of +0.037.

That is the comparison this verdict exists to record. Constitution §1's edge
thesis is **small markets**, and it was right. The 1,141 cells were spent
violating it.

CORRECTION (2026-09-21, same day): an earlier draft of this paragraph said the
user "told me to stop looking at sports." That is a paraphrase and it is wrong.
His actual words were: *"were not trying to trade the sports markets i already
have projects for that we want to trade the main financial markets, (stocks,
options, futures,etc.)"* — that is SCOPING, not dismissal. He said sports was
already covered by another project of his (EdgeBot, which predates this work) and
asked that THIS effort be aimed at the markets that were not covered. Given that
he had just been shown a firm composed of 54 crypto / 45 equity / 1 sports
hypotheses, that instruction was the reasonable read of the evidence in front of
him.

So the §1 drift is not attributable to the user. The 1,141 cells in equity and
crypto were generated by the AUTO-PIPELINE, nine at a time, unprompted. The
thing whose behaviour contradicts §1 is the generator, not the operator. That
distinction matters for what gets fixed: the fix is in `generator.py`/`ideas.py`
and the universes they are allowed to propose, not in anyone's judgement.

Honest caveats on H27, because CLV is not profit: the book is **-304, ROI -2%**
over those 399 bets. Positive CLV with negative realised P&L is consistent at
n=399 -- CLV converges faster than P&L -- but it is not proof of profit. The
CLV-predictive split is the right signature though: beat-close 251 bets at 49%
win for +318, missed-close 148 bets at 49% win for -622. Identical hit rate,
opposite P&L, so the effect lives in the PRICE obtained, not in picking winners,
which is what a genuine line-value edge looks like. Capacity is tiny by
construction. That is the trade: a real edge that does not scale.

### Kill

H136 -> graveyard. No re-weighting, no risk parity, no dropping the worst sleeve.
The leave-one-out table was reported precisely so that dropping one afterwards is
visibly a goalpost move.

### Two defects to fix separately

1. `xsec_reversal.equ` returned full-sample Sharpe **-3.780**, which is
   implausible and reads as a bug, not a signal.
2. `mom_volscaled.equ` and `xsec_momentum.equ` correlate at **+0.967** -- near
   duplicates counted as two independent cells against the firm's own ceiling.
3. The auto-pipeline registered **12 hypotheses twice under the same name** (14
   redundant headers), and collided with hand-registered H124 and H133 because it
   takes the next integer without checking. Ceiling impact is negligible (log
   growth: N=1,141 vs 1,015 moves the bar 0.930 -> 0.928), but it wastes compute
   and makes the record un-auditable.

## H141. Crypto trend family vs a point-in-time universe — **FAIL** (2026-09-21)

<!-- Back-filled to this ledger 2026-09-21. Transcribed from
     graveyard/crypto/H141-VERDICT.md, which is the run's record of
     record. Constitution S2: the autopsy is filed here, win or lose. -->

Registered 2026-09-21 before the data existed (`graveyard/crypto/H141-SURVIVORSHIP-SPEC.md`,
now also in HYPOTHESES.md). Run 2026-09-21 on 733 of 734 USDT symbols ever listed
on Binance spot. Cost: $0.

> **Registered FAIL condition:** point estimate below +0.20, **or** annualised
> excess below +8%.
> **Result: −0.352 and −19.38%. Both tripped.**

### One engine, one window, one rule. Only the universe changed.

| | hindsight 30 | **point-in-time** |
|---|---:|---:|
| Annualised return | +22.07% | **−7.50%** |
| Sharpe | +0.661 | **+0.120** |
| Max drawdown | 63.2% | 81.1% |
| Growth of $1 | **5.48×** | **0.51×** |
| Rebalances | 223 | 223 |
| Median names held | 6 | 9 |
| Turnover | 30.6 | 59.1 |

**18% of the Sharpe survives.** A strategy that turned $1 into $5.48 turns it into
51 cents once the universe is chosen causally instead of in hindsight.

Against SPY on a paired difference, `benchmark.compare(fill_flat=True)`, 2000 bootstraps:

| arm | diff-sharpe | 95% CI | ann diff | verdict |
|---|---:|---|---:|---|
| hindsight 30 | −0.040 | [−0.520, +0.460] | −5.13% | TIES |
| **point-in-time** | **−0.352** | [−0.826, +0.112] | **−19.38%** | TIES |

### Why: the universe was a selection, not a sample

| Binance archive census, 2026-09-21 | |
|---|---|
| USDT symbols with daily history | 734 |
| Still trading | 491 |
| **Delisted / stopped** | **243 (33.1%)** |
| Died after ≥12 months of trading | 214 |
| Deaths in 2024 / 2025 / 2026 | 46 / 51 / 40 |
| Firm universe present in the archive | 27 |
| **Of the firm's 27, delisted** | **0** |

Zero deaths in a 27-name list drawn from a population where a third died. The
point-in-time universe holds BUSD for years and PEPE in 2024 — names a 2026 author
would never think to write down.

### What this does and does not establish

**Does:** within one engine, one window and one trend rule, hindsight universe
selection accounts for essentially the entire result.

**Does not:** this is NOT a reproduction of H63. H63 ran 2015-01→2026-07 on Yahoo
data with a fixed 30-name list; this runs 2018-02→2026-08 on Binance with a
top-20-by-volume rule. The hindsight arm is a **control isolating the universe
effect**, not a replication. Declared before the run, when the archive's 2017 start
date was discovered.

Three caveats, all pointing the same way — they make the FAIL *more* credible:

- **Delisting treatment is generous.** Dead holdings marked out at last print; real
  delistings are worse, so the point-in-time result is optimistic.
- **The benchmark understates SPY.** `benchmark_bars.csv` `adj_close` is price-only
  (8.93% CAGR over 19.9y). Both arms are measured against a weakened SPY and still lose.
- **Binance is one venue**, and its own listing decisions are a selection of a
  different kind.

### Consequence, per the registered spec

The crypto time-series trend family is **buried**. The nine near-misses in
`GRAVEYARD-REVIEW.md` — H63, H98, H120, H105, H34, H29, H68 — are annotated
**explained-by-survivorship**, not unresolved. H63's lower bound of −0.018 was not a
near miss on a real edge; it was a near miss on an artefact.

Forbidden from here: re-tuning the lookback, the rebalance period, the top-N, or the
venue. No second holdout.

**Strategy trials consumed: 1.**

### Two bugs found and fixed before the run counted

Both caught because the first execution crashed rather than producing a
plausible-looking number, which is the good failure mode:

1. `HINDSIGHT` held base names (`BTC`) but the price map is keyed by full symbol
   (`BTCUSDT`), so the hindsight arm matched nothing and held **zero** positions for
   the entire run — reporting `median_held: 0` instead of erroring.
2. `eligible()` requires 20 active days in the last 30, so a symbol can qualify on a
   date it did not itself print; `px[s][d]` then raised `KeyError`.

The smoke test beforehand exercised the universe machinery and **not the trading
loop**, which is why it passed both. Noted for next time.

Artefacts: `graveyard/crypto/h141.py`, `census.py`, `census.json`, `h141_results.json`,
`h141_point_in_time_daily.csv`, `h141_hindsight_30_daily.csv`.

## H142. SPX open-interest walls as intraday reference levels on ES — **FAIL** (2026-09-21)

<!-- Full verdict: graveyard/gamma/H142-VERDICT.md. Summary filed here per
     Constitution S2: the autopsy lives in this ledger, win or lose. -->

Registered before any options data was purchased. Run the same day. Data cost
**$29.36** against a $30.35 quote; 13/13 definition and 13/13 statistics months,
receipt in `graveyard/gamma/data/RECEIPT.json`.

> **Registered gate, BOTH required:** p < 0.05 two-sided against the permutation
> distribution AND median reaction ≥ 0.55 ES points. **Result: p = 1.0000.**

| | |
|---|---:|
| Sessions analysed | 233 |
| Levels offered | 466 |
| **Levels ever touched** | **2 (0.4%)** |
| Permutation mean / sd | 17.872 / 0.097 |
| **Two-sided p** | **1.0000** |

**p = 1.0000 means nothing was measured, not that no effect exists.** Two touches
out of 466 leaves the test with no power, and the permutation arm is equally
degenerate. Recorded this way deliberately: the weaker claim is the true one.

### Instrument audit first, per House Rule 2

The same `react()` pointed at a control level it must find — the prior session's
15:59 close:

| level | touched | median reaction |
|---|---:|---:|
| **control: prior 15:59 close** | **132/233 = 56.7%** | **9.75 ES pts** |
| call wall | 2/233 = 0.9% | — |
| put wall | 0/233 = 0.0% | — |

The machinery works. The walls sit a median of **626 (call) and 747 (put) ES
points outside the session's own high–low range**, against a median session range
of 60.2 points — roughly **ten daily ranges away**. Unreachable, not merely
untouched.

### Why

The registered rule picked one of four strikes on all 233 sessions: calls
7000/6000/5000/8800, puts 6000/7000/5000. Round-thousand strikes carry ~8× the
open interest of strikes near spot (2026-03-26, ES 6642: 7000C=162,850 and
6000P=167,676 against 6800C=18,916 and 6600P=24,414). The largest-OI strike is a
legacy round number, every session. The level definition is degenerate on this
chain.

### Consequence

Open-interest walls are **buried**; **no further options data is purchased for
this line.** Forbidden as registered: changing the 30-day window, using the 2nd
or 3rd largest strike, switching the horizon, scoring call walls alone, dropping
untouched sessions. The spec blocked every repair in advance, including the
obvious one — taking the largest-OI strike *near spot*.

**Recorded, not a rescue:** the purchase contains only the SPX **monthly** chain
(`asset = SPX`, expiries Fridays/Thursdays only). SPXW weeklies are absent.
Whether SPXW open interest behaves differently is a different question on data
this project does not own — a new hypothesis, a new number and a new purchase
needing Peter's approval. H142's burial does not depend on it.

**Strategy trials consumed: 1.** Total spent on this line: $29.36.

## H143. Index-level overnight drift on ES — **NOT CONFIRMED** (2026-09-21)

Full verdict: `graveyard/overnight/H143-VERDICT.md`. Registered and committed
**before** the run (`24c3bc9`, 18:08:34 UTC). Data cost **$0** — the overnight
bars were always in the archives. 4,090 of 4,090 windows traded, no skips.

| gate | requirement | result | |
|---|---|---|---|
| 1 | net mean>0 AND Sharpe>0.5 BOTH halves | train **+0.081**, hold **+0.454** | FAIL |
| 2 | holdout 95% CI excludes zero | **[-0.385, +1.298]** | FAIL |
| 3 | holdout Sharpe > ceiling N=8 | **0.454** vs **0.854** | FAIL |
| 4 | BEATS spy_buyhold (total return) | **LOSES TO**, -9.84%/yr, dS -0.585 | FAIL |
| 5 | holdout t > 3.0 | **t = 1.08** | FAIL |

### Costs take half the effect

Gross Sharpe **+0.731**, mean +1.079 pts/trade. One round trip costs **0.550
pts** ($27.50). Net Sharpe **+0.203**, mean +0.529 pts. **51% of the gross edge
goes to a single round trip.** The paper screen argued the single-stock cost
objection would not transfer to one ES contract. It transferred.

### The loosened gate did not matter

Gate 3 used N=8 rather than the firm's 1,159 cumulative cells, argued on the
grounds that this idea came from a $0 literature screen and was not found inside
that search. Holdout Sharpe 0.454 **fails at N=8 (0.854) and at N=1,167
(1.575)**. The concession was granted and was not needed; this verdict does not
depend on how N is counted for externally sourced ideas.

### Contamination disclosure was accurate

The registration disclosed a derivable gross Sharpe of ~0.74. Measured **0.731**.
The gate was set on the five unknowns and all five failed. The better-looking
`gap=1` subset was declined in advance and would not have saved it (0.445).

### Forbidden, flagged before anyone tries it

Era 2024-2027 nets +2.963 pts at Sharpe **+1.205** on 681 windows and clears
every Sharpe gate alone. **That is not a result** — it is a subset chosen by
reading a table, and the registered split already placed those windows inside a
holdout that failed. The published decay-since-2012 story also runs backwards
here (early eras negative, recent positive), further reason to read the
single-era number as noise.

Risk, not gated: win rate 52.5%, skew -0.70, worst window **-217.30 pts
(-$10,865)** on one contract.

**Strategy trials consumed: 1.** Overnight drift on ES is buried.

## H146. Equity 30d XS reversal bi-weekly rebal medium book - NOT CONFIRMED (2026-09-21)  [RENUMBERED 2026-09-22 from H136: duplicate label collision with hand-registered entry; content, params, gates, date and verdict unchanged]

```
TRAIN  (first 65%)  ret  -3.3%  sharpe -0.31  maxDD 32.3%
HOLDOUT (last 35%)  ret  -3.4%  sharpe -0.26  maxDD 29.3%
FULL                ret  -3.3%  sharpe -0.29  vol 10.0%
Neighborhood best cell +0.03  vs  noise ceiling 0.92  (N=1168 cells, 17y)
Gate: ann>0 & sharpe>0.3 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.31, holdout sh -0.26 vs bar 0.3). No edge after 10bps costs.

## H147. Crypto 6m TS trend 10-day rebal - NOT CONFIRMED (2026-09-21)  [RENUMBERED 2026-09-22 from H137: duplicate label collision with hand-registered entry; content, params, gates, date and verdict unchanged]

```
TRAIN  (first 65%)  ret +48.3%  sharpe +0.94  maxDD 90.6%
HOLDOUT (last 35%)  ret -20.8%  sharpe -0.43  maxDD 82.6%
FULL                ret +19.1%  sharpe +0.59  vol 55.8%
Neighborhood best cell +0.78  vs  noise ceiling 0.91  (N=1177 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the holdout half (train sh 0.94, holdout sh -0.43 vs bar 0.4). No edge after 10bps costs.

## H148. Crypto annual XS momentum 1M skip monthly rebal 6-side - NOT CONFIRMED (2026-09-21)  [RENUMBERED 2026-09-22 from H138: duplicate label collision with hand-registered entry; content, params, gates, date and verdict unchanged]

```
TRAIN  (first 65%)  ret  -4.2%  sharpe -0.11  maxDD 59.9%
HOLDOUT (last 35%)  ret  -2.8%  sharpe +0.01  maxDD 54.1%
FULL                ret  -3.7%  sharpe -0.06  vol 22.0%
Neighborhood best cell +0.12  vs  noise ceiling 0.91  (N=1186 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh -0.11, holdout sh 0.01 vs bar 0.4). No edge after 10bps costs.

## H149. Crypto 60d XS reversal monthly rebal ultra-tight 5-side - NOT CONFIRMED (2026-09-21)  [RENUMBERED 2026-09-22 from H139: duplicate label collision with hand-registered entry; content, params, gates, date and verdict unchanged]

```
TRAIN  (first 65%)  ret  +0.7%  sharpe +0.19  maxDD 70.0%
HOLDOUT (last 35%)  ret  -0.1%  sharpe +0.23  maxDD 67.0%
FULL                ret  +0.4%  sharpe +0.20  vol 37.4%
Neighborhood best cell +0.20  vs  noise ceiling 0.91  (N=1195 cells, 17y)
Gate: ann>0 & sharpe>0.4 both halves AND best>ceiling -> FAIL
```

Autopsy: NOT CONFIRMED - fails the pre-set gate in the train half (train sh 0.19, holdout sh 0.23 vs bar 0.4). No edge after 10bps costs.

## H144. ES opening-range break-of-structure retest — **NOT CONFIRMED** (2026-09-22)

Registered PRE-RESULT and PRE-CODE in commit 33f5adc, before `orb_struct.py`
existed. Spec `graveyard/orbstruct/H144-H145-SPEC.md`, sha256
99bdc39c287fe9dcd246e8ba12c4df5f61ddff871796dccfd470df325daf0058. All five
gates, both 9-cell neighborhoods, the $27.50 cost model, the 200-trade power
floor and the kill rule were fixed in that commit. **Cost to run: $0** — it
reuses the ES minute bars H133-ES already paid for.

**Sample.** Identical to H133-ES by construction: 1,608,271 front-month ES RTH
minute bars, 4,049 eligible sessions, **16.07 years**. The opening range is held
at 09:30–09:59 exactly as H133-ES registered it, so the range is a CONTROL and
the entry trigger and stop are the only things that vary.

### Instrument audit — passed before the verdict was read

| check | H133-ES | H144 | |
|---|---:|---:|---|
| sessions evaluated | 4,049 | 4,049 | same |
| sessions with a break | 3,882 | 3,882 | **exact match** |

The spec required the break count to match or the run is void. It matches to the
session. The code fires where it should.

| H144 stage | sessions |
|---|---:|
| no break | 167 |
| break, never retested | 456 |
| retested, never confirmed | 1,318 |
| **confirmed and traded** | **2,108** |

2,108 taken trades clears the 200 power floor by 10x. Exits: 1,635 stop, 473
time.

### Gates — ALL FOUR FAILED

| gate | requirement | result | |
|---|---|---|---|
| 1 | net>0 AND sharpe>0.5 in BOTH halves | train −$54,212.50 / −1.157; holdout **+$18,055.00 / +0.287** | **FAIL** |
| 2 | holdout 95% block-bootstrap CI excludes zero | +0.287 [−0.495, +1.002], P(>0.5)=28.6%, STRADDLES | **FAIL** |
| 3 | best of 9 cells > 0.5230 (N=9 over 16.07y) | best cell (rt30_brk660) = **−0.2259** | **FAIL** |
| 4 | BEATS spy_buyhold, paired difference | **LOSES TO**: −12.35%/yr vs +15.59%/yr, diff-sharpe −0.704 [−1.227, −0.268] | **FAIL** |
| 5 | $40 stress does not sink gates 1–2 | n/a, 1 and 2 already failed. For the record: train −$71,150 / −1.516; holdout +$8,642.50 / +0.137 | - |

Gate 4 was also run with `fill_flat=True`, the corrected benchmark treatment
H133-ES established, which is the treatment that FAVOURS the strategy: still
**LOSES TO**, −10.12%/yr vs +8.91%/yr, diff-sharpe −0.517 [−0.969, −0.094],
n=5,002. The interval sits entirely below zero under both treatments, so this is
not a "cannot distinguish" result.

All nine neighborhood cells are negative: −0.2259, −0.2964, −0.2984, −0.3433,
−0.3987, −0.3999, −0.4003, −0.4162, −0.4172.

### Finding 1: the stop was never the problem

This is what the hypothesis was for, and it answers the question cleanly.

| | H133-ES (range stop) | H144 (structure stop) |
|---|---:|---:|
| median risk per trade | 9.50 pts = **$475** | 3.50 pts = **$175** |
| net over 16.07y | −$67,542 | **−$36,158** |
| max drawdown | 99.70% | **92.92%** |
| **sharpe** | **−0.2770** | **−0.2984** |

The structure stop does exactly what it was argued to do: it risks **36.8%** of
what the range stop risked, and it cuts the dollar loss roughly in half. And the
Sharpe does not improve — it is marginally worse. Risking less money per trade
changes the magnitude of the loss and not its sign, because Sharpe is invariant
to position size. **Better risk control on a rule with no edge produces a
smaller loss, not a profit.** That is worth stating plainly because "tighten the
stop" is the single most common piece of advice attached to this strategy
family, and on 16 years of ES it moves nothing that matters.

### Finding 2: the recent window is positive, and that means nothing

The holdout is **positive** (+$18,055, sharpe +0.287) and so are the last two
regime windows:

| period | n | net | sharpe | geometric |
|---|---:|---:|---:|---:|
| 2010-2012 | 642 | −$14,228 | −1.933 | −20.55% |
| 2013-2015 | 739 | −$12,595 | −1.321 | −16.48% |
| 2016-2019 | 997 | −$20,510 | −1.169 | −19.96% |
| 2020-2021 | 498 | −$5,032 | −0.311 | −14.24% |
| **2022-2023** | **498** | **+$9,543** | **+0.394** | **+8.37%** |
| **2024-2026** | **675** | **+$6,665** | **+0.217** | **−0.10%** |

Without the pre-registration this is exactly where "the retest version works, it
just needed the modern regime" gets written. Gate 2 already answered it: the
holdout interval spans the bar with P(>0.5) = 28.6%. Two positive windows out of
six, selected after the fact, is what noise looks like. Note also that 2024-2026
is positive in dollars and **−0.10% geometric** — the arithmetic mean flatters
again, for the third hypothesis running.

**2022-2023 is now positive in H133-ES, H144 and H145.** That is one market
period, not three pieces of evidence, and it is not a finding about any of them.

### Kill

H144 → graveyard. Per the registered kill rule: no second neighborhood, no
regime filter, no re-cut window, no post-hoc target, no "but 2024-2026". The
break-of-structure retest on ES is closed.

---

## H145. ES failed-break fade — **NOT CONFIRMED** (2026-09-22)

Same commit, same spec, same sessions, same $0.

### Instrument audit

| H145 stage | sessions |
|---|---:|
| no break | 167 |
| broke, never came back inside | 819 |
| **failed and traded** | **3,063** |

3,063 taken trades, well clear of the power floor. Exits: the fade reaches its
target often, which is exactly the shape the spec predicted in advance.

### Gates — ALL FOUR FAILED

| gate | requirement | result | |
|---|---|---|---|
| 1 | net>0 AND sharpe>0.5 in BOTH halves | train −$58,237.50 / −1.563; holdout −$17,632.50 / −0.368 | **FAIL** |
| 2 | holdout CI excludes zero | −0.368 [−1.323, +0.480], P(>0.5)=2.4% | **FAIL** |
| 3 | best of 9 cells > 0.5230 | best cell (fw45_brk660) = **−0.6402** | **FAIL** |
| 4 | BEATS spy_buyhold | **LOSES TO**: −19.48%/yr vs +15.59%/yr, diff-sharpe −1.250 [−1.863, −0.706] | **FAIL** |
| 5 | $40 stress | n/a. For the record: train −$83,112.50 / −2.228; holdout −$31,045 / −0.648 | - |

With `fill_flat=True`: still **LOSES TO**, −16.08%/yr vs +8.91%/yr, diff-sharpe
−0.918 [−1.456, −0.422].

All nine cells negative and none of them close: −0.6402, −0.6634, −0.7717,
−0.7776, −0.7942, −0.8141, −0.8334, −0.8935, −0.9134.

### Finding: fading the failure is worse than taking the break

| rule | sharpe | net | max DD |
|---|---:|---:|---:|
| H133-ES — take every break | −0.2770 | −$67,542 | 99.70% |
| H144 — wait for the retest | −0.2984 | −$36,158 | 92.92% |
| **H145 — fade the failed break** | **−0.8141** | **−$75,870** | 97.22% |

H145 is the worst of the three by a wide margin, and it is worse than the rule
it was designed to exploit. The mechanism argued that a close back inside the
range is a completed liquidity sweep with the auction rejecting the level. On
16.07 years of ES that is not what it is. The registered expected failure mode —
"high win rate with a left tail that eats it" — was stated in advance and is
what the numbers show.

### Kill

H145 → graveyard. Same kill rule, same prohibitions.

---

## What H133-ES, H144 and H145 say together

Three different entry mechanisms, one opening range held constant as a control,
the same 4,049 sessions, the same 16.07 years, the same cost model:

| entry mechanism | trades | sharpe | net | vs SPY |
|---|---:|---:|---:|---|
| take the break (H133-ES) | 3,882 | −0.2770 | −$67,542 | LOSES TO |
| wait for retest + BOS (H144) | 2,108 | −0.2984 | −$36,158 | LOSES TO |
| fade the failed break (H145) | 3,063 | −0.8141 | −$75,870 | LOSES TO |

Twenty-seven neighborhood cells across the three (9 + 9 + 9). **Every one of the
twenty-seven is negative.** Not one cell in any direction, on any window, with
any stop, turns a profit before the gates are even applied.

The honest summary is not "opening-range breakout does not work on ES." It is
stronger than that: **the 09:30–09:59 opening range on ES carries no
directional information that any of continuation, confirmed continuation, or
reversion can extract.** The level is known to everyone and priced accordingly.
Three mechanisms is enough; a fourth entry rule on this same range is forbidden
without a mechanism argument that does not reduce to "enter somewhere else
relative to the same two numbers."

This also closes the loop with Zarattini, Barbon & Aziz (2024), reviewed
2026-09-21, whose own **unfiltered ORB returned +29% against SPY's +198%**.
Their result and this firm's three burials agree: the breakout is not where any
edge lives. Their claimed edge is entirely in cross-sectional SELECTION of
stocks in play, which is a different mechanism, is not testable within this
project's remaining budget (`PAPER-REVIEW-ORB-STOCKS-IN-PLAY.md`: $556 minimum
against $468 remaining), and must never be described as a test of ORB.

**N accounting:** cumulative cells 1195 → **1213** (+18). The cumulative bar
moves 0.910 → 0.940 at 16.07 years. The binding gate was the fresh N=9 ceiling
of 0.5230, and nothing came within 0.74 of it.

## EdgeBot hypotheses moved out (2026-09-22)

H27, H137, H138 and H139 are **EdgeBot** (sports betting), a separate
project. They lived in this file and shared its register, which is how
EdgeBot kept surfacing in Graveyard analysis. They now live in
`EDGEBOT-VERDICTS.md`, moved byte-identical (sha256-verified). They never
contributed to `cumulative_cells` -- only pipeline.py increments that --
so the Graveyard's noise ceiling is unchanged by this move.

## H150. Intraday mean reversion at reference levels on ES — **NOT CONFIRMED** (2026-09-24)

Registered PRE-RESULT and PRE-CODE in commit `7048d0e`; `levels.py` did not
exist at that commit. Spec sha256 `19ba6570...ddaa398`. **Cost to run: $0.**

**Sample.** 1,608,271 ES minute bars, 4,049 orb-eligible sessions, of which
**3,943 = 15.65 years** survive H150's two extra exclusions: 42 with an
ineligible prior session, **64 dropped at a contract roll** (registered in the
spec; a cross-session level taken over a roll sits on a different price scale on
a back-adjusted series, and would have been silent corruption).

### Instrument audit — passed before the verdict was read

| level | touched | taken | median risk |
|---|---:|---:|---:|
| `pdh` prior high | 38.4% | 1,493 | 4.25 pts |
| `pdl` prior low | 33.2% | 1,291 | 5.12 pts |
| `orh` OR high | 74.4% | 2,877 | 4.38 pts |
| `orl` OR low | 68.9% | 2,674 | 4.50 pts |
| `pdc` prior close *(CONTAMINATED)* | 52.5% | 2,027 | 4.50 pts |

Both registered VOID conditions cleared: every H133-ES break touched its own
boundary (**0 violations**), and `pdc` on H142's own window reproduced its touch
rate at **58.2% (142/244) against 56.7%**, inside the 5-point tolerance. All
five levels clear the 200-trade power floor by 6x or more.

### Gates — ALL FOUR SUBSTANTIVE GATES FAILED, EVERY LEVEL

| level | G1 halves | G2 holdout CI | G3 ceiling | G4 vs SPY | sharpe | net |
|---|---|---|---|---|---:|---:|
| `pdh` | FAIL | FAIL | FAIL | FAIL | −1.1345 | −$53,808 |
| `pdl` | FAIL | FAIL | FAIL | FAIL | −1.8244 | −$85,078 |
| `orh` | FAIL | FAIL | FAIL | FAIL | −1.1610 | −$115,699 |
| `orl` | FAIL | FAIL | FAIL | FAIL | −0.7054 | −$66,922 |
| `pdc` *(CONTAMINATED)* | FAIL | FAIL | FAIL | FAIL | −1.6991 | −$120,330 |

**All 36 cells are negative.** Best of the family is `orl_s1.0_t2.0` at
**−0.1645** against a registered N=36 ceiling of **0.6768** — short by 0.84.
Under `fill_flat=True`, the treatment that favours the strategy, every level
still **LOSES TO** `spy_buyhold` (`orl`: −0.234/yr vs +0.089/yr, diff-sharpe
−1.170 [−1.662, −0.744]).

Win rates cluster at 32–35% with roughly 2:1 planned reward:risk — the shape
that looks survivable and is not, once the stop rate is 63%.

### Finding: the reaction at these levels IS the random walk

Registered in advance as the expected failure mode, and it is what happened.

| level | observed median 30-min MFE | random-walk null | ratio |
|---|---:|---:|---:|
| `pdh` | 2.50 pts | 2.77 pts | **0.90x** |
| `pdl` | 3.50 pts | 3.36 pts | 1.04x |
| `orh` | 2.50 pts | 2.65 pts | **0.94x** |
| `orl` | 3.25 pts | 2.92 pts | 1.11x |
| `pdc` | 3.00 pts | 2.83 pts | 1.06x |

Null is driftless Brownian motion scaled to each session's own range:
`median = 0.6745*sigma*sqrt(30)`, `sigma` from `E[range] = sigma*sqrt(8n/pi)`.

Two of the five produce **less** excursion than noise. None produces meaningfully
more. This is the direct answer to the H142 control's apparently impressive
"9.75 points" — a level that does nothing at all still shows MFE, because MFE is
the maximum of a random walk, and these levels land on the null.

### Two defects in my own spec, recorded not repaired

Neither changes the verdict — gates 1–4 fail decisively on all 36 cells — but
both make gate 6's numbers untrustworthy, and the spec is not being edited after
the fact.

**Defect 1: gate 6 was registered TWO-SIDED.** It therefore reports PASS when
the observed result is significantly *worse* than the null, which is what
happened for `pdh` (p = 0.0498), `pdl` (p = 0.0100) and `pdc` (p = 0.0299) — all
three sit far BELOW their null means. A permutation gate should be one-sided in
the direction of the claim. As written, three "PASS" marks mean the opposite of
what a gate is for.

**Defect 2: the permutation pool used absolute prices across 16 years.** ES
traded roughly 1,000 to 6,000 over the sample, so a level drawn from a random
other session almost never falls inside today's range. **~566,000 of 788,600
session-permutations were dropped for an unreachable substitute — about 72%.**
The null is therefore built from a small, temporally clustered subsample, not
from the intended population. The right design substitutes the level's *offset*
from a session anchor, not its absolute price. That is a different spec.

So gate 6 is reported and **should be read as uninformative**, not as support in
either direction.

### Kill

All four gated levels -> graveyard. Per the registered kill rule: no level added
now, no touch-definition change, no second neighborhood, no regime filter, no
re-cut window, and no post-hoc candle-pattern filter to rescue them.

**And specifically forbidden, registered in advance:** this may NOT be read as
evidence that momentum works at these levels. Costs apply in both directions,
and continuation at the opening range is already buried three times over
(H133-ES, H144, H145). The mirror is a separate hypothesis with its own N.

`pdc` remains CONTAMINATED and is not a result.

**N accounting:** cumulative cells 1213 -> **1249** (+36). The cumulative bar
moves 0.940 -> **0.9547** at 15.65 years. The binding gate was the fresh N=36
ceiling of 0.6768, and nothing came within 0.84 of it.

**What is still untested:** whether a candle-pattern filter at a level adds
anything. It cannot be tested until it is written as arithmetic on OHLC, and it
cannot be tested on these four levels, which are now closed.

## H151. Characterization study at ES reference levels — **VOID** (2026-09-24)

Registered PRE-RESULT PRE-CODE in `44956c3`, spec sha256 `e1155dfa...585130`.
Run the same day. **Cost $0. No test statistic was computed.**

The spec's own validity gate fired on the first level:

> "If more than 10% of control levels fall outside the session range, the
> control is broken and this study is VOID — the same failure H150 hit, and it
> must not pass silently twice."

**Result: 51.7% of control levels fell outside the session range.** The run
exited at `pdh` before any permutation statistic was formed.

### Why the control failed

The matched control was `C_s = open_s + (L_s' - open_s')`: take another
session's offset-from-open and apply it here. That fixes H150's defect (which
substituted an absolute price across a 1,000-to-6,000 ES range) but only
halfway. **It preserves the offset's direction and magnitude in points, not in
units of the session's own scale.** ES session ranges vary from roughly 20 to
150 points; a 60-point offset that is comfortably inside a wild day is
unreachable on a quiet one. Half the draws were therefore untouchable, which is
the same degeneracy H142 died of and the same one H150's gate 6 suffered — in a
third costume.

### What this costs

**Zero cells.** No comparison was made, so no multiple-comparison cost was
incurred; cumulative stays at 1249. The gate did exactly its job: it caught a
broken instrument *before* a number existed to be talked into meaning something.

### Contamination disclosure

Before exiting, the run printed `pdh`'s REAL-arm descriptive statistics —
touch rate 0.3837, rejection rate 0.4924, extremum rate 0.0826, absolute move
2.50 pts, signed reversion -0.25 pts. **These were seen.** They are one arm of a
two-arm comparison and say nothing on their own about the answer, since no
control values were produced. The successor hypothesis records this and is not
treated as fully blind on `pdh`.

### Successor

H152, registered separately, with a **scale-invariant** control: the offset is
carried across sessions in units of the opening-range height `H`, a quantity
known at 10:00. Everything else — levels, touch definition, the five statistics,
the Bonferroni alpha, the effect-size floors, the outcome table, the kill
rules — is inherited from H151 unchanged.

## H152. Characterization, scale-invariant control — **VOID** (2026-09-24)

Registered in `ed70915`. Run the same day. **No test statistic was computed;
zero cells consumed.**

The registered 10% gate fired again: **52.9% of control levels fell outside the
session range** (H151: 51.7%).

**This VOID is my error, and the error is in the gate, not the control.** `pdh`
is touched on only 38.4% of sessions — being out of range is an intrinsic
property of a prior-day high, not a defect. A gate demanding the control be
almost always reachable forbids it from resembling the thing it controls for,
and makes S1 (touch rate) untestable by construction. At 52.9% the control is in
fact slightly MORE reachable than the real level.

The gate was written to catch H142, where the tested level sat ten daily ranges
away and the control did not. What matters there is **asymmetry between the
arms**, not the absolute rate. I encoded the symptom instead of the disease.

Successor: H153, identical in every respect except the gate, which becomes
`abs(control out-of-range - real out-of-range) <= 10pp`. **Registered as the
final attempt**: a fourth control would be iteration wearing a hypothesis label.

Blindness intact — no control statistic has been produced at any point in H151
or H152. `pdh`'s real arm has now been seen twice and is labelled partially
contaminated.

## H153. Characterization at ES reference levels — **NO STRUCTURE FOUND** (2026-09-24)

Registered PRE-RESULT PRE-CODE in `93dcf48`, spec sha256 `2d2af08c...33674`.
Third and final attempt. **Cost $0.** This answers the question H150 could not:
not "does this trade rule pay" but "is there any measurable relationship between
price and these levels at all."

The corrected gate — **asymmetry** between the arms rather than an absolute
reachability floor — passed on both prior-day levels and produced the first
control statistics this line of work has ever generated.

### `pdh` — prior session high. 1,513 touches. Out-of-range: real 53.4% vs control 52.9%, gap 0.5pp. OK

| statistic | real | control | diff | needed | p | |
|---|---:|---:|---:|---:|---:|---|
| S1 touch rate | 0.3837 | 0.3976 | −1.38pp | 5.00pp | 0.0547 | no |
| S2 rejection rate | 0.4924 | 0.4822 | +1.02pp | 5.00pp | 0.3781 | no |
| S3 extremum rate | 0.0826 | 0.0820 | +0.06pp | 5.00pp | 0.9204 | no |
| S4 absolute move | 2.50 pts | 2.75 pts | −0.25 pts | 0.55 pts | 0.0746 | no |
| S5 signed reversion | −0.25 pts | +0.04 pts | −0.29 pts | 0.55 pts | 0.0796 | no |

### `pdl` — prior session low. 1,308 touches. Out-of-range: real 61.1% vs control 61.8%, gap 0.6pp. OK

| statistic | real | control | diff | needed | p | |
|---|---:|---:|---:|---:|---:|---|
| S1 touch rate | 0.3317 | 0.3260 | +0.57pp | 5.00pp | 0.3035 | no |
| S2 rejection rate | 0.4251 | 0.4531 | −2.80pp | 5.00pp | 0.0498 | no |
| S3 extremum rate | 0.0604 | 0.0856 | −2.52pp | 5.00pp | 0.0050 | no |
| S4 absolute move | 3.50 pts | 3.13 pts | +0.37 pts | 0.55 pts | 0.0448 | no |
| S5 signed reversion | 0.00 pts | +0.23 pts | −0.23 pts | 0.55 pts | 0.3134 | no |

**Ten statistics, ten failures.** Not one clears the Bonferroni alpha of 0.0025,
and not one has an effect large enough to trade even if it had. The three that
look interesting at a naive 5% — `pdl` S2 (p=0.0498), S3 (p=0.0050), S4
(p=0.0448) — are exactly what 20 pre-registered tests produce by chance, and all
three miss the effect-size floor as well. The spec forbade calling these
"borderline" or "promising" in advance, and they are not.

**A prior-day high or low behaves like any price at the same distance from the
open, in the units the session itself provides.** Price is not more likely to
stop there, reverse there, or move differently after touching it.

### `orh` / `orl` — the question is not askable, and that is the finding

VOID on the gate: real out-of-range **0.0%** vs control **22.6%**, gap 22.6pp.

This is not a broken control. **The opening-range boundary is inside the session
range by definition** — the range is built from the session's own first 30
minutes, so price has already been there. No transplanted level can match a
reachability of exactly 100%, and no fair control exists.

Which means the headline number from H150 — `orh` touched on **74.4%** of
sessions, `orl` on 68.9% — is **a tautology, not evidence.** Those levels get
touched because they are made of the price that already happened. Any reasoning
that starts "but the opening range gets respected so often" is reading
arithmetic as a market fact.

Per the spec's registered hard stop, no fourth control is written. `orh` and
`orl` close as **not answerable by this method**.

### N accounting

H151 and H152 consumed **zero** cells — neither produced a test statistic.
H153 consumed **10**, not the registered 20: `orh` and `orl` voided before any
statistic was formed. Cumulative **1249 -> 1259**.

### What this closes, and what it does not

**Closes.** Prior-session high and low as intraday reference levels on ES, in
both directions: H150 killed them as a trade, H153 shows there was nothing there
to trade. Opening-range boundaries close as unanswerable. The kill rules stand —
no sixth statistic, no second control, no new level, no horizon change.

**Does not close.** Whether a candle-pattern filter at a level adds anything.
It remains unwritten as arithmetic and therefore untestable, and it can no
longer be tested on these four levels.

**Method note worth keeping.** Three validity gates were written today and two
were wrong — H151's caught a real defect, H152's encoded the symptom of H142's
failure (absolute unreachability) rather than the disease (asymmetry between the
arms). Calibrating an instrument before measuring is legitimate; doing it a
fourth time would have been iteration wearing a hypothesis label, which is why
the hard stop was registered in advance rather than decided afterwards.

## H154. Month-end rebalance flow on ES — **NOT CONFIRMED** (2026-09-24)

Registered PRE-RESULT PRE-CODE in `9c05d81`, spec sha256 `22b42586...4ea64b`.
**Cost $0.** First hypothesis in this project generated from a named mechanism
rather than a pattern search, and — stated plainly — **the best result in 154
hypotheses.** It still fails every gate.

**Sample.** 4,049 eligible sessions, 2010-06 to 2026-09, **196 calendar months,
193 trades** (2 flat months skipped, no contract-roll skips). The spec said 192
was the maximum; the true population is 193. Minor, recorded.

| | |
|---|---:|
| Trades | 193 (128 short, 65 long) |
| Win rate | 53.9% |
| Gross | **+$53,838** |
| Costs | −$5,308 |
| **Net** | **+$48,530** |
| Mean gross per trade | **+$278.95** |
| **Cost as a share of gross mean** | **10%** |

### Gates — ALL FOUR FAILED

| gate | result | |
|---|---|---|
| 1 | train Sharpe **+0.073**, holdout **+0.634** | **FAIL** (train) |
| 2 | holdout CI **[−0.470, +1.668]**, straddles zero | **FAIL** |
| 3 | best of 9 cells **+0.354** vs ceiling **0.520** | **FAIL** |
| 4 | vs SPY total return: **TIES**, dS −0.095 [−0.532, +0.304] | **FAIL** |
| 5 | $40 stress: train +0.044, holdout +0.622 | n/a, 1–2 already failed |

### Why this failure is not like the other 153

Three things are different, and none of them is a pass.

**1. Costs stopped being the story.** The round trip is **10% of the gross mean**,
against **51%** for H143's overnight window and a cost-dominated picture across
the whole intraday family. A one-month holding period amortises $27.50 in a way
a 30-minute holding period cannot. That is a structural property of the horizon,
not a property of this signal.

**2. It TIES the benchmark instead of losing to it.** Every prior ES hypothesis
returned **LOSES TO**. This one returns **TIES**: +4.34%/yr against SPY total
return's +10.95%/yr, difference not distinguishable from zero. First time.

**3. It came closest to the ceiling.** Best cell +0.354 against 0.520. Still
short by 0.166, but nothing in 1,259 prior cells got this close with a positive
sign.

### Why it still fails, and the failure is correct

The train half is **+0.073** — indistinguishable from zero — and the holdout is
**+0.634**. A strategy whose entire result lives in the back third of the sample
is the exact shape gate 1 exists to reject. The holdout CI spans **2.14 Sharpe
units**. At n=193 over 16.3 years the standard error on an annualised Sharpe is
**0.248**, which the spec registered in advance: this test could only ever detect
a large effect, and what is here is not large.

The registered expectation was "an old, widely published effect, so expect a
small gross edge mostly eaten by costs." Half right. The edge is small and
unstable, but the costs did **not** eat it. That is the part worth carrying
forward.

### Two defects in my own runner, recorded not repaired

**Defect 1: `k = 1` is not a trade.** With entry at the k-th-to-last session and
exit at the last, `k=1` makes entry day equal exit day: gross exactly zero, cost
$27.50, zero variance. Two of the nine registered cells returned Sharpe 0.0 and a
third returned −1.75e16, a numerical blow-up from dividing by ~0. **Three of nine
neighborhood cells carried no information.** The grid should have been
`k in {2,3,5}`. This makes gate 3 marginally *easier*, not harder, since dead
cells cannot become the maximum — but it inflates N without buying anything.

**Defect 2: gate 4 was annualised wrong.** `benchmark.compare` was called with
`periods=12` while `fill_flat=True` expands the series to 5,000 daily
observations. Recomputed at `periods=252`: verdict unchanged at **TIES**, but the
numbers move materially — dS from −0.021 to −0.095, CI from [−0.116, +0.066] to
[−0.532, +0.304], annualised strategy from +0.20% to **+4.34%** and benchmark
from +0.50% to **+10.95%**. The corrected figures are the ones quoted above.

Neither defect changes the verdict. Both are recorded rather than quietly fixed.

### Kill

H154 to the graveyard. Per the registered kill rules: no sign flip, no second
neighborhood, no extra `k` or `theta`, no switch to quarter-ends or another
index, no dropping 2020, no re-cut split, and **no sweep of the other trading
days of the month.**

**What may be carried forward is the horizon, not the signal.** The finding that
a one-month hold reduces cost drag from 51% to 10% is about holding periods and
applies to any future hypothesis. It is not evidence for month-end flow.

**N accounting:** 1259 -> **1268** (+9, three of them dead). Ceiling at 16.28
years: **0.9553**.

## H155. Pre-FOMC announcement drift on ES — **NOT CONFIRMED** (2026-09-24)

Registered PRE-RESULT PRE-CODE in `70a55f6`. Spec sha256 `91caf864...1fc9a8`,
dates sha256 `95d1e73e...e5a789`. **Cost $0.**

**The first hypothesis in this project to pass gate 3.** It fails the other
three, and the reasons it fails are more interesting than the pass.

**Sample.** 130 of 133 scheduled FOMC announcement days, 2010-06 to 2026-09. The
three missing are 2010-01-27, 2010-03-16 and 2010-04-28, all before the ES data
begins on 2010-06-08. **No skips** — no roll conflicts, no missing 13:45 bars.

| | |
|---|---:|
| Trades | 130 |
| Win rate | 53.8% |
| Mean | **+4.006 pts** |
| Median | +1.250 pts |
| Gross | +$26,038 |
| **Net** | **+$22,462** |
| Cost as share of gross mean | **14%** |

### Gates

| gate | result | |
|---|---|---|
| 1 | train **+0.364**, holdout **+0.563** | **FAIL** (train) |
| 2 | holdout CI **[−0.764, +1.814]** | **FAIL** |
| 3 | best cell **+0.7006** vs N=3 ceiling **0.3674** | **PASS** |
| 4 | vs SPY total return: **TIES**, dS −0.352 [−0.764, +0.057] | **FAIL** |
| 5 | $40 stress: train +0.308, holdout +0.543 | n/a |

Neighborhood: `d1 = +0.4308`, **`d2 = +0.7006`**, `d3 = +0.2960`.

### On the gate 3 pass — what it is and is not

The N=3 ceiling is **0.3674**, and 0.7006 clears it. That is a real pass under
the rule as registered.

**It does not clear the cumulative bar.** At 1,271 cumulative cells over 16.28
years the ceiling is **0.9370**, and 0.7006 is well short. The constitution gates
on fresh N and reports cumulative; both numbers are here so neither can be
quoted alone.

**And the passing cell is not the registered one.** The registered cell is
`d = 1`, at +0.4308. The cell that clears is `d = 2`. Gate 3 is defined on the
best of the neighborhood, so the pass stands as registered — but the honest
reading is that a two-day window looked better than the one-day window the
mechanism actually predicts, which is a point against the mechanism, not for it.

### My registered expectation was wrong, and in the more dangerous direction

The spec predicted decay: "the sample is almost entirely post-publication, so
expect a positive but small mean, a Sharpe well under 0.5, and a holdout weaker
than the train half."

| era | n | net | sharpe |
|---|---:|---:|---:|
| 2010-2013 | 29 | +$303 | **+0.058** |
| 2014-2017 | 32 | −$355 | **−0.082** |
| 2018-2021 | 31 | +$4,872 | +0.380 |
| **2022-2026** | **38** | **+$17,643** | **+0.768** |

The effect is not decaying. It is **strengthening**, and essentially all of the
money arrives after 2018. That is the opposite of what I registered.

**This makes the result more suspicious, not less.** Twelve flat years followed
by four strong ones is the exact shape of a regime artifact. A plausible story is
available — 2022-2026 is a hiking cycle in which FOMC meetings became the
dominant scheduled event and pre-positioning grew — and the availability of a
plausible post-hoc story for a recent-only result is precisely the trap this
register exists to catch. Gate 1 caught it: the train half is **+0.364**, below
the 0.5 bar, and the holdout CI spans **2.58 Sharpe units**.

### What carries forward

**The horizon lesson holds a second time.** Cost is **14%** of the gross mean
here and **10%** in H154, against **51%** in H143's overnight window and near
total in the intraday family. Two mechanism-driven, multi-hour-to-multi-day
hypotheses have now both landed in the 10-15% band. That is a property of
holding periods and it applies to anything tested from here.

**Event-driven is no longer an empty column.** The register had zero hypotheses
mentioning news, earnings, events or announcements before today.

### Kill

H155 to the graveyard. Per the registered kill rules: no sign flip, no fourth
`d`, no moving the exit past 13:45 to capture the announcement reaction, no
adding the unscheduled meetings, no dropping 2020, no re-cut split, and **no
promoting `d = 2` to the registered cell.**

Specifically forbidden and worth naming, because it is the tempting move: the
2022-2026 sub-period may **not** be split out and reported as a finding. A
regime that is only visible after the fact, with a story attached afterwards, is
not a hypothesis. If the hiking-cycle mechanism is real it can be registered as
its own hypothesis, with its own conditioning variable defined in advance and
its own N — on a sample that does not include the window that suggested it.

**N accounting:** 1268 -> **1271** (+3). Fresh N=3 ceiling 0.3674; cumulative
ceiling 0.9370 at 16.28 years.

## H160. Order-flow IC replication on ES — **NOT CONFIRMED** (2026-10-01)

rho = -0.0087 out of sample (251 sessions) against a discovery -0.0234.
Gate 1 (p<0.01) FAIL at p=0.0187. Gate 2 (|rho|>=0.010) FAIL at 0.0087.
Gate 3 PASS. Two of three fail -> the order-flow line is buried per the
registered kill rule. My registered prediction (-0.014, all three pass)
was wrong. Full autopsy: graveyard/orderflow/H160-VERDICT.md

## H162. Does naming a structural counterparty predict a better outcome? — **NOT TESTABLE, GATE DROPPED** (2026-10-01)

Registered PRE-LABEL in `f3e31be`, spec sha256 `29ba83cb...3cb499b`. Power
check ran before the spec. **Cost $0 data, ~$0.03 external model.** Full
autopsy: `graveyard/mechanism/H162-VERDICT.md`, labels in
`H162-LABELS.md`.

A meta-test of my own proposal, so I did not do the labelling: the 24
mechanism cells went to an external model with mechanism names and markets
only — no Sharpes, no verdicts, no outcome ordering.

> **Registered prediction:** gates 1 and 2 fail, verdict INCONCLUSIVE leaning
> DROP.
> **Result: NO on 24 of 24 cells.** Zero variance in the predictor, no gate
> evaluable. Verdict class correct, my reasoning wrong.

| | |
|---|---:|
| hypotheses labelled | 24 cells covering all 151 |
| labelled YES | **0** |
| distinct mechanism families behind the 138 scored rows | **6** |
| ICC of holdout Sharpe within cells | 0.514 |
| effective N of the pooled 138 rows | **20.3** |
| best achievable MDE | 0.682 Sharpe |
| effect that would have mattered | 0.600 Sharpe |

**Three things this bought.**

1. **The register is 6 ideas, not 138.** Effective N 20.3 after the design
   effect. Every prior count of "hypotheses tested" overstates the search by
   roughly 7x. Use 20, not 138, in any future multiple-testing adjustment.

2. **The gate rejects 24 of 24, including every flow hypothesis.** A filter
   that rejects everything is a restatement of "do not trade". Dropped per
   its own kill rule; not to be re-proposed without outside evidence.

3. **"Obliged to trade" is not "obliged to pay a concession."** The
   labeller's rejection of month-end flow — being required to rebalance is
   not being required to lose — is the defect in my phrasing. The operative
   version needs four conjuncts: named party, must trade, at a time known in
   advance, with no discretion over price. Conjunct 4 does all the work and
   was missing. It is a **generation prompt, unproven**, and never a reason
   to skip a gate.

**Scoring my own prediction.** I expected the low-volatility anomaly —
leverage-constrained investors chasing beta through price — to be the
register's strongest YES and to drag the named group down, since it is the
worst cell on file (median holdout −1.180 crypto, −0.750 equity, 0/18
positive). It was labelled NO: a borrowing limit constrains financing, it
does not mandate a losing trade. The example I used to justify proposing the
gate does not survive the gate.

**One observation that is not a test.** H154 is the only hypothesis in 151
generated from a named mechanism rather than a pattern search, and this
ledger recorded it on 2026-09-24 as the best result in 154: cost 10% of gross
mean against 51% for H143, the first and only **TIES** against SPY where
every other ES hypothesis returned **LOSES TO**, and the closest any of 1,259
cells came to its ceiling with a positive sign (+0.354 vs 0.520). It still
failed all four gates. **n=1, selected after the fact, on no pre-specified
metric.** Recorded so it is not lost; it is not evidence, and this sentence
is the rebuttal if it is ever cited as such.

## H161. Is crypto vol-scaled momentum a regime, or an effect? — **NOT CONFIRMED** (2026-10-01)

Registered PRE-DATA PRE-CODE in `02d5530`, spec sha256 `34a3a5b1...f4a7592f`;
pre-run addendum `9079557`, sha256 `eec08801...6177f294b0`. **Cost $0.**
Full autopsy: `graveyard/crypto/H161-VERDICT.md`.

> **Registered prediction:** fail, roughly 1 in 4 to clear. **CORRECT.**

| gate | requirement | result | |
|---|---|---|---|
| 1 | same sign as `IC_cal` | cal **−0.0054** vs fresh **+0.0131** | **FAIL** |
| 2 | \|IC\| ≥ 0.40·\|IC_cal\| | 0.0131 vs 0.0022 | PASS (degenerate — see below) |
| 3 | \|t\| > 2.58 | **+0.511** | **FAIL** |
| 4 | \|IC\| ≥ MDE | 0.0131 vs **0.0660** | **FAIL** |

Kill rule fires: `mom_volscaled` on crypto is buried and the hunt stops.

**The premise was broken.** The ranking the signal uses — `px.shift(3)/px.shift(60)−1`,
identical to plain 60-3 XS momentum, since vol scaling touches size not order —
has mean daily IC **−0.0062 in train (1,612 days)** and **−0.0054 in the
original holdout (1,487 days)**. It has never predicted. There was nothing for
a third window to replicate.

**Where the +0.460 came from.** Not the ranking. Holdout PnL attribution on the
52-name frame: the **9 symbols Twelve Data no longer carries produced 31.3% of
holdout PnL from 17% of the universe**; dropping them cuts net holdout Sharpe
from **+0.853 to +0.472**. Top 3 names = 37.2% of PnL. It is not a few lucky
days — the 10 largest name-days are 2.4% of 27,867 non-zero name-days. The
shape is inverse-vol sizing loading into a particular set of small crypto names
over a particular stretch. Neither "a regime" nor "an effect". Fresh window on
the money route: gross −0.023, net **−0.344**.

**Three errors, owned in the autopsy.**

1. **The registered MDE was 1.7× too optimistic and was knowable in advance.**
   The spec used `(1/√49)/√90` = 0.0149. The realised sd of the daily IC is
   **0.27 in both original halves** — already on disk when the spec was written
   — implying **effective breadth ~14, not 43**; mean pairwise daily return
   correlation over the test window is **0.482**. True SE 0.0256, true MDE
   **0.0660**. I used a formula where the realised dispersion of the statistic
   was sitting in the data. **Error #10**, same class as the overlap-blind IC SE.
2. **Gate 2 was degenerate.** 40% of a near-zero `IC_cal` is 0.0022; noise
   clears it. Computing `IC_cal` before writing the gates would have killed the
   hypothesis instead of testing it.
3. **Dead code in the runner** (a `drop` after the derived frame, and a no-op
   line). It changed nothing — the spliced return touches only the final
   calibration day, 1 of 1,487, and never the test window. Disclosed, not
   quietly patched.

**Data note.** yfinance now returns an empty frame for all 52 crypto tickers;
the refresh ran through the Twelve Data connector. 9 symbols unavailable there,
4 of them 2024-25 memecoins — a survivorship tilt that ran **in favour of a
pass** and was disclosed before the run. Vendor splice measured on ETH overlap
(~0.1%); the 2026-07-04 return was dropped.

Register after this verdict: **158 hypotheses / 154 verdicts / 0 confirmed**,
six mechanism families, effective N 20.3.

---

# Imported verdicts: `tsahalisp/gex-vol-research` H-001..H-016 = Graveyard H163-H178 (imported 2026-10-06)

Copied from that repo's README scorecard at `0c14009`; numbers not re-derived
here (Databento licence: the 1m data is not in this repo). Provenance caveat
in HYPOTHESES.md applies. **15 NOT CONFIRMED, 1 numerical pass that its own
pre-registered timing check then failed. 0 tradable.**

## H163 (H-001). PDH break continuation, ES — **NOT CONFIRMED**
+0.18 pts, t 0.94, below a same-time control. The 2-year dev sample showed +2.29.

## H164 (H-002). Level fades on high-GEX days — **NOT CONFIRMED**
Right direction (t 2.01), below the multiple-testing bar; fades still lose after costs.

## H165 (H-003). Level breaks on low-GEX days — **NOT CONFIRMED**
NQ goes the other way.

## H166 (H-004). Last-30-min momentum on low-GEX days — **NOT CONFIRMED**
About break-even after costs.

## H167 (H-005). Trend following, 21 futures — **NOT CONFIRMED**
Sharpe 0.44 gross, 0.08 net; turnover 139x notional/yr.

## H168 (H-006). SPX put selling vs S&P 500 — **NOT CONFIRMED**
Excess Sharpe 0.46 vs 0.55; drawdown -37% vs -55%. Required a logged correction and re-run.

## H169 (H-007). GEX switch for weekly put selling — **NOT CONFIRMED**
Sharpe 0.31 -> 0.11; low-GEX weeks pay more premium.

## H170 (H-008). Trend sleeve on S&P 500 — **NOT CONFIRMED**
Sharpe 0.82 -> 0.70; 2022 loss -20% -> -9%.

## H171 (H-009). GEX in next-day ES vol forecast — **NUMERICAL PASS, NOT AN EDGE**
DM t 2.46 (2014-24), ~1.4% lower log-RV MSE; NQ t 1.47; later ES t 2.41. Volatility, not direction. Superseded by H172.

## H172 (H-010). H171 under a one-release GEX lag — **NOT CONFIRMED**
ES DM t 1.74 (bar 2.0), NQ 0.28; lag 2 removes the main-sample gain. Usable only if GEX is in hand the same evening, unproven.

## H173 (H-011). Vol-managed S&P 500 vs buy-and-hold — **NOT CONFIRMED**
Sharpe 0.78 vs 0.75 post-2016, wins 52% of bootstrap draws (bar 90%). Max drawdown -22% vs -34%: the dependable part.

## H174 (H-012). Round-number break continuation — **NOT CONFIRMED**
ES -0.33 pts gross, no better than the momentum control.

## H175 (H-013). First half hour predicts last half hour — **NOT CONFIRMED**
ES -0.06 gross; negative on both markets after 2016.

## H176 (H-014). Small opening gaps fade — **NOT CONFIRMED**
ES +0.40 gross (t 1.63), -0.15 net.

## H177 (H-015). Month-end rebalancing, open-to-close — **NOT CONFIRMED**
ES +0.10 gross over 170 months; positive 2010-16, negative 2017-24. Second scoring of the H154 mechanism on the same history.

## H178 (H-016). Stock/bond decile rebalancing, next session — **NOT CONFIRMED**
ES +1.11 net, t 0.92, 699 sessions; NQ t 1.32. Right sign on both. A confirmation on Aug-2024-onward data (~113 sessions) has ~5-13% power; not recommended.

## H179. Multi-asset risk-premia portfolio — **NOT CONFIRMED** (2026-10-06)

Registered PRE-DATA (`4d728d9`), run once by `graveyard/portfolio/h179_run.py`
on yfinance dividend-adjusted closes (SPY/EFA/IEF/GLD/DBC) and FRED DTB3,
2007-03-02 -> 2026-10-05; holdout 2016-01-01 onward (10.73 y). Cost $0.
Pre-run checks: common start 2006-02-06, no price gaps, max daily moves
plausible (SPY 14.5% = Oct 2008), weights unchanged when future data is altered.
One bug caught BEFORE the run (relative `__file__` path broke the lib import).

| gate | requirement | result | |
|---|---|---|---|
| 1 | excess Sharpe > 0.5 both halves | 0.862 / **0.451** | FAIL |
| 2 | holdout one-sided 95% bootstrap lower bound > 0 | **-0.0001** | FAIL (by a hair) |
| 3 | best of 6 cells > 0.578 | 0.654 (trend OFF, 8%) | PASS |
| 4 | Sharpe >= SPY **and** maxDD <= 0.6 x SPY | 0.451 vs 0.754 / -16.5% vs -33.7% | FAIL (Sharpe), PASS (drawdown) |
| 5 | gates 1-2 at 25 bp | 0.795 / 0.367 | FAIL |

Reported: DSR 0.570 (N=6), 0.292 (N=27); PBO across the 6 cells 0.567 (single
PBO is noisy). Full sample: excess Sharpe 0.630 vs SPY 0.559; max drawdown
**-16.5% vs -55.2%**; CAGR 6.5% vs 11.1%; vol 8.2%.

> **Registered prediction: FAIL, drawdown passes, Sharpe loses to a strong
> 2016-2026 S&P. CORRECT on every part.**

What it says: over 20 years the book matched the S&P's risk-adjusted return
with a third of the drawdown and about 60% of the return. In the 2016-2026
holdout it lost to the S&P on Sharpe. The trend filter cost Sharpe in the
holdout (0.45 on vs 0.65 off) -- that comparison is a search result, not a
finding, and the kill rule forbids promoting the trend-off cell.

**Kill rule fires: Phase 1 ends and the register RE-FREEZES.** H180 (forward,
timing only) continues on its own clock.

## H181. Breadth momentum on CRSP — **NOT CONFIRMED** (2026-10-06)

Spec committed PRE-DATA (`e5cb6d5`); data pulled after, from Peter's WRDS
account (CRSP CIZ `msf_v2` 1992-01 -> 2025-12, 3,199,856 stock-months;
Fama-French factors). Run once: `graveyard/breadth/h181_run.py`. Cost $0.

Data-step decisions, made before any strategy number existed:
legacy `msf` stops 2024-12, so CIZ `msf_v2` is used; CIZ `mthret` already
contains the delisting return (0 of 19,307 delisting months missing a return,
corr with `delret` 0.675), so `delret` is not compounded twice; CRSP `msi`
stops 2024-12, so gate 4 uses Fama-French Mkt-RF (built from CRSP VW);
momentum read as standard 12-1 (formation T uses T-11..T-1). Eligibility is
judged only at formation; held stocks keep their next-month return whatever
their flags. 452 held stock-months had no next-month row and were set to 0.
Pre-run checks: 2,699-4,865 eligible stocks per month; Mkt-RF in decimals;
signal unchanged when future returns are altered.

| gate | requirement | result | |
|---|---|---|---|
| 1 | net Sharpe > 0.5 both halves | 0.323 / 0.234 | FAIL |
| 2 | holdout bootstrap lower bound > 0 | -0.128 | FAIL |
| 3 | best of 6 cells > 0.473 | 0.322 (TOP3000-VW-skip) | FAIL |
| 4 | CAPM alpha t > 2 (NW 6) | alpha 7.0%/yr, t 1.47, beta -0.15 | FAIL |
| 5 | gates 1-2 at doubled costs | 0.219 / 0.084 | FAIL |

Shown, not gates: DSR 0.357 (N=6), 0.134 (N=28); PBO 0.603. Full sample
1994-2025: mean 7.9%/yr, Sharpe 0.28 (vol ~28%/yr). Worst months: 2001-01
-38.2%, 2009-04 -33.3%.

> **Prediction: FAIL, first half passes gate 1, holdout 0.1-0.4.**
> Verdict and holdout range CORRECT; "first half passes gate 1" WRONG (0.32).

What it says: breadth did not rescue momentum. The widest universe was the best
cell (0.32 holdout vs 0.23), which is the direction breadth predicts, but the
size of the help was small next to momentum's crash risk. The return is real
on paper (7-8%/yr) but arrives with ~28% volatility and two one-month losses
over 30%, so it never clears a risk-adjusted bar.

**Kill rule fires: Phase 2 ends and the register re-freezes.**

## H182. Multi-factor composite (value + profitability + investment + momentum) — **NOT CONFIRMED** (2026-10-06)

Registered PRE-DATA (`5d66002`); Compustat pulled after; run once
(`graveyard/factors/h182_run.py`, panel `fcommon.py`). Cost $0.
Data-step deviation, logged before results: USC's WRDS does not include the
CRSP-Compustat link table (permission denied on `crsp_a_ccm`), so Compustat is
linked by CUSIP (Compustat security CUSIP -> every CRSP permno that carried it).
Coverage of the top-1,000 universe: book-to-market 91-96%, profitability
91-96%, asset growth 92-99%. Also logged: XSGA/XINT missing -> 0; fundamentals
used 6-18 months after fiscal year-end.

| gate | requirement | result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 both halves | 0.541 / **-0.145** | FAIL |
| 2 | holdout bootstrap lower bound > 0 | -0.611 | FAIL |
| 3 | best of 4 cells > 0.416 | 0.360 (TOP3000-EW) | FAIL |
| 4 | CAPM alpha t > 2 | alpha 0.0%/yr, t 0.00 | FAIL |
| 5 | doubled costs | 0.417 / -0.284 | FAIL |

DSR 0.05 (N=4), 0.004 (N=29); PBO 0.58. Correlation with the momentum-only book
0.34. Full sample: 4.8%/yr, vol 19.8%, Sharpe 0.24. Worst month -18.5%
(2025-05); 2009-04 -10.5% (H181 lost -33.3% that month).

> **Prediction: FAIL narrowly; holdout Sharpe 0.3-0.6; much smaller crashes;
> alpha t 1.5-3.** Verdict CORRECT, crash reduction CORRECT (-18.5% vs -38%).
> Holdout Sharpe WRONG (-0.14, not 0.3-0.6). Alpha t WRONG (0.00).

What it says: combining the signals did what it was designed to do on crashes,
roughly halving the worst month, but it removed the return along with the
risk. 2010-2025 the composite earned nothing in the 1,000 largest stocks. The
better-looking cells (TOP3000-EW 0.36) are search results and are not promoted.

**Kill rule fires: register re-freezes.** H183 (study, no kill rule) reported below.

## H183. 12-anomaly post-publication replication — **1 of 12 survives gross, 0 net** (2026-10-06)

Registered PRE-DATA (`5d66002`), run once (`graveyard/factors/h183_run.py`).
Same CRSP/Compustat panel and CUSIP link as H182. Top 3,000 stocks, price >= $5,
value-weighted decile long-short, post-publication months only (not before 1994).

| id | anomaly (paper) | window | gross %/yr | gross t | net %/yr | net t |
|---|---|---|---:|---:|---:|---:|
| H183.1 | Size (Banz 1981) | 1994-2025 | -1.9 | -0.84 | -5.5 | -2.42 |
| H183.2 | Value (Fama & French 1992) | 1994-2025 | -2.5 | -0.60 | -4.4 | -1.05 |
| H183.3 | Earnings yield (Basu 1977) | 1994-2025 | 5.6 | 1.52 | 3.0 | 0.80 |
| H183.4 | Momentum (Jegadeesh & Titman 1993) | 1994-2025 | 13.8 | **2.75** | 9.3 | 1.87 |
| H183.5 | Short-term reversal (Jegadeesh 1990) | 1994-2025 | -2.8 | -0.75 | -12.2 | -3.24 |
| H183.6 | Long-term reversal (De Bondt & Thaler 1985) | 1997-2025 | -2.1 | -0.49 | -4.8 | -1.15 |
| H183.7 | Gross profitability (Novy-Marx 2013) | 2014-2025 | 7.9 | 1.83 | 6.2 | 1.45 |
| H183.8 | Operating profitability (Fama & French 2015) | 2016-2025 | 7.3 | 1.15 | 5.6 | 0.88 |
| H183.9 | Asset growth (Cooper, Gulen & Schill 2008) | 2009-2025 | 3.7 | 0.86 | 1.7 | 0.41 |
| H183.10 | Accruals (Sloan 1996) | 1997-2025 | 3.4 | 1.37 | 1.5 | 0.58 |
| H183.11 | Net share issuance (Pontiff & Woodgate 2008) | 2009-2025 | 4.4 | 1.51 | 2.3 | 0.77 |
| H183.12 | Low volatility (Ang et al. 2006; monthly proxy) | 2007-2025 | -3.7 | -0.54 | -6.4 | -0.95 |

Survive at t > 2 gross: **1** (momentum). At t > 3: **0**. At t > 2 net: **0**.

> **Prediction: at most 4 survive at t > 2 gross, at most 2 at t > 3, short-term
> reversal dead net of costs. CORRECT on all three.**

What it says: after publication, in the 3,000 largest US stocks, most famous
anomalies are not distinguishable from zero, and several flipped sign. Seven of
twelve still point the paper's way gross, but small. Caveats: one construction
(VW deciles, top 3,000, price >= $5) differs from many original papers; CUSIP
link instead of CCM; low volatility uses a monthly proxy; profitability and
operating profitability have only 10-12 post-publication years.

# Phase 3 batch, H184-H189: all run 2026-10-07 (registered PRE-DATA `014660c`)

All six were run once each on 2026-10-07 by `graveyard/phase3/p3_run.py` (unchanged since `014660c`; spec sha256 d3e5ffd8da4a).
The cadence moved from weekly to back-to-back, logged before any run (`d2c8e18`). Data: CRSP msf_v2 + Compustat
(CUSIP link) + Ken French FF3, 1994-01..2025-12; holdout 2010-01..2025-12 (16.0 yr). Gate 3 N = 180. Cost $0.

## H184. Liquid slow momentum (top 500, quarterly signal) — **NOT CONFIRMED** (2026-10-07)

| gate | requirement | result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 both halves | 0.234 / 0.088 | FAIL |
| 2 | holdout bootstrap lower bound > 0 | -0.296 | FAIL |
| 3 | holdout Sharpe > 0.806 | 0.088 | FAIL |
| 4 | CAPM alpha t > 2 (NW6, holdout) | alpha 2.2%/yr, t 0.45 | FAIL |
| 5 | doubled costs | 0.159 / -0.012 | FAIL |

Shown, not gates: DSR 0.009 (N=180). Full sample 4.6%/yr, vol 27.0%, Sharpe 0.17; gross 0.26 full, 0.19 holdout.
Worst month -37.8% (2001-01); 2009-04 -34.0%. Correlation with the momentum book 0.93. TOP3000-EW holdout (info) 0.21.

> **Prediction: FAIL; holdout net 0.0-0.4.** Verdict CORRECT, holdout 0.088 CORRECT.

What it says: restricting momentum to the 500 most liquid stocks and trading quarterly cut costs, but it left the same
book (0.93 correlated) with the same crashes. There was almost nothing left in 2010-2025.

## H185. Volatility-scaled momentum (Barroso & Santa-Clara) — **NOT CONFIRMED** (2026-10-07)

| gate | requirement | result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 both halves | 0.508 / 0.211 | FAIL |
| 2 | holdout bootstrap lower bound > 0 | -0.139 | FAIL |
| 3 | holdout Sharpe > 0.806 | 0.211 | FAIL |
| 4 | CAPM alpha t > 2 (NW6, holdout) | alpha 4.0%/yr, t 1.35 | FAIL |
| 5 | doubled costs | 0.363 / 0.043 | FAIL |

Shown, not gates: DSR 0.031 (N=180). Full sample 5.0%/yr, vol 14.0%, Sharpe 0.36. Worst month -16.2% (2014-03);
2009-04 -11.3%. Correlation with the momentum book 0.87. TOP3000-EW holdout (info) 0.27.

> **Prediction: FAIL; worst month far smaller than -38%; holdout 0.3-0.6.** Verdict CORRECT, crash CORRECT
> (-16.2%), holdout WRONG (0.211, below the range).

What it says: vol scaling did what the paper claims on risk. The worst month is less than half of plain momentum's,
and 2009-04 drops from -34% to -11%. But the holdout return was too small to matter.

## H186. 52-week-high proximity (George & Hwang) — **NOT CONFIRMED** (2026-10-07)

| gate | requirement | result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 both halves | 0.063 / 0.051 | FAIL |
| 2 | holdout bootstrap lower bound > 0 | -0.326 | FAIL |
| 3 | holdout Sharpe > 0.806 | 0.051 | FAIL |
| 4 | CAPM alpha t > 2 (NW6, holdout) | alpha 10.1%/yr, t 2.14 | PASS |
| 5 | doubled costs | -0.068 / -0.129 | FAIL |

Shown, not gates: DSR 0.006 (N=180). Full sample 1.6%/yr, vol 27.3%, Sharpe 0.06; gross 0.21 full, 0.23 holdout.
Worst month -35.9% (2001-01); 2009-04 -33.6%. Correlation with the momentum book 0.72. TOP3000-EW holdout (info) -0.06.

> **Prediction: FAIL; holdout 0.0-0.4.** Verdict CORRECT, holdout 0.051 CORRECT.

What it says: the CAPM alpha t of 2.14 comes from a market beta of -0.69 (the book is short the market), not from
returns: Sharpe was 0.05. Costs ate the gross 0.23. It fails four of five gates.

## H187. Residual (FF3) momentum (Blitz et al.) — **NOT CONFIRMED** (2026-10-07)

| gate | requirement | result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 both halves | 0.258 / -0.461 | FAIL |
| 2 | holdout bootstrap lower bound > 0 | -0.866 | FAIL |
| 3 | holdout Sharpe > 0.806 | -0.461 | FAIL |
| 4 | CAPM alpha t > 2 (NW6, holdout) | alpha -5.7%/yr, t -1.97 | FAIL |
| 5 | doubled costs | 0.004 / -0.745 | FAIL |

Shown, not gates: DSR 0.000 (N=180). Full sample -1.2%/yr, vol 13.9%, Sharpe -0.08; gross 0.18 full, -0.18 holdout.
Worst month -16.1% (2009-04). Correlation with the momentum book 0.51. TOP3000-EW holdout (info) -0.50.

> **Prediction: FAIL but closest of the six; holdout 0.4-0.8; alpha t 1.5-3.** Verdict CORRECT. "Closest" WRONG
> (it was among the worst; H189 was closest). Holdout WRONG (-0.461). Alpha t WRONG (-1.97).

What it says: this was the worst miss in the batch. The published residual-momentum premium was negative in
2010-2025 even before costs. Its smoother crashes did not come with any return.

## H188. Same-calendar-month seasonality (Heston & Sadka) — **NOT CONFIRMED** (2026-10-07)

| gate | requirement | result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 both halves | 0.157 / -0.271 | FAIL |
| 2 | holdout bootstrap lower bound > 0 | -0.715 | FAIL |
| 3 | holdout Sharpe > 0.806 | -0.271 | FAIL |
| 4 | CAPM alpha t > 2 (NW6, holdout) | alpha -8.3%/yr, t -1.93 | FAIL |
| 5 | doubled costs | -0.233 / -0.658 | FAIL |

Shown, not gates: DSR 0.000 (N=180). Full sample -1.3%/yr, vol 16.9%, Sharpe -0.08; gross 0.31 full, 0.12 holdout.
Worst month -22.2% (2001-02); 2009-04 -2.0%. Correlation with the momentum book 0.12. TOP3000-EW holdout (info) -1.60.

> **Prediction: FAIL; gross positive, net holdout < 0.3.** Verdict CORRECT, gross positive CORRECT (0.31 / 0.12),
> net holdout CORRECT (-0.271).

What it says: there is a seasonal signal gross (0.31 full sample), but net of costs it is negative in the holdout. The equal-weight info cell (-1.60) shows how badly the costs land on small stocks.

## H189. 10-month market trend timing (long-only) — **NOT CONFIRMED** (2026-10-07)

| gate | requirement | result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 both halves | 0.722 / 0.757 | PASS |
| 2 | holdout bootstrap lower bound > 0 | 0.332 | PASS |
| 3 | holdout Sharpe > 0.806 | 0.757 | FAIL |
| 4 | holdout Sharpe >= market and maxDD <= 0.6x market | 0.757 vs 0.873 / -17.9% vs -24.8% (0.72x) | FAIL |
| 5 | doubled costs | 0.716 / 0.750 | PASS |

Shown, not gates: DSR 0.608 (N=180). Full sample 8.1%/yr, vol 11.0%, Sharpe 0.74. Worst month -16.1% (1998-08);
2009-04 0.0%. In the market 77% of months, 46 switches.

> **Prediction: FAIL gate 4 on Sharpe; drawdown condition passes.** Verdict CORRECT, Sharpe part CORRECT
> (0.757 < 0.873), drawdown WRONG (0.72x the market's, not under 0.6x).

What it says: this is the best result in the batch and passes three gates, but in 2010-2025 it did not beat just
holding the market. It is the same lesson as H173 and H179:
risk control works, but the return doesn't beat buy-and-hold.

**Phase 3 stop rule: 0 of 6 CONFIRMED. The CRSP/Compustat line is closed and the register re-freezes (see HYPOTHESES.md).**
Prediction record for the batch: 6 of 6 verdicts correct; 12 of 17 parts correct (verdicts included).

## H194. Filtered ES opening-range breakout (three published ORB filters) — **NOT CONFIRMED, UNDERPOWERED** (2026-10-08)

Registered PRE-RESULT in `09869f0` (with the general unfreeze). Runner `graveyard/orbfilter/h194_run.py` was committed in `352aa88` before it ran. Run once. Data: the H133-ES sample, 4,049 eligible sessions over 16.07 years. Cost $0.

| Filter (prior 20 sessions only) | Sessions passing |
|---|---:|
| Normalized ORB 0.6-1.5x | 3,000 |
| ORB / daily ATR 0.05-0.25 | 1,166 |
| Relative volume 1-10x | 1,776 |
| **All three** | **110** |

110 trades, under the registered 200-trade power floor: **UNDERPOWERED**.

| Gate | Requirement | Result | |
|---|---|---|---|
| 1 | net > 0 and Sharpe > 0.5 in both halves | train -$4,045 / -0.26; holdout -$61 / -0.00 | FAIL |
| 2 | holdout CI excludes zero | -0.00 [-1.24, +0.76] | FAIL |
| 3 | Sharpe > 0.670 (N=37 over 16.07 y) | -0.10 | FAIL |
| 4 | beats SPY buy-and-hold | LOSES, diff-Sharpe -0.87 [-1.42, -0.38] | FAIL |
| 5 | $40 stress | train -0.30, holdout -0.03 | FAIL |

Shown, not gated: win rate 36.4%; net -$4,105; max drawdown -$9,848; worst day -$1,379; geometric -1.5%/yr. Unfiltered H133-ES on the same sessions at $29.48: 3,882 trades, Sharpe -0.31, -$75,229. Of the regimes, only 2022-2023 was positive (+0.65). The firm-wide ceiling (N=1,250) is 0.94.

> **Prediction: FAIL; holdout -0.5 to +0.3.** Verdict CORRECT. Holdout -0.00 CORRECT. "Cuts trades 3-5x" WRONG: the cut was 35x. The ORB/ATR filter is tuned for a shorter range than our 30-minute one, which was a registered deviation.

What it says: the filters cut losses mostly by trading less, and what's left is still negative. A 15-minute-range version would be a NEW ID, not a re-run. Given every ORB cell on this sample is negative, it isn't a priority.

## H195. IBS mean reversion on SPY, daily — **CONFIRMED** (2026-10-08) — first CONFIRMED in the register

Registered PRE-DATA in `43d7f5a`. The runner `graveyard/spydaily/h195_h196_run.py` was committed in `431bd5d` before it ran, and it ran once. Data: SPY from yfinance, 1993-02-01 to 2026-10-07 (8,479 days, 0 days with High = Low). Halves split at 2009-11-27. Risk-free from Ken French monthly data; 2026-07 to 2026-10 carry the last value forward (disclosed). Cost: 1 bp/side, with a 5 bp/side stress test.

| Gate | Requirement | Result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 in both halves | 0.804 / 0.932 | PASS |
| 2 | Second-half bootstrap lower bound > 0 | 0.504 | PASS |
| 3 | Second-half Sharpe > 0.789 (N=188, Y2≈16.9) | 0.932 | PASS |
| 4 | Long-only: Sharpe ≥ SPY's AND max DD ≤ 0.6x SPY's (second half) | 0.932 vs 0.785 / -18.9% vs -33.7% (0.56x) | PASS |
| 5 | 5 bp/side stress keeps gates 1-2 | 0.636 / 0.750, lower bound 0.327 | PASS |

Shown, not gated: 988 trades; 38% of days in the market; median hold 2 days, longest 18; CAGR 13.8% including cash; +0.44% gross per trade; 69% wins in both halves.

> **Prediction: FAIL (second half 0.2-0.7, fails gate 3 and/or 4).** WRONG on every part. The second half was stronger than the first.

**Checks run after the verdict (they cannot change it):**
- An independent re-implementation (trade-list loop instead of the vectorized runner) reproduces exactly 988 trades. Second-half daily Sharpe before rf and costs is 1.02.
- Per-trade mean by era: 1993-2000 +0.40%, 2001-2008 +0.36%, 2009-2015 +0.40%, 2016-2020 +0.51%, 2021-2026 +0.41%. No decay so far.
- Entering at the NEXT day's open instead of the signal close still earns +0.32% per trade in the second half (69.7% wins). So the result does not depend on the unrealistic same-close fill.
- The same rule on QQQ, IWM and DIA from 2000 earns +0.49%, +0.37% and +0.37% per trade.
- SPY OHLC from yfinance matched Twelve Data exactly on 89 days (2026-06 to 2026-10). IBS signals agreed 100%.

**What CONFIRMED licenses, per register rules:** no live money yet.
- Next: a separately registered replication on different data (ES futures from our own Databento minute bars, 2010-2026) and a forward paper period.
- Caveats: this is a widely published rule; it holds overnight (incompatible with prop-firm flat-by-close rules); and it is long-only, so exposure is to down-gaps after weak closes. Its max DD was -18.9% versus SPY's -33.7%.

## H196. Turnaround Tuesday on SPY — **NOT CONFIRMED** (2026-10-08)

Same commit, data, costs and gates as H195.

| Gate | Requirement | Result | |
|---|---|---|---|
| 1 | Sharpe > 0.5 in both halves | 0.626 / 0.584 | PASS |
| 2 | Second-half bootstrap lower bound > 0 | 0.112 | PASS |
| 3 | Second-half Sharpe > 0.789 | 0.584 | FAIL |
| 4 | Long-only vs SPY | 0.584 < 0.785 (DD -7.5% vs -33.7% passes) | FAIL |
| 5 | 5 bp stress | 0.385 / 0.297, lower bound -0.209 | FAIL |

698 trades, 8.2% exposure, +0.21% gross per trade, CAGR 6.3% including cash.

> **Prediction: FAIL gate 4 (drawdown condition passes).** CORRECT.

Real but small, and too thin to survive realistic costs.

## H197. IBS replication on ES futures — **DOES NOT REPLICATE** (2026-10-08), missed R4 by a hair

Registered PRE-RESULT in `a04b992`. Runner `469d1a8`, run once. Data: ES RTH bars, 2010-06-07 to 2026-09-18. 4,053 days kept, 132 excluded (early closes or incomplete), 66 rolls with the return set to 0. Split at 2018-07-26.

| Gate | Requirement | Result | |
|---|---|---|---|
| R1 | full-sample bootstrap lower bound > 0 | Sharpe 0.854, lower bound 0.420 | PASS |
| R2 | Sharpe > 0.5 in both halves | 0.686 / 1.000 | PASS |
| R3 | $40 stress: mean > 0 and R1 holds | Sharpe 0.835, lower bound 0.401 | PASS |
| R4 | Sharpe ≥ buy-and-hold AND max DD ≤ 0.6x buy-and-hold | 0.854 vs 0.834 PASS / -18.8% vs -30.1% = **0.626x** FAIL | FAIL |

Shown, not gated: 423 trades; 35% exposure; +0.39% gross per trade; +$261,652 per ES contract over 16 years after $29.48 costs (no compounding, 1 contract).

> **Prediction: REPLICATES, full Sharpe 0.6-1.0.** The Sharpe part is CORRECT (0.854). The verdict part is WRONG: the drawdown condition failed.

What it says: the edge itself replicates on independent futures data. It is positive in both halves, survives costs and has a bootstrap lower bound of 0.42. What fails is the registered risk condition. Its max drawdown was 0.63x buy-and-hold's, not ≤ 0.60x, so it did not clearly beat simply holding ES on risk. Per the registered rule, H195's confirmation is **downgraded to "SPY-data only"**. No gate is re-cut and no window is re-chosen.

FP-195 (the forward paper log) was registered before this result as a no-capital implementation check. It runs as registered and carries no decision weight.

## H198. Williams %R(2) on SPY — **CONFIRMED** (2026-10-08), not independent of H195
Registered `ae550fb`, runner `ca91a15`, run once. Same data, costs and gates as H195. N = 190.

| Gate | Result | |
|---|---|---|
| 1 Sharpe > 0.5 in both halves | 1.064 / 0.815 | PASS |
| 2 Second-half bootstrap lower bound > 0 | 0.396 | PASS |
| 3 Second-half Sharpe > 0.790 | 0.815 | PASS |
| 4 vs SPY (second half) | 0.815 ≥ 0.785; DD -16.7% vs -33.7% (0.50x) | PASS |
| 5 5 bp stress | 0.938 / 0.681, lower bound 0.262 | PASS |

630 trades, 22% exposure, +0.61% gross per trade. **89% of its in-market days are also H195's; daily correlation 0.75.** This is the same effect, not new evidence.
> Prediction (pass 1-2; second half 0.6-0.9; gate 4 borderline; overlap > 60%): CORRECT on all parts. Gate 4 passed rather than "borderline".

## H199. SPY new 252-day high, hold 21 days — **NOT CONFIRMED** (2026-10-08)
Halves 0.073 / 0.587; second-half lower bound 0.140; below the 0.790 bar; below SPY's 0.785; stress 0.037 / 0.534. 142 trades, +0.82% gross per trade, 35% exposure. Fails gates 1, 3, 4 and 5.
> Prediction (FAIL gate 4): CORRECT.

## H200. Williams %R(2) replication on ES — **DOES NOT REPLICATE** (2026-10-08)
Registered `429c410`, runner `16218ad`.

| Gate | Result | |
|---|---|---|
| R1 full-sample lower bound > 0 | Sharpe 0.671, lower bound 0.233 | PASS |
| R2 both halves > 0.5 | 0.242 / 1.050 | FAIL |
| R3 $40 stress | 0.657, lower bound 0.219 | PASS |
| R4 vs buy-and-hold | 0.671 < 0.834 | FAIL |

261 trades, +0.40% gross per trade, +$203,308 per ES contract. H198 is downgraded to "SPY-data only".
> Prediction (R1-R3 pass, R4 borderline): WRONG on R2 (2010-2018 was weak) and on R4 (it failed on Sharpe as well).

**Family read (H195, H197, H198, H200):** buying index ETFs/futures after a weak close and selling into strength is positive in every test, on both data sources, and survives costs. On SPY 1993-2026 it beats buy-and-hold on risk. On ES 2010-2026 it does not clearly beat simply holding ES (IBS: Sharpe 0.85 vs 0.83 but DD 0.63x; %R: Sharpe 0.67 vs 0.83).

## H201. IBS on an equal-weight SPY/QQQ/IWM/DIA book — **CONFIRMED** (2026-10-08)
Registered `4062e7b`, runner `fcd5c14`, run once. 2000-05-30 to 2026-10-07, split at 2013-08-02. N = 193.

| Gate | Result | |
|---|---|---|
| 1 Sharpe > 0.5 in both halves | 0.813 / 0.961 | PASS |
| 2 Second-half bootstrap lower bound > 0 | 0.478 | PASS |
| 3 Second-half Sharpe > 0.894 | 0.961 | PASS |
| 4 vs SPY (second half) | 0.961 ≥ 0.759; DD -15.8% vs -33.7% (0.47x) | PASS |
| 5 5 bp stress | 0.654 / 0.768, lower bound 0.289 | PASS |

CAGR 13.5% vs SPY 8.6% (2000-2026, including cash); average exposure 40%; mean sleeve correlation 0.69.
> Prediction (CONFIRMED, second half 0.9-1.3): CORRECT. Contamination as registered: the per-ETF per-trade means were seen beforehand. Same family as H195/H198, not independent of them.

## H202. IBS overlay on buy-and-hold SPY (1x, 1.5x after weak closes) — **NOT CONFIRMED** (2026-10-08)
Halves 0.452 / 0.876 (gate 1 FAIL). Lower bound 0.437 PASS. 0.876 > 0.791 PASS. Gate 4 PASS (0.876 ≥ 0.785; DD -30.3% vs -33.7%). Stress 0.403 / 0.825 (gate 5 FAIL). CAGR 16.0% vs SPY 10.9%; average leverage 1.19x.
> Prediction (pass 1, 2, 4; G3 marginal): WRONG on gate 1. 1993-2009 was below 0.5 because the base 1x SPY carries the 2000-2002 and 2008 drawdowns.

## H203. IBS + 200-day trend filter — **NOT CONFIRMED** (2026-10-08)
Halves 0.629 / 0.655. Lower bound 0.198. Below the 0.791 bar and below SPY's 0.785. Stress 0.450 / 0.445 with lower bound -0.017. 665 trades vs H195's 988.
> Prediction (within ±0.15 of 0.93; trades down about 30%): trades CORRECT (-33%). Sharpe WRONG: the filter made it worse (-0.28). The best IBS entries happen in downtrends.

## H204. Where the IBS return comes from: overnight vs intraday — DIAGNOSTIC (2026-10-10)
Registered `99a43ae`, runner `add135c`, run once. SPY 1993-02-01 to 2026-10-07, split at 2009-11-27. ES 2010-06-07 to 2026-09-18 (67 pairs dropped for rolls or a missing 09:30 bar). Identity check: (1+on)(1+id) equals close-to-close to 2e-16.

Mean per day in bp, gross. CIs are a stationary block bootstrap (mean block 10, 5,000 draws, seed 204).

| Days | n | Overnight | Intraday | Close-to-close | Overnight share of log return |
|---|---:|---:|---:|---:|---:|
| SPY, H195 held | 3,201 | **8.67** [6.30, 11.02] | **4.81** [1.37, 8.49] | 13.48 | 67% |
| SPY, all | 8,478 | 4.04 | 0.73 | 4.77 | 93% |
| SPY, H195 flat | 5,277 | 1.23 | -1.74 | -0.51 | — |
| SPY held, 1st half | 1,718 | 8.69 [5.60, 11.76] | 4.69 [-0.69, 10.44] | 13.36 | 68% |
| SPY held, 2nd half | 1,483 | 8.65 [5.09, 12.42] | 4.96 [0.57, 9.38] | 13.62 | 65% |
| ES, H197 held | 1,389 | 7.64 [4.45, 10.84] | 4.20 [0.19, 8.21] | — | 66% |
| ES, all | 3,986 | 3.13 | 2.32 | — | 59% |

**Read.** About two-thirds of the IBS held-day return is overnight. But most of that is SPY's ordinary overnight drift, which every day earns.

Against the all-days baseline, the *extra* from IBS is about the same in each leg:
- overnight: +4.6 bp (8.67 vs 4.04)
- intraday: +4.1 bp (4.81 vs 0.73)

So the signal improves both legs. Both legs are positive with CIs above zero on the full sample, and the same holds on ES.

**Practical.** Keep holding close to close. Exiting at the open would throw away a real third of the return and double the trading (see H205).
> Prediction (overnight share >50%, 55-75%; overnight CI excludes 0; intraday positive but CI includes 0; ES same signs): CORRECT on share (67%), overnight CI, ES signs. WRONG on intraday: its full-sample CI excludes zero (it includes zero only in the first half).

## H205. IBS overnight-only on SPY — **NOT CONFIRMED** (2026-10-10)
Registered `99a43ae`, run once with H204. N = 194. 3,201 held days, each a round trip.

| Gate | Result | |
|---|---|---|
| 1 Sharpe > 0.5 in both halves | 0.827 / 0.754 | PASS |
| 2 Second-half bootstrap lower bound > 0 | 0.320 | PASS |
| 3 Second-half Sharpe > 0.791 | 0.754 | FAIL |
| 4 vs SPY (second half) | 0.754 < 0.785; DD -14.6% vs -33.7% | FAIL (Sharpe) |
| 5 5 bp stress | -0.333 / -0.217 | FAIL |

CAGR 8.2% (with cash). The rf convention while flat intraday (6.5/24 of the day's rf) is disclosed in the runner.
> Prediction (passes 1 and 2 at 1 bp; fails 5; gate 4 Sharpe below SPY): CORRECT on all three.

## H206. Multiple-testing hurdles for H195 and H201 — BOTH SURVIVE, including the holdout (2026-10-10)
Registered `43477aa`, runner `0bc25d1`, run once. Hurdles (one-sided, 5%): HLZ fixed 3.0; Bonferroni/Holm-top M = 194 → 3.473; effective M = 27 → 2.902. BHY not run (past p-values not stored).

| Series | Years | Sharpe | t (iid) | t (Newey-West 10) | > 3.47? |
|---|---:|---:|---:|---:|---|
| H195 full | 33.6 | 0.857 | 4.97 | **5.60** | YES |
| H195 2nd half | 16.8 | 0.932 | 3.82 | **4.17** | YES |
| H201 full | 26.3 | 0.866 | 4.44 | **5.11** | YES |
| H201 2nd half | 13.2 | 0.961 | 3.48 | **3.86** | YES |

The NW t is higher than the iid t in every row, because the returns are slightly negatively autocorrelated. The plain t understates significance.
> Prediction: CORRECT except H201's second half, which I expected just below 3.47 and which cleared it at 3.86 (NW).
> Read: the register's one family of confirmed results is not a multiple-testing artefact, even when charged for all 194 tests. This says nothing about forward decay (FP-195 is the forward check) or about independence (H201 shares H195's family).

## H207. IBS before vs after 2008 — DIAGNOSTIC (2026-10-10)
Registered `43477aa`, run once with H206. PRE 1993-2007, POST 2008-2026. Gross per-day means in bp.

| | PRE | POST | POST − PRE [95% CI] |
|---|---:|---:|---|
| H195 net Sharpe | 0.738 | 0.942 | — |
| Held-day overnight | 8.58 | 8.75 | +0.2 [−4.6, +5.0] |
| Held-day intraday | 2.36 | 6.98 | +4.6 [−2.3, +11.6] |
| Held-day close-to-close | 10.89 | 15.78 | +4.9 [−3.5, +13.9] |
| Held-day overnight share | 83% | 57% | — |
| All days: overnight / intraday | 5.15 / −0.67 | 3.16 / 1.85 | — |
| All days: overnight share | 129% | 67% | — |

- **IBS did not weaken after 2008.** The overnight leg is unchanged. The intraday leg grew, but not significantly.
- On ordinary days, SPY's intraday return went from negative to positive after 2008. That matches Knuteson's claim that the index overnight/intraday gap closed around then.
> Prediction (held-day legs unchanged; all-days intraday higher POST; all-days overnight share falls POST): CORRECT on all four checks. Contamination as registered: H204's 2009-11 halves were already seen.

## H208. IBS on a 15-ETF book (11 sector SPDRs, EFA, EEM, TLT, GLD): CONFIRMED (2026-10-10)
Registered c6d59bc; runner 96b4a49 (committed before results); one run; `results/h208_results.json`, log `h208_209.log`.

| Gate | Result | |
|---|---|---|
| 1 both halves > 0.5 | 0.836 / 1.113 | PASS |
| 2 holdout bootstrap lower bound > 0 | 0.606 | PASS |
| 3 > bar (N = 195, 13.9 holdout yrs) | 1.113 > 0.872 | PASS |
| 4 vs SPY (H2 Sharpe ≥, DD ≤ 0.6x) | 1.113 vs 0.838; DD 11.9% vs 33.7% (0.35x) | PASS |
| 5 stress 5 bp | 0.628 / 0.837, lower bound 0.339 | PASS |

- Sample 1999-01-04 to 2026-10-07, split 2012-11-16. Full Sharpe 0.93 (SPY 0.43). CAGR 11.6% (SPY 8.7%).
- **Every one of the 15 ETFs has a positive net Sharpe.** Range: XLRE 0.30 to XLC 1.14 (XLC has only 8 years). Trades per ETF: 254-868. Mean per trade: 0.17-0.57%.
- Cluster drop by year: the top year is 2020, 13.7% of the total. Dropping it does not flip the sign. **Reporting bug, disclosed:** the runner's row came out NaN because the book's first day (1999-01-04) has no live sleeve. I re-ran the row post hoc with that one NaN day dropped (not a gate, so the verdict is unchanged).
- **Prediction scorecard:**
  - CONFIRMED: right.
  - H2 Sharpe 0.8-1.2 (1.11): right.
  - ≥ 11/13 equity ETFs positive (13/13): right.
  - TLT and GLD < 0.3: **wrong**. They came in at 0.47 and 0.41, and the TLT+GLD sub-book reached 0.60. IBS is not only an equity-index effect in this sample.
  - Correlation with H201's book 0.5-0.75: **wrong**. It was 0.88, so this is mostly the same bet and not a diversifier.
- What it means: H195's rule generalises across 15 new instruments without any tuning. That makes "fitted to SPY" a much weaker explanation. It does NOT add a second independent edge (corr 0.88). It joins the confirmed IBS family as H208.

## H209. IBS on SPY, entries only when VIX is above its 1-year median: NOT CONFIRMED (2026-10-10)
Registered c6d59bc; runner 96b4a49; one run; `results/h209_results.json`.

| Gate | Result | |
|---|---|---|
| 1 both halves > 0.5 | 0.840 / 0.790 | PASS |
| 2 holdout bootstrap lower bound > 0 | 0.355 | PASS |
| 3 > bar (N = 196) | 0.790 vs 0.792 | **FAIL (by 0.002)** |
| 4 vs SPY | 0.790 vs 0.785; DD 17.4% vs 33.7% | PASS |
| 5 stress 5 bp | 0.723 / 0.672, lower bound 0.240 | PASS |

- Trades 614 vs H195's 987, exposure 22%. H195 run with the same code: H2 Sharpe 0.93. The filter costs about 0.14 of Sharpe by cutting trades. The bar is the bar; no rounding.
- **Diagnostic (H195's own 987 trades split by regime on the entry day):**

| Regime | n | Mean per trade | Win rate | Vol-normalised mean |
|---|---:|---:|---:|---:|
| HIGH VIX | 553 | 0.55% | 70.5% | 0.319 |
| LOW VIX | 434 | 0.22% | 67.1% | 0.191 |
| HIGH − LOW | | +0.34% [0.12%, 0.55%] | | |

- Prediction scorecard:
  - HIGH mean > LOW with the CI excluding 0: right.
  - Vol-normalised means within 30%: **wrong**. HIGH is 67% higher, so high-VIX trades are better even per unit of risk.
  - Strategy NOT CONFIRMED, H2 within ±0.2 of 0.93, failing G3 or G4: right.
- What it means: dropping the low-VIX trades loses more from trade count than it gains from quality. Sizing UP in high VIX, instead of filtering out low VIX, is the obvious next variant. That would be a NEW ID with its own N; it is not run here.

## H210. IBS on SPY with VIX-regime sizing (1.5x high / 0.5x low): NOT AN IMPROVEMENT (2026-10-10)
Registered 759ed92; runner e3962b8 (committed before results); one run; `results/h210_results.json`.

| Gate | Result | |
|---|---|---|
| 1 both halves > 0.5 | 0.789 / 0.835 | PASS |
| 2 holdout bootstrap lower bound > 0 | 0.388 | PASS |
| 3 > bar (N = 197) | 0.835 > 0.792 | PASS |
| 4 vs SPY (DD ≤ 0.6x) | DD 26.5% vs 33.7% (0.79x) | **FAIL** |
| 5 stress 5 bp | 0.657 / 0.695, lower bound 0.242 | PASS |
| Improvement: H2 ≥ H195's 0.932 + 0.10 | 0.835 | **FAIL** (0.10 *worse*) |

- Exposure is about the same as H195 (0.39 vs 0.38), so this is a pure reallocation of risk. The full-sample max drawdown is 37.0% vs H195's 26.1% (same code). The top year is 2020 (14%), and dropping it does not flip the sign.
- Prediction scorecard: right on all five calls (gates 1/2/5 pass, H2 in 0.80-0.95, worse DD, G4 fails, NOT AN IMPROVEMENT).
- **The assumption behind the prediction was wrong:** median VIX on HIGH entries was 21.9 vs 16.3 on LOW, a ratio of 1.34, not "about double". With 1.34, the mean/variance-optimal HIGH:LOW weight is about (0.319/0.191)/1.34 ≈ 1.25:1. That is a mild tilt; 3:1 is far too much. The direction of the conclusion holds: heavy VIX sizing hurts. A 1.25:1 tilt would gain very little and would be a new ID chosen after seeing this, so it is NOT registered.
- Status: the VIX-conditioning line is closed (H209 filter and H210 sizing both lose to plain H195). Keep H195 at equal notional.
