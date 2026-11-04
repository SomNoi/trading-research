# SIW v2 exit v3 (SL $5 / TP $20, trailing after 15 min)
Dukascopy BID XAUUSD M5 Oct29-Nov3, entry next open, cost $0.28/0.01, $ = per 0.01 lot. Trail from best price since entry, activated after 3 bars; stop never looser than SL; stop checked before TP in a bar; best updated after the bar. Timeout 48 bars. IN-SAMPLE, small n.

| set   | dir   | exit   |   n | win   |    net |   avg |   worst |   best | exits                     |
|:------|:------|:-------|----:|:------|-------:|------:|--------:|-------:|:--------------------------|
| his20 | S     | T2     |  15 | 93%   |  63.01 |  4.20 |   -1.70 |   9.49 | TRAIL:15                  |
| his20 | S     | T3     |  15 | 87%   |  64.68 |  4.31 |   -2.70 |  19.72 | TRAIL:14 TP:1             |
| his20 | S     | T5     |  15 | 87%   |  76.78 |  5.12 |   -4.70 |  19.72 | TRAIL:13 TP:2             |
| his20 | S     | T2+BE  |  15 | 87%   |  63.19 |  4.21 |   -0.54 |   9.49 | TRAIL:15                  |
| his20 | S     | T3+BE  |  15 | 87%   |  66.85 |  4.46 |   -0.54 |  19.72 | TRAIL:14 TP:1             |
| his20 | S     | T5+BE  |  15 | 87%   |  82.96 |  5.53 |   -0.54 |  19.72 | TRAIL:13 TP:2             |
| his20 | B     | T2     |   5 | 80%   |  16.50 |  3.30 |   -0.67 |   6.43 | TRAIL:5                   |
| his20 | B     | T3     |   5 | 80%   |  14.23 |  2.85 |   -0.67 |   5.43 | TRAIL:5                   |
| his20 | B     | T5     |   5 | 60%   |   7.57 |  1.51 |   -1.01 |   4.77 | TRAIL:5                   |
| his20 | B     | T2+BE  |   5 | 80%   |  16.50 |  3.30 |   -0.67 |   6.43 | TRAIL:5                   |
| his20 | B     | T3+BE  |   5 | 80%   |  14.23 |  2.85 |   -0.67 |   5.43 | TRAIL:5                   |
| his20 | B     | T5+BE  |   5 | 60%   |   7.98 |  1.60 |   -0.67 |   4.77 | TRAIL:5                   |
| his20 | all   | T2     |  20 | 90%   |  79.51 |  3.98 |   -1.70 |   9.49 | TRAIL:20                  |
| his20 | all   | T3     |  20 | 85%   |  78.90 |  3.95 |   -2.70 |  19.72 | TRAIL:19 TP:1             |
| his20 | all   | T5     |  20 | 80%   |  84.35 |  4.22 |   -4.70 |  19.72 | TRAIL:18 TP:2             |
| his20 | all   | T2+BE  |  20 | 85%   |  79.69 |  3.98 |   -0.67 |   9.49 | TRAIL:20                  |
| his20 | all   | T3+BE  |  20 | 85%   |  81.08 |  4.05 |   -0.67 |  19.72 | TRAIL:19 TP:1             |
| his20 | all   | T5+BE  |  20 | 80%   |  90.95 |  4.55 |   -0.67 |  19.72 | TRAIL:18 TP:2             |
| allv2 | S     | T2     | 148 | 55%   | 127.48 |  0.86 |   -5.28 |  13.51 | TRAIL:115 SL:30 TO:3      |
| allv2 | S     | T3     | 148 | 51%   | 134.20 |  0.91 |   -5.28 |  19.72 | TRAIL:112 SL:30 TP:3 TO:3 |
| allv2 | S     | T5     | 148 | 47%   | 107.77 |  0.73 |   -5.28 |  19.72 | TRAIL:110 SL:30 TP:4 TO:4 |
| allv2 | S     | T2+BE  | 148 | 54%   | 127.19 |  0.86 |   -5.28 |  13.51 | TRAIL:115 SL:30 TO:3      |
| allv2 | S     | T3+BE  | 148 | 49%   | 145.80 |  0.99 |   -5.28 |  19.72 | TRAIL:112 SL:30 TP:3 TO:3 |
| allv2 | S     | T5+BE  | 148 | 41%   | 113.72 |  0.77 |   -5.28 |  19.72 | TRAIL:112 SL:30 TP:3 TO:3 |
| allv2 | B     | T2     |  81 | 40%   | -43.09 | -0.53 |   -5.28 |  19.72 | TRAIL:54 SL:26 TP:1       |
| allv2 | B     | T3     |  81 | 36%   | -22.21 | -0.27 |   -5.28 |  19.72 | TRAIL:52 SL:26 TP:3       |
| allv2 | B     | T5     |  81 | 33%   | -79.64 | -0.98 |   -5.28 |  19.72 | TRAIL:52 SL:26 TP:3       |
| allv2 | B     | T2+BE  |  81 | 40%   | -40.68 | -0.50 |   -5.28 |  19.72 | TRAIL:54 SL:26 TP:1       |
| allv2 | B     | T3+BE  |  81 | 35%   | -15.07 | -0.19 |   -5.28 |  19.72 | TRAIL:52 SL:26 TP:3       |
| allv2 | B     | T5+BE  |  81 | 28%   | -53.95 | -0.67 |   -5.28 |  19.72 | TRAIL:52 SL:26 TP:3       |
| allv2 | all   | T2     | 229 | 50%   |  84.39 |  0.37 |   -5.28 |  19.72 | TRAIL:169 SL:56 TO:3 TP:1 |
| allv2 | all   | T3     | 229 | 45%   | 111.99 |  0.49 |   -5.28 |  19.72 | TRAIL:164 SL:56 TP:6 TO:3 |
| allv2 | all   | T5     | 229 | 42%   |  28.13 |  0.12 |   -5.28 |  19.72 | TRAIL:162 SL:56 TP:7 TO:4 |
| allv2 | all   | T2+BE  | 229 | 49%   |  86.51 |  0.38 |   -5.28 |  19.72 | TRAIL:169 SL:56 TO:3 TP:1 |
| allv2 | all   | T3+BE  | 229 | 44%   | 130.73 |  0.57 |   -5.28 |  19.72 | TRAIL:164 SL:56 TP:6 TO:3 |
| allv2 | all   | T5+BE  | 229 | 36%   |  59.77 |  0.26 |   -5.28 |  19.72 | TRAIL:164 SL:56 TP:6 TO:3 |

## Previous: 15-min time exit (close of bar 3, no SL)
| set   | dir   |   n |   win |    net |   avg |   worst |
|:------|:------|----:|------:|-------:|------:|--------:|
| his20 | S     |  15 |  0.87 |  63.71 |  4.25 |   -0.75 |
| his20 | B     |   5 |  0.80 |  17.52 |  3.50 |   -0.76 |
| allv2 | S     | 148 |  0.59 | 137.84 |  0.93 |   -8.40 |
| allv2 | B     |  81 |  0.44 | -59.52 | -0.73 |  -12.89 |