# XAUUSD 'blind' read of 2026-10-15 00:00–06:35 ICT + Kai's swing-high breakout test: REPORT

**Data labels:**
- **Part 1:** Dukascopy XAU/USD M1 bid+ask → mid, M5/H1 in UTC (ICT = UTC+7 shown alongside). File data/refcheck/XAUUSD_M1_20261011_20261015.parquet covers 2026-10-11 22:00..2026-10-15 03:59 UTC. Post-holdout, separate, not merged.
- **Part 2:** Dukascopy XAU/USD M1 → M5/H1, historical 2019-01-01..2025-10-09; the holdout was not loaded. BACKTEST after Kai's IC costs (XAU p90 12/11/10 points; 20:30–24:00 UTC and weekend 40 points; $3.50/lot/side; $0.05/oz/side slippage; swap with Wednesday ×3). Flat 1% risk ($100 per R on $10k). IS/OOS is labelled per table.

## Part 1: rules-based read at 06:35 ICT (bar 2026-10-14 23:35 UTC)
> **HONESTY NOTE:** this is NOT a blind read. In the previous job I already saw the outcome of this window: the long trigger at 06:40 ICT, 4139.63 at 08:00 ICT (Dukascopy), and the user's report of about 4151. To limit hindsight, the read below is computed mechanically by code using only bars up to and including 23:35 UTC (scripts/xau_swingbo.py `read`; state saved in results/xau_blindread_state.json). The decision follows the two pre-registered rule sets, not judgement. **One example proves nothing.**

**State at the close of 23:35 UTC / 06:35 ICT:**
- **M5:** close 4101.325; EMA55_M5 4101.183 (price sits right on the EMA); ATR14_M5 $2.71.
- **M5 trend:** 53 consecutive closes above the EMA55 and the EMA rising, so M5 is up.
- **H1 (last completed bar 22:00 UTC, i.e. the 22:00–23:00 bar):** close 4106.74; EMA55_H1 4144.57, which was 4166.55 ten bars earlier. The H1 trend is **DOWN**: price is about $38 below a falling H1 EMA55.
  - Caveat: only 70 H1 bars of warm-up are in the refcheck file, so EMA55_H1 is approximate. The direction is unambiguous.
- **Session context:**
  - The XAU daily break was 20:55 → 22:00 UTC (03:55 → 05:00 ICT; bar gap of 1h05).
  - 23:35 UTC is inside our 20:30–24:00 UTC rollover entry block.
  - Dukascopy spread: $0.56 now, vs a 1-day median of $0.53. The window median was $0.53, with a maximum of $0.94.
  - Kai's IC model charges 40 points ($0.40) of rollover spread in this window, versus 10–12 points in the core sessions.
- **Window range (17:00–23:35 UTC):** low 4078.05 at 17:15 UTC (00:15 ICT); high 4112.01 at 22:45 UTC (05:45 ICT).

**M5 fractal 3-3 swings since 12:00 UTC (swing bar time):**

| UTC | ICT | type | price |
|---|---|---|---|
| 2026-10-14 11:55:00+00:00 | 18:55 | L | 4136.971 |
| 2026-10-14 12:25:00+00:00 | 19:25 | H | 4155.875 |
| 2026-10-14 12:40:00+00:00 | 19:40 | L | 4085.13 |
| 2026-10-14 13:20:00+00:00 | 20:20 | L | 4079.68 |
| 2026-10-14 13:35:00+00:00 | 20:35 | H | 4107.545 |
| 2026-10-14 14:00:00+00:00 | 21:00 | L | 4086.655 |
| 2026-10-14 14:40:00+00:00 | 21:40 | H | 4106.0 |
| 2026-10-14 15:10:00+00:00 | 22:10 | L | 4083.302 |
| 2026-10-14 15:25:00+00:00 | 22:25 | H | 4095.975 |
| 2026-10-14 16:00:00+00:00 | 23:00 | L | 4073.582 |
| 2026-10-14 16:55:00+00:00 | 23:55 | H | 4084.18 |
| 2026-10-14 17:15:00+00:00 | 00:15 | L | 4078.052 |
| 2026-10-14 17:30:00+00:00 | 00:30 | H | 4090.766 |
| 2026-10-14 18:00:00+00:00 | 01:00 | L | 4080.446 |
| 2026-10-14 18:30:00+00:00 | 01:30 | H | 4096.098 |
| 2026-10-14 18:50:00+00:00 | 01:50 | L | 4091.1 |
| 2026-10-14 19:20:00+00:00 | 02:20 | H | 4106.602 |
| 2026-10-14 19:40:00+00:00 | 02:40 | L | 4098.355 |
| 2026-10-14 20:00:00+00:00 | 03:00 | H | 4103.44 |
| 2026-10-14 20:45:00+00:00 | 03:45 | L | 4096.875 |
| 2026-10-14 22:00:00+00:00 | 05:00 | H | 4109.055 |
| 2026-10-14 22:45:00+00:00 | 05:45 | H | 4112.015 |
| 2026-10-14 23:10:00+00:00 | 06:10 | L | 4100.015 |

