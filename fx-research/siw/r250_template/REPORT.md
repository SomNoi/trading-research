# R250 — SIW v2 top-3 of 2026-11-03 as templates, matched on IC 17 mo, Exit v4 — **ไม่เจอ**
Watch-only. PREREG.md sha256 8295d1a5…eabb08 (locked before IC outcomes).

## Step 1 — Nov 3 ICT (Dukascopy BID = SUBSTITUTE source; IC ends label 2026-10-09 17:55)
68 SIW v2 signals, Exit v4 (SL10/TP20/close L+2, $0.28). All 68 exited on TIME. Top 3: T1 SELL A_PIN 13:35 ICT +$8.41 · T2 BUY B_ENGULF 00:50 ICT +$5.90 · T3 SELL B_ENGULF 15:30 ICT +$5.74 (all in nov3_signals.csv).

## Step 2 — fingerprints (dir-adjusted: +ve = with trade direction; ATR14 units; hr = ICT; g=green L, g1/g2=green L-1/L-2)
| name   | side   | kind     |   hr |   body |   rej |   oth | g     | g1    | g2    |   rng_atr |   atr |   gap_a |   s21_a |   s55_a |   d21_a |   leg_atr |
|:-------|:-------|:---------|-----:|-------:|------:|------:|:------|:------|:------|----------:|------:|--------:|--------:|--------:|--------:|----------:|
| T1     | S      | A_PIN    |   13 |  0.151 | 0.644 | 0.205 | False | True  | True  |     0.64  | 4.123 |   1.505 |  -0.032 |   0.165 |  -0.391 |     0.728 |
| T2     | B      | B_ENGULF |    0 |  0.205 | 0.043 | 0.752 | True  | False | False |     1.488 | 3.886 |   2.489 |  -0.406 |   0.145 |  -1.045 |     0.854 |
| T3     | S      | B_ENGULF |   15 |  0.385 | 0.465 | 0.15  | False | True  | False |     0.622 | 3.457 |   2.179 |   0.227 |   0.33  |   0.816 |     1.49  |
T1: tiny-body shooting star (uw 64%), red, after 3 green bars into EMA21 (close $1.6 above EMA21) in established downtrend, Asia/London pre-open hour 13 ICT.
T2: green bar with long upper wick classed engulf after 2 red bars, strong uptrend gap 2.5 ATR, close 1 ATR below EMA21 (deep pullback), 00 ICT (NY late).
T3: red engulf after G/R/R, downtrend gap 2.2 ATR, close 0.8 ATR below EMA21, leg 1.5 ATR, 15 ICT (London open).

## Step 3/4 — matches on IC BID M5 (2025-05 → 2026-10-09), IS/OOS cut 2026-03-18/19, Bonferroni Z(N=6658)=4.33
| tier   | set   |   cap |   tpd |   IS_n |    IS_E |   OOS_n |   OOS_win |   OOS_E |   OOS_E15 |   OOS_PF |   OOS_Z |   RAND_OOS_E |   RAND_p_ge_obs | gate   |
|:-------|:------|------:|------:|-------:|--------:|--------:|----------:|--------:|----------:|---------:|--------:|-------------:|----------------:|:-------|
| TIGHT  | T1    |     1 | 1     |      8 |  -0.07  |       8 |     0.5   |  -0.554 |    -0.694 |    0.63  |  -0.511 |       -0.251 |           0.57  | fail   |
| TIGHT  | T2    |     1 | 0     |      0 | nan     |       0 |   nan     | nan     |   nan     |  nan     | nan     |      nan     |         nan     | fail   |
| TIGHT  | T3    |     1 | 1     |      1 |  -0.01  |       0 |   nan     | nan     |   nan     |  nan     | nan     |      nan     |         nan     | fail   |
| TIGHT  | UNION |     1 | 1     |      9 |  -0.063 |       8 |     0.5   |  -0.554 |    -0.694 |    0.63  |  -0.511 |       -0.278 |           0.562 | fail   |
| TIGHT  | UNION |     2 | 1.118 |     10 |   0.366 |       9 |     0.444 |  -0.512 |    -0.652 |    0.62  |  -0.531 |       -0.276 |           0.558 | fail   |
| TIGHT  | UNION |     3 | 1.118 |     10 |   0.366 |       9 |     0.444 |  -0.512 |    -0.652 |    0.62  |  -0.531 |       -0.117 |           0.568 | fail   |
| LOOSE  | T1    |     1 | 1     |     74 |  -0.286 |      58 |     0.603 |   0.523 |     0.383 |    1.413 |   1.01  |       -0.139 |           0.116 | fail   |
| LOOSE  | T2    |     1 | 1     |      1 |  -3.04  |       1 |     0     |  -3.85  |    -3.99  |    0     | nan     |       -0.13  |           0.848 | fail   |
| LOOSE  | T3    |     1 | 1     |     13 |  -0.152 |      10 |     0.5   |   0.218 |     0.078 |    1.108 |   0.145 |       -0.253 |           0.376 | fail   |
| LOOSE  | UNION |     1 | 1     |     77 |  -0.507 |      63 |     0.587 |   0.49  |     0.35  |    1.376 |   0.989 |       -0.223 |           0.12  | fail   |
| LOOSE  | UNION |     2 | 1.621 |    124 |  -0.195 |     103 |     0.534 |   0.521 |     0.381 |    1.422 |   1.366 |       -0.176 |           0.074 | fail   |
| LOOSE  | UNION |     3 | 1.971 |    154 |  -0.416 |     122 |     0.508 |   0.17  |     0.03  |    1.118 |   0.473 |       -0.165 |           0.244 | fail   |

Baselines: R249 all-SIW SELL OOS E −$0.05 PF 0.97 (n 4337); BUY OOS −$0.52 PF 0.72 (n 3832). RANDOM = same side/ICT hour/EMA sign/split, 500 draws (RAND_p_ge_obs = share of random draws ≥ observed).

## Reading
- TIGHT: only 17 days in 17 months matched (T2 zero, T3 one). Too rare to test; OOS −$0.55. 
- LOOSE: the best-looking cell (UNION cap2) OOS n103 E +$0.52 PF 1.42 Z 1.37, 1.5x cost +$0.38, random p 0.07 — but IS is negative (−$0.20, n124) and Z is far below 4.33. Sign flips between IS and OOS = noise. Cap3 drops to +$0.17. T1-loose: IS −$0.29, OOS +$0.52.
- 0/12 cells pass the gate.

## Caveat
The 3 templates were chosen with hindsight as the 3 best of 68 trades on one day, from a substitute data source (Dukascopy), during a 9-day down regime. A day's best trades are mostly luck (all 68 were time exits within 10 min). Matching them on history is a test of whether that luck has a shape; it does not.

**Verdict: ไม่เจอ.** N 6646 → 6658 (+12).
