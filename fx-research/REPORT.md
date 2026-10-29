# fx-research REPORT (generated 2026-10-11 ICT) - walk-forward OOS, after costs

**Bottom line: 0 of 29 strategy x symbol candidates pass the pass bar.** The closest is the USDJPY New York-open breakout (session_bo,
NY session, stop at the opposite edge of the 3h pre-range, exit at 16:00 NY). It met every check except max drawdown (-26% at 1% risk vs the 20% limit).
Its OOS t-stat (2.69) is below the Bonferroni threshold (3.54, N=252), and its deflated-Sharpe probability is ~0. Treat it as a
candidate for a fresh, pre-registered test, not a validated system. Holdout (2025-10-10 -> 2026-10-10) was NOT loaded or tested.

## Data
Dukascopy M1 BID+ASK candles, 2019-01-01 -> 2026-10-09, for EURUSD, GBPUSD, USDJPY, AUDUSD, XAUUSD. Pulled through Dukascopy's public freeserv chart endpoint
(the same one the dukascopy-python package uses), with a throttle of 1 request per 2 s, resume support and a STOP-file check. Cleaning: aligned bid/ask by timestamp, built mid OHLC as the
bid/ask average, kept the spread, and dropped zero-volume filler bars. All data is UTC. Coverage and gaps are in data/*_coverage.json. Only weekday gaps are holiday closures
(1 Jan for FX; Good Friday, 25 Dec and 1 Jan for XAU). XAU has 82 "non-closure" gaps of 15 min or more, mostly US-holiday early closes.
Not IC Markets prices. Dukascopy's own spreads are wider (XAU median $0.35-0.61/oz) but are not used for costs.

## Walk-forward and holdout
IS 24 months rolling, OOS 6 months, 10 non-overlapping OOS windows from 2021-01-01 to 2025-10-10. Params are chosen per window by the highest IS t-stat of net R at 1x costs
(minimum 30 IS trades, IS trades must close before the OOS window starts). Only stitched OOS results are reported. M1 data is cut at 2025-10-10 right after loading, so the last 12 months stay untouched.

## Costs (1x; from IC_COSTS_FROM_KAI_20261011.md, IC Markets Raw MT5 demo probe dated 2026-10-11)
- Commission: $3.50/lot/side.
- Spreads: p90 points per session (FX points 1e-5, JPY 1e-3, XAU $0.01):
  - EURUSD 1/1/1, GBPUSD 2/2/3, USDJPY 2/2/2, AUDUSD 1/1/1, XAUUSD 12/11/10 (Asia/London/NY).
  - 16:00-20:30 UTC (not measured) uses 1.5x the NY value.
  - Rollover 20:30-24:00 UTC and weekends use the weekend-close spread: 12/44/33/32/40 pts.
  - Half the spread is charged at entry and half at exit.
- Slippage: 0.1 pip per side for FX, $0.05/oz per side for XAU, on every fill.
- Swaps from the same file, Wednesday x3. These are today's rates applied to past years, which is a caveat.
- Entries are blocked 20:30-24:00 UTC and on Sat/Sun.
- Minimum stop: 5 pips for FX, $1.00/oz for XAU. Tighter stops are widened to it and TP is scaled. Broker stops_level is 0.
- Sensitivity runs at 1.5x and 2x on spread + commission + slippage.
- Sizing: 1% risk per trade on a $10k reference account, non-compounded.

## Multiple testing
252 trials are logged in results/trials.csv: 209 WF param combos, 6 robustness combos, plus 37 pilot combos from before the scope update. The cost-model re-run did not count as new trials.
Deflated Sharpe uses daily net R. Strict cross-trial variance 0.0157; pooled within-grid variance 0.0058. Bonferroni one-sided 5%: t >= 3.54.
No candidate clears either test.

## Ranked OOS table (sorted by pass, then PF)
Pip columns are pips for FX and $/oz for XAU. cost_to_gross = average cost / |average gross trade|.

| strategy         | symbol   | track                             |    n |   win |   pf |   pf_1_5x |   pf_2x |   exp_R |   exp_usd |   maxdd_pct |   worst_streak | years_pos   | wf_pos   | t_vs_bonf   |   dsr_pooled |   avg_gross_pips |   avg_cost_pips |   cost_to_gross | passes   |
|:-----------------|:---------|:----------------------------------|-----:|------:|-----:|----------:|--------:|--------:|----------:|------------:|---------------:|:------------|:---------|:------------|-------------:|-----------------:|----------------:|----------------:|:---------|
| 1_donchian       | USDJPY   | H1/H4 confirmation track          |  711 | 33.9  | 1.28 |      1.24 |    1.2  |    0.15 |     14.68 |      -26.46 |             13 | 3/5         | 8/10     | 2.06/3.54   |            0 |             3.97 |            1.43 |            0.36 | False    |
| 3_session_bo     | USDJPY   | M5 primary                        | 1173 | 42.11 | 1.26 |      1.19 |    1.11 |    0.13 |     12.84 |      -26.14 |             12 | 5/5         | 9/10     | 2.69/3.54   |            0 |             3.52 |            1.69 |            0.48 | False    |
| 5_tsmom          | USDJPY   | D1 reference (published research) |   24 | 51.81 | 1.21 |      1.21 |    1.21 |    0.17 |     17.33 |      -37.28 |              6 | 3/5         | 7/10     | 1.14/3.54   |            0 |             3.77 |            0.14 |            0.04 | False    |
| 5_tsmom          | XAUUSD   | D1 reference (published research) |   23 | 50.2  | 1.08 |      1.08 |    1.08 |    0.07 |      7.05 |      -56.04 |              6 | 2/5         | 5/10     | 0.46/3.54   |            0 |             5.18 |            0.03 |            0.01 | False    |
| 6_fx_seasonality | USDJPY   | M5 primary                        | 1242 | 46.46 | 0.98 |      0.92 |    0.87 |   -0.01 |     -0.73 |      -37.47 |             12 | 2/5         | 5/10     | -0.30/3.54  |            0 |             0.08 |            1.37 |           16.17 | False    |
| 6_fx_seasonality | EURUSD   | M5 primary                        | 1241 | 47.78 | 0.97 |      0.93 |    0.88 |   -0.01 |     -0.84 |      -28.87 |              7 | 3/5         | 3/10     | -0.36/3.54  |            0 |             0.53 |            1.01 |            1.91 | False    |
| 6_fx_seasonality | GBPUSD   | M5 primary                        | 1630 | 47.67 | 0.96 |      0.92 |    0.88 |   -0.01 |     -1.38 |      -45.49 |             11 | 3/5         | 5/10     | -0.59/3.54  |            0 |             0.6  |            1.19 |            1.99 | False    |
| 3_session_bo     | GBPUSD   | M5 primary                        | 1158 | 40.5  | 0.96 |      0.92 |    0.89 |   -0.02 |     -2    |      -51.45 |             13 | 3/5         | 4/10     | -0.49/3.54  |            0 |             0.58 |            1.15 |            1.96 | False    |
| 3_session_bo     | EURUSD   | M5 primary                        | 1163 | 40.67 | 0.96 |      0.91 |    0.87 |   -0.02 |     -2.19 |      -46.01 |              9 | 2/5         | 4/10     | -0.61/3.54  |            0 |             0.3  |            1.04 |            3.45 | False    |
| 4_kaze           | USDJPY   | M1/M5 primary                     | 6100 | 38.66 | 0.94 |      0.88 |    0.83 |   -0.03 |     -3.31 |     -232.2  |             16 | 0/5         | 1/10     | -1.99/3.54  |            0 |             0.89 |            1.56 |            1.75 | False    |
| 5_tsmom          | EURUSD   | D1 reference (published research) |   23 | 50.2  | 0.94 |      0.93 |    0.93 |   -0.06 |     -5.47 |      -28.12 |              8 | 2/5         | 4/10     | -0.39/3.54  |            0 |            -0.03 |            0.1  |            3.14 | False    |
| 3_session_bo     | AUDUSD   | M5 primary                        | 1103 | 42.61 | 0.9  |      0.84 |    0.78 |   -0.05 |     -5.08 |      -77.18 |             11 | 2/5         | 2/10     | -1.39/3.54  |            0 |            -0.1  |            1.16 |           11.57 | False    |
| 4_kaze           | XAUUSD   | M1/M5 primary                     | 6663 | 38.77 | 0.9  |      0.84 |    0.78 |   -0.06 |     -6.37 |     -516.92 |             19 | 1/5         | 2/10     | -4.15/3.54  |            0 |             0.18 |            0.3  |            1.71 | False    |
| 3_session_bo     | XAUUSD   | M5 primary                        | 1045 | 40.38 | 0.89 |      0.86 |    0.83 |   -0.06 |     -5.64 |      -76.69 |             14 | 2/5         | 3/10     | -1.51/3.54  |            0 |             0.05 |            0.29 |            6.36 | False    |
| 6_fx_seasonality | AUDUSD   | M5 primary                        | 1240 | 46.21 | 0.88 |      0.83 |    0.78 |   -0.04 |     -4.26 |      -62.87 |             10 | 0/5         | 3/10     | -1.80/3.54  |            0 |            -0.24 |            1.01 |            4.31 | False    |
| 4_kaze           | EURUSD   | M1/M5 primary                     | 4638 | 40.38 | 0.88 |      0.83 |    0.78 |   -0.06 |     -6.29 |     -298.67 |             14 | 0/5         | 1/10     | -3.88/3.54  |            0 |            -0.08 |            1.08 |           13.13 | False    |
| 5_tsmom          | GBPUSD   | D1 reference (published research) |   26 | 48.59 | 0.88 |      0.87 |    0.87 |   -0.11 |    -11.22 |      -47.04 |              9 | 1/5         | 4/10     | -0.81/3.54  |            0 |            -1.8  |            0.14 |            0.08 | False    |
| 4_kaze           | GBPUSD   | M1/M5 primary                     | 6082 | 36.27 | 0.83 |      0.77 |    0.72 |   -0.11 |    -10.73 |     -661.35 |             16 | 0/5         | 1/10     | -6.63/3.54  |            0 |            -0.26 |            1.38 |            5.38 | False    |
| 5_tsmom          | AUDUSD   | D1 reference (published research) |   32 | 44.98 | 0.82 |      0.82 |    0.82 |   -0.17 |    -17.22 |      -55.41 |              6 | 1/5         | 1/10     | -1.24/3.54  |            0 |            -4.93 |            0.14 |            0.03 | False    |
| 2_asian_mr       | EURUSD   | M5 primary                        |  926 | 54.75 | 0.81 |      0.62 |    0.47 |   -0.07 |     -7.43 |      -72.8  |              8 | 1/5         | 1/10     | -2.74/3.54  |            0 |             0.78 |            1    |            1.29 | False    |
| 1_donchian       | XAUUSD   | H1/H4 confirmation track          |  304 | 29.93 | 0.8  |      0.78 |    0.77 |   -0.1  |    -10.42 |      -46.73 |             12 | 2/5         | 2/10     | -1.45/3.54  |            0 |            -1    |            0.29 |            0.29 | False    |
| 4_kaze           | AUDUSD   | M1/M5 primary                     | 4311 | 40.99 | 0.8  |      0.74 |    0.7  |   -0.1  |    -10.06 |     -435.25 |             14 | 0/5         | 0/10     | -6.45/3.54  |            0 |            -0.68 |            1.22 |            1.79 | False    |
| 2_asian_mr       | GBPUSD   | M5 primary                        |  837 | 55.56 | 0.79 |      0.62 |    0.49 |   -0.09 |     -9.19 |      -79.79 |              9 | 0/5         | 0/10     | -3.04/3.54  |            0 |             0.96 |            1.1  |            1.15 | False    |
| 2_asian_mr       | AUDUSD   | M5 primary                        | 1711 | 53.18 | 0.78 |      0.66 |    0.55 |   -0.1  |    -10.06 |     -172.93 |              8 | 1/5         | 2/10     | -4.55/3.54  |            0 |             0.4  |            1    |            2.5  | False    |
| 1_donchian       | GBPUSD   | H1/H4 confirmation track          |  413 | 30.99 | 0.75 |      0.74 |    0.72 |   -0.12 |    -11.54 |      -51.82 |             17 | 0/5         | 4/10     | -2.17/3.54  |            0 |            -6.36 |            1.2  |            0.19 | False    |
| 1_donchian       | EURUSD   | H1/H4 confirmation track          |  170 | 31.18 | 0.7  |      0.69 |    0.68 |   -0.18 |    -17.65 |      -31.05 |             13 | 1/5         | 4/10     | -1.81/3.54  |            0 |            -5.06 |            1.03 |            0.2  | False    |
| 2_asian_mr       | USDJPY   | M5 primary                        |  989 | 52.88 | 0.7  |      0.57 |    0.47 |   -0.14 |    -13.6  |     -134.47 |              8 | 0/5         | 0/10     | -4.65/3.54  |            0 |             0.26 |            1.34 |            5.23 | False    |
| 1_donchian       | AUDUSD   | H1/H4 confirmation track          |  698 | 30.09 | 0.69 |      0.67 |    0.64 |   -0.17 |    -16.92 |     -118.09 |             15 | 0/5         | 0/10     | -3.69/3.54  |            0 |            -4.39 |            1.05 |            0.24 | False    |
| 2_asian_mr       | XAUUSD   | M5 primary                        | 1127 | 52.26 | 0.68 |      0.57 |    0.48 |   -0.14 |    -14.36 |     -174.15 |             10 | 0/5         | 1/10     | -5.70/3.54  |            0 |            -0.16 |            0.29 |            1.81 | False    |

Per-candidate detail (per year, per regime, cost sensitivity, WF windows, checklist): results/reports/<strategy>_<symbol>.md

## Robustness of the near-miss (USDJPY NY breakout, fixed rule, OOS span only; diagnostic, not selection)
| tf    |   pre_range_h |    n |    pf |   pf_1_5x |   exp_R |   maxdd_pct |   worst_streak |   tstat | exp_R_by_year                                                      |
|:------|--------------:|-----:|------:|----------:|--------:|------------:|---------------:|--------:|:-------------------------------------------------------------------|
| 5min  |             2 | 1198 | 1.23  |     1.151 |   0.128 |     -35.872 |             14 |   2.347 | {2021: 0.174, 2022: 0.175, 2023: 0.196, 2024: 0.086, 2025: -0.028} |
| 5min  |             3 | 1173 | 1.263 |     1.186 |   0.128 |     -26.142 |             12 |   2.687 | {2021: 0.171, 2022: 0.15, 2023: 0.136, 2024: 0.089, 2025: 0.085}   |
| 5min  |             4 | 1133 | 1.299 |     1.222 |   0.126 |     -21.2   |              9 |   2.878 | {2021: 0.144, 2022: 0.162, 2023: 0.097, 2024: 0.115, 2025: 0.111}  |
| 15min |             2 | 1182 | 1.262 |     1.182 |   0.144 |     -31.727 |             14 |   2.616 | {2021: 0.174, 2022: 0.205, 2023: 0.206, 2024: 0.105, 2025: -0.006} |
| 15min |             3 | 1163 | 1.287 |     1.208 |   0.139 |     -25.108 |             12 |   2.88  | {2021: 0.171, 2022: 0.165, 2023: 0.15, 2024: 0.094, 2025: 0.103}   |
| 15min |             4 | 1125 | 1.322 |     1.243 |   0.134 |     -19.311 |              9 |   3.056 | {2021: 0.149, 2022: 0.173, 2023: 0.106, 2024: 0.13, 2025: 0.111}   |

The neighbourhood is a plateau (PF 1.23-1.32, positive on both long and short), not a single spike. The 15-min / 4h-range variant gets DD under 20%,
but that was found by looking at the OOS span, so it cannot count as a pass. It needs a new pre-registered WF that includes range length in the grid,
then the one-time holdout test. The edge is shrinking: PF fell from 1.37 in 2021 to 1.16 in 2025. Per regime, most of the gain comes from ADX<20 hours and normal volatility.

## Gold flag
XAU spread + commission + slippage is about $0.29/oz per round turn, versus FX about 1.0-1.7 pips.
Small-timeframe gold systems don't cover it. Kaze XAU averages $0.18/oz gross against $0.30/oz cost. Session breakout averages $0.05 gross against $0.29 cost.
Asian mean reversion averages -$0.16 gross. Gold needs a much larger edge per trade than these intraday rules provide.

## Candidate status
1. Session-open momentum (M5): USDJPY near miss (see above). EURUSD, GBPUSD, AUDUSD and XAU fail; their PF is about 0.9-0.96 because gross edge is about cost.
2. Asian MR (M5): fails on every symbol. Win rate is 53-56%, but average gross is 0.3-1 pip against about 1-1.3 pip cost.
3. Kaze M5+M1 (archive definition, lookahead fixed): fails on every symbol. 0-1 of 5 years positive, PF 0.80-0.94, gross below cost.
4. FX seasonality (Breedon & Ranaldo 2013): gross is about 0-0.6 pip per trade, cost is larger, so it fails.
5. Donchian H1/H4 (confirmation track): USDJPY PF 1.28 but only 3 of 5 years positive (2023-25 flat or negative) and DD 26%. All others fail.
6. TSMOM (Moskowitz-Ooi-Pedersen 2012, D1 weekly): far too few trades (23-32 position changes) and DD 28-56%. Reference only.
No promotions to M15/H1/H4 were run because nothing survived. The M15 runs above are only a diagnostic.

---
## Addendum 2026-10-11 (12:10 ICT): follow-up tracks

All 501 logged trials have now been run. None passes the bar.
- Trial count: results/trials.csv plus 37 pilot trials; a crashed re-run was de-duplicated.
- Bonferroni one-sided 5% t threshold: 3.72.
- DSR, strict and pooled: 0.00 for every new candidate.

### Track 1: NYBO M15/4h, pre-registered test. CLEAR FAIL
- Pre-registration: prereg/NYBO_M15_4h_PREREG.md
  - sha256 50729e0d…
  - Registered 2026-10-11T04:02:10Z (11:02 ICT).
- Test: 5 untouched pairs, 2021-01 to 2025-10-09. The downloaded data ends 2025-10-09 23:59 UTC.
- Holds-up criteria met: 0 of 5.
  - Pooled PF by cost multiplier: 0.904 (1x), 0.803 (1.5x), 0.714 (2x).
  - Expectancy by year: negative in all 5 years.
  - Per-pair PF at 1x: EURJPY 0.90, GBPJPY 0.81, AUDJPY 0.86, USDCAD 0.98, USDCHF 0.93.
- Holdout: the USDJPY holdout was NOT run and is still unused (no results/HOLDOUT_USED_NYBO marker exists).
- Report: results/reports/NYBO_M15_4h_prereg_REPORT.md

### Track 2: new families. 0 of 24 pass, nothing promoted
- Families: ORB on the Tokyo and Frankfurt opens; London 4pm fix flow (all days and month-end); USD-basket cross-pair residual fade; 08:30/10:00 NY news-shock drift/fade.
- Best results:
  - XAU fix_flow: PF 1.03, n=115.
  - EURUSD Frankfurt ORB: PF 1.00, DD −57%.
- Files: results/reports/TRACK2_SUMMARY.md and results/reports/{strategy}_{SYM}.md

### Track 3: Kai demo techniques, flat 1% risk. All CLEAR FAIL
| Technique | Symbols | PF range |
|---|---|---|
| T01 | XAU + 4 FX | 0.73–0.80 |
| T06 | XAU + 4 FX | 0.61–0.76 |
| T08 | XAU + 4 FX | 0.70–0.82 |
| T15 | XAU | 0.86 |

- On every symbol, average gross edge per trade is about 0. On XAU that is roughly $0.00–0.01/oz gross against $0.29 of costs.
- Definitions were hashed before testing: prereg/TRACK3_DEFINITIONS.md
- Per-technique reports: results/reports/track3/*_REPORT.md
- Demo deal analysis: results/kai_demo_analysis.md. Martingale up-sizing produced the positive demo totals; at a flat lot, T08, T15 and MCM1 are negative.

### Dukascopy vs IC: no material problem
- results/dukascopy_vs_ic.md
