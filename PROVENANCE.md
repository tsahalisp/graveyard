# Provenance: the IBS family (H195–H210)

The research lives in a private repository (it also holds unrelated projects). These are its commits for each ID, in order: registration (spec + prediction), then the runner, then the result. The registering commit always comes before the code that produced the result. Times are git author times (US Eastern). Git times are self-reported, so treat this as a record, not a proof. The private history is available on request.

| Commit | Time | Message |
|---|---|---|
| 43d7f5a | 2026-10-08 13:44 | REGISTER H195 IBS on SPY, H196 Turnaround Tuesday (PRE-DATA) |
| 431bd5d | 2026-10-08 13:45 | H195/H196 runner (before any result) |
| a5f089d | 2026-10-08 13:48 | H195 IBS on SPY CONFIRMED (first in register); H196 Turnaround Tuesday NOT CONFIRMED |
| a04b992 | 2026-10-08 13:52 | REGISTER H197 IBS replication on ES (PRE-RESULT) + FP-195 forward paper period |
| 469d1a8 | 2026-10-08 13:52 | H197 runner (before result) |
| a794d17 | 2026-10-08 13:54 | H197 DOES NOT REPLICATE (R4 DD 0.626x vs 0.6x); H195 downgraded to SPY-data only |
| 7174d87 | 2026-10-08 13:55 | FP-195 forward paper log (launchd 16:20/21:05 ET, no orders); signals verified vs reference on Aug-Oct 2026 |
| ae550fb | 2026-10-08 14:04 | REGISTER H198 Williams %R(2) SPY, H199 252-day high hold 21d (PRE-DATA) |
| ca91a15 | 2026-10-08 14:04 | H198/H199 runner (before results) |
| 429c410 | 2026-10-08 14:05 | REGISTER H200 Williams %R(2) ES replication (PRE-RESULT) |
| 16218ad | 2026-10-08 14:05 | H200 runner (before result) |
| 336619a | 2026-10-08 14:06 | H198 CONFIRMED (same effect as H195), H199 NOT CONFIRMED, H200 DOES NOT REPLICATE |
| 4062e7b | 2026-10-08 14:09 | REGISTER H201 4-ETF IBS, H202 IBS overlay, H203 IBS+200d filter (PRE-RESULT) |
| fcd5c14 | 2026-10-08 14:09 | H201-H203 runner (before results) |
| 01557cf | 2026-10-08 14:10 | H201 4-ETF IBS CONFIRMED; H202 overlay, H203 trend filter NOT CONFIRMED |
| 99a43ae | 2026-10-09 23:48 | Register H204 (IBS overnight/intraday decomposition, diagnostic) and H205 (IBS overnight-only) before any leg split is computed |
| add135c | 2026-10-09 23:49 | H204/H205 runner (before results) |
| 926778f | 2026-10-09 23:50 | H204 diagnostic: IBS return ~2/3 overnight, but IBS adds ~equally to both legs; H205 overnight-only NOT CONFIRMED (G3, G4, G5) |
| 43477aa | 2026-10-10 00:19 | Register H206 (multiple-testing hurdles for H195/H201) and H207 (IBS pre/post 2008), diagnostics |
| 0bc25d1 | 2026-10-10 00:19 | H206/H207 runner (before results) |
| 16920af | 2026-10-10 00:20 | H206: H195 and H201 clear Bonferroni M=194 (NW t 5.60/4.17, 5.11/3.86); H207: IBS not weaker after 2008 |
| c6d59bc | 2026-10-10 00:50 | H208-H209 REGISTERED: IBS 15-ETF book; IBS high-VIX entries (pre-result, N=195/196) |
| 96b4a49 | 2026-10-10 00:51 | H208-H209 runner (before results) |
| 7b883f6 | 2026-10-10 00:52 | H208 CONFIRMED (15-ETF IBS book, H2 1.11, all 15 ETFs positive, corr 0.88 w/ H201); H209 NOT CONFIRMED (G3 by 0.002; high-VIX trades better per unit risk) |
| 34c5839 | 2026-10-10 14:10 | FP-195: fix prev_close reset on every rerun (pre-START rows overwrote it; would mis-state P&L on held days, signals unaffected) |
| 759ed92 | 2026-10-10 14:11 | H210 REGISTERED: IBS VIX-regime sizing 1.5x/0.5x (pre-result, N=197, improvement criterion +0.10) |
| e3962b8 | 2026-10-10 14:11 | H210 runner (before results) |
| e6222e7 | 2026-10-10 14:11 | H210 NOT AN IMPROVEMENT: VIX sizing H2 0.835 vs H195 0.932, DD 37% vs 26%; VIX line closed |
