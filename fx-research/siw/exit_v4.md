# SIW v2 exit v4 — SL $10 / TP $20 cap / time exit 10 min
Data: Dukascopy XAU/USD BID M5 2026-10-23 20:50 → 2026-11-04 11:00 ICT (2076 bars). Entry = open of L+1; per bar SL checked before TP (worst case); else exit at close of L+2. $ per 0.01 lot after $0.28 cost. all SIW v2 = detect() default (dedupe=1).

**IN-SAMPLE, ~1 week, rules tuned on the same data. Not proof of edge.**

| set             | dir   |   n | win   |   total |   avg |   worst |   best | exits              |
|:----------------|:------|----:|:------|--------:|------:|--------:|-------:|:-------------------|
| all SIW v2      | S     | 253 | 55%   |  103.30 |  0.41 |  -10.28 |  12.00 | TIME:251 SL:2      |
| all SIW v2      | B     | 211 | 49%   |   -6.51 | -0.03 |  -10.28 |  19.72 | TIME:208 SL:2 TP:1 |
| all SIW v2      | all   | 464 | 52%   |   96.79 |  0.21 |  -10.28 |  19.72 | TIME:459 SL:4 TP:1 |
| his 20 picks    | S     |  15 | 87%   |   46.94 |  3.13 |   -1.63 |   8.06 | TIME:15            |
| his 20 picks    | B     |   5 | 100%  |   18.13 |  3.63 |    0.33 |   6.17 | TIME:5             |
| his 20 picks    | all   |  20 | 90%   |   65.07 |  3.25 |   -1.63 |   8.06 | TIME:20            |
| his 2 buys Nov4 | B     |   2 | 50%   |    3.90 |  1.95 |   -3.41 |   7.31 | TIME:2             |
| his 2 buys Nov4 | all   |   2 | 50%   |    3.90 |  1.95 |   -3.41 |   7.31 | TIME:2             |

## His 2 buys Nov 4
- confirm 11-04 06:45 ICT, entry 3930.51 @ 06:50, exit by 07:00 ICT -> TIME +7.31 (EMA21>EMA55: True, SIW detects: True)
- confirm 11-04 09:30 ICT, entry 3940.04 @ 09:35, exit by 09:45 ICT -> TIME -3.41 (EMA21>EMA55: True, SIW detects: True)
