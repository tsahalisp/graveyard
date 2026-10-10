# The Graveyard

A one-person research process for testing trading strategies. Every idea is written down and committed **before** I look at its data; the verdict is whatever the pre-set gates say. About 195 verdicts so far. Most ideas are dead, hence the name.

| | |
|---|---|
| Hypotheses registered | H1–H210 |
| Confirmed in markets | **1 family**: IBS mean reversion (H195 SPY, H198 Williams %R, H201 4-ETF book, H208 15 new ETFs) |
| Failed replications kept on record | IBS on ES futures (drawdown 0.63× vs a 0.60× limit); ES order flow (IC fell to 37% of the original) |
| Multiple-testing check | Confirmed IDs clear Bonferroni over 194 tests on Newey-West t (H206) |

## Reproduce the headline in one command

```bash
pip install -r requirements.txt
python reproduce.py
```

It downloads public prices (Yahoo Finance via `yfinance`) and recomputes H195 and H208 against all five gates. On 2026-10-10 it printed:

| ID | Rule | H1 / H2 Sharpe | Noise bar | Max DD (H2) vs SPY | Verdict |
|---|---|---|---|---|---|
| H195 | IBS on SPY, 1993–2026 | 0.80 / 0.93 | 0.79 | 18.9% vs 33.7% | CONFIRMED |
| H208 | Same rule on 15 ETFs it was never tuned on, 1999–2026 | 0.84 / 1.11 | 0.87 | 11.9% vs 33.7% | CONFIRMED |

Yahoo re-adjusts dividends over time, so the third decimal can drift. (H208's registered H2 is 1.113; this script drops the book's first, empty day, which moves the split by one day and prints 1.110.)

## The rule

IBS = (Close − Low) / (High − Low). Buy at the close when IBS < 0.2; sell at the first close with IBS > 0.8. Thresholds were never tuned. Costs are 1 bp per side, stressed to 5 bp.

## The five gates (set before every run)

1. Sharpe > 0.5 in **both** halves of the sample.
2. 95% block-bootstrap lower bound of the holdout Sharpe > 0.
3. Holdout Sharpe > √(2 ln N) / √years, the Sharpe that the best of N worthless strategies reaches by luck. N is the running count of tests in the register, so the bar rises as I test more.
4. Beat buy-and-hold SPY: holdout Sharpe ≥ SPY's and max drawdown ≤ 0.6× SPY's.
5. Still passes 1 and 2 at 5 bp/side.

## Repository map

| Path | What |
|---|---|
| `reproduce.py` | Standalone rerun of H195 and H208 |
| `register/HYPOTHESES.md` | Every pre-registration, in order, with predictions |
| `register/VERDICTS.md` | Every verdict, failures included, with prediction scorecards |
| `PROVENANCE.md` | Commit hashes and timestamps showing spec → runner → result order for the IBS family |
| `lib/` | Validation toolkit: deflated Sharpe, PBO, block bootstrap, Lo (2002) Sharpe, cluster drop, win/payoff, bid-ask bounce check, permutation tests. `python lib/test_validate.py` → 28/28 |
| `ibs/` | The original one-shot runners for H195–H210, as committed. They read paths from the private research repo, so use `reproduce.py` to rerun |
| `data/` | Fama-French factors (risk-free rate), from Kenneth French's data library |

## What this is not

- **Not new alpha.** IBS is a published rule. The work is in testing it honestly: holdouts, rising bars, replications, and stress tests.
- **Not a live track record.** A forward paper log started 2026-10-09.
- **Not cherry-picked.** The register keeps the ~190 failures and my wrong predictions next to the passes. That includes my written prediction that IBS would fail.

## How it was built

I designed the process, the gates and the hypotheses, and made every keep/kill call. Much of the code was written with an AI coding assistant (Claude) working to those specs. The register keeps every rule I set before results came in, including where my own predictions were wrong.

Not included: the sports-betting model (H27, H137–H139), which lives in a separate private project.
