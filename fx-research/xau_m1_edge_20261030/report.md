# XAU M1 human-behavior edge — REPORT (2026-10-30 ICT)
## Verdict: **NO EDGE / ไม่เจอ** — 0 of 25 hypotheses passed the Phase-3 kill. Phase 4 (MC/WFA/Tue–Thu) skipped as preregistered. Pine Script: N/A.
- Data: Dukascopy mid M1, 2022-01-01 ICT → **2026-10-10 03:59 ICT (=2026-10-09 20:59 UTC)**, 1,692,996 bars. No extension fetched (optional; not needed for a verdict).
- Cost: USER model $0.65/trade RT (0.45 spread + 0.15 slip + 0.05 comm). Kai IC model exists elsewhere, not used here.
- Primary: SL $3.5, TP 1.5R, 25-bar time stop, entry next-bar open, session-gated (ASIA 05–13, LDN 14–19, NY 19:30–23:30 ICT), same-bar SL/TP → SL.
- Trials this study: **125** (25 primary + 100 sensitivity); survivor grid not run (no survivors). Fleet N_TRIALS now **1080**, Z_BONF ≈ 3.909.
- Caveat: OOS 2024→end overlaps the fleet holdout (2025-10-10+), as the mission specified.
## Key numbers (PF after cost; grossPF = before cost, OOS)
| hyp                 |   IS_PF |   OOS_PF |   REC_PF |   OOS_WR |   OOS_N |    OOS_net |   OOS_maxDD |   sens_PF_min |   grossPF |   gross_exp |
|:--------------------|--------:|---------:|---------:|---------:|--------:|-----------:|------------:|--------------:|----------:|------------:|
| 01_ASIA_H_SWEEP     |   0.41  |    0.61  |    0.578 |    0.391 |     417 |   -297.618 |     301.772 |         0.616 |     0.956 |      -0.064 |
| 02_ASIA_L_SWEEP     |   0.442 |    0.773 |    0.79  |    0.426 |     357 |   -154.023 |     205.311 |         0.625 |     1.141 |       0.219 |
| 03_EQH_SWEEP        |   0.408 |    0.638 |    0.697 |    0.386 |    9998 |  -6198.16  |    6204.68  |         0.392 |     1.022 |       0.03  |
| 04_EQL_SWEEP        |   0.397 |    0.632 |    0.69  |    0.389 |    9052 |  -5749.94  |    5756.6   |         0.355 |     1.011 |       0.015 |
| 05_PDH_FAKE         |   0.487 |    0.476 |    0.524 |    0.356 |     264 |   -284.605 |     286.795 |         0.48  |     0.742 |      -0.428 |
| 06_PDL_FAKE         |   0.737 |    0.827 |    0.837 |    0.455 |     253 |    -85.454 |     134.934 |         0.675 |     1.193 |       0.312 |
| 07_FRACTAL_HUNT     |   0.414 |    0.682 |    0.711 |    0.393 |   36009 | -22545.6   |   22566     |         0.499 |     1.015 |       0.024 |
| 08_BIG_BAR_REJ      |   0.75  |    0.714 |    0.713 |    0.394 |   12831 |  -9112.81  |    9132.12  |         0.241 |     0.971 |      -0.06  |
| 09_RUN3_REJ         |   0.723 |    0.723 |    0.722 |    0.399 |   13903 |  -9456.93  |    9469.16  |         0.261 |     0.985 |      -0.03  |
| 10_PIN              |   0.579 |    0.692 |    0.697 |    0.398 |   18760 | -13096     |   13148.2   |         0.61  |     0.974 |      -0.048 |
| 11_UPWICK_AFTER_UP  |   0.684 |    0.719 |    0.728 |    0.403 |    7538 |  -4947.62  |    4962.54  |         0.365 |     0.997 |      -0.006 |
| 12_LOWWICK_AFTER_DN |   0.67  |    0.73  |    0.732 |    0.406 |    7836 |  -4939.66  |    4943.57  |         0.336 |     1.01  |       0.02  |
| 13_EXPANSION_FADE   |   0.543 |    0.706 |    0.722 |    0.409 |   20756 | -12187.9   |   12197.1   |         0.155 |     1.039 |       0.063 |
| 14_DOUBLE_EXP_FADE  |   0.753 |    0.747 |    0.768 |    0.425 |    3924 |  -2030.21  |    2059.44  |         0.044 |     1.079 |       0.133 |
| 15_LDN_FVG          |   0.553 |    0.699 |    0.723 |    0.418 |     685 |   -362.354 |     362.354 |         0.119 |     1.086 |       0.121 |
| 16_NY_FVG           |   0.595 |    0.696 |    0.687 |    0.411 |     688 |   -427.542 |     451.342 |         0.09  |     1.017 |       0.029 |
| 17_LDN_DRIVE        |   0.898 |    0.755 |    0.769 |    0.416 |     344 |   -165.569 |     165.569 |         0.493 |     1.106 |       0.169 |
| 18_NY_DRIVE         |   0.79  |    0.682 |    0.689 |    0.405 |     415 |   -300.395 |     307.392 |         0.513 |     0.961 |      -0.074 |
| 19_ASIA_DRIVE       |   0.568 |    0.474 |    0.471 |    0.375 |     267 |   -265.265 |     269.865 |         0.438 |     0.773 |      -0.344 |
| 20_OPEN_GAP_FILL    |   0.556 |    0.799 |    0.793 |    0.454 |     324 |   -119.321 |     133.068 |         0.159 |     1.188 |       0.282 |
| 21_EMA_1p5ATR       |   0.422 |    0.684 |    0.716 |    0.399 |   27113 | -16210.4   |   16228.1   |         0.158 |     1.034 |       0.052 |
| 22_VWAP_1p5ATR      |   0.432 |    0.668 |    0.704 |    0.391 |   16318 | -10344.4   |   10350.6   |         0.238 |     1.01  |       0.016 |
| 23_EMA_2p5ATR       |   0.438 |    0.67  |    0.711 |    0.398 |   13793 |  -8470.23  |    8485.89  |         0.094 |     1.024 |       0.036 |
| 24_ATR_CHANNEL      |   0.443 |    0.662 |    0.704 |    0.394 |   20694 | -13192.4   |   13210.4   |         0.12  |     1.008 |       0.013 |
| 25_STREAK8          |   0.446 |    0.66  |    0.696 |    0.394 |    2176 |  -1354.92  |    1371.87  |         0.192 |     1.019 |       0.027 |

