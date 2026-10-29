# REB-H4 binary-option feasibility (numbers only)

Prereg: prereg/REB_H4_BINARY_PREREG.md (sha256 fe461e9a…, registered 2026-10-11 18:19 ICT). Script: scripts/reb_h4_binary.py. Generated 2026-10-11 18:20 ICT.
This is research arithmetic only: no trading, and no IQ Option (or IQ-Paper / IQ Dashboard) access.

## Verdict
**NOT FEASIBLE.**
- No Wilson 95% lower bound clears any breakeven: 55.6% (80% payout), 54.1% (85%) or 53.5% (87%). This holds for every expiry and every symbol, and for the pooled result.
- The best pooled lower bound is 46.3%. Pooled point hit rates are 48–50%, i.e. coin-flip or worse.
- Even the point estimates (best: USDJPY 60 min, 52.0%) are below every breakeven.
- Every expected value per $1 stake at 85% payout is negative (−0.04 to −0.15).

Why this is plausible: REB-H4's backtest edge comes from a few large intraday trend days held to 20:00 UTC, with a 46% win rate. Over 5–60 minutes after the breakout the direction is about random. Some breakouts even revert at first, because entries are at the level, after the move.

## Method
- **Signals:** REB-H4 fixed (f = 0.5, opp) with the F2 H4 swing filter, USDJPY and EURUSD, 2019-01-01..2025-10-09. The holdout was not used.
- **Entry and strike:** the entry instant is the first M1 bar inside the M5 fill bar that reaches the entry price. Strike = the entry price.
- **Expiry and outcome:** expiry price = M1 mid open at entry + T. A win requires a move strictly in the trade direction; ties count as losses and are shown.
- **Interval:** Wilson 95%. Breakeven = 1/(1 + payout).
- **Cost blind spots:**
  - Dukascopy mid is used. A binary platform's quote feed and its strike/expiry rounding may differ.
  - Any platform-side spread or latency would make the result worse.

## Per symbol and pooled
| Group | Expiry (min) | n | wins | ties | dropped | hit % | Wilson 95% lo % | Wilson hi % | EV/stake @85% | clears 55.6/54.1/53.5? |
|---|---|---|---|---|---|---|---|---|---|---|
| USDJPY | 5 | 380 | 185 | 4 | 0 | 48.7 | **43.7** | 53.7 | -0.099 | no/no/no |
| EURUSD | 5 | 427 | 216 | 2 | 0 | 50.6 | **45.9** | 55.3 | -0.064 | no/no/no |
| POOLED | 5 | 807 | 401 | 6 | 0 | 49.7 | **46.3** | 53.1 | -0.081 | no/no/no |
| USDJPY | 15 | 380 | 191 | 1 | 0 | 50.3 | **45.3** | 55.3 | -0.070 | no/no/no |
| EURUSD | 15 | 427 | 200 | 1 | 0 | 46.8 | **42.2** | 51.6 | -0.133 | no/no/no |
| POOLED | 15 | 807 | 391 | 2 | 0 | 48.5 | **45.0** | 51.9 | -0.104 | no/no/no |
| USDJPY | 30 | 379 | 193 | 1 | 1 | 50.9 | **45.9** | 55.9 | -0.058 | no/no/no |
| EURUSD | 30 | 427 | 197 | 1 | 0 | 46.1 | **41.5** | 50.9 | -0.146 | no/no/no |
| POOLED | 30 | 806 | 390 | 2 | 1 | 48.4 | **45.0** | 51.8 | -0.105 | no/no/no |
| USDJPY | 60 | 379 | 197 | 0 | 1 | 52.0 | **47.0** | 57.0 | -0.038 | no/no/no |
| EURUSD | 60 | 427 | 198 | 0 | 0 | 46.4 | **41.7** | 51.1 | -0.142 | no/no/no |
| POOLED | 60 | 806 | 395 | 0 | 1 | 49.0 | **45.6** | 52.5 | -0.093 | no/no/no |

## Pooled per year (15 and 30 min)
| Expiry (min) | Year | n | wins | ties | dropped | hit % | Wilson 95% lo % | Wilson hi % | EV/stake @85% | clears 55.6/54.1/53.5? |
|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 2019 | 127 | 52 | 0 | 0 | 40.9 | **32.8** | 49.6 | -0.243 | no/no/no |
| 15 | 2020 | 126 | 63 | 0 | 0 | 50.0 | **41.4** | 58.6 | -0.075 | no/no/no |
| 15 | 2021 | 130 | 60 | 1 | 0 | 46.2 | **37.8** | 54.7 | -0.146 | no/no/no |
| 15 | 2022 | 116 | 62 | 0 | 0 | 53.4 | **44.4** | 62.3 | -0.011 | no/no/no |
| 15 | 2023 | 108 | 54 | 1 | 0 | 50.0 | **40.7** | 59.3 | -0.075 | no/no/no |
| 15 | 2024 | 112 | 62 | 0 | 0 | 55.4 | **46.1** | 64.2 | +0.024 | no/no/no |
| 15 | 2025 | 88 | 38 | 0 | 0 | 43.2 | **33.3** | 53.6 | -0.201 | no/no/no |
| 30 | 2019 | 126 | 54 | 1 | 1 | 42.9 | **34.6** | 51.6 | -0.207 | no/no/no |
| 30 | 2020 | 126 | 69 | 0 | 0 | 54.8 | **46.1** | 63.2 | +0.013 | no/no/no |
| 30 | 2021 | 130 | 56 | 1 | 0 | 43.1 | **34.9** | 51.7 | -0.203 | no/no/no |
| 30 | 2022 | 116 | 63 | 0 | 0 | 54.3 | **45.3** | 63.1 | +0.005 | no/no/no |
| 30 | 2023 | 108 | 53 | 0 | 0 | 49.1 | **39.8** | 58.4 | -0.092 | no/no/no |
| 30 | 2024 | 112 | 58 | 0 | 0 | 51.8 | **42.6** | 60.8 | -0.042 | no/no/no |
| 30 | 2025 | 88 | 37 | 0 | 0 | 42.0 | **32.3** | 52.5 | -0.222 | no/no/no |

Per year, the pooled 15-minute hit rate is above 53.5% only in 2024 (55.4%, lower bound 46.1%), and the 30-minute rate only in 2020 (54.8%) and 2022 (54.3%). No year's lower bound comes near any breakeven. The weakest years are 2019 (41–43%) and 2025 to 10-09 (42–43%).

## Multiple testing
- 8 trials were logged in results/trials.csv (2 symbols × 4 expiries; the pooled result is not counted as a separate trial).
- Total trials are now **640**; Bonferroni one-sided 5% threshold t = **3.78**.
- No row would survive even without the correction.

Files: results/reb_h4_binary_summary.csv, results/reb_h4_binary_peryear.csv, results/reb_h4_binary_signals.parquet (per-signal strike/expiry prices), results/reb_h4_binary_gate.json.
