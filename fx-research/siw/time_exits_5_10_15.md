# SIW v2 time exits: close at 5 / 10 / 15 min
Data: Dukascopy XAU/USD BID M5, 2026-10-23 20:50 → 2026-11-04 11:00 ICT (2076 bars, refreshed with latest Dukascopy bars).
Entry = open of bar after the confirm bar. Exit = close of bar 1/2/3 after entry (5/10/15 min), hard SL $5 checked first in each bar (worst-case intrabar).
$ = price move per 0.01 lot (1 oz: $1 move = $1), minus $0.28 cost per trade (same convention as exit_v3.py). allv2 = all SIW v2 signals (modes abc, dedupe=1).

**IN-SAMPLE, small n, ~1 week of data. The rules were tuned on this same week. Treat it as a description of the data, not proof of an edge.**

| set           | dir   | exit   |   n | win   |   total |   avg |   worst |   best |   sl_hits |
|:--------------|:------|:-------|----:|:------|--------:|------:|--------:|-------:|----------:|
| allv2         | S     | 5min   | 253 | 49%   |  -18.61 | -0.07 |   -5.28 |   9.77 |        15 |
| allv2         | S     | 10min  | 253 | 53%   |   39.01 |  0.15 |   -5.28 |  12.00 |        25 |
| allv2         | S     | 15min  | 253 | 52%   |   69.91 |  0.28 |   -5.28 |  10.97 |        45 |
| allv2         | B     | 5min   | 211 | 44%   |  -50.11 | -0.24 |   -5.28 |  11.82 |        13 |
| allv2         | B     | 10min  | 211 | 48%   |   -8.11 | -0.04 |   -5.28 |  25.87 |        26 |
| allv2         | B     | 15min  | 211 | 45%   |  -25.28 | -0.12 |   -5.28 |  28.50 |        46 |
| allv2         | all   | 5min   | 464 | 47%   |  -68.73 | -0.15 |   -5.28 |  11.82 |        28 |
| allv2         | all   | 10min  | 464 | 51%   |   30.90 |  0.07 |   -5.28 |  25.87 |        51 |
| allv2         | all   | 15min  | 464 | 49%   |   44.63 |  0.10 |   -5.28 |  28.50 |        91 |
| his20         | S     | 5min   |  15 | 73%   |   19.49 |  1.30 |   -1.55 |   5.89 |         0 |
| his20         | S     | 10min  |  15 | 87%   |   46.94 |  3.13 |   -1.63 |   8.06 |         0 |
| his20         | S     | 15min  |  15 | 87%   |   63.71 |  4.25 |   -0.75 |  10.97 |         0 |
| his20         | B     | 5min   |   5 | 100%  |   16.97 |  3.39 |    0.54 |   8.35 |         0 |
| his20         | B     | 10min  |   5 | 100%  |   18.13 |  3.63 |    0.33 |   6.17 |         0 |
| his20         | B     | 15min  |   5 | 80%   |   17.52 |  3.50 |   -0.76 |   7.46 |         0 |
| his20         | all   | 5min   |  20 | 80%   |   36.46 |  1.82 |   -1.55 |   8.35 |         0 |
| his20         | all   | 10min  |  20 | 90%   |   65.07 |  3.25 |   -1.63 |   8.06 |         0 |
| his20         | all   | 15min  |  20 | 85%   |   81.23 |  4.06 |   -0.76 |  10.97 |         0 |
| his_buys_nov4 | B     | 5min   |   2 | 100%  |    8.19 |  4.10 |    3.55 |   4.64 |         0 |
| his_buys_nov4 | B     | 10min  |   2 | 50%   |    3.90 |  1.95 |   -3.41 |   7.31 |         0 |
| his_buys_nov4 | B     | 15min  |   2 | 50%   |    1.03 |  0.52 |   -5.28 |   6.31 |         1 |
| his_buys_nov4 | all   | 5min   |   2 | 100%  |    8.19 |  4.10 |    3.55 |   4.64 |         0 |
| his_buys_nov4 | all   | 10min  |   2 | 50%   |    3.90 |  1.95 |   -3.41 |   7.31 |         0 |
| his_buys_nov4 | all   | 15min  |   2 | 50%   |    1.03 |  0.52 |   -5.28 |   6.31 |         1 |

## His 2 buys today (Nov 4)
- confirm 2026-11-04 06:45 ICT (detected by SIW: True) entry 3930.51 @ 06:50 ICT: 5m +4.64, 10m +7.31, 15m +6.31
- confirm 2026-11-04 09:30 ICT (detected by SIW: True) entry 3940.04 @ 09:35 ICT: 5m +3.55, 10m -3.41, 15m -5.28