**Best OOS PF:** 06_PDL_FAKE 0.83 (WR 45.5%, N 253, net −$85/oz); 20_OPEN_GAP_FILL 0.80; 02_ASIA_L_SWEEP 0.77. None close to 1.25. Kill needs PF>1.25 → all fail criterion 1 already.
**Why:** before cost almost every rule is ~coin-flip (gross PF 0.74–1.19, expectancy −$0.43…+$0.31/trade). $0.65/trade is larger than any gross edge. The best gross ideas (PDL fake-break, open-gap fill, Asia-low sweep: +$0.2–0.3/trade) are long-side reclaims, which fits gold's 2024–26 bull trend (beta, not behaviour). By-session PF columns are in summary.csv (IS_/OOS_{ASIA,LDN,NY}_PF); no session is profitable after cost for any hypothesis.
## Top 3 survivors: none.
## Charts: charts/oos_equity_top6.png, charts/oos_equity_all25.png (all go down).
## Checklist for when an edge dies (for any future candidate)
- Live spread > $0.70 or slippage > $0.20 → stop; on M1 the cost is the whole edge.
- Red-folder news (NFP, CPI, FOMC, Powell) ±30 min → no trades.
- Rolling 100-trade PF < 1.0, or DD > 25% of cumulative profit → pause.
- WR down > 5 pp vs backtest → re-check.
- Regime change: ATR14 M1 outside the IS 10–90th percentile → stand down.
- Broker feed differs from Dukascopy mid (IC bid ≈ −$0.04) → re-validate.