- **Structure:** after the 20:45 UTC low (4096.88), M5 printed higher highs 4109.06 → 4112.02 and a higher low of 4100.02 at 23:10 UTC. That is a short-term HH/HL inside an H1 downtrend.
- **Bigger picture since 12:00 UTC:** lower highs from 4155.88 down to about 4106, then a base around 4074–4080.

**Mechanical decision at 06:35 ICT: WAIT** (no order under either rule set).
- **Swing-breakout rule (Part 2):**
  - The long needs the H1 trend up, and it is down, so there is no buy-stop. It would have sat above SH 4112.02 at 4112.12.
  - The short side would have a sell-stop below the 23:10 swing low at 4099.92 (SL 4105.32, R $5.40; EMA-touch pullback met). But the 20:30–24:00 UTC block forbids it.
  - Even with the block OFF, that sell-stop was never filled through 08:00 ICT (the low after 23:35 was 4100.91).
- **EMA55-pullback rule (prereg XAU_EMA55_PB):**
  - With X = $0 there is no touch: the low 4101.218 is above the EMA 4101.183.
  - With X ≥ $0.30 there is a touch, but the trigger at 23:40/23:45 UTC is inside the entry block, so no trade.

**Reveal 06:40–08:00 ICT (23:40–01:00 UTC, Dukascopy mid):**
- The 23:40 bar closed 4105.23. Price ran to 4146.68 at 00:45 UTC (07:45 ICT) and was 4139.63 at 08:00 ICT.

**Grading:**
- **Our mechanical WAIT:** it missed a +$41 move. By construction, a blocked rule cannot catch it.
- **Kai's plan** (WAIT at 06:35; long on a close > 4105.17; SL 4099.92; TP 4111.91):
  - Triggered on the 23:40 bar close at 4105.23 (R = $5.31). TP hit at 23:57 UTC (06:57 ICT): +$6.68 = +1.26R.
  - MFE before TP: +$7.47 (1.41R). MAE: $0.06 (0.01R). It would have won.
  - Kai graded himself wrong. If that was for leaving most of the move (MFE to 08:00 = +$41.4 = 7.8R), the trade itself still hit its TP.
- **EMA55-PB with the block OFF (diagnostic only; X ≥ 0.30, stop entry 4102.55, SL 4099.92, R $2.63):** MAE $1.64 (0.62R). The 2R TP (4107.81) was hit on the 23:45 bar. MFE to 08:00 = +$44.1 = 16.8R.
- **Context:** 1 example out of thousands of signals. Part 2 and the earlier tests (EMA55 PB: 72 + 30 variants) show what happens on average.

## Part 2: swing-high breakout, Kai's idea (prereg/XAU_SWINGBO_PREREG.md, sha256 d05e0009…, registered 2026-10-15T05:16:15Z = 12:16 ICT, before any run)
**Verdict: NO EDGE.**
- The stitched walk-forward OOS fails the pass bar (every OOS year positive, PF>=1.2 @1x, PF>1.0 @1.5x, DD<=20%).
- It is roughly breakeven after costs: gross PF just above 1, net about 0.
- The holdout was NOT run.

### Walk-forward OOS, stitched 2021-01..2025-10-09 (decisive)
| set                                                                       |    n |   win |   avgR |   pf_gross |   pf_1x |   pf_1_5x |   pf_2x |   maxdd_R |   streak |     t |   med_stop |   cost_R |   exp_usd |
|:--------------------------------------------------------------------------|-----:|------:|-------:|-----------:|--------:|----------:|--------:|----------:|---------:|------:|-----------:|---------:|----------:|
| WF OOS stitched                                                           | 1026 |  42.4 |  0.003 |      1.209 |   1.009 |     0.924 |   0.848 |     -21.9 |        8 |  0.12 |       4    |    0.065 |       0.3 |
| finalist ('swl', 'exp', 1.0, 'psh') fixed 2021–25 (info, not independent) |  607 |  38.6 | -0.07  |      1.061 |   0.809 |     0.71  |   0.627 |     -52.5 |       10 | -1.9  |       3.56 |    0.089 |      -7   |
| finalist 2019–2025 (in-sample)                                            |  920 |  36.7 | -0.087 |      1.035 |   0.766 |     0.664 |   0.578 |     -86.4 |       17 | -2.94 |       3.36 |    0.098 |      -8.7 |

