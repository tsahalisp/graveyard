# Hypothesis pre-registration ledger

Rule: an entry must be complete BEFORE the first backtest of the idea runs.
No goalpost moves after data. Template:

## H<N>. <name> (registered YYYY-MM-DD, PRE-DATA)
- Claim: <what is mispriced and why>
- Who's on the other side: <who is supplying the edge and why they persist>
- Expected effect size: <rough magnitude>
- Test: <exact procedure, universe, dates, costs>
- Verdict gate: <pass/fail rule, set in advance>
- Kill rule in live/paper: <when to stop>

---

## H1. Cross-sectional momentum 12-1 (registered 2026-07-03, PRE-DATA)
- Claim: stocks that beat their peers over the past 12 months (skipping the
  most recent month) keep beating them over the next month. (Jegadeesh &
  Titman 1993 — the most replicated equity anomaly.)
- Who's on the other side: underreaction — investors anchor on old prices and
  absorb news slowly; the disposition effect makes them sell winners too early
  and hold losers too long. They persist because it's psychology, not error.
- Expected effect size: academic long-short is ~6-10%/yr gross on broad
  universes, but momentum is KNOWN to be weakest in megacaps — on our 89
  large caps, expect 0-6%/yr net. A weak positive is the realistic win.
- Test (exact, no deviations):
  - Universe: the 89 config equities. Survivorship-biased (documented) —
    long-short netting reduces but does not remove the bias, so any verdict
    is CONDITIONAL on later point-in-time re-test.
  - Signal on rebalance day t: total adj return from t-252 to t-21.
    Eligibility: 252 prior trading days of data.
  - Portfolio: rank eligible names; long top 18 at +1/36 each, short bottom
    18 at -1/36 each (dollar-neutral, gross exposure = 1). Rebalance every
    21 trading days. Weights held (ffill) between rebalances.
  - Costs: 10 bps per unit turnover, via engine.py.
  - Split: TRAIN = through 2018-12-31, HOLDOUT = 2019-01-01 on. Declared now.
- Verdict gate (set in advance): CONFIRMED only if net annualized long-short
  return > 0 AND net Sharpe > 0.30 in BOTH halves. Anything else = NOT
  CONFIRMED -> graveyard with autopsy.
- Kill rule if it ever trades paper: stop if rolling 12-month net < -10%.

## H2. Short-term cross-sectional reversal (registered 2026-07-03, PRE-DATA)
- Claim: last week's relative losers bounce, winners fade, over the next week
  (Lehmann 1990 / Jegadeesh 1990). Liquidity provision in disguise: you get
  paid for absorbing short-term order-flow pressure.
- Who's on the other side: impatient traders demanding immediacy — funds
  forced to sell today, chasers buying green candles. They persist because
  urgency is structural.
- Expected effect size + PREDICTED FAILURE MODE: gross ann +2-8% is plausible
  even on megacaps, BUT weekly full-book rotation means enormous turnover;
  at 10 bps we predict costs eat most or all of it. Registering this
  prediction explicitly: gross > 0, net likely fails the gate. The point of
  the test is to measure the cost wall precisely.
- Test (exact): universe = 89 config equities; signal at rebalance day t =
  total adj return t-5 -> t; eligibility 60 prior trading days; long bottom
  18 at +1/36, short top 18 at -1/36; rebalance every 5 trading days;
  costs 10 bps via engine.py; TRAIN <= 2018-12-31, HOLDOUT >= 2019-01-01.
  Report BOTH gross and net.
- Verdict gate (same deployment bar as H1): NET ann > 0 AND NET sharpe > 0.30
  in both halves.
- Kill rule if it ever trades paper: rolling 6-month net < -8%.

## H3. Crypto cross-sectional momentum (registered 2026-07-03, PRE-DATA)
- Claim: among crypto majors, past-90d winners (skipping last 7d) outperform
  losers over the following weeks. Rationale: crypto is retail-dominated,
  narrative-driven, no index-rebalancing arbitrage — the underreaction that
  weakened in megacap equities should be stronger here.
- Who's on the other side: retail chasing last week's pump (hence the 7d skip)
  and bagholders averaging down losers.
- Expected effect: literature suggests crypto momentum exists but is noisy;
  net +0-15%/yr long-short plausible. HONESTY CLAUSE: only 13 assets in
  firm.db (survivors, majors) — quintiles impossible; we run 4-long/4-short.
  Thin cross-section = wide error bars = this test is UNDERPOWERED by
  construction and any verdict is weak evidence either way.
- Test (exact): universe = 13 CRYPTO symbols (UNI-USD excluded); signal at
  rebalance day t = adj return t-90 -> t-7 (calendar days, 365-day series);
  eligibility 90 prior days; long top 4 at +1/8, short bottom 4 at -1/8;
  rebalance every 7 days; costs 20 bps per unit turnover (crypto spreads);
  periods=365 for annualization. TRAIN <= 2021-12-31, HOLDOUT >= 2022-01-01
  (puts one full bear cycle in holdout, declared now).
- Verdict gate: net ann > 0 AND net sharpe > 0.30 in BOTH halves.
- Kill rule if papered: rolling 6-month net < -15% (crypto vol tolerance).

## H4. Crypto momentum, POWERED universe (registered 2026-07-03, PRE-DATA)
- Claim: same mechanism as H3 (retail underreaction/chasing in crypto), which
  H3 could not fairly test with 13 survivor-majors. H4 is the powered re-test,
  NOT a rescue of H3 — different universe, new registration, H3 stays buried.
- Universe: 13 majors + ~54 Kraken top-volume USD pairs (fetched
  programmatically 2026-07-03; fiat/stables removed; whatever fails fetch or
  the quality gate is excluded and listed). Survivorship: current listings
  only — documented; verdict is conditional on that as with all crypto tests.
- Test (exact): signal = adj return t-90 -> t-7; eligibility 90 prior days;
  long top 12 at +1/24, short bottom 12 at -1/24; rebalance every 7 days;
  skip rebalances with < 24 eligible names; costs 20 bps; periods=365.
  Split: TRAIN <= 2024-12-31 (contains the 2022 bear), HOLDOUT >= 2025-01-01
  (~18 months). Declared before running.
- Verdict gate: net ann > 0 AND net sharpe > 0.30 in BOTH halves.
- Kill rule if papered: rolling 6-month net < -15%.

## H5. Book-player skill persistence (registered 2026-07-03, DATA CLOCK RUNNING)
- Claim: in Peter's book (WagerLocks), player weekly results persist —
  trailing winners keep winning, trailing losers keep losing (skill and tilt
  are stable traits at recreational scale). PROPRIETARY data: nobody else
  observes these specific players.
- Uses: (a) book management — limit/adjust terms for persistent winners;
  (b) signal — persistent winners' sides may be tail-worthy (needs bet-level
  data, a later phase).
- Data status: capture began 2026-07-03 — Doros now persists per-player
  weekly nets to data/wagerlocks_history.json (idempotent per week; week 6/8
  backfilled from cache, 12 players). TEST REQUIRES >= 15 weeks — earliest
  verdict ~mid-October 2026. No peeking before then.
- Test (exact, set now): rank players by trailing-8-week net at each week t;
  top-third vs bottom-third mean next-week net difference > 0 with t-stat > 2
  across >= 15 evaluation weeks.
- The firm's first patience trade. It cannot be rushed.