- t 0.12 vs Bonferroni 3.82 (761 trials). DSR (strict) = 0.000.
- Checks: {'every OOS year positive': False, 'PF>=1.2 @1x': False, 'PF>1.0 @1.5x': False, '>=300 trades': True, 'DD<=20%': False, 'streak<=12': True}.

### IS vs OOS per window
| oos_start                 | oos_end                   | param                      |   is_score |   n_oos |   oos_R |
|:--------------------------|:--------------------------|:---------------------------|-----------:|--------:|--------:|
| 2021-01-01 00:00:00+00:00 | 2021-07-01 00:00:00+00:00 | ('swl', 'stop', 4.0, '1R') |     -0.017 |     231 |  11.957 |
| 2021-07-01 00:00:00+00:00 | 2022-01-01 00:00:00+00:00 | ('swl', 'stop', 4.0, '1R') |      0.233 |     139 |   5.17  |
| 2022-01-01 00:00:00+00:00 | 2022-07-01 00:00:00+00:00 | ('swl', 'stop', 4.0, '1R') |      0.426 |     213 |  -3.99  |
| 2022-07-01 00:00:00+00:00 | 2023-01-01 00:00:00+00:00 | ('swl', 'stop', 4.0, '1R') |      1.157 |     217 |  -1.48  |
| 2023-01-01 00:00:00+00:00 | 2023-07-01 00:00:00+00:00 | ('swl', 'exp', 4.0, '1R')  |      0.934 |      35 |  -1.804 |
| 2023-07-01 00:00:00+00:00 | 2024-01-01 00:00:00+00:00 | ('swl', 'exp', 4.0, '1R')  |      0.061 |      17 |  -1.122 |
| 2024-01-01 00:00:00+00:00 | 2024-07-01 00:00:00+00:00 | ('swl', 'exp', 4.0, '1R')  |     -0.507 |      44 |   4.415 |
| 2024-07-01 00:00:00+00:00 | 2025-01-01 00:00:00+00:00 | ('swl', 'exp', 4.0, '1R')  |     -0.324 |      41 |   1.222 |
| 2025-01-01 00:00:00+00:00 | 2025-07-01 00:00:00+00:00 | ('swl', 'exp', 4.0, '1R')  |      0.26  |      57 | -11.203 |
| 2025-07-01 00:00:00+00:00 | 2025-10-10 00:00:00+00:00 | ('swl', 'exp', 1.0, 'psh') |     -0.054 |      32 |   0.379 |

### WF OOS per year (1x)
|   entry_time |   n |   expR |    sumR |
|-------------:|----:|-------:|--------:|
|         2021 | 370 |  0.046 |  17.128 |
|         2022 | 430 | -0.013 |  -5.47  |
|         2023 |  52 | -0.056 |  -2.926 |
|         2024 |  85 |  0.066 |   5.637 |
|         2025 |  89 | -0.122 | -10.824 |

### Per variant (12; block ON)
- IS19-20 = 2019-01..2020-12. 21-25 = 2021-01..2025-10-09, which is not independent if you pick from this table.
- med_stop is $/oz. cost_R = average cost / risk.

| variant (pullback,entry,floor,exit)   |   IS19-20 n |   IS avgR |   IS PF |   21-25 n |   21-25 win |   21-25 avgR |   21-25 pf_gross |   21-25 pf_1x |   21-25 pf_1_5x |   21-25 pf_2x |   21-25 maxdd_R |   21-25 streak |   21-25 t |   21-25 med_stop |   21-25 cost_R |   21-25 exp_usd |
|:--------------------------------------|------------:|----------:|--------:|----------:|------------:|-------------:|-----------------:|--------------:|----------------:|--------------:|----------------:|---------------:|----------:|-----------------:|---------------:|----------------:|
| ('swl', 'stop', 1.0, '1R')            |        1335 |    -0.067 |   0.854 |      3299 |        41.1 |       -0.074 |            1.075 |         0.836 |           0.74  |         0.656 |          -249.1 |             15 |     -4.11 |             3.21 |          0.104 |            -7.4 |
| ('swl', 'stop', 1.0, 'psh')           |        1335 |    -0.083 |   0.791 |      3299 |        39.4 |       -0.084 |            1.058 |         0.785 |           0.68  |         0.592 |          -280.6 |             13 |     -5.17 |             3.21 |          0.103 |            -8.4 |
| ('swl', 'stop', 4.0, '1R')            |         666 |    -0.001 |   0.998 |      2235 |        41.2 |       -0.028 |            1.099 |         0.927 |           0.853 |         0.786 |           -86   |             11 |     -1.43 |             4.09 |          0.063 |            -2.8 |
| ('swl', 'stop', 4.0, 'psh')           |         666 |    -0.016 |   0.951 |      2235 |        42.2 |       -0.041 |            1.077 |         0.873 |           0.788 |         0.711 |          -102.8 |             12 |     -2.38 |             4.09 |          0.062 |            -4.1 |
| ('ema', 'stop', 1.0, '1R')            |        1813 |    -0.116 |   0.769 |      4558 |        40.5 |       -0.085 |            1.071 |         0.825 |           0.726 |         0.642 |          -413   |             14 |     -5    |             2.88 |          0.115 |            -8.5 |
| ('ema', 'stop', 1.0, 'psh')           |        1813 |    -0.128 |   0.716 |      4558 |        37.3 |       -0.094 |            1.058 |         0.785 |           0.681 |         0.593 |          -444.6 |             14 |     -5.84 |             2.88 |          0.115 |            -9.4 |
| ('ema', 'stop', 4.0, '1R')            |         891 |    -0.042 |   0.896 |      2986 |        41.3 |       -0.031 |            1.094 |         0.922 |           0.847 |         0.78  |          -125.9 |             14 |     -1.79 |             4    |          0.065 |            -3.1 |
| ('ema', 'stop', 4.0, 'psh')           |         891 |    -0.05  |   0.849 |      2986 |        40.5 |       -0.044 |            1.068 |         0.867 |           0.784 |         0.709 |          -154.7 |             10 |     -2.88 |             4    |          0.064 |            -4.4 |
| ('swl', 'exp', 1.0, '1R')             |         313 |    -0.126 |   0.734 |       607 |        39.2 |       -0.068 |            1.054 |         0.846 |           0.761 |         0.686 |           -47   |              8 |     -1.66 |             3.56 |          0.089 |            -6.8 |
| ('swl', 'exp', 1.0, 'psh')            |         313 |    -0.122 |   0.689 |       607 |        38.6 |       -0.07  |            1.061 |         0.809 |           0.71  |         0.627 |           -52.5 |             10 |     -1.9  |             3.56 |          0.089 |            -7   |
| ('swl', 'exp', 4.0, '1R')             |         153 |    -0.08  |   0.806 |       388 |        41.2 |        0.002 |            1.176 |         1.006 |           0.932 |         0.865 |           -17.9 |             10 |      0.05 |             4.69 |          0.057 |             0.2 |
| ('swl', 'exp', 4.0, 'psh')            |         153 |    -0.045 |   0.849 |       388 |        43.3 |       -0.005 |            1.2   |         0.984 |           0.893 |         0.812 |           -17.1 |             10 |     -0.12 |             4.69 |          0.057 |            -0.5 |

Per year (avg net R, 1x, all variants):

| variant (avg R/yr, 1x)      |   2019 |   2020 |   2021 |   2022 |   2023 |   2024 |   2025 |
|:----------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| ('swl', 'stop', 1.0, '1R')  | -0.094 | -0.044 | -0.077 | -0.059 | -0.134 | -0.023 | -0.08  |
| ('swl', 'stop', 1.0, 'psh') | -0.124 | -0.048 | -0.101 | -0.085 | -0.126 | -0.034 | -0.072 |
| ('swl', 'stop', 4.0, '1R')  |  0.028 | -0.008 |  0.046 | -0.013 | -0.052 | -0.029 | -0.076 |
| ('swl', 'stop', 4.0, 'psh') | -0.005 | -0.019 |  0.018 | -0.049 | -0.069 | -0.035 | -0.062 |
| ('ema', 'stop', 1.0, '1R')  | -0.141 | -0.096 | -0.123 | -0.116 | -0.11  | -0.067 |  0.003 |
| ('ema', 'stop', 1.0, 'psh') | -0.162 | -0.102 | -0.123 | -0.124 | -0.108 | -0.088 | -0.011 |
| ('ema', 'stop', 4.0, '1R')  |  0.008 | -0.053 | -0.065 | -0.028 | -0.044 | -0.048 |  0.014 |
| ('ema', 'stop', 4.0, 'psh') | -0.018 | -0.057 | -0.069 | -0.051 | -0.062 | -0.055 | -0.002 |
| ('swl', 'exp', 1.0, '1R')   | -0.127 | -0.125 | -0.047 | -0.152 | -0.037 |  0.054 | -0.143 |
| ('swl', 'exp', 1.0, 'psh')  | -0.119 | -0.124 | -0.08  | -0.172 | -0.033 |  0.059 | -0.081 |
| ('swl', 'exp', 4.0, '1R')   |  0.048 | -0.11  |  0.164 | -0.021 | -0.056 |  0.066 | -0.136 |
| ('swl', 'exp', 4.0, 'psh')  |  0.104 | -0.08  |  0.153 | -0.064 | -0.088 |  0.053 | -0.081 |