## H6. Time-series trend on megacaps (6m) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on equity; params `{'lookback': 126, 'reb': 21}` (id ccd8678a7).
- Mechanism: Hold each name long/short by the SIGN of its own 6-month return. Trend persistence from slow information diffusion — distinct from H1's cross-sectional rank.
- Counterparty (why it persists): Mean-reverters and calendar rebalancers fading the trend.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 126, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=49 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H7. Risk-parity 12-1 momentum on megacaps (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 252, 'reb': 21}` (id ca4158a42).
- Mechanism: Same momentum edge as H1 but each leg sized by inverse vol so a few wild names don't own the risk — cleaner Sharpe if the edge is real.
- Counterparty (why it persists): Same as momentum; retail selling winners early.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 252, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=58 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H8. Low-volatility anomaly on megacaps (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on equity; params `{'vol_lb': 126, 'reb': 21}` (id c7bf45bf4).
- Mechanism: Long low-vol / short high-vol. Leverage-constrained investors overpay for high-beta 'lottery' names, so low-vol earns more per unit risk.
- Counterparty (why it persists): Leverage-constrained funds bidding up high-beta.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 126, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=67 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H9. Time-series trend on crypto majors (3m, weekly) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 90, 'reb': 7}` (id c1fad9915).
- Mechanism: Crypto trends are strong, retail-driven, and weakly arbitraged; hold by sign of 90d return, weekly rebalance.
- Counterparty (why it persists): HODLers ignoring trend + forced liquidations paying the move.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 90, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=76 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H10. Risk-parity momentum on crypto majors (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 90, 'reb': 7}` (id cec97e270).
- Mechanism: Cross-sectional 3m momentum in crypto, inverse-vol sized — H3/H4 died equal-weight; risk-parity is a genuinely different risk profile.
- Counterparty (why it persists): Same as crypto momentum.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 90, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=85 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H11. Short-horizon reversal on crypto majors (5d) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 5, 'reb': 5}` (id ca0387fef).
- Mechanism: Crypto overreacts on 3-5 day horizons; buy recent losers, short recent winners (liquidity provision). H2 was equity — crypto is a fresh test.
- Counterparty (why it persists): Momentum chasers and liquidations paying the spread.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 5, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=91 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H12. Low-volatility tilt on crypto majors (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 90, 'reb': 7}` (id cbb47fa44).
- Mechanism: Even in crypto, the calmest majors may earn better risk-adjusted returns than the lottery tokens (same leverage-constraint mechanism).
- Counterparty (why it persists): Lottery-seeking retail overpaying for high-vol tokens.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 90, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=100 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H13. Fast cross-sectional momentum on crypto (63d) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 63, 'skip': 5, 'reb': 7}` (id ccb29e799).
- Mechanism: H3/H4 tested SLOW (252d) momentum and buried it. Fast 3-month momentum is a distinct horizon where crypto's retail flow is strongest.
- Counterparty (why it persists): Slow rebalancers and retail late to rotations.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 63, 'skip': 5, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=109 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H14. Fast time-series trend on megacaps (3m) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on equity; params `{'lookback': 63, 'reb': 10}` (id ce66a062b).
- Mechanism: Shorter-horizon trend (3m) captures faster regime shifts than the 6m version; sign-based, biweekly.
- Counterparty (why it persists): Reversal traders and rebalancers.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 63, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=118 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H15. Overnight 1-day reversal megacaps (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 1, 'reb': 1, 'n_side': 10}` (id c31c14167).
- Mechanism: Single-day price impact from large institutional order flow creates a measurable overshoot that reverts the next session; microstructure friction prevents HFT from fully arbitraging at daily-bar resolution
- Counterparty (why it persists): Index rebalancers and passive ETF creations/redemptions who must transact at close regardless of price; larger quants skip this because capacity is tiny and turnover is extreme
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 1, 'reb': 1, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=122 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H16. Long-horizon 12-1 momentum with 1-month skip equity (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 252, 'skip': 21, 'reb': 21, 'n_side': 15}` (id c88823183).
- Mechanism: Annual return window captures analyst-revision and earnings-surprise drift over multiple quarters; skipping last month avoids the well-documented short-term reversal that contaminated H1 (which used tighter skip); fundamentally driven by slow information diffusion into price
- Counterparty (why it persists): Value managers who fade multi-year winners as 'expensive'; they accept momentum losses as residual tracking error against benchmarks
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 252, 'skip': 21, 'reb': 21, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=131 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H17. Crypto 1-month XS momentum weekly rebal (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 30, 'skip': 2, 'reb': 5, 'n_side': 8}` (id c15deb81b).
- Mechanism: Retail attention cycles in crypto operate on ~30-day horizons driven by social media narratives; cross-sectional winner persistence at this frequency reflects herding and attention rotation rather than fundamental revisions
- Counterparty (why it persists): Crypto market makers who delta-hedge inventory and create transient price pressure; larger quants avoid due to fragmented liquidity and custody/regulatory friction
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 30, 'skip': 2, 'reb': 5, 'n_side': 8}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=140 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H18. 2-day crypto cross-sectional reversal (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 2, 'reb': 2, 'n_side': 10}` (id cf51ed6f9).
- Mechanism: 2-day window captures weekend/holiday illiquidity-driven dislocations and leveraged-long liquidation cascades unique to 24/7 crypto markets; mean reversion is faster than equity due to absence of after-hours vs open gap structure
- Counterparty (why it persists): Momentum chasers and levered perp traders who amplify short-term moves; larger firms skip due to execution complexity on fragmented CEX/DEX venues at daily bar granularity
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 2, 'reb': 2, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=146 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H19. Funding carry: long crowded-short crypto (7d) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `funding_carry` on crypto; params `{'lookback': 7, 'reb': 1, 'n_side': 4, 'direction': -1}` (id c8f911d4f).
- Mechanism: Perpetual funding as positioning. Persistently NEGATIVE funding = crowded shorts paying to stay short; those names are squeeze / mean-reversion candidates. Long the most-negative-funding majors, short the most-positive. NEW DATA: Binance funding, exchange-true.
- Counterparty (why it persists): Retail shorts paying funding to hold bearish bets; basis-trade arbitrageurs are capacity-constrained by exchange collateral + withdrawal friction.
- Test (set BEFORE data): factors.funding_carry(px, **{'lookback': 7, 'reb': 1, 'n_side': 4, 'direction': -1}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=152 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H20. Funding carry: long crowded-long crypto (7d) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `funding_carry` on crypto; params `{'lookback': 7, 'reb': 1, 'n_side': 4, 'direction': 1}` (id cc30f27a1).
- Mechanism: The opposite sign, pre-registered so the GATE — not us — picks the direction: long the highest-funding (crowded-long / carry) names, short the lowest. Symmetric registration avoids sign-picking bias.
- Counterparty (why it persists): Same market, opposite crowd; retail longs overpaying funding for directional exposure.
- Test (set BEFORE data): factors.funding_carry(px, **{'lookback': 7, 'reb': 1, 'n_side': 4, 'direction': 1}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=158 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H21. Time-series funding: long each crowded-short name (14d) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `funding_ts` on crypto; params `{'lookback': 14, 'reb': 1, 'n_side': 4, 'direction': -1}` (id cd0d2b29d).
- Mechanism: Per-asset positioning (NOT cross-sectional): hold each crypto long when its OWN funding is persistently negative (crowded shorts, squeeze risk), short when positive. A distinct mechanism from the ranked funding_carry — catches single-name squeezes the cross-section averages away.
- Counterparty (why it persists): Retail shorts paying funding on individual names; capacity-constrained per name.
- Test (set BEFORE data): factors.funding_ts(px, **{'lookback': 14, 'reb': 1, 'n_side': 4, 'direction': -1}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=164 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H22. Equity 1-day micro-reversal (tight universe) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 1, 'reb': 1, 'n_side': 15}` (id c811dabc6).
- Mechanism: Intraday liquidity provision by market makers creates transient price impact that mean-reverts within one session; narrowing to 15 names per side concentrates on the most liquid megacaps where bid-ask bounce is fastest and institutional order flow is most predictable
- Counterparty (why it persists): Retail momentum chasers and algorithmic trend-followers who push prices beyond fundamental value intraday; large HFTs avoid daily-bar signals as too slow, leaving the edge to slower systematic traders
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 1, 'reb': 1, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=168 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H23. Equity 1-month XS momentum (monthly horizon) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 21, 'skip': 1, 'reb': 5, 'n_side': 20}` (id c43ae172c).
- Mechanism: One-month momentum captures earnings-revision and analyst-upgrade cycles that are distinct from the 12-1 intermediate horizon; institutions digest quarterly guidance over 3-5 weeks creating persistent buying of recent winners at a timescale too short for annual rebalancers but too long for HFTs
- Counterparty (why it persists): Contrarian value funds rebalancing monthly who systematically buy laggards; large quants avoid this horizon as it sits in the reversal-to-momentum transition zone making it noisy for large AUM
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 21, 'skip': 1, 'reb': 5, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=177 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H24. Crypto 6-month XS momentum (long horizon) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 180, 'skip': 7, 'reb': 7, 'n_side': 10}` (id c28496924).
- Mechanism: Six-month horizon in crypto captures full adoption/narrative cycles (DeFi, L2, AI tokens) as retail capital rotates into established outperformers; distinct from the buried 90-day and 30-day signals by spanning multiple narrative arcs rather than a single hype wave
- Counterparty (why it persists): Crypto index rebalancers and passive holders who sell winners to maintain weights; venture-style crypto funds with lockups cannot exploit daily-rebalanced signals at this horizon
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 180, 'skip': 7, 'reb': 7, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=186 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H25. Equity annual time-series trend (monthly rebal) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on equity; params `{'lookback': 252, 'reb': 21}` (id c4e88167c).
- Mechanism: Each megacap's own 252-day sign captures long-duration macro regime shifts (rate cycles, sector rotations) that are orthogonal to cross-sectional ranking; monthly rebalancing reduces turnover and 10bps cost drag while maintaining exposure to multi-month trending behavior documented in managed-futures literature
- Counterparty (why it persists): Quarterly pension rebalancers who mechanically sell equity when prices rise; insurance companies with liability-driven mandates that reduce equity on strength, providing persistent trending fuel
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 252, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=195 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H26. Crypto 2-week reversal (weekly rebal) (registered 2026-07-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 14, 'reb': 7, 'n_side': 8}` (id c76753d90).
- Mechanism: Two-week horizon in crypto captures post-listing and post-airdrop hype exhaustion where tokens rally on narrative then revert as retail exits; weekly rebalancing avoids the noise of daily crypto reversals (H18 buried) while remaining faster than the monthly horizon; 8 names per side concentrates on the most liquid majors with tightest spreads
- Counterparty (why it persists): Retail crypto momentum traders chasing 2-week breakouts; centralized exchange market makers widen spreads on volatile smaller names, leaving this niche to systematic players willing to hold a week
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 14, 'reb': 7, 'n_side': 8}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=204 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H28. Crypto 2-week XS reversal weekly rebal (registered 2026-07-13, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 10, 'reb': 5, 'n_side': 15}` (id c3da4abed).
- Mechanism: Retail-driven momentum chasing in crypto overshoots on 10-day horizons; market makers widen spreads post-spike creating temporary mispricings that revert. Distinct from buried 2-day (H18) and 10-14 day (H26 was 14d monthly rebal) configs — this uses 10d lookback with weekly rebal.
- Counterparty (why it persists): Retail momentum traders and leveraged long/short participants who chase 2-week moves; crypto perp arbitrageurs focused on basis rather than spot cross-section.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 10, 'reb': 5, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=222 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H29. Crypto 6-month time-series trend monthly rebal (registered 2026-07-13, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 126, 'reb': 21}` (id c7222e79d).
- Mechanism: Long-horizon (6-month) time-series trend in crypto captures macro regime persistence (bull/bear cycles in BTC/ETH ecosystems) with monthly rebal reducing noise and costs. Distinct from buried 3-month (H9 weekly) and 12-month (H25 was equity); crypto 6m TS untested.
- Counterparty (why it persists): Crypto venture funds and spot holders who ignore trend signals; DeFi yield farmers indifferent to directional momentum on monthly horizons.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 126, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=231 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H30. Crypto 90-5 vol-scaled momentum biweekly rebal (registered 2026-07-13, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 90, 'skip': 5, 'reb': 10}` (id c22338f25).
- Mechanism: Vol-scaling dampens crypto's fat-tailed return distribution, making the momentum signal cleaner by normalizing position sizes across assets with wildly different realized vols (BTC vs. small-cap alts). 90-day lookback with 5-day skip captures intermediate trend; biweekly rebal balances responsiveness vs. costs. All prior crypto momentum configs were either unscaled or different horizons.
- Counterparty (why it persists): Discretionary crypto traders who size positions by conviction not vol; retail who oversize volatile alts and undersize stable ones.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 90, 'skip': 5, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=240 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H31. Equity annual vol-scaled momentum monthly rebal (registered 2026-07-13, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 252, 'skip': 21, 'reb': 21}` (id c9ff6050d).
- Mechanism: Classic 12-1 momentum (H1) failed without vol-scaling; vol-scaling the same signal forces risk-parity sizing across megacaps with very different beta/vol profiles (e.g., NVDA vs. BRK), potentially recovering the edge obscured by return dispersion. H7 buried risk-parity momentum but used different params/family; this uses mom_volscaled which explicitly scales by inverse realized vol rather than equal-risk weighting.
- Counterparty (why it persists): Large index funds constrained to cap-weight; factor investors running unscaled momentum who create overcrowding at the signal level rather than the risk level.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 252, 'skip': 21, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=249 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H32. Equity 3-day XS reversal semi-weekly rebal (registered 2026-07-14, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 3, 'reb': 3, 'n_side': 20}` (id c82d05d43).
- Mechanism: 3-day horizon captures institutional order-flow mean-reversion distinct from 1-day microstructure and 5-day already tested; semi-weekly rebalance reduces turnover vs daily while still harvesting short-horizon price pressure from ETF arbitrage flows and block trades in megacaps
- Counterparty (why it persists): Passive index rebalancers and ETF creation/redemption desks who create transient price pressure; larger stat-arb firms focus on sub-daily or monthly horizons making 3-day daily-close signals less crowded
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 3, 'reb': 3, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=258 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H33. Equity 6-month XS momentum weekly rebal tighter book (registered 2026-07-14, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 126, 'skip': 5, 'reb': 5, 'n_side': 15}` (id c469b7adc).
- Mechanism: 6-month lookback with 1-week skip targets an intermediate momentum horizon distinct from the buried 12-1 annual and 1-month signals; tighter 15-name book concentrates in highest-conviction names reducing noise; 6m window captures earnings-cycle-length price trends without reverting to the annual mean-reversion zone
- Counterparty (why it persists): Retail momentum chasers who use annual rankings; institutional managers constrained to monthly rebalance miss the intermediate horizon; 10bps costs manageable at weekly rebal with only 15 names per side
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 126, 'skip': 5, 'reb': 5, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=267 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H34. Crypto 1-month time-series trend weekly rebal (registered 2026-07-14, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 20, 'reb': 5}` (id cc684678c).
- Mechanism: 20-day own-sign trend captures the medium-frequency momentum cycle in crypto driven by retail herding and leveraged perp funding feedback loops; distinct from buried 63-day (H9) and 126-day (H29) crypto TS trend; 20-day horizon aligns with typical retail attention cycles and exchange-driven liquidation cascades
- Counterparty (why it persists): Market makers who flatten exposure daily cannot hold 20-day directional bets; risk-parity funds that rebalance monthly miss this horizon; retail who buys dips after sustained drawdowns provides the opposing flow
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 20, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=276 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H35. Equity 6m vol-scaled momentum monthly rebal (registered 2026-07-14, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 126, 'skip': 5, 'reb': 21}` (id c615016f6).
- Mechanism: Inverse-vol sizing on 6-month momentum specifically addresses the low-vol anomaly interaction: high-momentum megacaps are often high-vol (NVDA-type names), vol-scaling reweights toward steadier compounders; 6m horizon is distinct from buried annual (H31) and provides a cleaner signal in the intermediate trend zone; monthly rebal keeps costs contained
- Counterparty (why it persists): Benchmark-constrained fund managers who cannot underweight high-vol high-momentum names due to index weight pressures; vol-targeting overlay funds that scale entire books rather than cross-sectionally
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 126, 'skip': 5, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=285 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H36. Crypto 1-month XS momentum 2-day skip weekly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 30, 'skip': 2, 'reb': 5, 'n_side': 10}` (id c4f57b2a4).
- Mechanism: One-month cross-sectional momentum with a 2-day microstructure skip captures genuine trend-following alpha in crypto without contamination from bid-ask bounce; the 2-day skip is meaningfully different from the 5-day and 7-day skips tested previously and targets the regime where retail FOMO persists but short-term reversal has dissipated.
- Counterparty (why it persists): Retail participants chasing recent winners late; professional market-makers who hedge directionally but don't run cross-sectional books across 10 names at weekly frequency.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 30, 'skip': 2, 'reb': 5, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=294 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H37. Crypto 9-month time-series trend monthly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 180, 'reb': 21}` (id c68c41d23).
- Mechanism: 9-month lookback sits between the buried 6-month and the known underperformance of very long horizons; crypto macro cycles (halving-driven bull/bear regimes) have dominant frequencies near 6-12 months, and 9 months may better capture the mid-cycle continuation phase while monthly rebalancing keeps turnover low relative to crypto volatility.
- Counterparty (why it persists): Discretionary crypto funds with quarterly mandates that are slow to rotate; retail holders anchoring to cost basis rather than trend.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 180, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=303 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H38. Crypto 60d vol-scaled momentum biweekly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 60, 'skip': 3, 'reb': 10}` (id c1008db62).
- Mechanism: 60-day vol-scaled momentum with 3-day skip and biweekly rebalancing targets the 2-3 month trend horizon that is structurally distinct from the 90-day (buried H30) and 1-month (buried H34) configurations; inverse-vol sizing dampens the impact of high-vol altcoin blowups while preserving trend signal, and biweekly rebal reduces excessive turnover vs weekly.
- Counterparty (why it persists): Unlevered HODLers and volatility-blind trend followers who size positions equally regardless of risk; larger quants focus on perps/derivatives rather than spot cross-sectional.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 60, 'skip': 3, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=312 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H39. Crypto 2-week XS reversal 12-side weekly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 10, 'reb': 5, 'n_side': 12}` (id cdc3d2667).
- Mechanism: 10-day lookback (distinct from the 5-day H11 and 14-day H26/H28 already buried) targets a window where liquidation cascades and forced deleveraging fully unwind; 12 names per side vs 10 expands the book to reduce idiosyncratic risk. The 10-day horizon is the approximate half-life of funding-driven price dislocations in crypto.
- Counterparty (why it persists): Leveraged long-biased retail traders stopped out at cycle lows; perpetual futures arbitrageurs who close hedges after funding normalizes, creating reverting price pressure in spot.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 10, 'reb': 5, 'n_side': 12}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=321 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H40. Crypto 30-2 XS momentum tri-daily rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 30, 'skip': 2, 'reb': 3, 'n_side': 10}` (id c759ffd7d).
- Mechanism: One-month relative strength in crypto reflects retail herding and exchange-listing effects on a compressed time scale; skipping 2 days avoids bid-ask microstructure noise while 3-day rebalancing captures the fast decay of this signal before reversal sets in — a horizon untested among buried configs (all were 5d, 7d, 14d, 21d skip or lookback).
- Counterparty (why it persists): Retail trend-followers and yield farmers rotating into hot tokens; institutional desks avoid 3-day crypto rebal due to custody/settlement friction and compliance overhead.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 30, 'skip': 2, 'reb': 3, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=330 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H41. Crypto short-window low-vol bi-weekly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 30, 'reb': 10}` (id cdaa6087b).
- Mechanism: The 12-month low-vol anomaly (H12) failed, but in crypto volatility regimes shift rapidly; a 30-day realized vol window with 10-day rebalancing tracks recent vol clustering (GARCH-like persistence) rather than slow structural risk — a distinct mechanism from annual risk sorting. Low-vol names in crypto often have deeper liquidity and institutional backing, reducing crash risk.
- Counterparty (why it persists): Retail speculators seeking lottery-like payoffs in high-vol altcoins; they systematically overpay for volatility, leaving low-vol names underpriced on a risk-adjusted basis.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 30, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=339 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H42. Equity 3-week XS reversal weekly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 15, 'reb': 5, 'n_side': 15}` (id c52786e3d).
- Mechanism: Intermediate-horizon (3-week) price dislocations in megacaps driven by institutional rebalancing flows and ETF creation/redemption pressure; mean-reversion at 3 weeks captures the unwinding of these flows after settlement cycles complete, distinct from 1-5 day micro-reversal (buried) and momentum horizons.
- Counterparty (why it persists): Passive ETF rebalancers and index-fund flows that create persistent but temporary price pressure; large stat-arb desks avoid this window because the signal-to-noise at 3 weeks is too weak for their capital base.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 15, 'reb': 5, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=348 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H43. Equity 9-month XS momentum 2-week skip weekly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 180, 'skip': 10, 'reb': 5, 'n_side': 15}` (id c3e0d3f15).
- Mechanism: 9-month lookback (roughly 180 days) with a 10-day skip targets the momentum sweet spot between the buried 6-month and 12-month regimes; analyst coverage revisions and earnings estimate drift sustain relative price trends over this window. The 2-week skip avoids microstructure reversal contamination without the full 21-day skip that may discard valid signal.
- Counterparty (why it persists): Sell-side momentum strategies typically run monthly with 12-1 standard parameters; the 9-month non-standard window is systematically under-mined by institutional products, leaving room for a nimble single-account trader.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 180, 'skip': 10, 'reb': 5, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=357 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H44. Crypto 45-day time-series trend weekly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 45, 'reb': 5}` (id c2b9d528c).
- Mechanism: 45-day (roughly 2-month) own-sign trend in crypto sits between the buried 1-month (21d) and 3-month (63d) and 6-month regimes; crypto narratives (protocol upgrades, halving cycle sentiment) evolve over 6-8 week windows. Time-series (long-only directional) sidesteps cross-sectional crowding while capturing regime persistence.
- Counterparty (why it persists): Retail trend-followers use round-number lookbacks (30, 60, 90 days); systematic CTA desks require longer horizons for adequate t-stat. The 45-day non-standard window occupies an uncrowded niche.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 45, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=366 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H45. Crypto 6-month vol-scaled momentum biweekly rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 120, 'skip': 5, 'reb': 10}` (id c3c1d86e8).
- Mechanism: Vol-scaling (risk-parity weighting) on a 120-day momentum signal with 5-day skip and biweekly rebalance — distinct from buried H30 (90d, 5skip, 10reb) and H38 (60d). At 120 days, crypto assets exhibit regime-persistent momentum tied to macro liquidity cycles; vol-scaling corrects for the extreme cross-sectional vol dispersion between BTC/ETH and alt-coins, improving signal quality.
- Counterparty (why it persists): Unscaled momentum dominates retail and small-fund crypto strategies; vol-scaled versions require daily vol estimation infrastructure that most participants lack. Larger quant funds skip crypto due to custody/regulatory friction.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 120, 'skip': 5, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=375 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H46. Crypto 3-day XS reversal tri-daily rebal (registered 2026-08-05, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 3, 'reb': 3, 'n_side': 10}` (id c2670286e).
- Mechanism: 3-day cross-sectional reversal on crypto with tri-daily rebalance (every 3 trading days) targets liquidity-driven overshoots from leveraged liquidation cascades; distinct from buried 2-day (H18, daily rebal), 5-day (H11), and 14-day (H26/H28) regimes. The 3-day window aligns with typical margin-call settlement and re-entry cycles in perpetual futures markets.
- Counterparty (why it persists): Liquidation-driven moves punish undercapitalized leveraged traders who cannot hold through the reversal window; market makers widen spreads during cascades, making this trade unattractive for high-frequency shops but viable at daily-bar execution.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 3, 'reb': 3, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=384 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H47. Equity 20d XS momentum 5d skip daily rebal (registered 2026-08-22, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 20, 'skip': 5, 'reb': 5, 'n_side': 15}` (id cc9a59bec).
- Mechanism: Fast mean-reversion window (20d) with skip to avoid microstructure; daily rebal captures intraweek volatility spikes in mega-cap rotation.
- Counterparty (why it persists): Statistical arbitrage firms with higher slippage costs or daily rebalance friction.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 20, 'skip': 5, 'reb': 5, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=393 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H48. Crypto 2-week time-series trend 2-day rebal (registered 2026-08-22, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 14, 'reb': 2}` (id c139dc3b5).
- Mechanism: Ultra-short TS trend on crypto with aggressive (2-day) rebal captures momentum continuation in intraweek cycles; crypto volatility regime favors faster mean-reversion than equity.
- Counterparty (why it persists): Discretionary macro traders; execution costs of 2-day rebal exceed value for most institutions.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 14, 'reb': 2}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=402 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H49. Equity 60d vol-scaled momentum 10d skip 10d rebal (registered 2026-08-22, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 60, 'skip': 10, 'reb': 10}` (id cf9b29455).
- Mechanism: Medium-horizon vol-scaled momentum avoids drawdowns by reducing position size in high-vol regimes; 10d rebal balances gamma bleed vs. execution.
- Counterparty (why it persists): Equal-weight momentum traders or those ignoring volatility expansion in crowded regimes.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 60, 'skip': 10, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=411 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H50. Crypto 1-week XS reversal 3-day rebal 20-side (registered 2026-08-22, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 7, 'reb': 3, 'n_side': 20}` (id c5af6b48b).
- Mechanism: Crypto exhibits stronger intraweek mean reversion than equity due to leverage/liquidation cascades; 7d window captures tactical overshoots missed by longer-horizon strategies.
- Counterparty (why it persists): Leveraged traders forced to unwind; institutions with weekly-or-longer rebal cycles.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 7, 'reb': 3, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=420 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H51. Crypto 20d low-vol tilt 10-day rebal (registered 2026-08-22, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 20, 'reb': 10}` (id cc15d6a61).
- Mechanism: Crypto low-vol anomaly stronger than equity due to retail concentration in high-beta names; 10d rebal captures regime shifts faster than monthly.
- Counterparty (why it persists): Narrative-driven retail capital and leverage-seeking smart money; larger firms don't scale this efficiently.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 20, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=429 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H52. Equity 2-week XS reversal weekly rebal (registered 2026-08-24, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 10, 'reb': 5, 'n_side': 15}` (id c03f80d2d).
- Mechanism: 10-day losers in large-cap equities attract mean-reversion buying as options market makers delta-hedge and short-sellers cover; distinct from 3-day and 5-day horizons already buried because it captures the full weekly liquidity cycle rather than noise-level microstructure
- Counterparty (why it persists): Trend-following CTAs and momentum ETFs that hold losing positions into weekly rebalance; large systematic shops skip this because the alpha decays inside typical execution windows for >$10B AUM
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 10, 'reb': 5, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=438 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H53. Equity 12-1 XS momentum monthly rebal wider book (registered 2026-08-24, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 252, 'skip': 21, 'reb': 21, 'n_side': 20}` (id c4ea22d0d).
- Mechanism: Standard 12-1 momentum with n_side=20 rather than the default tighter book; wider cross-section reduces idiosyncratic risk and may reveal the aggregate factor premium obscured by concentration in the buried H1/H16 tests; monthly rebalance cuts costs on a slower-moving signal
- Counterparty (why it persists): Index investors forced to sell recent losers during rebalances and buy winners; large quants avoid wider books because of market-impact at scale
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 252, 'skip': 21, 'reb': 21, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=447 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H54. Equity 3-month low-vol monthly rebal (registered 2026-08-24, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on equity; params `{'vol_lb': 63, 'reb': 21}` (id cdc3426c9).
- Mechanism: Distinct from 12-month low-vol (H8 buried): 3-month realized vol is more responsive to regime changes and captures the lottery-preference premium among megacaps that have recently gone through earnings-driven vol spikes; monthly rebal avoids over-trading a slow signal
- Counterparty (why it persists): Options sellers who push up implied vol on recent movers, creating a mismatch between realized and implied that low-vol longs exploit; large risk-parity funds use annualized vol estimates and ignore the 3-month window
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 63, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=456 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H55. H55. Equity 40d XS momentum 3d skip 5d rebal tight 15-side (registered 2026-08-26, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 40, 'skip': 3, 'reb': 5, 'n_side': 15}` (id c077fa3a8).
- Mechanism: Micro-cap regime momentum: 40-day window captures institutional lag on medium-liquidity megacaps; 3-day skip removes micro-reversal noise; 5-day rebal captures regime persistence without overfitting; tight 15-side reduces sector concentration vs. prior 20+ side attempts.
- Counterparty (why it persists): Stat-arb funds anchored on 60d+ windows; they miss faster regime shifts at 40d horizon and larger position sizes inflate their transaction costs.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 40, 'skip': 3, 'reb': 5, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=465 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H56. H56. Crypto 14-day time-series trend 3-day rebal (registered 2026-08-26, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 14, 'reb': 3}` (id ce214dc49).
- Mechanism: Ultra-short carry regime: crypto majors exhibit 2-week micro-trends driven by funding-rate cycles and leverage unwinding, distinct from longer-horizon mean reversion. 3-day rebal captures regime shifts faster than weekly/biweekly attempts (H34, H44, H48).
- Counterparty (why it persists): Macro hedge funds and TradFi entering crypto on weekly+ rebalance schedules; they miss intra-week volatility clustering.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 14, 'reb': 3}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=474 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H57. H57. Equity 90d vol-scaled momentum 2d skip 15d rebal (registered 2026-08-26, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 90, 'skip': 2, 'reb': 15}` (id c369dc4a4).
- Mechanism: Mega-cap regime: 90-day window + vol scaling removes noise on low-vol mega-caps (AAPL, MSFT, NVDA); 2-day skip avoids execution friction; 15-day rebal (not monthly, not daily) aligns with mega-cap trading desk rebalance cycles. Distinct from H31 (monthly, 6m) and H49 (daily, 10d skip).
- Counterparty (why it persists): Passive index trackers and long-only mega-cap allocators; they ignore vol-adjusted momentum and over-weight on strength regardless of volatility regime.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 90, 'skip': 2, 'reb': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=483 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H58. H58. Crypto 4-day XS reversal 2-day rebal 15-side (registered 2026-08-26, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 4, 'reb': 2, 'n_side': 15}` (id c50c500ad).
- Mechanism: Micro-reversal on crypto: 4-day window captures intra-week liquidation cascades on leverage; tighter 15-side (vs. 20-side H50) reduces concentration; 2-day rebal avoids weekend vol spike. Distinct from H50 (20-side, 3-day) and H18/H26 (longer horizons).
- Counterparty (why it persists): Algorithmic liquidation bots that front-run known leverage levels; retail leverage traders who don't track intra-day regime shifts.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 4, 'reb': 2, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=489 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H59. H59. Crypto 30d low-vol 7-day rebal (registered 2026-08-26, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 30, 'reb': 7}` (id cb3e23237).
- Mechanism: Vol-regime stability: 30-day rolling vol captures regime shifts faster than longer windows; crypto has fat tails but 7-day rebal (not daily, not weekly) lets winners run while avoiding regime overhang. Distinct from H41 (biweekly, unspecified window) and H12 (longer horizon).
- Counterparty (why it persists): Volatility-seeking traders and derivative hedge funds; they profit from realized vol exceeding implied, so they leave low-vol assets unhedged.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 30, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=498 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H60. Equity 6m XS momentum 5d skip bi-weekly rebal (registered 2026-08-26, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 126, 'skip': 5, 'reb': 10, 'n_side': 10}` (id caaff1393).
- Mechanism: Standard 6-month cross-sectional momentum with 5-day skip and bi-weekly (10-day) rebalancing — H33 tested weekly rebal with tighter book; bi-weekly reduces turnover and transaction costs, potentially allowing the signal to survive the 10bps cost hurdle that killed weekly variants.
- Counterparty (why it persists): Index-rebalancing funds and mean-reversion desks operating at weekly frequency; bi-weekly rebal is too slow for HFT and too fast for monthly funds, leaving a gap.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 126, 'skip': 5, 'reb': 10, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=507 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H61. Crypto 90d low-vol monthly rebal (registered 2026-08-26, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 90, 'reb': 21}` (id c65871648).
- Mechanism: Shorter windows (20d) and different rebal frequencies were buried (H41, H51); 90-day volatility estimation is more stable, better capturing persistent structural differences in crypto asset volatility regimes (BTC/ETH as anchors vs. speculative altcoins). Monthly rebal reduces costs vs. bi-weekly.
- Counterparty (why it persists): Retail speculators who concentrate in high-vol altcoins seeking lottery-like payoffs; institutional crypto funds tend to be benchmark-aware rather than explicitly low-vol tilted.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 90, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=516 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H62. Equity 2-week XS reversal 20-side weekly rebal (registered 2026-08-27, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 10, 'reb': 5, 'n_side': 20}` (id c916c8cd9).
- Mechanism: 10-day price pressure from institutional rebalancing and index flows reverses at weekly horizon; 20-side book captures more of the cross-section than tighter books that were buried
- Counterparty (why it persists): Momentum-chasing retail and ETF flow followers who push prices away from fair value over 2-week windows; large stat-arb desks avoid this horizon as turnover is too high for their AUM
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 10, 'reb': 5, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=525 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H63. Crypto 6-month time-series trend bi-weekly rebal (registered 2026-08-27, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 120, 'reb': 10}` (id cbe4a88d4).
- Mechanism: Distinct from buried 90d and 180d ts_momentum on crypto: 120-day window captures a regime transition horizon where trend-following CTA-style capital builds positions; bi-weekly rebal reduces noise vs monthly while limiting costs vs weekly
- Counterparty (why it persists): Mean-reversion traders and hodlers who fade trends; large trend-followers avoid crypto due to custody/regulatory constraints leaving the edge partially unexploited
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 120, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=534 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H64. Equity 40d vol-scaled momentum 5d skip bi-weekly rebal (registered 2026-08-27, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 40, 'skip': 5, 'reb': 10}` (id cbaa188b5).
- Mechanism: Vol-scaling over a 40-day window with 5-day skip isolates intermediate-horizon risk-adjusted trend; distinct from buried 60d/90d/20d variants — this window sits between short-term noise and long-horizon crowding, and vol-scaling removes beta from the signal
- Counterparty (why it persists): Unscaled momentum traders who are forced to cut on vol spikes; crowded quant funds that operate at 12-1 horizon and get caught in reversals
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 40, 'skip': 5, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=543 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H65. Crypto 21d XS momentum 3d skip weekly rebal tight book (registered 2026-08-27, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 21, 'skip': 3, 'reb': 5, 'n_side': 8}` (id c84de170b).
- Mechanism: 1-month momentum in crypto with 3-day skip avoids the well-documented 1-3 day reversal in crypto, targeting the sustained directional drift from liquidity cascades and narrative momentum; tight 8-side book focuses on the most liquid names where execution is feasible
- Counterparty (why it persists): Retail investors chasing recent narratives who buy tops and sell bottoms; institutional desks avoid due to small notional capacity and reputational risk
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 21, 'skip': 3, 'reb': 5, 'n_side': 8}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=552 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H66. Equity 60d low-vol monthly rebal (registered 2026-08-27, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on equity; params `{'vol_lb': 60, 'reb': 21}` (id ce5214919).
- Mechanism: 60-day vol window is shorter than the buried 3-month and annual variants, capturing more recent vol regime shifts; monthly rebal aligns with institutional risk-budget cycles; low-vol premium persists due to leverage-constrained investors bidding up safe assets
- Counterparty (why it persists): Benchmark-constrained managers forced to hold high-vol names to track indices; retail investors with lottery preferences who overpay for high-vol names
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 60, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=561 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H67. Equity 40d XS momentum 7d skip 20d rebal 20-side (registered 2026-08-29, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 40, 'skip': 7, 'reb': 20, 'n_side': 20}` (id cfff3480e).
- Mechanism: Intermediate momentum window (40d) with meaningful skip (7d) isolates persistent cross-sectional strength from transient noise. 20-side concentration on megacaps captures conviction without over-trading. 20d rebal balances decay without whipsaws.
- Counterparty (why it persists): Mean-reversion traders and short-term volatility arbitrage desks who scalp reversals; they fade extended momentum.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 40, 'skip': 7, 'reb': 20, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=570 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H68. Crypto 21d time-series trend 5-day rebal (registered 2026-08-29, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 21, 'reb': 5}` (id c3788953c).
- Mechanism: Crypto exhibits persistent own-asset directional bias over 3-week horizons due to retail/leverage momentum cascades and low institutional anchor. 5-day rebal frequency captures regime persistence without fading into choppy reversals that kill longer holds.
- Counterparty (why it persists): Large crypto desks and hedge funds that systematically liquidate extended positions or enforce daily/weekly portfolio rebalancing constraints.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 21, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=579 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H69. Equity 120d vol-scaled momentum 10d skip 30d rebal (registered 2026-08-29, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 120, 'skip': 10, 'reb': 30}` (id cd39570eb).
- Mechanism: Risk-adjusted momentum using 120-day window avoids the noise of shorter horizons. 10d skip removes microstructure and short-term reversals. Vol-scaling reduces drawdowns in high-volatility regimes and concentrates capital on stable trends.
- Counterparty (why it persists): Naive momentum followers who ignore volatility expansion; they get destroyed in crisis drawdowns. Risk-parity desks that rebalance equally.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 120, 'skip': 10, 'reb': 30}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=588 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H70. Crypto 45-day low-vol 14-day rebal (registered 2026-08-29, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 45, 'reb': 14}` (id cd42dacce).
- Mechanism: Crypto low-vol anomaly emerges over medium-term horizons (6-8 weeks). 45-day window captures regime persistence without degrading to daily noise. 14-day rebal balances capture of rolling volatility shifts without over-trading.
- Counterparty (why it persists): Systematic risk-parity and volatility arbitrage desks that short realized vol or trade vol term-structure; they suppress low-vol outperformance.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 45, 'reb': 14}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=597 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H71. Equity 1-year XS momentum 1-month skip quarterly rebal wide (registered 2026-08-31, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 252, 'skip': 21, 'reb': 63, 'n_side': 25}` (id c226b3038).
- Mechanism: Very long-lookback momentum captures multi-month institutional trends; 1-month skip avoids microstructure noise. Quarterly rebal reduces transaction drag on megacaps while maintaining signal freshness. 25-side book lets position sizing match equity-universe liquidity.
- Counterparty (why it persists): Mean-reversion traders & short-term CTAs who fade extended rallies; weak hands who sell into continuation.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 252, 'skip': 21, 'reb': 63, 'n_side': 25}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=606 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H72. Crypto 10-day time-series trend daily rebal (registered 2026-08-31, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 10, 'reb': 1}` (id c70f14109).
- Mechanism: Crypto exhibits strong intra-month auto-correlation from retail & leveraged flow; 10-day horizon is short enough to ride post-shock reversals but long enough to filter daily noise. Daily rebal captures momentum decay within a single week without overshooting.
- Counterparty (why it persists): Liquidation cascades & margin calls that create false momentum signals; stat-arb algos that scalp micro-reversals.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 10, 'reb': 1}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=612 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H73. Equity 20-day low-vol bi-weekly rebal (registered 2026-08-31, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on equity; params `{'vol_lb': 20, 'reb': 21}` (id c1ba1525a).
- Mechanism: Short vol lookback (20d) captures recent realized volatility, which predicts next 2-week vol regime better than annual vol for megacaps. Bi-weekly rebal is operational sweet spot: low enough to catch vol-regime flips, high enough to avoid daily noise.
- Counterparty (why it persists): Volatility sellers (variance swaps, vol ETN managers) who are long realized vol; vol-targeting funds forced to rebalance into high-vol names.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 20, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=621 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H74. Crypto 45-day vol-scaled momentum 3-day skip weekly rebal (registered 2026-08-31, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 45, 'skip': 3, 'reb': 7}` (id cb8175209).
- Mechanism: Crypto momentum is strong but extremely path-dependent; inverse-vol scaling dampens crashes caused by black-swan volatility spikes. 45d lookback (8-9 weeks) is sweet spot: long enough to capture alt-season flows, short enough to avoid regime changes. 3-day skip filters liquidation noise; 7-day rebal aligns with options expiry cycles.
- Counterparty (why it persists): Volatility explosions that void momentum (margin calls); leverage-liquidation cascades that gap through stops.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 45, 'skip': 3, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=630 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H75. Equity 10-day XS reversal weekly rebal 10-side (registered 2026-09-02, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 10, 'reb': 5, 'n_side': 10}` (id c74e5e85f).
- Mechanism: Liquidity-provision premium: 10-day window captures institutional flow overshoot that fully mean-reverts within a week; tighter 10-side book avoids the most illiquid names where costs dominate. Distinct from all buried configs by combining mid-range lookback with a tighter book.
- Counterparty (why it persists): Momentum-chasing retail and ETF rebalancers who push prices past fair value over 2 weeks; large quants avoid because signal decays before they can scale positions cost-effectively.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 10, 'reb': 5, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=639 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H76. Crypto 6-month TS trend monthly rebal (registered 2026-09-02, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 180, 'reb': 30}` (id c560e3a03).
- Mechanism: Six-month own-sign trend on crypto captures medium-term adoption and narrative cycles (DeFi, Layer-2 waves) where assets trend in isolation independent of cross-sectional rank. Monthly rebal reduces noise vs bi-weekly. Distinct from H29/H63 which used xsec_momentum or bi-weekly reb.
- Counterparty (why it persists): Short-term crypto traders who fade multi-month moves expecting mean reversion; large TradFi quants avoid crypto TS trend due to regulatory/custody constraints.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 180, 'reb': 30}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=648 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H77. Equity 60d XS momentum 2d skip 10d rebal (registered 2026-09-02, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 60, 'skip': 2, 'reb': 10, 'n_side': 20}` (id c26f1453e).
- Mechanism: Three-month cross-sectional momentum with minimal skip (2d) and bi-weekly rebalancing targets the intermediate-horizon price leadership that reflects analyst estimate revisions and fund flow persistence, at a rebal cadence distinct from all buried equity XS momentum configs.
- Counterparty (why it persists): Contrarian value funds that fade 3-month winners; large momentum quants use 12-1 or 6-1 lookbacks, leaving the 3-month window under-crowded.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 60, 'skip': 2, 'reb': 10, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=657 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H78. Crypto 30d vol-scaled momentum 1d skip weekly rebal (registered 2026-09-02, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 30, 'skip': 1, 'reb': 5}` (id cd2b0686e).
- Mechanism: Vol-scaling a 30-day crypto signal normalises for regime-dependent volatility explosions (exchange hacks, liquidation cascades), isolating genuine directional information. 1-day skip avoids microstructure noise. No buried config used lookback=30 with skip=1 for mom_volscaled on crypto.
- Counterparty (why it persists): Unscaled momentum traders who get blown out by vol spikes and then capitulate, creating the return after vol normalisation; large firms avoid raw crypto vol due to margin requirements.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 30, 'skip': 1, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=666 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H79. Crypto 10-day XS reversal 5d rebal 10-side tight book (registered 2026-09-02, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 10, 'reb': 5, 'n_side': 10}` (id cb79984dc).
- Mechanism: 10-day reversal on a tight 10-name book in crypto targets the over-extension of narrative-driven pumps in major tokens; tight book concentrates in names with genuine liquidity and known reversal patterns. All buried crypto reversal configs used 1-5 day lookbacks, 2-3 day rebal, or wider books.
- Counterparty (why it persists): Retail narrative traders who chase token pumps for 1-2 weeks before institutional arbitrageurs close the gap; large market-makers already flat by day 10 so they are not providing the reversion capital.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 10, 'reb': 5, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=675 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H80. Equity 7d XS reversal 3d rebal 15-side (registered 2026-09-03, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 7, 'reb': 3, 'n_side': 15}` (id c656998e4).
- Mechanism: Weekly institutional rebalancing and retail momentum-chasing create 7-day overshoots in large-cap equities; mean reversion is harvested on a 3-day cycle before next rebalancing window obscures signal. Distinct from buried 2d/5d/10d/14d/21d lookbacks.
- Counterparty (why it persists): Retail trend-followers and weekly index rebalancers who overshoot; large quants avoid sub-10-day equity reversal due to capacity constraints and execution complexity at scale.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 7, 'reb': 3, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=684 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H81. Crypto 6-month TS trend biweekly rebal (registered 2026-09-03, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 180, 'reb': 14}` (id cbd9af2b9).
- Mechanism: 6-month own-sign time-series trend on crypto captures macro crypto cycle phases (risk-on/risk-off regimes) at a horizon where retail FOMO and institutional allocation flows persist. Biweekly rebal balances turnover vs. signal decay. Distinct from buried monthly-rebal 6m TS (H76) by tighter rebalancing frequency.
- Counterparty (why it persists): Retail investors buying/selling at cycle peaks and troughs; larger quants avoid due to high crypto volatility making TS positions uncomfortable to hold at scale without intraday hedging infrastructure.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 180, 'reb': 14}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=693 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H82. Equity 30d vol-scaled momentum 1d skip weekly rebal (registered 2026-09-03, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 30, 'skip': 1, 'reb': 5}` (id c08372032).
- Mechanism: 30-day vol-scaled momentum captures intermediate-term price trends while normalizing for individual stock volatility regimes. 1-day skip avoids microstructure reversal. This horizon sits between the failed 20d and 40d/60d buried variants, and weekly rebal is distinct from buried biweekly/monthly configs at similar lookbacks.
- Counterparty (why it persists): Risk-parity unwinds and vol-targeting funds that mechanically reduce exposure during high-vol periods, creating momentum in low-vol survivors; larger firms skip this horizon as too short for their AUM.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 30, 'skip': 1, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=702 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H83. Crypto 2-week XS momentum 1d skip weekly rebal tight (registered 2026-09-03, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 14, 'skip': 1, 'reb': 5, 'n_side': 10}` (id c9049bc56).
- Mechanism: 14-day cross-sectional momentum in crypto reflects short narrative cycles (protocol upgrades, regulatory news) where winning tokens continue outperforming losers for 1-2 additional weeks. 1-day skip removes overnight reversal noise. Distinct from buried 21d-skip-3d, 30d-skip-2d, and 14d reversal variants.
- Counterparty (why it persists): Retail crypto traders rotating into recent losers hoping for mean reversion; crypto-native market makers who are delta-neutral and cannot absorb directional momentum flow efficiently.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 14, 'skip': 1, 'reb': 5, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=711 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H84. Crypto 60d low-vol monthly rebal (registered 2026-09-03, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 60, 'reb': 21}` (id ccbf11824).
- Mechanism: 60-day volatility lookback in crypto identifies structurally lower-beta assets (stablecoins excluded, but coins with genuine lower vol relative to universe) that benefit from institutional preference for 'safer' crypto allocations and less forced liquidation during drawdowns. Monthly rebal reduces turnover. Distinct from buried 20d-10d-rebal, 30d-7d-rebal, 45d-14d-rebal, 90d-monthly configs.
- Counterparty (why it persists): Retail speculators who prefer high-vol lottery-ticket cryptos; leverage-seeking traders who systematically overpay for high-vol assets and create a low-vol premium.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 60, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=720 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H85. Equity 4d XS reversal 2d rebal 20-side (registered 2026-09-04, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 4, 'reb': 2, 'n_side': 20}` (id c76a97b5a).
- Mechanism: Intraweek institutional order flow creates 4-day price pressure in mega-caps; reversal occurs as liquidity providers unwind. 4-day window avoids the 5-day and 7-day burial zones, 2-day rebal captures mean reversion before next pressure cycle.
- Counterparty (why it persists): Momentum-following retail and passive front-runners who push prices transiently; larger quants avoid sub-week horizons in equity due to capacity constraints relative to AUM.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 4, 'reb': 2, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=726 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H86. Crypto 120d XS momentum 5d skip bi-weekly rebal tight (registered 2026-09-04, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 120, 'skip': 5, 'reb': 14, 'n_side': 10}` (id c64698b4f).
- Mechanism: 4-month cross-sectional momentum in crypto captures retail-driven trend following and narrative cycles (Layer-1 vs DeFi rotation). Skip-5 avoids reversal contamination. Bi-weekly rebal balances turnover vs signal decay at this horizon.
- Counterparty (why it persists): Crypto retail holders anchored to single narratives; institutional desks focus on shorter horizons or BTC/ETH only, leaving altcoin relative strength less arbitraged.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 120, 'skip': 5, 'reb': 14, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=735 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H87. Equity 12m vol-scaled momentum 1m skip quarterly rebal (registered 2026-09-04, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 252, 'skip': 21, 'reb': 63}` (id c8123d10b).
- Mechanism: Annual momentum scaled by realized vol at quarterly rebalance differs from buried monthly variants: lower turnover means less cost drag on slow-moving vol-adjusted signals. Vol-scaling corrects for beta dispersion among megacaps across sectors.
- Counterparty (why it persists): Index rebalancers and passive funds that add to winners mechanically without vol-weighting; fundamental managers who fade momentum on valuation.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 252, 'skip': 21, 'reb': 63}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=744 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H88. Equity 6m XS momentum 5d skip monthly rebal wide book (registered 2026-09-04, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 180, 'skip': 5, 'reb': 21, 'n_side': 25}` (id ce17cc42d).
- Mechanism: 6-month relative strength at monthly rebalance with wider 25-side book spreads risk across more names, reducing idiosyncratic blow-ups. 5-day skip avoids reversal. Monthly rebal not tested at this combination vs buried weekly/bi-weekly 6m variants.
- Counterparty (why it persists): Sector-rotation ETF investors who rotate on quarterly themes; fundamental analysts who underreact to sustained 6-month price signals.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 180, 'skip': 5, 'reb': 21, 'n_side': 25}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=753 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H89. Crypto 6m XS momentum 10d skip monthly rebal tight (registered 2026-09-06, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 180, 'skip': 10, 'reb': 21, 'n_side': 10}` (id c3bd641de).
- Mechanism: Long-horizon cross-sectional momentum in crypto captures structural adoption cycles and narrative persistence; 10-day skip avoids short-term reversal contamination; monthly rebal reduces costs on volatile names.
- Counterparty (why it persists): Contrarian crypto traders fading winners as 'overbought'; institutional desks avoiding illiquid alts leave the edge uncrowded at this horizon.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 180, 'skip': 10, 'reb': 21, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=762 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H90. Equity annual TS trend quarterly rebal (registered 2026-09-06, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on equity; params `{'lookback': 252, 'reb': 63}` (id c87aabeca).
- Mechanism: Annual own-sign trend on megacaps captures secular earnings growth regimes and sector rotation; quarterly rebalancing keeps costs low relative to the slow-moving signal.
- Counterparty (why it persists): Value investors who short expensive winners; their systematic fade creates the persistent underreaction exploited here.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 252, 'reb': 63}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=771 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H91. Crypto 10d low-vol ultra-fast rebal (registered 2026-09-06, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 10, 'reb': 3}` (id ce9f7168d).
- Mechanism: Very short-window volatility ranking in crypto reacts to regime shifts within the week; low-vol names after a market spike are safer stores of value for forced sellers, creating a transient defensive premium not yet tested at this speed.
- Counterparty (why it persists): Momentum traders piling into high-vol winners post-spike; risk desks forced to sell low-vol positions for margin cover.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 10, 'reb': 3}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=780 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H92. Crypto 90d vol-scaled momentum 7d skip biweekly rebal (registered 2026-09-06, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 90, 'skip': 7, 'reb': 14}` (id c542f243c).
- Mechanism: 90-day vol-adjusted signal on crypto balances medium-term trend with risk normalization; 7-day skip avoids micro-reversal; biweekly rebal is a distinct cadence from all prior buried configs (prior tests used 1d or 3d skip, not 7d).
- Counterparty (why it persists): Unlevered buy-and-hold crypto allocators who ignore position sizing; smaller quant shops lack the infrastructure to scale vol-adjusted books across 52 names.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 90, 'skip': 7, 'reb': 14}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=789 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H93. Equity 90d XS momentum 20d skip 5d rebal 25-side (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 90, 'skip': 20, 'reb': 5, 'n_side': 25}` (id c81153498).
- Mechanism: Intermediate-horizon cross-sectional strength with meaningful skip to avoid microstructure bounce; 25-side book captures momentum without over-concentration. 5d rebal cycle balances turnover vs. decay.
- Counterparty (why it persists): Mean-reversion traders and systematic rebalancers who supply liquidity at momentum extremes; large passive inflows also push prices too far.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 90, 'skip': 20, 'reb': 5, 'n_side': 25}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=798 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H94. Crypto 60d time-series trend 3-day rebal (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 60, 'reb': 3}` (id cbcfb50b7).
- Mechanism: Time-series momentum on crypto with ultra-frequent rebalancing captures trend persistence within crypto's high-intraday volatility. 60-day window balances signal strength and regime changes.
- Counterparty (why it persists): Trend-following quants and CTAs who herd into same signals; crypto liquidity providers who step in front during large momentum moves.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 60, 'reb': 3}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=807 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H95. Crypto 15d low-vol tilt 5-day rebal (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 15, 'reb': 5}` (id c2ada98c9).
- Mechanism: Short lookback volatility on crypto captures mean-reversion in realized vol spikes; crypto vol clustering is extreme. 5-day rebal exploits temporary vol decompression windows.
- Counterparty (why it persists): Short-vol sellers and volatility arb shops who receive premium from vol spike; retail panic-selling into vol spikes.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 15, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=816 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H96. Equity 8-day XS reversal 2-day rebal 30-side (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 8, 'reb': 2, 'n_side': 30}` (id c77e83fd2).
- Mechanism: Slightly longer reversal window than H32 (3-day), but with faster rebalancing and wider book. Captures order-flow microstructure and temporary crowding in mid-cap momentum without fighting mega-cap staleness.
- Counterparty (why it persists): Momentum ignition traders and short-term flow-chasers who exhaust liquidity; index traders causing temporary dislocations.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 8, 'reb': 2, 'n_side': 30}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=825 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H97. Equity 75d vol-scaled momentum 15d skip weekly rebal (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 75, 'skip': 15, 'reb': 7}` (id cc93ba0b7).
- Mechanism: Mid-range lookback with vol normalization reduces whipsaw in mega-cap momentum; skip avoids short-term reversal shock. Weekly rebal keeps turnover controlled while capturing duration-adjusted momentum.
- Counterparty (why it persists): Risk parity funds and vol-targeting CTAs who reduce size into vol spikes; liquidity providers collecting vol risk premium.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 75, 'skip': 15, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=834 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H98. Crypto 1M Time-Series Trend 7D Rebal (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 30, 'reb': 7}` (id ced85b791).
- Mechanism: Crypto intramonth trends often persist more strongly than cross-sectional; 30-day lookback captures price momentum within a single regime shift; 7-day rebalance balances signal freshness vs. transaction friction in lower-liquidity names.
- Counterparty (why it persists): Crypto traders stuck in mean-reversion strategies; momentum-chasing retail forced to liquidate during drawdowns.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 30, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=843 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H99. Equity 3M Low-Vol Tilt 20D Rebal (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on equity; params `{'vol_lb': 90, 'reb': 20}` (id ca13e32f9).
- Mechanism: 90-day realized vol window captures medium-term regime; 20-day rebalance is tight enough to adapt to vol clustering without incurring daily churn; low-vol anomaly is structurally weak in equity but 20d rebal may reveal time-varying seasonal edge (q-end, earnings cycles).
- Counterparty (why it persists): Volatility sellers forced into hedging; risk-parity funds crowded in same low-vol names.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 90, 'reb': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=852 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H100. Crypto 60D Vol-Scaled Momentum 3D Skip 5D Rebal (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 60, 'skip': 3, 'reb': 5}` (id c6808af8d).
- Mechanism: 60-day window + 3-day skip captures post-spike vol crush reversions specific to crypto's microstructure; vol-scaling improves Sharpe by reducing position size in drawdown scenarios; 5-day rebal is aggressive but realistic for crypto 24/7 markets and accommodates rapid regime shifts.
- Counterparty (why it persists): Leverage-constrained funds stuck in fixed positions; vol-scaled mechanics penalize crowded trades at precise moment of unwinding.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 60, 'skip': 3, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=861 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H101. Equity 5D XS Reversal 2D Rebal 30-side (registered 2026-09-08, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 5, 'reb': 2, 'n_side': 30}` (id c3e59c227).
- Mechanism: 5-day lookback on 89-stock universe captures cross-sectional mean reversion around macro events and earnings surprises (not intra-day); 2-day rebal is ultra-responsive to overnight gap fills and sector rotation; 30-side ensures deep enough book to avoid overfitting while staying tighter than buried H52 (which had weekly).
- Counterparty (why it persists): Momentum chasers forced to unwind after failed breakouts; gap-fill algos that systematically reverse sharp 5d moves.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 5, 'reb': 2, 'n_side': 30}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=867 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H102. H102: Equity 1Y XS momentum 1M skip quarterly rebal ultra-wide (registered 2026-09-11, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 252, 'skip': 21, 'reb': 63, 'n_side': 30}` (id c02c148cb).
- Mechanism: Ultra-wide cross-section (30-side) on 1Y momentum with 1M skip captures slow institutional rotation and reduces microstructure noise. Quarterly rebalance frequency aligns with earnings seasons and fund rebalancing cycles.
- Counterparty (why it persists): Mean-reversion traders and overconfident momentum chasers who front-run the quarterly turn; larger funds avoid 30-side positioning due to execution friction.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 252, 'skip': 21, 'reb': 63, 'n_side': 30}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=876 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H103. H103: Crypto 6-day XS reversal daily rebal ultra-wide (registered 2026-09-11, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 6, 'reb': 1, 'n_side': 25}` (id c808aaf39).
- Mechanism: Crypto's retail-driven mispricings over ~1 week often reverse sharply. Daily rebalance captures mean-reversion with minimal lag. Ultra-wide 25-side book exploits cross-asset dispersion where smaller-cap majors spike disproportionately on short-term sentiment swings.
- Counterparty (why it persists): Retail FOMO-driven momentum traders and algorithmic momentum chasers; larger funds avoid daily 25-side turnover due to execution costs and market impact.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 6, 'reb': 1, 'n_side': 25}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=882 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H104. H104: Equity 6M vol-scaled momentum 10D skip monthly rebal tight (registered 2026-09-11, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 180, 'skip': 10, 'reb': 30}` (id c8ddde7bd).
- Mechanism: 6-month lookback captures mid-term institutional flows; vol-scaling mitigates large drawdowns from high-vol names and improves risk-adjusted returns. 10-day skip avoids short-term reversals. 30-day rebalance is administratively efficient and reduces trading friction vs. tighter schedules.
- Counterparty (why it persists): Volatility shock traders and unscaled trend-followers who get whipsawed on vol spikes; larger quants avoid tighter intra-month rebalancing due to operational overhead.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 180, 'skip': 10, 'reb': 30}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=891 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H105. H105: Crypto 4-month time-series trend biweekly rebal (registered 2026-09-11, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 120, 'reb': 14}` (id c48be83fb).
- Mechanism: 4-month time-series trend (120 days) captures crypto regime persistence without over-fitting to micro-reversals. Biweekly rebalance balances capturing true trend shifts vs. chasing noise. Crypto's structural volatility and event-driven cycles (network upgrades, regulatory news) often persist over 2-4 month horizons.
- Counterparty (why it persists): Mean-reversion specialists who expect faster reversals; larger funds constrained by position limits and liquidity on size in spot/futures markets.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 120, 'reb': 14}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=900 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H106. H106: Crypto 45-day low-vol tilt 3-week rebal (registered 2026-09-11, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 45, 'reb': 21}` (id ce1885f28).
- Mechanism: Crypto major names exhibit strong low-vol premium (BTC, ETH tend to outperform on volatility dips). 45-day vol window balances regime sensitivity vs. stale estimates. 3-week rebalance captures vol regime shifts without excessive churn. Contrasts with failed shorter horizons due to vol spikes being transient.
- Counterparty (why it persists): Vol-targeting funds and leverage traders who deleverage into low-vol regimes; systematic sellers of vol spikes who flatten positions into calm periods.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 45, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=909 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H107. H107: Equity 15d XS reversal 10d rebal 20-side (registered 2026-09-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 15, 'reb': 10, 'n_side': 20}` (id cd14eeaef).
- Mechanism: 3-week horizon captures mean-reversion after institutional rebalancing flows and index-driven overshoot; 10-day rebal reduces turnover vs daily/3d tested variants while staying within reversion window
- Counterparty (why it persists): Passive index funds and momentum chasers who push prices beyond fair value over 2-3 week windows; large quants skip because AUM makes 20-stock books too small
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 15, 'reb': 10, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=918 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H108. H109: Crypto 45d XS momentum 5d skip 10d rebal 8-side (registered 2026-09-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 45, 'skip': 5, 'reb': 10, 'n_side': 8}` (id c9a4c010a).
- Mechanism: 45-day window with 5-day skip avoids short-term reversal contamination while capturing medium-term relative strength from narrative and liquidity rotation across crypto sectors; 8-side tighter than most tested variants
- Counterparty (why it persists): Retail traders chasing short-term pumps; institutional crypto desks lack systematic XS infrastructure at this horizon
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 45, 'skip': 5, 'reb': 10, 'n_side': 8}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=927 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H109. H110: Equity 9m vol-scaled momentum 1m skip monthly rebal (registered 2026-09-12, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 180, 'skip': 21, 'reb': 21}` (id c542bb29d).
- Mechanism: 9-month lookback with 1-month skip and monthly rebal sits between the 6m and 12m windows already buried but at a distinct horizon; vol-scaling normalizes signal across high/low vol regimes common in megacaps post-2020
- Counterparty (why it persists): Fundamental long-only managers with fixed rebal schedules who cannot dynamically size by volatility; risk-parity funds focus on longer horizons
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 180, 'skip': 21, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=936 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H110. H111: Crypto 7d XS reversal 3d rebal 10-side (registered 2026-09-12, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 7, 'reb': 3, 'n_side': 10}` (id c4dbebc05).
- Mechanism: Weekly overreaction in crypto driven by weekend retail sentiment spikes and liquidation cascades creates predictable mean-reversion; 10-side tighter than H39/H50 tested variants to focus signal on most extreme movers
- Counterparty (why it persists): Retail momentum chasers and leveraged long traders who get liquidated at extremes; crypto market makers don't hold directional positions
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 7, 'reb': 3, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=945 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H111. Equity 6d XS reversal 3d rebal 25-side (registered 2026-09-14, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 6, 'reb': 3, 'n_side': 25}` (id ce10d7f33).
- Mechanism: Institutional order-flow over a 6-day window creates transient price pressure in megacaps that partially reverts; 3-day rebal captures mean reversion before momentum reasserts. Distinct from buried 5d/7d/8d/10d/15d attempts by combining 6d lookback with wider 25-side book.
- Counterparty (why it persists): Retail momentum chasers and passive index rebalancers who create short-term overshooting; larger HFTs focus on intraday, leaving daily-bar reversal to smaller shops.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 6, 'reb': 3, 'n_side': 25}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=954 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H112. Crypto 180d XS momentum 14d skip biweekly rebal 8-side (registered 2026-09-14, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 180, 'skip': 14, 'reb': 14, 'n_side': 8}` (id c25921407).
- Mechanism: 6-month relative strength with a 2-week skip to avoid short-term reversal contamination; biweekly rebal balances cost and signal freshness. 180d lookback is distinct from buried 90d, 120d, 63d, 21d, 30d attempts; 14d skip and 8-side book not previously combined.
- Counterparty (why it persists): Crypto retail allocators who chase recent 1-4 week performance rather than 6-month relative strength; institutional crypto desks avoid concentrated 8-name books due to tracking error constraints.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 180, 'skip': 14, 'reb': 14, 'n_side': 8}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=963 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H113. Equity 45d vol-scaled momentum 2d skip weekly rebal (registered 2026-09-14, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 45, 'skip': 2, 'reb': 7}` (id c353f50c7).
- Mechanism: 45-day vol-scaled momentum sits between the buried 30d and 60d lookbacks; inverse-vol sizing reduces drawdown in high-vol megacaps. 2d skip avoids microstructure noise. Weekly rebal is distinct from bi-weekly/monthly used in nearby buried hypotheses at different lookbacks.
- Counterparty (why it persists): Benchmark-constrained active managers who cannot easily run vol-neutral books; risk-parity funds operate at longer horizons leaving this window open.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 45, 'skip': 2, 'reb': 7}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=972 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H114. Equity 20d XS momentum 2d skip weekly rebal 20-side (registered 2026-09-14, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 20, 'skip': 2, 'reb': 5, 'n_side': 20}` (id cd7352cdb).
- Mechanism: 1-month cross-sectional momentum with 2-day skip targets the intermediate horizon where earnings revision cycles and institutional accumulation create persistent relative-strength signals. 20-side wider book vs buried H47 (20d/5d skip/daily rebal) and distinct reb/skip combination.
- Counterparty (why it persists): Weekly rebalancing mutual funds that create predictable price pressure; stat-arb desks focus on shorter intraday signals leaving this daily-bar window.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 20, 'skip': 2, 'reb': 5, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=981 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H115. Crypto ultra-short 3-day time-series trend daily rebal (registered 2026-09-16, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 3, 'reb': 1}` (id c0bb110bf).
- Mechanism: Crypto shows mean-reversion at 2–5d horizons in literature (small sample bias); testing 3-day own-asset sign persistence captures intra-week volatility clustering before liquidity dries up. Daily rebal captures micro-regime changes faster than prior tests.
- Counterparty (why it persists): Market makers hedging directional crypto exposure; intraday noise traders who reverse fast
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 3, 'reb': 1}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=987 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H116. Crypto ultra-short 5d low-vol tilt tri-daily rebal (registered 2026-09-16, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on crypto; params `{'vol_lb': 5, 'reb': 3}` (id c51dd5c34).
- Mechanism: Crypto volatility is mean-reverting at 5–10d windows; low-vol anomaly is opposite in crypto vs equity (high-vol crash recovery). Tri-daily rebalance (3 trading days) catches short-window vol clusters before intra-week correlations spike.
- Counterparty (why it persists): Leverage-constrained spot traders seeking stable assets; vol-targeting funds that buy crashed low-vol after spikes
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 5, 'reb': 3}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=993 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H117. Equity 3M vol-scaled momentum 5d skip 10d rebal (registered 2026-09-16, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 90, 'skip': 5, 'reb': 10}` (id c7a078372).
- Mechanism: Momentum sized by inverse vol avoids regime crashes better than raw momentum; 3-month lookback + 5-day skip + 10-day rebal creates a sweet spot between noise suppression and macro regime capture on megacaps
- Counterparty (why it persists): Risk-parity funds that trim winners in high-vol regimes; quant funds with longer rebal cycles miss intra-month reversals
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 90, 'skip': 5, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1002 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H118. Crypto 1-day XS reversal daily rebal ultra-wide (registered 2026-09-16, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 1, 'reb': 1, 'n_side': 25}` (id cd148cf2a).
- Mechanism: Crypto shows overnight/intraday liquidation cascades that reverse within 24h; wider 25-side book captures full tail of losers/gainers. Daily rebal prevents stale rankings during volatile crypto sessions.
- Counterparty (why it persists): Leverage liquidators and panic sellers; long-only retail that cannot short
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 1, 'reb': 1, 'n_side': 25}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1006 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H119. Equity 20d XS reversal 10d rebal 15-side (registered 2026-09-17, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 20, 'reb': 10, 'n_side': 15}` (id ca4894e16).
- Mechanism: Month-end institutional window-dressing and tax-loss harvesting create predictable mean-reversion at the 1-month horizon in large-cap equities; distinct from shorter windows already buried
- Counterparty (why it persists): Retail momentum chasers and passive index rebalancers who push recent winners further; large HF avoid due to capacity constraints at this slow turnover
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 20, 'reb': 10, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1015 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H120. Crypto 6-month TS trend monthly rebal slow (registered 2026-09-17, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 120, 'reb': 21}` (id c9e5ffc1d).
- Mechanism: 6-month trend in each crypto asset captures adoption wave dynamics and macro risk-on/off cycles that are autocorrelated; monthly rebal differs from biweekly already tested by substantially reducing noise from short-term volatility
- Counterparty (why it persists): Long-only crypto hodlers and market makers who do not systematically exploit directional persistence at this horizon
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 120, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1024 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H121. Equity 9M XS momentum 1M skip monthly rebal tight (registered 2026-09-17, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on equity; params `{'lookback': 180, 'skip': 21, 'reb': 21, 'n_side': 10}` (id cf2698eb6).
- Mechanism: 9-month lookback with 1-month skip isolates the intermediate-horizon momentum window distinct from 6M and 12M already buried; tighter 10-side book reduces factor crowding that dilutes signal in wide books
- Counterparty (why it persists): Short-volatility systematic sellers and fundamental value investors who fade recent winners prematurely
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 180, 'skip': 21, 'reb': 21, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1033 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H122. Crypto 6M vol-scaled momentum 10d skip biweekly refined (registered 2026-09-17, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 180, 'skip': 10, 'reb': 14}` (id ccd2f17c7).
- Mechanism: Inverse-vol sizing on 6-month crypto momentum allows smaller coins with high recent vol but weaker trend to be underweighted relative to dominant trend leaders; 10-day skip avoids microstructure reversal; biweekly rebal is a distinct cadence from monthly and weekly already tested
- Counterparty (why it persists): Retail yield-farmers chasing high-vol alts regardless of trend direction; large quants skip due to limited crypto data history and operational complexity
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 180, 'skip': 10, 'reb': 14}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1042 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H123. Crypto 30d XS reversal weekly rebal tight 8-side (registered 2026-09-17, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 30, 'reb': 5, 'n_side': 8}` (id c7c8b1159).
- Mechanism: 30-day horizon captures over-extension from altcoin season rotations and whale-driven pumps that subsequently revert; tight 8-side book concentrates in most extreme dislocations where mean reversion is sharpest and avoids dilution from noisy mid-rank coins
- Counterparty (why it persists): Trend-following retail and CTA-style bots that chase the most recent monthly outperformers in crypto without accounting for reversion
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 30, 'reb': 5, 'n_side': 8}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1051 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H124. Equity 60d XS reversal monthly rebal medium book (registered 2026-09-18, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 60, 'reb': 21, 'n_side': 15}` (id c56b599e7).
- Mechanism: Intermediate-horizon mean reversion in megacaps driven by institutional flow reversals and index rebalancing pressure over a 3-month window; monthly rebal keeps costs manageable for a slow signal.
- Counterparty (why it persists): Trend-following CTAs and momentum indices that push prices away from fair value over 1-3 months; large shops avoid this horizon because it conflicts with their momentum books and has moderate capacity.
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 60, 'reb': 21, 'n_side': 15}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1060 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H125. Crypto 1-year time-series trend monthly rebal (registered 2026-09-18, PRE-DATA, auto-pipeline)
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 252, 'reb': 21}` (id c671b2ceb).
- Mechanism: Annual time-series trend captures structural adoption cycles and macro-driven directional regimes in crypto; most buried crypto TS signals used 10-90 day lookbacks, leaving the 1-year horizon untested. Long-only bias of retail means persistent uptrends are exploitable.
- Counterparty (why it persists): Buy-and-hold retail holders and short-term traders who do not systematically fade or ride annual trends; large quants avoid crypto annual signals due to limited history and regime instability.
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 252, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1069 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H126. Crypto 12-1 XS momentum monthly rebal tight book (registered 2026-09-18, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 252, 'skip': 21, 'reb': 21, 'n_side': 8}` (id ca7c9f526).
- Mechanism: Annual cross-sectional momentum with 1-month skip mirrors the classic equity factor but in crypto where institutional adoption flows create persistent winner/loser divergence over 12-month horizons; 8-side tight book avoids illiquid names.
- Counterparty (why it persists): Retail investors who chase recent performance over short windows (days/weeks) but ignore annual relative strength; large quants avoid crypto annual momentum due to regime breaks and limited data.
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 252, 'skip': 21, 'reb': 21, 'n_side': 8}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1078 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H127. Equity 6M low-vol weekly rebal (registered 2026-09-18, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on equity; params `{'vol_lb': 126, 'reb': 5}` (id c941de29e).
- Mechanism: Semi-annual volatility lookback captures structural low-vol premium driven by leverage-constrained institutional investors who overpay for high-vol lottery stocks; weekly rebal keeps signal fresh without excessive turnover. Distinct from buried monthly/bi-weekly specs by using a mid-range 126d window with weekly rebal.
- Counterparty (why it persists): Retail and growth-oriented fund managers who systematically overweight high-volatility names; large quants skipped this parameter combo because it sits between their standard monthly and daily rebal strategies.
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 126, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1087 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H128. Equity 1M vol-scaled momentum 2d skip tri-daily rebal (registered 2026-09-18, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 21, 'skip': 2, 'reb': 3}` (id c3ae7e944).
- Mechanism: Short-term (1-month) vol-scaled momentum with a 2-day microstructure skip captures intermediate-speed relative-strength signals after bid-ask bounce is avoided; tri-daily rebal balances signal freshness against costs. No buried test covers this exact lookback/skip/rebal combo.
- Counterparty (why it persists): Market makers and statistical arbitrageurs who focus on intraday and overnight signals, missing the 3-4 week directional drift; large momentum shops use longer lookbacks and miss this fast-intermediate window.
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 21, 'skip': 2, 'reb': 3}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1096 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H124b. ES opening-range breakout, 09:30-10:00 range, intraday (registered 2026-09-18, PRE-DATA, from the bennnytrades/tradexlabs ORB claim)
- NUMBERING CORRECTION (2026-09-20): registered as H124 on 2026-09-18, colliding with the auto-pipeline's H124 (Equity 60d XS reversal) registered the same day. Renamed H124b here and in VERDICTS.md. Content, date and verdict unchanged; only the label was ambiguous.
- Family/universe: `orb` on es_futures; params `{'or_end': 600, 'brk_end': 720, 'exit': 955}` — spec frozen verbatim in AUTOMATED-TRADING-RESEARCH.md on 2026-09-15, before any intraday result was inspected.
- Mechanism: The first 30 minutes of the cash session set a reference range under maximum overnight-information uncertainty. A close outside it within the next two hours marks the point where one side's resting inventory has been cleared and the other side must chase, producing short-horizon continuation. Flat by 15:55, so no overnight gap risk is carried.
- Counterparty (why it persists): Overnight holders and opening-auction participants unwinding into the breakout, plus mean-reversion traders fading the opening range who are stopped out and must buy back.
- Why bigger firms leave it on the table: THEY DO NOT, and that is stated rather than argued around. ORB is among the most widely published intraday rules in existence. The only honest claim is that it is capacity-constrained at the size a $500 budget implies. §1's edge test is NOT satisfied; this is registered as a screen of a public claim, not as a proprietary edge.
- Test (set BEFORE data): `research/orb.py`. ES continuous 1-min, 2024-08-25..2026-08-24. 491 eligible sessions (1.95y) after excluding 5 scheduled early closes, 3 sessions with missing minutes, 1 missing previous close. Opening range = high/low of 09:30-09:59. Entry = next-minute OPEN after the first one-minute CLOSE outside the range between 10:00 and 11:59. Stop = opposite range boundary, conservative same-bar treatment (stop assumed filled before any favourable excursion in the same bar). Time exit 15:55. One trade per day, no profit target. Costs 1 tick slippage/side + $1.25 commission/side = $27.50 round trip on ES. Train = first 65% of sessions, holdout = last 35%. 3x3 neighborhood over range-end {09:45, 10:00, 10:30} x breakout-cutoff {11:00, 12:00, 13:00}.
- Gate (pre-set): ALL FOUR must hold.
  1. Net > 0 AND Sharpe > 0.5 in BOTH halves.
  2. Holdout 95% bootstrap CI on Sharpe excludes zero (lower bound > 0).
  3. Best neighborhood cell clears the noise ceiling at N=9 over 1.95y = **1.50**.
  4. BEATS spy_buyhold on a paired difference (`benchmark.compare` -> "BEATS") over the overlapping window.