**TP leg vs trailed leg (average gross R of each 50% leg; in-sample 2019–2025):**

| param                       |    l1 |    l2 |
|:----------------------------|------:|------:|
| ('ema', 'stop', 1.0, '1R')  | 0.023 | 0.042 |
| ('ema', 'stop', 1.0, 'psh') | 0.002 | 0.042 |
| ('ema', 'stop', 4.0, '1R')  | 0.029 | 0.036 |
| ('ema', 'stop', 4.0, 'psh') | 0.005 | 0.036 |
| ('swl', 'exp', 1.0, '1R')   | 0.007 | 0.02  |
| ('swl', 'exp', 1.0, 'psh')  | 0.006 | 0.02  |
| ('swl', 'exp', 4.0, '1R')   | 0.035 | 0.042 |
| ('swl', 'exp', 4.0, 'psh')  | 0.044 | 0.042 |
| ('swl', 'stop', 1.0, '1R')  | 0.038 | 0.048 |
| ('swl', 'stop', 1.0, 'psh') | 0.013 | 0.048 |
| ('swl', 'stop', 4.0, '1R')  | 0.033 | 0.054 |
| ('swl', 'stop', 4.0, 'psh') | 0.006 | 0.054 |

### Hours (ICT, entry hour; WF OOS; information only)
|      |      0 |      1 |      2 |      3 |      7 |      8 |      9 |     10 |     11 |     12 |     13 |     14 |     15 |     16 |     17 |     18 |     19 |     20 |     21 |     22 |     23 |
|:-----|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| n    | 60     | 51     | 38     | 13     | 28     | 33     | 32     | 34     | 17     | 18     | 43     | 68     | 78     | 56     | 63     | 60     | 73     | 82     | 62     | 60     | 57     |
| expR |  0.036 | -0.145 | -0.171 | -0.418 | -0.079 |  0.307 | -0.004 |  0.037 | -0.012 |  0.061 | -0.211 |  0.068 |  0.009 | -0.149 |  0.015 |  0.002 |  0.304 | -0.107 |  0.306 | -0.145 | -0.033 |

## Part 3: Kai's lessons against the numbers
- **"Breakouts of swing highs extend":**
  - Kai's breakout of the latest M5 swing high in the H1 trend direction is the best XAU family we have tested on M5. The stitched OOS is near breakeven: 1026 trades, gross PF 1.209, net PF 1.009.
  - By comparison, the M5 EMA55 pullback had gross PF about 0.92 and net 0.69.
  - So the extension is real enough to cover costs once stops are floored at $4. Those variants are the least negative in-sample: the $4 floor beats the $1 floor in every pair. But it is not a statistically meaningful edge after 761 trials (Bonferroni t 3.82).
- **"Quiet pullback volume isn't a reason to wait":** we could not test a volume rule credibly.
  - Dukascopy 'volume' is its own tick/lot count, not exchange volume, and differs from IC's tick volume. It is unreliable as a filter, and we did not use it.
  - Our pullback rules ignore volume entirely and still found nothing robust, so waiting on volume is unsupported either way.
- **"Scale out + trail":**
  - Earlier, the fixed 2R exit (C) was the best exit in-sample across the EMA55 tests. Trailing variants (B) were no better after costs.
  - In this test, the trailed 50% leg averaged about +0.02 to +0.05R gross (in-sample), slightly better than the take-profit leg (+0.00 to +0.04R). Neither is large enough to cover costs of about 0.06–0.12R, and the 1R and 'prior swing high' TP choices barely differ. On 15 Oct, a stop trailed under M5 swing lows would have captured more than the fixed 1.26R TP, but on average trailing gives back most run-ups.
  - Scaling out is a risk-shaping choice, not an edge.
- **Bottom line:** Kai's read on 15 Oct was a good trade on one bar. Systematically, the same idea is about breakeven on 2021–25 OOS data after IC costs.