- Recorded in advance, so it cannot be revised after: the CUMULATIVE-cell ceiling (N=1015 over 1.95y) is **2.67**. Gate 3 uses the fresh N=9 count because this is the first test on this instrument and this frequency. That is a judgement call, made now, in writing.
- Power note, also in advance: 491 sessions over 1.95 years is a SHORT sample. Even a genuinely good strategy may fail gate 3 here. A failure is evidence about this test's power as much as about ORB, and reads as "not demonstrated on two years", not "disproven".
- Kill rule: fail any gate -> graveyard. No goalpost moves, no re-cut of the window, no second neighborhood.

## H129. Equity 3d XS reversal 3d rebal 10-side (registered 2026-09-19, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 3, 'reb': 3, 'n_side': 10}` (id cbd6d97dd).
- Mechanism: Short-horizon price reversals in megacaps driven by institutional order-splitting and end-of-day rebalancing flows; 3-day window captures mean-reversion before momentum reasserts; tighter 10-side book avoids most-liquid names where arbitrage is fastest
- Counterparty (why it persists): Retail momentum chasers and ETF rebalancers who push prices temporarily away from fair value; large HFT firms ignore daily-bar signals as too slow for them but megacap desks too large to act at this frequency
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 3, 'reb': 3, 'n_side': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1105 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H130. Crypto 120d XS momentum 7d skip biweekly rebal 6-side (registered 2026-09-19, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 120, 'skip': 7, 'reb': 14, 'n_side': 6}` (id c6490408b).
- Mechanism: 4-month cross-sectional momentum in crypto captures structural allocation waves (exchange listings, ETF flows, protocol upgrade cycles) that persist longer than short-run noise; 7-day skip avoids reversal; ultra-tight 6-side book concentrates in highest-conviction signals where retail herding is strongest
- Counterparty (why it persists): Retail allocators who rotate into recent winners after media coverage peaks, providing sustained flow; institutional crypto desks too capacity-constrained in small alts to absorb opposite side efficiently
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 120, 'skip': 7, 'reb': 14, 'n_side': 6}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1114 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H131. Crypto 6m vol-scaled momentum 14d skip monthly rebal (registered 2026-09-19, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on crypto; params `{'lookback': 180, 'skip': 14, 'reb': 21}` (id c3155319a).
- Mechanism: 6-month vol-normalized momentum on crypto with a 14-day skip (longer than typical) specifically avoids the well-documented 1-2 week crypto reversal zone; monthly rebal minimizes crypto transaction costs; vol-scaling reduces sizing in high-dispersion regimes when momentum signals are noisiest; 180-day horizon captures medium-term adoption waves
- Counterparty (why it persists): Leveraged perp traders who create vol spikes around catalyst events, inflating denominator and reducing position size precisely when risk is highest, providing a natural risk filter
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 180, 'skip': 14, 'reb': 21}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1123 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H132. Equity 6m low-vol quarterly rebal (registered 2026-09-19, PRE-DATA, auto-pipeline)
- Family/universe: `low_vol` on equity; params `{'vol_lb': 126, 'reb': 63}` (id ccd12744f).
- Mechanism: 6-month realized volatility lookback on megacaps with quarterly rebalancing targets the structural low-volatility anomaly driven by benchmark-constrained institutional managers who systematically overprice high-beta/high-vol stocks; quarterly rebal differs meaningfully from all buried weekly/monthly variants by dramatically reducing transaction costs and allowing factor to compound; megacap universe ensures execution feasibility
- Counterparty (why it persists): Benchmark-hugging fund managers forced to hold high-vol megacaps to avoid tracking error; retail investors with lottery-ticket preferences who overpay for high-vol names
- Test (set BEFORE data): factors.low_vol(px, **{'vol_lb': 126, 'reb': 63}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1132 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H133-ES. ES opening-range breakout, IDENTICAL rule, 16.29-year sample (registered 2026-09-20, PRE-DATA, PRE-PURCHASE)
- NUMBERING CORRECTION (2026-09-21): the auto-pipeline registered its own H133 (Equity 45d XS reversal) after this one. Renamed H133-ES here and in VERDICTS.md. Content, gates, date and verdict unchanged. Root cause: the pipeline picks the next integer without checking for headers added by hand. See the DUPLICATE-LABELS finding.
- Family/universe: `orb` on es_futures; params `{'or_end': 600, 'brk_end': 720, 'exit': 955}` — **byte-identical to H124b**. No re-search, no re-tune. The only thing that changes is the length of the sample.
- Relationship to H124b: H124b failed all four gates on 1.95 years (491 sessions, holdout Sharpe -0.67 [-3.20, +1.63], geometric -38.0%/yr). Its autopsy named the cause as insufficient sample for the firm's accumulated multiple-testing history, not as a disproof of the rule. H133 is the retest that autopsy called for. H124b stays buried regardless of what H133 returns.
- Mechanism: unchanged from H124b. The first 30 minutes of the cash session set a reference range under maximum overnight-information uncertainty; a close outside it within the next two hours marks the point where one side's resting inventory has been cleared and the other must chase. Flat by 15:55.
- Counterparty (why it persists): unchanged. Overnight holders and opening-auction participants unwinding into the breakout, plus range-faders stopped out and forced to buy back.
- Why bigger firms leave it on the table: THEY DO NOT. Restated verbatim from H124b because it has not become truer: ORB is among the most widely published intraday rules in existence. §1's edge test is NOT satisfied. This is a screen of a public claim, not a proprietary edge. The only defensible claim is capacity constraint at the size a $500 budget implies.
- Data (specified before purchase): Databento GLBX.MDP3, `ohlcv-1m`, symbols `ES.FUT` stype_in=`parent` (every expiration, 8,696,827 records) plus `definition` (189,255 records), 2010-06-06 .. 2026-09-20. Quoted read-only at **$31.75 + $0.16 = $31.91** before authorization; inside the $50 first-paid-research cap. Parent set chosen over the $20.59 pre-stitched ES.c.0 continuous series specifically so the roll is built and audited here rather than inherited from an uncertified vendor stitch (cf. Amendment A1).
- Roll rule (set BEFORE seeing the data): front month = the contract with the highest daily volume; on a tie, highest open interest; roll effective the NEXT session after the crossover, never the same session. Roll dates and the volume series that produced them get written to a QUALITY.md and are auditable. Intraday single-contract trades are unaffected by an additive price offset (entry and exit are on the same contract), so no back-adjustment is applied; this is stated now so it cannot be introduced later as a fix.
- Session calendar: `research/session_calendar.py`, extended backwards to 2010. Exclusions, stated in advance: scheduled early closes, sessions with missing minutes inside 09:30-16:00, sessions with no previous close. Every exclusion gets counted and reported; the count is part of the verdict, not a footnote.
- Test (set BEFORE data): `research/orb.py`, unmodified except for the data loader. Opening range = high/low of 09:30-09:59. Entry = next-minute OPEN after the first one-minute CLOSE outside the range between 10:00 and 11:59. Stop = opposite range boundary, conservative same-bar treatment. Time exit 15:55. One trade per day, no profit target. Capital $25,000 for Sharpe. Train = first 65% of eligible sessions (~10.6y), holdout = last 35% (~5.7y). 3x3 neighborhood over range-end {09:45, 10:00, 10:30} x breakout-cutoff {11:00, 12:00, 13:00}.
- Costs: gate applied at 1 tick slippage/side + $1.25 commission/side = **$27.50 round trip**, identical to H124b so the two results are directly comparable. A **$40.00 round-trip stress run is also reported**, and it is one-directional by construction: it can sink a marginal pass, it can NEVER rescue a failure. Recorded now because $27.50 is optimistic for 2010-2015 commissions and pretending otherwise later would be a goalpost move.
- Gate (pre-set): ALL FIVE must hold.
  1. Net > 0 AND Sharpe > 0.5 in BOTH halves.
  2. Holdout 95% block-bootstrap CI on Sharpe excludes zero (lower bound > 0).
  3. Best neighborhood cell clears the noise ceiling at **N=18 over 16.29y = 0.60**. N=18, not 9: these nine cells are the SECOND look at this rule on this instrument, and H124b's nine are counted against it. Counting them as fresh would be the cheat this gate exists to prevent.
  4. BEATS spy_buyhold on a paired difference (`benchmark.compare` -> "BEATS") over the overlapping window.
  5. The $40 stress run does not turn gate 1 or gate 2 negative.
- Recorded in advance so it cannot be revised after: the CUMULATIVE-cell ceiling (N=1141 over 16.29y) is **0.93**. Clearing 0.60 but not 0.93 will be reported as exactly that — cleared the family bar, did not clear the firm's whole search history — and will NOT be upgraded to a confirmation.
- Reported but NOT gated, fixed in advance to stop cherry-picking: per-year and per-regime breakdown (2010-2012, 2013-2015, 2016-2019, 2020-2021, 2022-2023, 2024-2026), MFE/MAE distribution, and the geometric annual return alongside the arithmetic one. H124b's autopsy found arithmetic -0.5%/yr against geometric -38.0%/yr; the geometric figure is the headline for every intraday verdict from here on. No subperiod may be promoted to the result.
- Power note, in advance: 16.29 years is ~4,100 eligible sessions, roughly 8x H124b. This sample can support a verdict that 1.95 years could not. That cuts both ways — a failure here is much harder to blame on sample size, and will be recorded as evidence against the rule rather than against the test.
- Upper-bound note, in advance: minute bars cannot resolve within-bar path, so stop fills are flattered. Tick data was priced at the same time ($77.48 for ONE year of `mbp-1`, $144.65 for one year of `trades`) and is outside the $500 ceiling. Every number H133 produces is therefore an UPPER BOUND on the achievable result. A pass here licenses a tick-data question, not a deployment.
- Kill rule: fail any gate -> graveyard. No goalpost moves, no re-cut of the window, no second neighborhood, no "but 2020 worked".

## H133. Equity 45d XS reversal monthly rebal medium book (registered 2026-09-20, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 45, 'reb': 15, 'n_side': 20}` (id c8ce8ba67).
- Mechanism: Medium-horizon mean reversion in megacaps captures overshoot from institutional momentum crowding that takes 6-8 weeks to unwind; monthly rebal reduces turnover costs on a slower signal
- Counterparty (why it persists): Trend-following CTAs and momentum ETFs that enter on breakout and exit only after extended drawdown; capacity constraints prevent larger firms from sizing small-cap-style reversal in megacaps
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 45, 'reb': 15, 'n_side': 20}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1141 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H134. Equity 20d vol-scaled momentum 1d skip weekly rebal (registered 2026-09-20, PRE-DATA, auto-pipeline)
- Family/universe: `mom_volscaled` on equity; params `{'lookback': 20, 'skip': 1, 'reb': 5}` (id cca2398b2).
- Mechanism: Short-window risk-parity momentum at 1-month horizon with minimal skip; volatility-scaling removes the size-of-move contamination that kills raw momentum at this horizon, letting the genuine short-term trend signal survive; 1-day skip avoids microstructure reversal
- Counterparty (why it persists): Delta-hedging desks that create transient dislocations and retail momentum chasers who enter without vol adjustment; quant funds avoid sub-30d vol-scaled equity signals due to high turnover relative to capacity
- Test (set BEFORE data): factors.mom_volscaled(px, **{'lookback': 20, 'skip': 1, 'reb': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1150 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H135. Crypto 60d XS momentum 5d skip weekly rebal tight book (registered 2026-09-20, PRE-DATA, auto-pipeline)
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 60, 'skip': 5, 'reb': 7, 'n_side': 6}` (id c9afbdf6a).
- Mechanism: 60-day lookback is a genuinely untested window in the buried list for crypto XS momentum with a 5-day skip; tight 6-side book concentrates in the highest-conviction winners/losers where the crypto momentum effect is strongest due to narrative clustering
- Counterparty (why it persists): Crypto retail who rotate into recent winners after news peaks; market-makers who are flat and institutional desks with no crypto mandate
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 60, 'skip': 5, 'reb': 7, 'n_side': 6}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1159 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H136. Mechanism-diversified portfolio of trend + carry sleeves (registered 2026-09-21, PRE-RESULT)
- Family/universe: a PORTFOLIO, not a new factor. Equal-weight across one representative cell of each mechanism selected by the rule below, on both equity and crypto.
- Why this exists: the firm has spent 1,141 cells hunting for ONE strategy that beats SPY. That is not how the industry produces a Sharpe above 1. The identity is `combined = s*sqrt(N) / sqrt(1 + (N-1)*rho)`: many weak, weakly-correlated sleeves. Measured on 2026-09-21, the firm's mechanism-level **rho is +0.037** across 12 (family, universe) cells -- near-independence, which is the expensive ingredient and we already have it. What we lacked was any test that asked whether components ADD to a book, rather than whether each BEATS SPY alone. A sleeve with Sharpe +0.3 and rho 0.05 to everything else is valuable and our gate discarded it by construction.
- Mechanism (portfolio-level): diversification across independent return sources. The counterparty is not a single trader; it is that each sleeve's own counterparty is distinct, so their losses do not arrive on the same days. rho=0.037 is the evidence that they do not.
- SELECTION RULE, fixed here and decided on MECHANISM grounds, NOT on performance:
  INCLUDE `ts_momentum`, `xsec_momentum`, `mom_volscaled`, `funding_carry`, `funding_ts` -- trend and carry. Both have a named structural counterparty: trend is paid by investors who fade persistent flows and by CTA capacity limits; funding carry is paid by leveraged perp longs who must pay the funding rate and cannot stop while levered.
  EXCLUDE `xsec_reversal` and `low_vol`. Reason stated in advance: neither has a counterparty argument this firm has ever written down that survives §1, and the low-vol premium is a documented, heavily-arbitraged public factor.
  One cell per (family, universe), taken in HYPOTHESES.md order, never by Sharpe.
- CONTAMINATION DISCLOSED: full-sample Sharpes of all 12 mechanism cells were seen on 2026-09-21 BEFORE this registration. The selection rule above uses none of them -- it is a mechanism rule -- but I cannot claim to be blind, so the gate is set harder than the firm's usual bar to compensate. Stating this rather than pretending otherwise.
- Test (set BEFORE the portfolio is run): equal weight, no optimization, no risk parity, no weights fitted to anything. Inner-joined on common dates. Costs 10bps as everywhere else. Train = first 65% of common dates, holdout = last 35%. Sleeve membership is FIXED by the rule above and does not change between train and holdout.
- Gate (pre-set): ALL FOUR.
  1. Holdout Sharpe > 0.5 AND holdout net > 0.
  2. Holdout 95% block-bootstrap CI on Sharpe excludes zero.
  3. Holdout Sharpe exceeds the noise ceiling at **N=1,141 cumulative cells** over the holdout's own length -- the full firm history, not a fresh count, because these sleeves were all found inside that search.
  4. BEATS spy_buyhold on a paired difference over the holdout, using `fill_flat=True` (the survivorship-of-days fix from 2026-09-21).
- Reported but NOT gated, fixed in advance: the correlation matrix, per-sleeve holdout Sharpe, and the equal-weight result with each sleeve dropped one at a time. No sleeve may be removed after the fact to improve the result.
- Two defects to investigate separately, NOT to be fixed inside this hypothesis: `xsec_reversal.equ` returned Sharpe -3.780, which is implausible and reads as a bug; `mom_volscaled.equ` and `xsec_momentum.equ` correlate at **0.967**, so they are near-duplicates and the firm has been counting them as two independent cells against its own noise ceiling for months.
- Kill rule: fail any gate -> graveyard. No re-weighting, no dropping the worst sleeve, no switching to risk parity, no adding a sleeve that would have helped.

## H140. Ten-sleeve intraday portfolio on ES (NUMBER RESERVED - NO SPEC ON DISK)
- **Status 2026-09-21: this number is reserved and MUST NOT be reused.** A v2 spec is referred to in the project handoff as "registered, not run, awaiting Peter's sign-off", but a filesystem-wide search on 2026-09-21 (`grep -rln "H140"` across `~/polytail` and `research/`) found **no spec file anywhere**.
- Nothing is registered under this number. No gate exists, so no run of it can be evaluated. Writing the spec now, after H136's ten-sleeve portfolio already returned NOT CONFIRMED, would be a post-hoc registration and is forbidden.
- Blocked regardless: G3 of the intended gate compares against `spy_buyhold`, and `data/benchmark_bars.csv` `adj_close` is price-only (see H141's limitation note). The benchmark must be fixed before any G3 can mean anything.
- To proceed: write the spec, fix the benchmark, then register it as a NEW number with a fresh date. Do not resurrect this one.

## H141. Does the crypto trend family survive a point-in-time universe? (registered 2026-09-21 PRE-DATA; back-filled to this ledger 2026-09-21)
- Source of record: `graveyard/crypto/H141-SURVIVORSHIP-SPEC.md`. Registered before any backtest was run on the new data.
- Family/universe: `ts_momentum` on crypto, but the OBJECT UNDER TEST IS THE UNIVERSE, not the factor. Kill test by design.
- Hypothesis: H63's excess over SPY (+22.25%/yr, diff-sharpe +0.542, CI [-0.018,+1.087], TIES) is substantially an artefact of hindsight universe selection and does not survive a causal point-in-time universe.
- Mechanism of the suspected artefact: `config.py` defines crypto as a hand-written list of 30 coins written in 2026 and backtested from 2015. Binance archive census 2026-09-21: 734 USDT symbols ever listed, 243 (33.1%) delisted, 214 of them after >=12 months trading, deaths concentrated in 2024/2025/2026 - exactly H63's holdout. Of the firm's 27 names present in the archive, **0 are delisted**. A 0% death rate drawn from a 33% population is a selection, not a sample.
- Point-in-time rule (fixed before the run): at each rebalance `t`, using only data timestamped on or before `t`, eligible = every USDT-quoted Binance spot symbol with >=180 calendar days of bars ending at `t` AND trading on >=20 of the last 30 sessions ending at `t`. Hold top 20 by trailing 30-day quote volume, equal weight, rebalance biweekly (14d), matching H63.
- Trend rule copied from H63 and NOT re-tuned: long if 126-day return to `t` is positive, else flat in that sleeve. Long-only, no shorts, no leverage. Costs 10bps/side, matching `config.py` COST_BPS, so the two arms differ ONLY in the universe.
- Delisting treatment, disclosed as generous: a stopped symbol is marked out at its last available close, proceeds to cash until next rebalance. Real delistings are worse, so a FAIL here is optimistic, not pessimistic.
- The trap named in advance so it cannot be reintroduced: downloading only symbols with ">=24 months of history" is FORBIDDEN - lifetime is known only in hindsight, and filtering on it smuggles back the exact bias under test. All 734 symbols are downloaded; eligibility is evaluated causally at each `t`.
- Gate (pre-set): PASS = whole 95% CI on diff-sharpe vs `spy_buyhold` above zero AND point estimate within 0.15 of the hindsight arm's +0.542. PARTIAL = beats on the point estimate but CI straddles zero. **FAIL = point estimate below +0.20, OR annualised excess below +8%.**
- Kill rule: on FAIL the crypto trend family is buried and the nine `GRAVEYARD-REVIEW.md` near-misses are annotated explained-by-survivorship. No re-tuning the lookback, the rebalance period, the top-N, or the venue. No second holdout.
- Known limitations stated up front: Binance is one venue and its own listing decisions are a selection of a different kind; and `benchmark_bars.csv` `adj_close` is price-only, not dividend-adjusted (8.93% CAGR over 19.9y), so every SPY comparison here understates SPY. That bias runs against the strategy in this kill test, which is the safe direction, but it must be fixed before any benchmark-as-gate constitution change.
- Strategy trials consumed: 1. One universe rule, one trend rule, no grid.
- **VERDICT: FAIL, 2026-09-21. See VERDICTS.md.**

## H142. Do SPX open-interest walls act as intraday reference levels on ES? (registered 2026-09-21 before any options data was purchased; back-filled to this ledger 2026-09-21)
- Source of record: `graveyard/gamma/H142-GAMMA-LEVELS-SPEC.md`. Stage 1 of 2. Kill test.
- Not a reopening of the buried August gamma screen: that used gamma as a rare market-wide REGIME FILTER (18 fires in 495 sessions) and stands buried. This tests a different object - a price level present in every session - built from per-strike open interest the firm has never owned. No filter has been loosened.
- Deliberately NOT built: no Black-Scholes, no implied volatility, no dealer-positioning sign convention. Carried over from the volume-profile failure, where an unobservable required assumption (how a bar's volume spreads across its range) dominated the answer - best reconstruction hit POC/VAH/VAL within one tick on only 22.6% of sessions. Dealer positioning has the same shape of problem: it cannot be observed, only assumed. Stage 1 tests only what is directly measured.
- Data: `OPRA.PILLAR`, schema `statistics` with `stat_type = OPEN_INTEREST (9)` plus schema `definition` for the strike/expiry map, symbol `SPX.OPT`, `stype_in=parent`, window 2025-09-18..2026-09-18. Quoted $26.37 + $3.98 = $30.35 via `metadata.get_cost`. Price series `firm/data/es_1m_continuous_v.csv`, already owned. Sessions per `orb.sessions()`, RTH minutes 570..955.
- SPX not SPY: 6x cheaper ($26.37 vs $159.77 for the same year) and it is where index-level dealer inventory concentrates.
- Levels, fixed before the data existed: for each eligible session `t`, using ONLY the prior session's end-of-day open interest, among contracts expiring within 30 calendar days - CALL WALL = strike with largest call OI, PUT WALL = strike with largest put OI. Ties break to the strike closest to the prior ES close, then to the lower strike.
- Basis adjustment: level in ES terms = `strike + basis`, where `basis = prior session ES 15:59 close - prior session SPX close`. SPX daily closes pulled free from a public source and stored alongside results. A day with no SPX close is EXCLUDED, not interpolated.
- Measurement: TOUCH = first RTH 1-minute bar of session `t` whose low <= level <= high; at most one touch per level per session; untouched sessions contribute no touch and the untouched count is reported. REACTION = from the touch bar's close, the maximum favourable excursion away from the level over the next 30 minutes, in ES points, in the direction price approached from, truncated at 15:55.
- Control is a PERMUTATION test, not random levels: random levels drawn from a session's own range would be biased toward the middle of the day's action. Instead hold session `t`'s price path fixed and substitute the walls from a different randomly chosen session `t'`, basis-adjusted to `t`. 200 permutations, seed 20260921.
- Gate (pre-set), BOTH required: **p < 0.05 two-sided against the permutation distribution AND observed median reaction >= 0.55 ES points** (one round trip, $27.50). A statistically detectable reaction smaller than the cost of trading it is a real phenomenon and a useless one; the volume-profile work already produced that shape and it must not count as a pass here.
- Kill rule: on FAIL, open-interest walls are buried and NO further options data is purchased for this line. Forbidden afterwards: changing the 30-day expiry window, using the 2nd or 3rd largest strike, switching the reaction horizon, scoring call walls alone because they beat put walls, or dropping untouched sessions.
- Reported but NEVER gating: 60-day and 7-day expiry windows, 2nd/3rd largest OI strikes, call and put walls separately, reaction at 10 and 60 minutes, touch frequency, and how far from the open walls typically sit.
- What a PASS licenses: Stage 2 only - a registered trading rule with its own gate, train/holdout split and one holdout opening. A PASS says the levels are REAL, not TRADEABLE. Different claims; the second needs its own spec.
- Strategy trials consumed: 1.
- **VERDICT: FAIL, 2026-09-21. See VERDICTS.md and graveyard/gamma/H142-VERDICT.md.**

## H143. Index-level overnight drift on ES (registered 2026-09-21, PRE-RESULT, screen of a published claim)
- Source of record: `graveyard/overnight/H143-ES-OVERNIGHT-SPEC.md`. Data cost **$0** -- the overnight bars were always in the archives; `build_es_continuous.py` filtered them at emit time, not at purchase.
- Family/universe: ES front-month futures, overnight close-to-open. Provenance is `firm/PAPER-SHORTLIST-2026-09-21.md`, a $0 literature screen that rejected four of five families and named this the one survivor, with its weaknesses recorded BEFORE any ES overnight data was inspected.
- Mechanism: the published claim is that retail market orders into the thin opening auction create pressure that reverses overnight. **Counterparty: none identified that survives §1.** The single-stock cost objection (40bps round trip on 1% of daily volume) does not transfer to one ES contract, which is the only reason this survived the screen -- but neither does the mechanism argument. Registered as a SCREEN OF A PUBLIC CLAIM, like H124b and H133-ES, not as a claim of edge.
- Prior stated in advance: index-level t-stat only 2-3 against Harvey-Liu-Zhu's ~3.0 hurdle; documented decay since ~2012, which the train/holdout split exposes directly since the holdout sits mostly post-decay.
- **CONTAMINATION DISCLOSED:** before this gate was written, the gross close-to-open mean and sd were computed and displayed while deciding how to treat multi-day windows -- all 4,090 windows +3.18 bps sd 68.28; gap=1 +4.08 sd 64.53; gap>1 -0.04 sd 80.27. An approximate GROSS Sharpe (~0.74 annualised) is therefore derivable from what was visible at registration. That is 8 inspected cells and they are charged to the ceiling. The gate is set on what remains unknown: net-of-cost, train/holdout, CI, t-statistic and benchmark. Note also that the better-looking `gap=1` subset was AVAILABLE and was DECLINED in favour of the full sample.
- Test (set BEFORE the run): long 1 ES contract, entry at the close of session `t`'s last RTH bar (the session's own `close_minute`, not a hardcoded 15:59), exit at the 09:30 open of session `t+1`. ALL 4,090 windows including the 891 spanning weekends/holidays -- no selection, decided on mechanism grounds because the tradeable overnight session is 929 minutes for a weekend and 929 for an ordinary night. Costs $27.50 round trip = 0.55 ES points, identical to `orb.py` and H142. Train = first 65% of windows, holdout = last 35%.
- Data: `firm/data/es_1m_24h.parquet` (5,694,226 bars), roll schedule verified identical to the audited `es_1m_continuous.csv`; trade-date map `firm/es_session.py`, 22 assertions, 0 non-session assignments across all bars; 75,996 bars (1.33%) on dates with no cash session excluded and counted, never reassigned.
- Gate (pre-set), ALL FIVE: (1) net mean/trade > 0 AND net Sharpe > 0.5 in BOTH halves; (2) holdout 95% block-bootstrap CI on Sharpe excludes zero; (3) holdout net Sharpe > noise ceiling at **N = 8** over the holdout's own length (ceiling ~0.854) -- N is the cells inspected for THIS hypothesis, because it was not found inside the firm's 1,159-cell search, and the asymmetry with internally generated ideas is flagged as a constitution question; (4) **BEATS `spy_buyhold`** on a paired difference over the holdout, `fill_flat=True`, against **`benchmark_bars_tr.csv`** -- the TOTAL-RETURN file, deliberately the harder bar, since the price-only file understates SPY by 2.008%/yr; (5) t-statistic on holdout mean net return > 3.0, the Harvey-Liu-Zhu hurdle.
- Kill rule: fail any gate -> graveyard. Forbidden afterwards: restricting to `gap=1`; changing entry or exit minute; adding a stop, target or filter; subsetting years; scaling size; dropping early closes; substituting the price-only benchmark.
- Reported but NEVER gating: the gap split and each bucket, gross vs net and cost drag, per-era breakdown, entry/exit minute sensitivity (+/-5, +/-15), early-close sessions, win rate, median, skew, worst window.
- What this CANNOT settle: one ES contract is ~$350k notional at 2026 prices. This tests whether the effect is real and survives its own costs, not whether the size suits the account. The sizing module (missing organ #1) does not exist. A PASS licenses a registered sizing question, not capital.
- Strategy trials consumed: 1.
- **VERDICT: NOT CONFIRMED, 2026-09-21, 0/5 gates. See VERDICTS.md and graveyard/overnight/H143-VERDICT.md.**

## H146. Equity 30d XS reversal bi-weekly rebal medium book (registered 2026-09-21, PRE-DATA, auto-pipeline)  [RENUMBERED 2026-09-22 from H136: duplicate label collision with hand-registered entry; content, params, gates, date and verdict unchanged]
- Family/universe: `xsec_reversal` on equity; params `{'lookback': 30, 'reb': 15, 'n_side': 12}` (id c25b150b2).
- Mechanism: Intermediate-horizon mean reversion in megacaps driven by institutional rebalancing flows and passive index inclusion mechanics; 30-day window captures institutional overshoot rather than micro-noise
- Counterparty (why it persists): Trend-following CTAs and momentum funds that push prices away from fair value over multi-week horizons; mega-cap universe too liquid for HFT arb but window too short for fundamental shops
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 30, 'reb': 15, 'n_side': 12}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.3 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1168 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H147. Crypto 6m TS trend 10-day rebal (registered 2026-09-21, PRE-DATA, auto-pipeline)  [RENUMBERED 2026-09-22 from H137: duplicate label collision with hand-registered entry; content, params, gates, date and verdict unchanged]
- Family/universe: `ts_momentum` on crypto; params `{'lookback': 180, 'reb': 10}` (id c5c5d9b6e).
- Mechanism: Long-horizon absolute trend in crypto driven by retail adoption cycles and macro risk-on/off regimes; each asset independently bets on continuation of multi-month directional move distinct from cross-sectional ranking
- Counterparty (why it persists): Discretionary traders fading extended moves on mean-reversion intuition; larger quant shops avoid crypto TS trend at this horizon due to AUM capacity and operational friction
- Test (set BEFORE data): factors.ts_momentum(px, **{'lookback': 180, 'reb': 10}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1177 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H148. Crypto annual XS momentum 1M skip monthly rebal 6-side (registered 2026-09-21, PRE-DATA, auto-pipeline)  [RENUMBERED 2026-09-22 from H138: duplicate label collision with hand-registered entry; content, params, gates, date and verdict unchanged]
- Family/universe: `xsec_momentum` on crypto; params `{'lookback': 252, 'skip': 21, 'reb': 21, 'n_side': 6}` (id ceaf1ddf4).
- Mechanism: Very long formation window (1 year) captures structural rotation between blockchain ecosystems; 1-month skip avoids reversal contamination; ultra-tight 6-side book focuses on strongest convictions only
- Counterparty (why it persists): Retail holders anchored to prior cycle winners; institutional crypto allocators with quarterly mandates too slow to rebalance
- Test (set BEFORE data): factors.xsec_momentum(px, **{'lookback': 252, 'skip': 21, 'reb': 21, 'n_side': 6}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1186 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H149. Crypto 60d XS reversal monthly rebal ultra-tight 5-side (registered 2026-09-21, PRE-DATA, auto-pipeline)  [RENUMBERED 2026-09-22 from H139: duplicate label collision with hand-registered entry; content, params, gates, date and verdict unchanged]
- Family/universe: `xsec_reversal` on crypto; params `{'lookback': 60, 'reb': 21, 'n_side': 5}` (id c96f7b6ff).
- Mechanism: Two-month horizon captures overcrowding and deleveraging cycles in crypto where leveraged longs accumulate in recent outperformers and then unwind; monthly rebal keeps costs low; 5-side ultra-tight book isolates extreme decile
- Counterparty (why it persists): Leveraged long-biased crypto funds and retail FOMO buyers chasing 2-month winners; larger quants avoid this because the signal is noisy at medium horizon but extreme decile filtering improves Sharpe
- Test (set BEFORE data): factors.xsec_reversal(px, **{'lookback': 60, 'reb': 21, 'n_side': 5}); next-bar fills, 10bps; train=first 65% of post-warmup days, holdout=last 35%; plus a 3x3 param neighborhood.
- Gate (pre-set): net ann>0 AND sharpe>0.4 in BOTH halves, AND best neighborhood cell clears the noise ceiling at N=1195 cumulative cells. Kill rule: fail any -> graveyard, no goalpost moves.

## H144. ES opening-range break-of-structure retest (registered 2026-09-22, PRE-RESULT, PRE-CODE)
- Full spec: `graveyard/orbstruct/H144-H145-SPEC.md`, sha256 99bdc39c287fe9dcd246e8ba12c4df5f61ddff871796dccfd470df325daf0058. Written before the strategy code existed.
- Data: `firm/data/es_1m_continuous.csv`, already owned and audited. **$0 to run.**
- Mechanism: resting stops cluster just outside the opening range, so a close beyond it is often the liquidity event itself and the break entry buys from the participants being flushed. H144 does not enter the liquidity event -- it waits for a retest of the broken level and a break of structure beyond the excursion high, and stops at the swing formed during the retest rather than at the far side of the range.
- Counterparty (why it persists): traders who entered on the break and are stopped out on the pullback. Structural flow, not informational.
- NOT a re-tune of H133-ES: the opening range is held at 09:30-09:59 EXACTLY as H133-ES registered it, so the range is a control and the ENTRY TRIGGER and STOP are the only things that vary. Changing the range would be the forbidden re-tune.
- Rule (set BEFORE data): OR 09:30-09:59; first 1-min close outside it in 10:00..brk_end; retest of the broken level within retest_window; first close beyond the post-break extreme within retest_window of the retest; entry next-minute OPEN; stop at the retest swing; exit 15:55 OPEN or stop; NO profit target; one trade/day; $27.50 round trip; conservative stop-wins-the-bar treatment.
- Registered cell: retest_window=30, brk_end=720.
- Neighborhood (fixed now, 9 cells): retest_window in {15,30,45} x brk_end in {660,720,780}.
- Gate (pre-set, identical to H133-ES): (1) net>0 AND sharpe>0.5 in BOTH halves; (2) holdout 95% block-bootstrap CI excludes zero; (3) best of 9 cells > sqrt(2 ln 9)/sqrt(Y); (4) BEATS spy_buyhold on paired difference; (5) $40 stress does not sink 1-2.
- Power floor (pre-set): under 200 taken trades the result is UNDERPOWERED, not a verdict.
- Instrument audit required before any verdict: break count must approximately match H133-ES on the same sessions, else the run is void.
- Kill rule: fail any gate -> graveyard. No second neighborhood, no vol/gap/volume/trend/news filter, no re-cut window, no post-hoc target, no moving the stop's timeframe, and none of the six exit-re-tune variants from the ORB Strategy Suite.

## H145. ES failed-break fade (registered 2026-09-22, PRE-RESULT, PRE-CODE)
- Full spec: `graveyard/orbstruct/H144-H145-SPEC.md`, same sha256 as above.
- Data: same file, same sessions. **$0 to run.**
- Mechanism: if the break has negative expectancy over 16 years, the informative event may be its FAILURE. A close back inside the range after an excursion is a completed liquidity sweep -- the stops outside the range have been taken and the auction has rejected the level. H145 fades that toward the opposite boundary.
- Counterparty (why it persists): breakout entrants now offside who must cover, plus the stop cluster on the far side of the range.
- NOT a sign flip of H133-ES: H133-ES traded every break unconditionally. H145 trades only breaks that then FAILED -- a conditioning event H133-ES never observed -- in the opposite direction, with a target H133-ES did not have.
- Rule (set BEFORE data): OR 09:30-09:59; first 1-min close outside it in 10:00..brk_end; first close back INSIDE the range within fail_window; entry next-minute OPEN opposite the break; stop at the excursion extreme; target the opposite range boundary; if a bar touches both, the STOP fills first; else 15:55 OPEN; one trade/day; $27.50 round trip.
- Registered cell: fail_window=30, brk_end=720.
- Neighborhood (fixed now, 9 cells): fail_window in {15,30,45} x brk_end in {660,720,780}.
- Gate (pre-set): identical five gates to H144 and H133-ES.
- Power floor (pre-set): under 200 taken trades -> UNDERPOWERED.
- Kill rule: identical to H144.
- Expected failure mode, stated in advance so it cannot be offered later as a surprise: high win rate with a left tail that eats it. Gate 2 is the one that should catch this.

## EdgeBot hypotheses moved out (2026-09-22)

H27, H137, H138 and H139 are **EdgeBot** (sports betting), a separate
project. They lived in this file and shared its register, which is how
EdgeBot kept surfacing in Graveyard analysis. They now live in
`EDGEBOT-HYPOTHESES.md`, moved byte-identical (sha256-verified). They never
contributed to `cumulative_cells` -- only pipeline.py increments that --
so the Graveyard's noise ceiling is unchanged by this move.

## H150. Intraday mean reversion at reference levels on ES (registered 2026-09-24, PRE-RESULT, PRE-CODE)
- Full spec: `graveyard/levels/H150-LEVEL-REVERSION-SPEC.md`, sha256 `19ba65709624dc49252a8f0ca67b0ac548801fb62b4480c2f2638f606ddaa398`, committed in `7048d0e` before `levels.py` existed.
- Data: `firm/data/es_1m_continuous.csv`, the same audited bars as H133-ES / H144 / H145. **$0 to run.**
- Origin: Peter's actual discretionary practice -- mark the first 15-minute candle's high and low, add other key levels, and fade them. Not RULES.md section 2, and not what H133-ES tested.
- Mechanism: a reference level that market participants can all compute is a place where resting orders concentrate, so a touch should be followed by rejection rather than continuation. This is the REVERSION direction; H133-ES, H144 and H145 tested continuation and conditional continuation at the same opening range.
- Gated levels (4, fixed before any result): `pdh` prior session RTH high, `pdl` prior session RTH low, `orh` opening-range high 09:30-09:59, `orl` opening-range low.
- Reported, NOT gated: `pdc`, the prior session's 15:59 close. **CONTAMINATED** -- its touch rate and MFE were read out of H142's instrument-audit table before this spec was written, so it cannot be registered fresh and may never be presented as a result.
- Excluded on evidence, not taste: volume-profile levels. 1-minute bars place POC+VAH+VAL within a tick on 24.6% of sessions against an 80% registered bar (`VOLUME-PROFILE-TICK-VERDICT.md`). The owned data cannot locate them.
- Excluded as unspecifiable: candle-pattern entry filters. This hypothesis tests the LEVEL alone; a pattern filter is a separate hypothesis and cannot be added post hoc to rescue a failure.
- Rule (set BEFORE data): first touch in 10:00..15:00; approach direction from the touching bar's open, tie-broken by the prior close; FADE it (from below -> short, from above -> long); entry next-minute OPEN; stop `s x H` beyond the level; target `t x H` from entry, where `H` is the opening-range height known at 10:00; if a bar touches both, the STOP fills first; else 15:55 OPEN; one trade/session/level; $27.50 round trip.
- New exclusion registered here: the prior session must be eligible AND trade the SAME contract. On a back-adjusted continuous series a cross-session level taken over a roll is on a different price scale. `orb.py`'s "roll offsets cancel" argument holds within one session; this hypothesis crosses one.
- Registered cell: `s=0.5, t=1.0`, every level.
- Neighborhood (fixed now): `s in {0.25,0.5,1.0}` x `t in {0.5,1.0,2.0}` = 9 cells x 4 levels = **36 fresh cells**, cumulative 1213 -> 1249. The family for the noise ceiling is 36, not 9, because the best of four levels will be chosen after seeing results.
- Gates (pre-set): the same five as H133-ES / H144 / H145, plus **gate 6, a permutation control** -- hold the session's real price path, substitute another session's level, 200 permutations, seed 20260924, two-sided p < 0.05. The substitute must land inside the session's own range, the constraint H142 lacked.
- Power floor (pre-set): under 200 taken trades -> UNDERPOWERED.
- Scored as realised P&L. **MFE is reported and barred from every gate** -- H142's `react()` measures maximum favourable excursion with hindsight, no stop and no exit, and is the most flattering statistic available.
- Kill rule: no level added after results, no `pdc` promotion, no touch-definition change, no second neighborhood, no regime filter, no re-cut split, no post-hoc pattern filter, and a negative fade result may NOT be read as evidence for momentum.
- Expected failure mode, stated in advance: touch rates high, MFE large because MFE is the maximum of a random walk, realised P&L far worse than the MFE implies, permutation arm resembling the real arm.

## H151. Characterization: is there ANY structure at ES reference levels? (registered 2026-09-24, PRE-RESULT, PRE-CODE)
- Full spec: `graveyard/levels/H151-CHARACTERIZATION-SPEC.md`, sha256 `e1155dfa2183ffdf1ca06db432d7c975feff92c1e47c7785de70d18650585130`.
- A MEASUREMENT, not a strategy: no stop, no target, no costs, no P&L. Answers the question H150 could not -- "this rule loses" is not "no relationship exists".
- Same four levels, same sample, same unwidened touch definition as H150. `pdc` excluded as CONTAMINATED.
- Five statistics: touch rate, rejection rate, extremum rate, absolute move, signed reversion. 200 permutations, seed 20260924.
- Bar: Bonferroni alpha 0.0025 **AND** an effect-size floor (5pp on rates, 0.55 ES pts on prices). Both required; significance alone at n~2000 is worthless.
- Control: another session's offset from the 09:30 open, in points. Registered validity gate: VOID if >10% of control levels fall outside the session range.
- Every outcome's meaning fixed in advance, including that a clearing statistic does NOT reopen H150 and does NOT authorize a trade.
- **VOID.** 51.7% out of range. Zero cells consumed.

## H152. Same, scale-invariant control (registered 2026-09-24, PRE-RESULT, PRE-CODE)
- Full spec: `graveyard/levels/H152-CHARACTERIZATION-SPEC.md`. Everything inherited from H151 except the control, which carries the offset in units of the receiving session's opening-range height.
- **VOID.** 52.9% out of range -- but the gate was mis-specified, not the control. See the verdict.

## H153. Same, corrected validity gate. FINAL ATTEMPT (registered 2026-09-24, PRE-RESULT, PRE-CODE)
- Full spec: `graveyard/levels/H153-CHARACTERIZATION-SPEC.md`, sha256 `2d2af08c727c0f305d8c5ed922d47aa10870ea8eece97d995acf4eb133e33674`.
- Only change from H152: the gate becomes **asymmetry between the arms** -- VOID if `abs(control out-of-range - real out-of-range) > 10pp`. That is the condition that would have caught H142; the absolute-rate version forbade the control from resembling what it controls for.
- Registered as the last attempt: if the gate fires, the line closes and no fourth control is written.
- Contamination: `pdh`'s real-arm descriptives were seen during the two VOIDs. No control statistic was ever produced, so the comparison stayed blind on all four levels.

## H154. Month-end rebalance flow on ES (registered 2026-09-24, PRE-RESULT, PRE-CODE)
- Full spec: `graveyard/calendar/H154-MONTH-END-FLOW-SPEC.md`, sha256 `22b425868ef0d820a5116715a261ce911aa9eb46ade6fd293baeae77604ea64b`, committed in `9c05d81` before `h154_run.py` existed.
- **First hypothesis in this project generated from a named mechanism rather than a pattern search.**
- Mechanism: fixed-weight mandates (60/40 pensions, target-date funds) end a strong equity month overweight equities and are REQUIRED to sell into the month-end; a weak month requires buying. The counterparty is a mandate, not an opinion.
- **Direction is derived, not fitted:** `R_m > 0` -> SHORT, `R_m < 0` -> LONG. A sign flip after results is forbidden by the kill rule.
- Rule: `R_m` measured from the prior month's last 15:55 close to the entry day's; enter at the 15:55 OPEN of the k-th-to-last eligible session; exit at the 15:55 OPEN of the last; one ES contract; $27.50 round trip; at most one trade per month; no stop, the holding period is set by the calendar.
- Registered cell: `k=3, theta=0.0`. Neighborhood: `k in {1,3,5}` x `theta in {0.0,0.01,0.02}` = 9 cells. Cumulative 1259 -> 1268.
- Gates: the standard five, with **gate 4 scored against `data/benchmark_bars_tr.csv`**, the total-return file, deliberately the harder bar.
- Power registered in advance: n <= ~192 is the entire population of month-ends in 16.1y, SE on annualised Sharpe ~0.249, so only a large effect is detectable. The 200-trade floor was deliberately NOT applied and the reason was stated before the run.
- Expected failure mode, stated in advance: an old, widely published effect, so a small gross edge mostly eaten by costs.

## H155. Pre-FOMC announcement drift on ES (registered 2026-09-24, PRE-RESULT, PRE-CODE)
- Full spec: `graveyard/events/H155-PRE-FOMC-SPEC.md`, sha256 `91caf8645106fa063a7c98d484b019cd5284fa23cec47d5011455fed971fc9a8`, committed in `70a55f6` before `h155_run.py` existed. Dates: `graveyard/events/fomc_dates.py`, sha256 `95d1e73ef2219eb77bc5408d8299f492d02905dd6cae5241c1b1e1cb03e5a789`.
- **First event-driven hypothesis in the register** — before this, zero hypotheses mentioned news, earnings, events or announcements.
- Mechanism (Lucca & Moench 2015): equity excess returns are abnormally high in the 24h before a SCHEDULED FOMC announcement, as compensation for holding risk into a known high-uncertainty release. The counterparty is an investor de-risking ahead of a known event.
- **Direction fixed by the mechanism: LONG.** Sign flip forbidden.
- Events: 133 scheduled announcement days 2010-2026, taken from the Federal Reserve's own calendar pages, not from memory. Unscheduled meetings, emergency meetings, conference calls, notation votes and one cancelled meeting are excluded and listed individually in the spec.
- Rule: enter at the 13:45 ET OPEN of the d-th eligible session before the announcement day; exit at the 13:45 ET OPEN on the announcement day; one ES contract; $27.50 round trip. 13:45 rather than 14:00 because the release time was not constant across the sample; the window therefore never overlaps the announcement.
- Registered cell `d=1`. Neighborhood `d in {1,2,3}` = 3 cells. Cumulative 1268 -> 1271.
- Gates: the standard five, gate 4 against `benchmark_bars_tr.csv` at `periods=252` under `fill_flat` — fixing the annualisation bug found in H154's runner.
- Power registered in advance: ~130 events is the entire population, SE on annualised Sharpe ~0.248, only a large effect detectable. The 200-trade floor deliberately not applied, reason stated before the run.
- Expected result, registered: post-publication decay. **This prediction turned out to be wrong in direction** — see the verdict.

## H156. Pre-FOMC drift, FORWARD-ONLY (registered 2026-09-24, n=0, evaluated ONCE at n=50)
- Full spec: `graveyard/events/H156-PRE-FOMC-FORWARD-SPEC.md`.
- Forward-only successor to H155. **Current n = 0. DO NOT PEEK.**
- Rule identical to H155's registered cell and nothing is tunable: scheduled FOMC announcements after 2026-09-18; LONG from 13:45 ET the session before to 13:45 ET on announcement day; one ES contract; $27.50 round trip. **One cell. A forward test has no search.**
- Evaluated once at n=50 on two gates: net > 0, and a 95% CI on the Sharpe that excludes zero. Gate 3 is not applied because N=1.
- Why: H155's holdout Sharpe was +0.5635 with 5.75 holdout years; the CI needs **12.1 years** to exclude zero, a shortfall of **6.3 years / 51 meetings**. Evidence grows as sqrt(time) and no additional hypothesis shortens it.
- Expected completion ~2032.
- Kill rules: no peeking (an interim look voids and restarts), no promoting H155's d=2 cell, no sign flip, no filter, no regime conditioning.

---

# Register reconciliation, 2026-10-06

H157-H162 were registered by commit (spec file committed before any data or
code) but never indexed here. The entries below are an INDEX ONLY, added
after the fact; the spec at the registration commit is the registration.
sha256 prefixes checked 2026-10-06: every spec on disk is byte-identical to
the version in its registration commit.

IDs H27, H137, H138, H139 live in `firm/EDGEBOT-HYPOTHESES.md` and stay there.
EdgeBot and Graveyard do not share a register.

## H157. Aggressor-signed order-flow reversion on ES (registered 2026-09-24, commit 22b0f04, INDEXED 2026-10-06)
- Spec: `graveyard/orderflow/H157-ORDERFLOW-REVERSION-SPEC.md`, sha256 `666fd9c26108...`
- Status: **NOT RUNNABLE.** Gate unreachable at any price (`graveyard/orderflow/H157-GATE-IS-UNREACHABLE.md`). Superseded in practice by H160.

## H158. Forward archive of aggressor-signed crypto flow (registered 2026-09-24, commit c2c6158, n=0, INDEXED 2026-10-06)
- Spec: `graveyard/H158-FORWARD-FLOW-SPEC.md`, sha256 `2d3525c126f2...`
- Status: **FORWARD, OPEN.** Evaluated once at n=500 days (~2028-Q3). No peeking.

## H159. Post-earnings announcement drift, 89 equities (registered 2026-09-29, commit 86bff8b, INDEXED 2026-10-06)
- Spec: `graveyard/fundamentals/H159-EARNINGS-SURPRISE-SPEC.md`, sha256 `aca9b7431c03...`
- Status: **OPEN, DATA INCOMPLETE.** Backfill 22 of 87 symbols (commit 0119af6). Not scored.

## H160. Order-flow IC replication on ES (registered 2026-10-01, commit a28d952, INDEXED 2026-10-06)
- Spec: `graveyard/orderflow/H160-FLOW-IC-REPLICATION-SPEC.md`, sha256 `e57ec791b3e0...`
- Status: scored, NOT CONFIRMED. See VERDICTS.md H160.

## H161. Crypto vol-scaled momentum: regime or effect (registered 2026-10-01, commit 02d5530, INDEXED 2026-10-06)
- Spec: `graveyard/crypto/H161-VOLSCALED-REGIME-SPEC.md`, sha256 `34a3a5b12cac...`
- Status: scored, NOT CONFIRMED. See VERDICTS.md H161.

## H162. Counterparty gate meta-test (registered 2026-10-01, commit f3e31be, INDEXED 2026-10-06)
- Spec: `graveyard/mechanism/H162-COUNTERPARTY-GATE-SPEC.md`, sha256 `29ba83cb108d...`
- Status: scored, GATE DROPPED. See VERDICTS.md H162.

---

# Imported register: `tsahalisp/gex-vol-research` (Devin), imported 2026-10-06

Sixteen hypotheses registered and scored in a separate repo (HEAD `0c14009`).
They count against this register's search from today: same researcher, same
ES/NQ history, overlapping ideas. Graveyard IDs H163-H178 map 1:1 to that
repo's H-001..H-016. The spec of record is the file in that repo, not this
index.

**Provenance caveat, stated once for all sixteen.** H-001..H-009: that repo's
own README says its git history starts AFTER scoring; snapshots of the
original registrations sit in `research/preregistration/` with source-commit
metadata from another project, not verifiable from here. H-010..H-016: each
has a "Register ... before scoring" commit, but the register and score
commits are 17-56 seconds apart (e.g. 293f00c 14:24:08 -> 0c14009 14:24:56).
Commit order is shown; that results were unseen at registration is not.
Treat these as weaker-provenance than H1-H162.

**Overlaps with existing Graveyard ideas (do NOT count as new families):**
H163/H174 ~ levels/C-SETUP line · H177 = H154 month-end flow (same mechanism,
second scoring on the same ES history) · H176 ~ gap-fill line · H175 ~ YT1
intraday momentum · H167/H170 ~ TS trend family.

## H163. First close through PDH continues 30 min (imported 2026-10-06 from gex-vol-research H-001)
- Data: ES 1m. Spec of record: `hypotheses/H-001 *.md` in that repo. Verdict: VERDICTS.md H163.

## H164. Level fades work better on high-GEX days (imported 2026-10-06 from gex-vol-research H-002)
- Data: ES/NQ 1m + SqueezeMetrics GEX. Spec of record: `hypotheses/H-002 *.md` in that repo. Verdict: VERDICTS.md H164.

## H165. Level breaks work better on low-GEX days (imported 2026-10-06 from gex-vol-research H-003)
- Data: ES/NQ 1m + GEX. Spec of record: `hypotheses/H-003 *.md` in that repo. Verdict: VERDICTS.md H165.

## H166. Last-30-min momentum on low-GEX days (imported 2026-10-06 from gex-vol-research H-004)
- Data: ES/NQ 1m + GEX. Spec of record: `hypotheses/H-004 *.md` in that repo. Verdict: VERDICTS.md H166.

## H167. Trend following on 21 liquid futures, after costs (imported 2026-10-06 from gex-vol-research H-005)
- Data: 21 futures daily. Spec of record: `hypotheses/H-005 *.md` in that repo. Verdict: VERDICTS.md H167.

## H168. Selling SPX puts beats owning the S&P 500, risk-adjusted (imported 2026-10-06 from gex-vol-research H-006)
- Data: Cboe PUT/WPUT. Spec of record: `hypotheses/H-006 *.md` in that repo. Verdict: VERDICTS.md H168.

## H169. GEX as on/off switch for weekly put selling (imported 2026-10-06 from gex-vol-research H-007)
- Data: WPUT + GEX. Spec of record: `hypotheses/H-007 *.md` in that repo. Verdict: VERDICTS.md H169.

## H170. A trend sleeve improves an S&P 500 position (imported 2026-10-06 from gex-vol-research H-008)
- Data: futures + S&P TR. Spec of record: `hypotheses/H-008 *.md` in that repo. Verdict: VERDICTS.md H170.

## H171. GEX improves next-day ES vol forecast beyond HAR+VIX (imported 2026-10-06 from gex-vol-research H-009)
- Data: ES/NQ RV + GEX + VIX. Spec of record: `hypotheses/H-009 *.md` in that repo. Verdict: VERDICTS.md H171.

## H172. H171's gain survives GEX lagged one release (imported 2026-10-06 from gex-vol-research H-010)
- Data: same. Spec of record: `hypotheses/H-010 *.md` in that repo. Verdict: VERDICTS.md H172.

## H173. Vol-managed S&P 500 beats buy-and-hold risk-adjusted (imported 2026-10-06 from gex-vol-research H-011)
- Data: S&P TR, T-bills. Spec of record: `hypotheses/H-011 *.md` in that repo. Verdict: VERDICTS.md H173.

## H174. First close through a round number continues 30 min (imported 2026-10-06 from gex-vol-research H-012)
- Data: ES/NQ 1m. Spec of record: `hypotheses/H-012 *.md` in that repo. Verdict: VERDICTS.md H174.

## H175. First half hour predicts last half hour (imported 2026-10-06 from gex-vol-research H-013)
- Data: ES/NQ 1m. Spec of record: `hypotheses/H-013 *.md` in that repo. Verdict: VERDICTS.md H175.

## H176. Small opening gaps fade in the first hour (imported 2026-10-06 from gex-vol-research H-014)
- Data: ES/NQ 1m. Spec of record: `hypotheses/H-014 *.md` in that repo. Verdict: VERDICTS.md H176.

## H177. Month-end stock/bond rebalancing sets last session's direction (imported 2026-10-06 from gex-vol-research H-015)
- Data: ES/NQ 1m. Spec of record: `hypotheses/H-015 *.md` in that repo. Verdict: VERDICTS.md H177.

## H178. Stocks far ahead of bonds (decile) predicts next session (imported 2026-10-06 from gex-vol-research H-016)
- Data: ES/NQ 1m. Spec of record: `hypotheses/H-016 *.md` in that repo. Verdict: VERDICTS.md H178.

---

# REGISTER FROZEN 2026-10-06

No new hypotheses are registered. Open items continue on their own clocks
only: H156 (FOMC forward, n=50), H158 (flow archive, ~2028-Q3), H159 (data
incomplete; finishing the backfill does not need a new ID). Any test proposed
after this line needs Peter's explicit unfreeze, written here, first.

# SCOPED UNFREEZE 2026-10-06 (Peter: "sure", in session, to the proposal below)

Exactly two new IDs may be registered: **H179** (multi-asset risk-premia
portfolio, Phase 1) and **H180** (forward-only GEX test). Nothing else. If H179
fails its gates, or drifts outside its backtest band on paper, Phase 1 ends
and the register re-freezes automatically. A third idea needs a new written
unfreeze line here.

## H179. Multi-asset risk-premia portfolio (registered 2026-10-06, commit 4d728d9, PRE-DATA)
- Spec: `graveyard/portfolio/H179-RISK-PREMIA-SPEC.md`, sha256 `944781d331d4...`
- SPY/EFA/IEF/GLD/DBC, 12-1 trend filter, inverse-vol, 10% vol target, no leverage, monthly. 6 cells. Gate 4 changed (declared pre-data): Sharpe >= SPY and maxDD <= 0.6x SPY. Prediction: FAIL.

## H180. GEX availability before the next session (registered 2026-10-06, commit 4d728d9, FORWARD, n=0)
- Spec: `graveyard/gamma/H180-GEX-AVAILABILITY-SPEC.md`, sha256 `a5afbb586def...`
- Evaluated once at n=60 covered sessions. Prediction: PASS.

# RE-FROZEN 2026-10-06 (automatic, H179 kill rule)
H179 NOT CONFIRMED -> Phase 1 ended. Only H180 (forward) remains open under the
scoped unfreeze. Any new ID needs a new written unfreeze line.

# SCOPED UNFREEZE 2026-10-06, Phase 2 (Peter: "unfreeze for phase 2 and go")

Exactly one new ID may be registered: **H181**, a breadth test on a
point-in-time US stock universe that includes delisted names. No data is bought
until Peter approves a precise quote ($50/item cap unless he waives it in
writing). If H181 fails its gates, Phase 2 ends and the register re-freezes.
H180 continues on its own clock.

## H181. Breadth momentum on CRSP (registered 2026-10-06, commit e5cb6d5, PRE-DATA)
- Spec: `graveyard/breadth/H181-BREADTH-MOMENTUM-SPEC.md`, sha256 `07343b36bb19...`
- 12-1 momentum, top-1000 VW decile long-short, size-graded costs, 1994+, holdout 2010+. 6 cells. Gate 4 = CAPM alpha t>2. Prediction: FAIL.

# RE-FROZEN 2026-10-06 (automatic, H181 kill rule)
H181 NOT CONFIRMED -> Phase 2 ended. Only H180 (forward, timing) remains open.
Any new ID needs a new written unfreeze line.

# SCOPED UNFREEZE 2026-10-06, CRSP research (Peter: "lets do a and b, unfreeze both")

Two new IDs may be registered: **H182** (multi-factor composite on CRSP +
Compustat) and **H183** (post-publication replication study of 12 published
anomalies, sub-tests H183.1-H183.12). WRDS data is academic, non-commercial
use only: nothing here becomes a live trading signal without re-testing on
commercially licensed data. H182 FAIL re-freezes the register; H183 reports
whatever it finds and has no kill rule.

## H182. Multi-factor composite on CRSP + Compustat (registered 2026-10-06, commit 5d66002, PRE-DATA)
- Spec: `graveyard/factors/H182-MULTIFACTOR-SPEC.md`, sha256 `45065f84cd4f...`. Prediction: FAIL narrowly.

## H183. 12-anomaly post-publication replication (registered 2026-10-06, commit 5d66002, PRE-DATA)
- Spec: `graveyard/factors/H183-REPLICATION-SPEC.md`, sha256 `59ecb1181682...`. Sub-tests H183.1-H183.12. Prediction: at most 4 of 12 survive at t > 2.

# RE-FROZEN 2026-10-06 (automatic, H182 kill rule)
H182 NOT CONFIRMED -> research phase ended. H183 reported (study). Only H180
(forward, timing) remains open. Any new ID needs a new written unfreeze line.

# SCOPED UNFREEZE 2026-10-06, Phase 3 (Peter: "unfreeze phase 3, 6 tests")

Exactly six new IDs may be registered: **H184-H189**, all in one spec file,
using only data already on disk plus public Fama-French factors. One test per
week by scheduled task, in ID order. Gate 3 is raised to N = 180 (every verdict
in the register). 0 of 6 CONFIRMED closes the CRSP/Compustat line and re-freezes
the register. Any CONFIRMED still means no live money: WRDS data is academic use
only, so a pass leads to a separately registered re-test on commercial data.

## H184-H189. Phase 3 batch (registered 2026-10-06, PRE-DATA)
- Spec: `graveyard/phase3/PHASE3-SPECS.md`, sha256 `d3e5ffd8da4a...`; code `p3sig.py` `57f673a7d2a6...`, `p3_run.py` `d12f7cd1e470...`
- H184 liquid quarterly momentum (top 500). Prediction: FAIL.
- H185 volatility-scaled momentum. Prediction: FAIL.
- H186 52-week-high proximity. Prediction: FAIL.
- H187 residual (FF3) momentum. Prediction: FAIL, closest of the six.
- H188 same-month seasonality. Prediction: FAIL.
- H189 10-month market trend timing (long-only gate 4). Prediction: FAIL.

# PAPER-PRACTICE 2026-10-06: H157 rule in Sierra Chart sim (NOT A HYPOTHESIS, NO ID)

Peter: "the orderflow lead we found intrigues me and i want to test it on my paper
account" ... "okay to everything you said you have my approval to work".

This is practice on the live pipeline, not a test. **It cannot produce a verdict
and cannot reopen the order-flow line**, which H160 closed on 2026-10-01 (rho
-0.0087, p 0.0187, gates 1 and 2 failed). No register ID is used; the register
stays frozen. Paper P&L from this run is never cited as evidence for or against
anything, in either direction.

- Rule: H157 spec section 2, frozen, unchanged (big_delta from >=10-lot aggressor
  prints per 1-min ES bar; trailing-20-session p10/p90; fade; k=5; clip +/-1;
  flat at the 15:59 bar close; RTH only). 1 ES contract in Sierra's sim account;
  the report also prints the MES equivalent (P&L / 10).
- Where: Sierra Chart Trade Simulation Mode on the free 10-minute-delayed CME feed
  (Package 3 cannot activate real-time Denali data; real-time without a funded
  futures account is the $78/month professional E-mini rate). Signal and fills both
  use the delayed data, so the book is internally consistent but 10 minutes behind
  the real market. Sim fills at the touch flatter real execution.
- Code: `graveyard/orderflow/paper/` (Sierra study `H157PaperPractice.cpp`, reference
  `h157_paper_ref.py`, health/P&L report `paper_report.py`, `diff_dump.py`).
- Verified before going live (2026-10-06):
  - Sierra data reproduces the Databento signal only with sub-trades re-bundled:
    big_delta equal on 100% of 13,290 RTH minutes (35 sessions, ESU26, Jun-Jul 2026);
    per-record (unbundled) matches 1.1%. The study defaults to re-bundled.
  - The C++ study equals the pandas reference on every RTH bar: big_delta, p10, p90,
    signal, target (ESU26 16,200 bars / 42 sessions; ESZ26 18,728 bars / 109 sessions).
  - Replay of 2026-10-05 at 240x in sim: orders fire, flat at the close, position
    equals the prior bar's target on 94.3% of bars (22 of 390 one bar late).
    First replay (orders at a closed-bar index, Exit calls) was broken: fixed by
    ordering on the last bar index and flattening with FlattenPosition.
- Cost for any P&L read-out: `graveyard/lib/costs.py` ES round trip ($29.48 with
  1 tick/side slippage, an assumption).
- Expected result, stated now: negative after costs. H160's out-of-sample IC is 37%
  of discovery; scaling the discovery edge (+1.01 ticks/trade) gives about +0.4 ticks
  gross against about 2.4 ticks round trip at costs.py ES rates.
- Known wrinkle: the trailing-20-session thresholds on ESZ26 still include a few
  pre-roll (back-month) sessions until about 2026-10-09.
- Stop rule: Peter decides when to stop. No longer than the Sierra paid period
  (ends 2026-11-28) unless he renews.

# SCOPED UNFREEZE 2026-10-07, Phase 4 (Peter: "i like and want to try all of these")

Up to four new IDs, **H190-H193**, one per idea below. Each ID is registered PRE-DATA
only after (1) its data is confirmed obtainable and (2) a power check, written before
any signal is paired with any outcome, shows the test can resolve. An idea that fails
either check is recorded here as ANSWERED and never runs. Gate 3 uses N = 184
(every verdict on file plus these four). 0 CONFIRMED re-freezes the register.

| ID | Idea | Data | Status at unfreeze |
|---|---|---|---|
| H190 | VIX futures roll / carry (short front VX in contango) | Cboe free per-contract daily CSVs, 2013 onward (pre-2013 not on Cboe's CDN; 2008 is NOT in sample, disclosed) | data confirmed, power check pending |
| H191 | Monthly-expiration pinning of ES/SPX near strikes (Ni, Pearson & Poteshman 2005 mechanism) | owned ES 1-min bars | power check pending |
| H192 | S&P 500 addition/deletion effect | CRSP via WRDS (academic) + public change lists | predicted FAIL: Greenwood & Sammon (2024) find additions earned 7.4% in the 1990s and under 1% in the 2010s |
| H193 | Level-1 order-book imbalance predicting ES moves at horizons a ~50 ms retail trader can reach | Databento TBBO, quote $245.31 for one year (9.4 GB). **Above the $50 item cap: needs Peter's explicit purchase approval** | blocked on purchase |

## Phase 4 pre-registration checks, 2026-10-07 (none of these pairs a signal with an outcome)

| ID | Check | Result | Status |
|---|---|---|---|
| H190 | Power. `graveyard/vix/h190_power.py`: 174 monthly VX contracts (455 weeklies dropped), 3,457 days 2013-01-02..2026-09-28 (13.74 yr); short-in-contango 85.4% of days; outcome sd $1,176/day, excess kurtosis 38 | True annual Sharpe needed: 0.85 (80% power, 1% one-sided), 0.87 (Gate 3 bar), **0.98** (80% chance both halves > 0.5). Kurtosis widens the Sharpe SE only ~2% at S=1 (Mertens; zero skew assumed). The only published figure found for a related VX term-structure rule is Sharpe 0.36 (Cheng, via Quantpedia), well below 0.98. No pre-2013 data on Cboe's CDN, so the sample can't grow | **ANSWERED: underpowered. Never runs.** |
| H191 | Power. `graveyard/pinning/h191_power.py`: 195 usable monthly-opex days (16.25 yr) in owned ES 1-min bars. Signal: distance from the 14:00 ET price to the nearest 25-pt level (sd 7.52 pts). Outcome: 14:00 to 15:59 change, sd 13.97 pts | MDE ρ = 0.227 vs break-even ρ = 0.048 (same ~5x gap as T1). At ρ = MDE the net annual Sharpe is 0.55, below the 0.80 Gate 3 bar; clearing Gate 3 needs ρ ≈ 0.30. ES-SPX basis adds unmodelled noise to the strike grid | **ANSWERED: underpowered. Never runs.** |
| H192 | Data. `graveyard/sp500adds/h192_datacheck*.py`: CRSP index lists (`crsp_a_indexes`) are **permission denied** on this WRDS subscription. Compustat `comp.idxcst_his` for the S&P 500 returns only the 503 **current** members (removed members missing, so it carries survivorship bias). Neither source has announcement dates, and the tradeable window starts at the announcement | No complete, survivor-free add/delete list with announcement dates. The effect was already predicted to FAIL (Greenwood & Sammon 2024) | **ANSWERED: fails data check. Never runs.** |
| H193 | Data purchase | $245.31 TBBO is over the $50 cap | still blocked on Peter's approval |

The math in H190 and H191 was cross-checked blind by GPT-6 Astra (2026-10-07). Its numbers matched. It corrected two things: the kurtosis effect on the Sharpe SE is small, and the H191 Sharpe at the MDE should be quoted net of costs (0.55 rather than 0.69 gross).
Phase 4 status: 0 of 3 eligible ideas registered. H193 is the only Phase 4 ID still open. If it is declined or fails its power check, the register re-freezes.

# DEVIATION 2026-10-07, Phase 3 cadence only (Peter: "do all the free stuff that is open")
PHASE3-SPECS.md section 4 said one test per week. Peter asked for all open free work now, so
H184-H189 run back to back today in ID order. Nothing else changes: the runner is the 014660c
p3_run.py, the spec sha256 is d3e5ffd8da4a, there is one run per ID and no reruns. The data is fixed
(CRSP through 2025-12), so the order and timing cannot change any result. The weekly scheduled task is
paused after the runs.

# RE-FROZEN 2026-10-07 (Phase 3 stop rule)
0 of 6 confirmed (H184-H189); the CRSP/Compustat line is closed. Phase 4 also registered nothing: H190, H191
and H192 are ANSWERED, and T1 is closed. Still open: H180 (forward GEX, evaluated ~Jan 2027) and H193 (waiting on
Peter's TBBO purchase approval; a free route was checked on 2026-10-07: USC WRDS has only TAQ sample days, no full
TAQ and no Intraday Indicators). Any new ID needs a new written unfreeze line.

# GENERAL UNFREEZE 2026-10-08 (Peter: "unfreeze everything")
The register is open. New IDs no longer need a per-batch unfreeze line. Everything that makes a verdict
mean something stays in force:
- Every ID is registered PRE-DATA (or PRE-RESULT with any contamination disclosed) and committed before it runs.
- One run per ID. No reruns, no re-tuning, no re-cut windows. A failure goes to the graveyard.
- The five gates stand. Gate 3's N keeps counting every test the firm has run (cumulative N is reported on every verdict).
- A pre-registration power check is required wherever the effect size is unknown.
- Unfreezing authorizes no spending. Any data purchase still needs Peter's explicit OK (e.g. H193 TBBO $245.31).

## H194. Filtered ES opening-range breakout: three published ORB filters at their stated values (registered 2026-10-08, PRE-RESULT)
- Source: Instagram reel by bennnytrades ("SuperCharging ORB with Research & Volatility"), screen-recorded by Peter on 2026-10-07. The filter settings were read off his TradingView "TradeX QuantORB 1.1" input panel at 0:39. Logged in project doc `claude/idea-intake-log.md`.
- Base rule: H133-ES EXACTLY (`orb.run` defaults): opening range 09:30-09:59, entry = next-minute open after the first 1-minute close outside the range between 10:00 and 11:59, stop = opposite boundary (conservative same-bar), time exit 15:55, one trade per day.
- NEW, the only thing tested: a session may trade only if ALL THREE filters hold. Each uses ONLY sessions before the current one (prior 20 eligible sessions):
  1. Normalized ORB: OR range / mean(OR range, prior 20) in [0.6, 1.5].
  2. ORB / daily ATR: OR range / ATR20 in [0.05, 0.25]. ATR20 = mean true range of the prior 20 eligible sessions' RTH (09:30-15:59) bars, TR = max(H, prev close) - min(L, prev close), where prev close is the previous eligible session's 15:59 close.
  3. Relative volume: OR volume (sum of 09:30-09:59 volume, `es_1m_continuous_v.csv`) / mean(OR volume, prior 20) in [1, 10].
  The first 20 eligible sessions are warm-up and untradeable. His "breakout candle quality" filter was switched OFF in the frame, so it is not used.
- Deviations from the reel, stated now: (a) ES 1-minute data, not MNQ on a 15-minute chart. (b) The 30-minute range is held at H133-ES's value as the control. Changing it would be a re-tune of a buried rule. (c) His volatility-surface "regime engine" is excluded because we have no IV history.
- Contamination: H133-ES, H144 and H145 already ran on this exact sample. The unfiltered rule is known: all 9 cells negative, 99.7% max drawdown. This test asks only whether the filter subset differs. It is NOT a fresh look at ORB.
- Data: `firm/data/es_1m_continuous.csv` (prices, through `orb.sessions`) and `es_1m_continuous_v.csv` (same bars plus volume). $0.
- Costs: `graveyard/lib/costs.py` ES = $29.48 round trip (1 tick/side + $2.24 commission/side). Stress: $40.00 round trip.
- Gates (all five must hold), identical machinery to H144/H145 (`h144_h145_run.gates` logic, single cell):
  1. Net > 0 AND Sharpe > 0.5 in BOTH halves (train = first 65% of eligible sessions, holdout = last 35%; untraded days count as 0).
  2. Holdout 95% block-bootstrap CI on Sharpe excludes zero.
  3. Registered cell Sharpe > sqrt(2 ln N)/sqrt(Y) with N = 37 (ORB family on this sample: H133-ES 18 + H144 9 + H145 9 + H194 1). The cumulative firm-wide ceiling is reported, not gated.
  4. BEATS spy_buyhold on a paired difference.
  5. The $40 stress does not turn gate 1 or 2 negative.
- Power floor: at least 200 taken trades, otherwise the verdict is UNDERPOWERED (not a pass).
- Reported, not gated: number of sessions passing each filter and all three; trades; win rate; geometric return; max drawdown; worst day; per-regime breakdown; and the same rule unfiltered on the same sessions for comparison.
- Prediction (written now): FAIL. Holdout Sharpe between -0.5 and +0.3. The filters cut trade count roughly 3-5x without turning a rule with all-negative cells positive.
- Kill rule: fail any gate -> graveyard. A pass licenses only a tick-data re-test plus a forward paper period, never a trade.

## MIDAS (SEC market-structure metrics) — pre-registration data and power check, 2026-10-08: ANSWERED, never runs
Peter: "yes do the midas test." Checked before any signal was paired with a return (`graveyard/midas/midas_check.py`):
- Data: `midas.security` has 21.1M daily rows, 3,519 dates from 2012-01-03 to 2025-12-31, and 14,891 tickers (13.4M stock rows, 7.7M ETF rows). Fields include cancel_to_trade, hidden_rate/volume and oddlot_rate/volume. 4.6-6.2% of metric values are null. The CRSP-TAQ link table `wrdsapps_link_crsp_taq.tclink` stops at 2014-12-31, so 2015+ would need a ticker-date link through CRSP stocknames.
- Candidate (not registered): abnormal odd-lot volume share as a retail-attention proxy, long low / short high, top 1,000 stocks, monthly. The MIDAS metrics are unsigned, so any test must take its direction from a theory like this one.
- Power (uses only the sample length): about 13.4 years after a 6-month warm-up, holdout 6.7 years. The Gate 3 bar at N = 186 is 1.25 on the holdout (0.88 on the full sample). 80% power to clear it needs a true Sharpe of about 1.57. 80% power for Gate 1 needs about 0.98. The register's own 2010-2025 cross-sectional holdouts (H184-H188) ran from -0.46 to +0.21, and H183's 12 published anomalies were indistinguishable from zero.
- The bar depends on years, not trading frequency, so a weekly or daily MIDAS signal faces the same requirement.
- Verdict: no MIDAS-based test can resolve a plausible effect, because the data starts in 2012. ANSWERED, and nothing is registered. Reopen only if a source with the same fields before 2012 appears.

## H195. IBS mean reversion on SPY, daily (registered 2026-10-08, PRE-DATA for this rule)
- Source: Peter asked to test the untested ideas from @quantifiedstrategies (Instagram blocked; their Substack IBS post combines IBS with a 3-day RSI, but those rules are paywalled). The rule below is the PUBLIC IBS rule from the literature (Pagonidis 2013, "The IBS Effect", NAAIM), not their version. The RSI filter is NOT used.
- IBS_t = (Close - Low) / (High - Low) of SPY's day t (raw OHLC; days with High = Low get IBS = 0.5).
- Rule: flat → buy at the close of day t when IBS_t < 0.2. Long → sell at the close of the first later day with IBS > 0.8. No stop, no max hold. Long-only, 1x. Cash earns the risk-free rate when flat.
- Returns: SPY total return from adjusted closes (yfinance `auto_adjust=True`), close-to-close. Costs 1 bp per side (2 bp round trip). Stress: 5 bp per side.
- Sample: SPY 1993-02-01 → 2026-10-07. Halves split at the midpoint date. Risk-free: Ken French daily-equivalent (monthly RF / trading days in month) from `graveyard/phase3/data/F-F_Research_Data_Factors.csv`. Sharpe on excess returns.
- Gates (H189 long-only template):
  1. Sharpe > 0.5 in both halves.
  2. Second-half 95% block-bootstrap CI on Sharpe excludes 0.
  3. Second-half Sharpe > sqrt(2 ln 188)/sqrt(Y2), about 0.79 for Y2 ≈ 16.8. N = 188 counts H195 and H196.
  4. Long-only rule: second-half Sharpe ≥ SPY buy-and-hold Sharpe AND max drawdown ≤ 0.6x SPY's, both measured in the second half.
  5. The 5 bp/side stress still passes gates 1-2.
- Power (sample length only): 80% power to clear gate 3 needs a true second-half Sharpe of about 1.0. A large published effect is detectable; a decayed one is not.
- Contamination: SPY prices were used as a benchmark throughout the register, and H179 traded SPY monthly. No IBS-type signal was ever computed.
- Prediction: FAIL. Full-sample Sharpe positive but the second half (2010-2026) weaker, 0.2-0.7. It fails gate 3 and/or 4 against a strong 2010-2026 SPY.

## H196. Turnaround Tuesday on SPY (registered 2026-10-08, PRE-DATA for this rule)
- Source: the same @quantifiedstrategies request. Their stated basic-version stats are 212 trades, +0.3% per trade, 56% wins, 1.8% CAGR, 2.5% exposure; their exact rules are paywalled. Public rule used here: if Monday's close < the previous trading day's close, buy SPY at Monday's close and sell at Tuesday's close. If Monday is a holiday, the week has no trade. If Tuesday is a holiday, exit at the next trading day's close.
- Returns, costs, sample, risk-free, halves, gates 1-5 and N: identical to H195.
- Power: same sample, so the same ~1.0 true Sharpe is needed. With ~2.5% exposure, the daily series is mostly risk-free, so a small mean can still produce a moderate Sharpe.
- Contamination: as H195. In addition, the register's descriptive London/NY look on 2026-10-07 touched ES day-of-session moves but not day-of-week.
- Prediction: FAIL gate 4. Sharpe below SPY buy-and-hold in 2010-2026, with the drawdown condition passing.
- Not tested from the same account: the Monday-Tuesday Nasdaq trade (rules not public) and Russell rebalancing (needs reconstitution dates, same family as H192).

## H197. IBS replication on ES futures (registered 2026-10-08, PRE-RESULT, replication of H195)
- Purpose: the separately registered re-test that H195's CONFIRMED verdict requires. The rule is identical to H195 (buy at the close when IBS < 0.2, sell at the first close with IBS > 0.8, long-only, 1x). The instrument and data are different: ES futures RTH bars from our own Databento purchase (`firm/data/es_1m_continuous.csv`), not yfinance SPY.
- Session bars: for each date with a 15:59 ET bar and at least 380 RTH minutes, High/Low = max/min over 09:30-15:59 and Close = the 15:59 bar's close. Early-close and incomplete days are excluded and counted.
- Rolls: the daily return is close_t / close_{t-1} - 1 only when both days are on the same contract. On a contract-change day the held return is set to 0 (66 rolls, disclosed). There is no back-adjustment.
- Returns as a % of notional (futures are already excess returns, so no risk-free). Cost: $29.48 round trip per ES (costs.py) as a % of notional at entry. Stress: $40.
- Sample: 2010-06-07 to 2026-09-18. Halves split at the midpoint date.
- Independence, disclosed: this overlaps H195's second half in time, and ES tracks SPY closely. It replicates the implementation and data source, NOT the time period. The forward paper period below is the true out-of-sample.
- Gates (replication gates, set now; no Gate 3 search penalty, because the parameters are inherited from H195 unchanged and nothing is searched):
  R1. Full-sample 95% block-bootstrap CI on Sharpe has lower bound > 0.
  R2. Sharpe > 0.5 in both halves.
  R3. Under the $40 stress, the full-sample mean daily return is > 0 and R1 still holds.
  R4. Long-only: full-sample Sharpe ≥ ES buy-and-hold Sharpe (same roll treatment) AND max drawdown ≤ 0.6x buy-and-hold's.
- Power (sample length only): about 16 years, so an observed Sharpe above about 0.49 is needed for R1. If the true Sharpe is about 0.9 (as in H195), power is about 95%.
- Prediction: REPLICATES. Full Sharpe 0.6-1.0. Fewer trades than H195 (2010+ only).
- If it fails: H195's confirmation is downgraded to "SPY-data only" and no paper capital follows.

## FP-195. Forward paper period for IBS (set 2026-10-08)
- From 2026-10-09 for 3 months (to 2027-01-08). After each close, a daily job computes IBS from that day's SPY bar and records the H195 position. The P&L is recorded on SPY at the close and as the 1-MES equivalent. No orders are sent anywhere.
- This is an implementation check, not evidence: about 3 months is roughly 20-25 trades, far too few for a statistical verdict. Pass = the job runs every trading day with no missed or stale days, the logged signals match a re-computation from a second data source (Twelve Data), and nothing breaks.
- Any real-money decision needs Peter, plus the H197 result and this period's log.

## H198. Williams %R(2) mean reversion on SPY (registered 2026-10-08, PRE-DATA for this rule)
- Source: @quantifiedstrategies Instagram post (read 2026-10-08). Rules are fully stated in the caption. Peter: "test any strategies you can."
- %R(2)_t = -100 x (HH2 - C_t) / (HH2 - LL2), where HH2/LL2 = highest high / lowest low of days t-1 and t (raw OHLC).
- Rule: flat → buy at the close when %R(2) < -90. Long → sell at the close of the first later day when Close_t > High_{t-1} OR %R(2) > -30. Long-only, 1x, cash earns rf.
- Data, costs, risk-free, halves and gates 1-5: identical to H195 (the same cached file `graveyard/spydaily/results/spy_yf_2026-10-08.csv`, 1993-02-01 to 2026-10-07). N = 190 for Gate 3 (H198 and H199 added).
- Overlap with H195, disclosed: the same short-term reversion family on the same instrument and data. The share of H198's in-market days also in H195's will be reported. A pass here is NOT independent evidence for H195.
- Prediction: passes gates 1-2. Second-half Sharpe 0.6-0.9. Gate 4 borderline. Overlap with H195 above 60%.

## H199. SPY new 252-day closing high, hold 21 days (registered 2026-10-08, PRE-DATA for this rule)
- Source: the same post set. Stated: 139 trades, +0.67% average, PF 1.73, 65.5% wins with the 21-day exit.
- Rule: flat → buy at the close of any day whose close is above the highest close of the prior 252 trading days. Hold exactly 21 trading days and sell at that close. No new entries while in a position. Long-only, 1x, cash earns rf.
- Data, costs, risk-free, halves, gates 1-5 and N: identical to H198.
- Prediction: FAIL gate 4. Second-half Sharpe below SPY's (it is a partial-exposure momentum hold in a strong bull market).

## H200. Williams %R(2) replication on ES futures (registered 2026-10-08, PRE-RESULT, replication of H198)
- H198's exact rule on the H197 data and plumbing: ES RTH bars from `es_1m_continuous.csv`, 2010-2026, the same day filter, roll days set to 0, costs $29.48 (stress $40), returns as a % of notional.
- Replication gates R1-R4: identical to H197 (full-sample CI lower bound > 0; Sharpe > 0.5 in both halves; $40 stress keeps R1 with mean > 0; Sharpe ≥ ES buy-and-hold AND max DD ≤ 0.6x buy-and-hold).
- Disclosed: H198 is 89% the same in-market days as H195 (daily return correlation 0.75), and H197 already failed R4 on drawdown alone (0.626x). This is mostly a second look at the same effect.
- Prediction: R1-R3 pass; R4 borderline (drawdown ratio 0.55-0.65).

## H201-H203. Three pre-specified IBS improvements (registered 2026-10-08, PRE-RESULT)
Peter: "is there any way to make the strategies better? ... just do em all." These are exactly three variants, each fixed in advance. There is no parameter search; the IBS thresholds stay at H195's 0.2 / 0.8. Gate 3 N = 193 (H201-H203 added). Common to all three: the yfinance data pulled in the runner and saved; costs 1 bp/side (stress 5 bp); risk-free as in H195; halves split at the sample midpoint; Sharpe on excess returns; gates 1, 2, 3 and 5 as in H195. Gate 4 is per ID, below.

### H201. IBS on an equal-weight 4-ETF book (SPY, QQQ, IWM, DIA)
- Each ETF runs H195's rule on its own data with 1/4 of the capital; flat sleeves earn rf. Daily book return = the mean of the 4 sleeves. Sample: the common start of all four (IWM's first full day, 2000) to 2026-10-07.
- Gate 4 (long-only): second-half Sharpe ≥ SPY buy-and-hold's AND max DD ≤ 0.6x SPY's, same window.
- Contamination: the per-ETF per-trade means (QQQ +0.49%, IWM +0.37%, DIA +0.37%) were seen in the H195 sensitivity check. The book-level Sharpe, drawdown and halves were not.
- Prediction: CONFIRMED. Second-half Sharpe 0.9-1.3 from diversification.

### H202. IBS overlay on buy-and-hold SPY
- Always hold 1.0x SPY. On days H195 would be long, hold 1.5x (the extra 0.5x is financed at rf). Same SPY data and window as H195.
- Gate 4 (overlay, set now): second-half Sharpe ≥ SPY buy-and-hold's AND max DD no worse than 1.15x SPY's. The overlay can't reduce drawdown below holding, so the H195 drawdown test does not apply.
- Prediction: passes gates 1, 2 and 4; Gate 3 marginal. The second-half Sharpe exceeds SPY's by 0.05-0.15.

### H203. IBS with a 200-day trend filter on SPY
- H195's rule, but new entries are only allowed when SPY's close is above its 200-day simple moving average of closes (computed through day t). Exits are unchanged. Same data and window as H195.
- Gate 4: as H195 (Sharpe ≥ SPY's AND DD ≤ 0.6x).
- Prediction: NOT better than H195. The second-half Sharpe is within ±0.15 of H195's 0.93, and the trade count drops by about 30%.

## H204. Where does the IBS return come from: overnight vs intraday (registered 2026-10-10, PRE-RESULT, diagnostic of H195)
- Source: Lou, Polk & Skouras (2019, JFE, "A Tug of War: Overnight Versus Intraday Expected Returns"), cited in two Discord servers (fully hedged 2026-09-19; Ether 2026-10-06). Discord review 2, plan item 1. Peter: "get to work on the plan".
- Type: DIAGNOSTIC, not a strategy. No gates and no Gate 3 count. It decomposes H195's held-day return; it cannot confirm or kill H195.
- Data: the cached H195 file `graveyard/spydaily/results/spy_yf_2026-10-08.csv` (adjOpen and adjClose already in it), 1993-02-01 to 2026-10-07. The position is H195's, recomputed identically (IBS < 0.2 buy at the close, first close with IBS > 0.8 sell).
- Legs for day t: overnight on_t = adjOpen_t / adjClose_{t-1} - 1; intraday id_t = adjClose_t / adjOpen_t - 1. Then (1+on)(1+id) = the adjusted close-to-close return.
- Reported, gross of costs, for (a) H195 held days, (b) all days, (c) H195 flat days:
  - mean overnight, mean intraday, and the overnight share of the summed log return;
  - a 95% CI for the held-day means, by stationary block bootstrap on the held-day series in date order (mean block 10, 5,000 resamples, seed 204);
  - each of these for both halves (split at H195's midpoint date).
- Replication on ES: the H197 data (`firm/data/es_1m_continuous.csv`) and the same 380-minute day filter. Overnight = 09:30 bar open / prior day's 15:59 close; intraday = 15:59 close / 09:30 open. Pairs that cross a roll are dropped and counted. The position is H197's (IBS from the RTH bars).
- Prediction (set now): the overnight leg carries MORE than half of H195's held-day log return on SPY (point estimate 55-75%), and the overnight mean's CI excludes zero. The intraday mean is positive but its CI includes zero. ES shows the same sign pattern.
- What it changes: nothing about H195's verdict. It decides whether H205 (below) is worth anything and tells the paper trader where the return sits.

## H205. IBS overnight-only on SPY (registered 2026-10-10, PRE-RESULT, same commit as H204)
- Rule: on every day H195 is held (a position carried from close t-1), hold SPY only over the overnight leg: buy at close t-1, sell at open t. Be flat intraday, with cash earning rf. Each held day is one round trip.
- Costs: 1 bp per side (2 bp per held day). Stress: 5 bp per side.
- Data, risk-free, halves and gates 1-5: identical to H195. Gate 4: second-half Sharpe ≥ SPY buy-and-hold's AND max DD ≤ 0.6x SPY's. N = 194 for Gate 3 (H205 added; H204 is a diagnostic and is not counted).
- Contamination, disclosed: H195's close-to-close results are known. Its leg split is not; H204 and H205 run in the same script, after this commit.
- Prediction: passes gates 1 and 2 at 1 bp. Gate 5 (stress) FAILS, because 10 bp per held day is about the size of the per-day edge. Gate 4: Sharpe below SPY's.

## H206. Do H195 and H201 survive multiple-testing hurdles? (registered 2026-10-10, PRE-RESULT, diagnostic)
- Source: Harvey, Liu & Zhu (2016, RFS, "...and the Cross-Section of Expected Returns"), from the fully hedged paper list (Discord review 2). Peter: "yes you can do 2 and 3".
- Type: DIAGNOSTIC. No new strategy, no Gate 3 count. It re-scores the register's two CONFIRMED IDs against stricter bars than Gate 3.
- Series: H195's and H201's net daily excess returns, exactly as in their runners (1 bp/side, rf from Fama-French), recomputed from the cached CSVs. Sample: full, and second half (H195 split 2009-11-27, H201 split 2013-08-02).
- Statistic: the t-stat of the mean daily excess return. (a) Plain iid. (b) Newey-West HAC with 10 lags (Bartlett).
- Hurdles, one-sided at 5%:
  - HLZ fixed t > 3.0.
  - Bonferroni, which equals Holm for the top-ranked test, over M = 194 register tests: z = Φ⁻¹(1 − 0.05/194) ≈ 3.47.
  - Bonferroni over the hand-counted effective M = 27 independent ideas (CLAUDE.md, 2026-10-06): ≈ 2.90.
  - BHY is NOT run, because it needs every past test's p-value and those were not stored consistently. Disclosed.
- Decision rule (set now): an ID "SURVIVES" if its full-sample NW t exceeds the M = 194 Bonferroni hurdle. It is "HOLDOUT-SURVIVES" if its second-half NW t also does.
- Contamination, disclosed: both IDs' Sharpe ratios are known, so the plain t ≈ SR × √years is roughly predictable. The new information is the NW correction and the hurdle comparison.
- Prediction: H195 full SURVIVES (plain t ≈ 4.6). H195 second half is borderline (≈ 3.8 vs 3.47) and survives. H201 full SURVIVES (≈ 4.4). H201 second half FAILS the 3.47 bar (≈ 3.5, too close; I predict just below once NW is applied). NW t is ≥ plain t for H195, because its returns are slightly negatively autocorrelated (lo_annualize, 2026-10-10).

## H207. Did the IBS return change after 2008? (registered 2026-10-10, PRE-RESULT, diagnostic)
- Source: Knuteson (2020, arXiv 2010.01727), from the fully hedged list. Per our paper notes, it reports that the index overnight/intraday divergence stopped around 2008.
- Type: DIAGNOSTIC. No gates.
- Data and legs: identical to H204 (SPY cached CSV, adjOpen/adjClose, H195 position). Eras: PRE = 1993-02-01 to 2007-12-31; POST = 2008-01-01 to 2026-10-07.
- Reported per era:
  - H195 net Sharpe (excess, 1 bp/side).
  - Held-day mean overnight, intraday and close-to-close in bp.
  - All-days mean overnight and intraday.
  - The difference POST − PRE in held-day means for each leg, with a 95% CI from a stationary block bootstrap (mean block 10, 5,000 draws, seed 207, each era resampled separately).
- Contamination, disclosed: H204 already reported halves split at 2009-11-27 (held-day overnight 8.69/8.65 bp, intraday 4.69/4.96 bp). A 2008 split is close to that, so this ID adds little. It is run because Peter asked and because the all-days split at 2008 has not been looked at.
- Prediction: held-day legs show no era change (difference CIs include 0). All-days intraday mean is higher POST than PRE (it was −0.73 bp in H204's first half), and the overnight share of the all-days return falls POST.

## H208-H209. IBS breadth and VIX regime (registered 2026-10-10, PRE-RESULT)
Peter: "yes" to plan items A and B ("sum up all the filters ... lay out what we need to keep testing more strategies"). Both use H195's rule unchanged (buy at close when IBS < 0.2, sell at the first close with IBS > 0.8). No parameter search. Costs 1 bp/side (stress 5 bp). Risk-free from the F-F file as in H201. Halves split at the sample midpoint. Gates 1, 2, 3 and 5 as H195. Gate 4 as H201 (second-half Sharpe ≥ SPY buy-and-hold's AND max DD ≤ 0.6x SPY's, same window). Gate 3 N: H208 = 195, H209 = 196. Both run once by `graveyard/spydaily/h208_209_run.py`. The data is pulled from yfinance in the runner and saved to `results/`. Standard rows (cluster_drop by calendar year, win_payoff) are reported for both.

### H208. IBS on a 15-ETF book outside the 4 US index ETFs
- Universe (fixed now): XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY, EFA, EEM, TLT, GLD.
- Each ETF runs H195's rule on its own data. A sleeve enters the book on its 2nd trading day of history. On each day the book is the equal-weight mean of the sleeves that exist that day (flat sleeves earn rf). Sample: 1999-01-04 (the first full sector SPDR year) to 2026-10-07.
- Also reported (diagnostic, no gates): per-ETF net Sharpe, trade count, mean per trade; the book's daily-return correlation with H201's 4-ETF book over the common window; the equity-only sub-book (11 sectors + EFA + EEM) vs the non-equity pair (TLT, GLD).
- Contamination: none of these 15 ETFs has been run through IBS in this register. The IBS literature (Pagonidis 2013 and similar) says the effect is strongest in equity indices and weak or absent in bonds and commodities. I have read that, so the prediction leans on it.
- Prediction: CONFIRMED. Second-half Sharpe 0.8-1.2. At least 11 of the 13 equity ETFs have positive net Sharpe. TLT and GLD each have a net Sharpe below 0.3. Correlation with H201's book is 0.5-0.75.

### H209. IBS on SPY, entries only in high-VIX regimes
- Regime on signal day t: VIX close_t > the median of VIX closes over days t-251..t (point-in-time, no future data). ^VIX daily from yfinance.
- Strategy: H195 on SPY, but a new entry is only allowed when the regime is HIGH. Exits are unchanged. Window: the H195 sample (1993-02-01 to 2026-10-07; the first 252 days after VIX starts are covered because VIX starts 1990).
- Diagnostic (no gates): H195's own trades split by the regime on their entry day. Reports, per regime, N trades, mean return per trade, win rate, mean return per trade divided by entry-day VIX/100/√252 (a vol-normalised mean), and the HIGH − LOW difference in mean per trade with a 95% CI by trade-level bootstrap (5,000 draws, seed 209).
- Contamination: H203 showed that a trend filter hurt H195 because the best entries come in downtrends. High VIX overlaps with downtrends, so I expect the HIGH trades to be the better ones.
- Prediction: Diagnostic: HIGH has the larger mean per trade (CI on the difference excludes 0), but the vol-normalised means are within 30% of each other. Strategy: NOT CONFIRMED. It halves the trade count. Its second-half Sharpe is within ±0.2 of H195's 0.93, and it fails at least one of Gate 3 or Gate 4.

## H210. IBS on SPY with VIX-regime sizing (registered 2026-10-10, PRE-RESULT)
- Source: the H209 diagnostic. High-VIX entries earned 0.55% per trade vs 0.22% for low-VIX entries, and were also better per unit of risk (vol-normalised 0.319 vs 0.191). Peter: "gonna do ... 3" (the sizing variant proposed after H209).
- Rule: H195's entries and exits, unchanged. The regime is the same as H209: VIX close_t > the median of days t-251..t, measured on the ENTRY day. Size is fixed for the whole trade: 1.5x notional if HIGH, 0.5x if LOW. The extra 0.5x is financed at rf; unused capital earns rf. Costs are 1 bp/side times notional (stress 5 bp).
- Daily excess return = w × held × (ret − rf) − w × turnover × cost.
- Window, risk-free, halves, and gates 1, 2, 3 and 5: as H209. Gate 4 as H195 (second-half Sharpe ≥ SPY's AND DD ≤ 0.6x). Gate 3 N = 197.
- **Improvement criterion (set now; this ID is a variant of a confirmed rule, so passing the gates alone proves little):** ADOPT only if all 5 gates pass AND the second-half Sharpe ≥ H195's same-code second-half Sharpe (0.932) + 0.10. Otherwise the verdict is "NOT AN IMPROVEMENT", even if all five gates pass.
- Contamination: the regime split's trade-level means are known (H209). The book-level Sharpe, drawdown and halves under this sizing are not.
- Reasoning behind the prediction: the Sharpe-optimal weight is about mean / variance = (vol-normalised mean) / σ. With σ proportional to VIX, and high-regime VIX roughly double the low-regime level, the optimal HIGH:LOW weight ratio is about (0.319/0.191) / 2 ≈ 0.85. That is near 1:1, not 3:1. So 1.5/0.5 overweights the high-vol trades, adding variance faster than return.
- Prediction: passes gates 1, 2 and 5. Second-half Sharpe 0.80-0.95, i.e. NOT higher than H195. Drawdown is worse than H195's 18.9%, and Gate 4 fails (DD > 0.6x SPY). Verdict NOT AN IMPROVEMENT.
- Also reported: the median VIX on HIGH and LOW entry days (to check the "about double" assumption), the cluster drop by year, and win/payoff.
