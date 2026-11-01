# R228 REPORT — xau_m5_news_realcal_20261101
Real-calendar (FRED/Fed) NFP/CPI/FOMC ±5/15m first spike ≥λ·ATR CONT/FADE, SL$5 TP$10 T12

## Verdict
ไม่เจอ. best family=CPI_FOMC arm=CONT lam=1.5 w=15 OOS E+0.853R ($+4.27/0.01lot) PF3.22 z1.87 n11 (IS E+0.098R n13); OOS>0 7/16; gate-PASS 0/16; Z_bonf 4.315; N=6266.

## Notes
Thin-n: only 16 NFP / 15 CPI / 11 FOMC in sample; OOS n≤11 per cell → n≥50 gate impossible, any positive cell is noise-level (best z 1.87). Real calendar removes R221 DOW-proxy weakness (proxy windows hit many non-event days, and 2025 shutdown shifted NFP to 11-20/12-16, CPI to 10-24) but answer is unchanged: no testable edge.

## Full grid (sorted by OOS E)
| family   | arm   |   lam |   w |   n_events |   n_is |   E_is |   Eusd_is |   PF_is |   WR_is |   z_is |   n_oos |   E_oos |   Eusd_oos |   PF_oos |   WR_oos |   z_oos | PASS   |
|:---------|:------|------:|----:|-----------:|-------:|-------:|----------:|--------:|--------:|-------:|--------:|--------:|-----------:|---------:|---------:|--------:|:-------|
| CPI_FOMC | CONT  |   1.5 |  15 |         26 |     13 |  0.098 |     0.489 |   1.151 |   0.385 |  0.232 |      11 |   0.853 |      4.265 |    3.222 |    0.636 |   1.869 | False  |
| CPI_FOMC | CONT  |   1   |  15 |         26 |     15 | -0.256 |    -1.28  |   0.669 |   0.267 | -0.722 |      11 |   0.853 |      4.265 |    3.222 |    0.636 |   1.869 | False  |
| NFP      | CONT  |   1.5 |  15 |         16 |      6 | -0.556 |    -2.78  |   0.368 |   0.167 | -1.112 |       6 |   0.444 |      2.22  |    1.841 |    0.5   |   0.662 | False  |
| NFP      | CONT  |   1.5 |   5 |         16 |      4 |  0.444 |     2.22  |   1.841 |   0.5   |  0.513 |       6 |   0.444 |      2.22  |    1.841 |    0.5   |   0.662 | False  |
| NFP      | FADE  |   1   |   5 |         16 |      6 | -0.556 |    -2.78  |   0.368 |   0.167 | -1.112 |       6 |   0.444 |      2.22  |    1.841 |    0.5   |   0.662 | False  |
| CPI_FOMC | CONT  |   1.5 |   5 |         26 |     11 |  0.308 |     1.538 |   1.534 |   0.455 |  0.651 |      11 |   0.308 |      1.538 |    1.534 |    0.455 |   0.651 | False  |
| CPI_FOMC | CONT  |   1   |   5 |         26 |     15 | -0.056 |    -0.28  |   0.92  |   0.333 | -0.148 |      11 |   0.035 |      0.175 |    1.052 |    0.364 |   0.076 | False  |
| NFP      | FADE  |   1.5 |   5 |         16 |      4 | -0.306 |    -1.53  |   0.614 |   0.25  | -0.408 |       6 |  -0.056 |     -0.28  |    0.92  |    0.333 |  -0.089 | False  |
| NFP      | CONT  |   1   |  15 |         16 |      9 | -0.056 |    -0.28  |   0.92  |   0.333 | -0.112 |       6 |  -0.056 |     -0.28  |    0.92  |    0.333 |  -0.089 | False  |
| NFP      | CONT  |   1   |   5 |         16 |      6 | -0.056 |    -0.28  |   0.92  |   0.333 | -0.089 |       6 |  -0.056 |     -0.28  |    0.92  |    0.333 |  -0.089 | False  |
| CPI_FOMC | FADE  |   1   |   5 |         26 |     15 |  0.144 |     0.72  |   1.227 |   0.4   |  0.367 |      11 |  -0.238 |     -1.189 |    0.69  |    0.273 |  -0.563 | False  |
| CPI_FOMC | FADE  |   1.5 |   5 |         26 |     11 |  0.035 |     0.175 |   1.052 |   0.364 |  0.076 |      11 |  -0.238 |     -1.189 |    0.69  |    0.273 |  -0.563 | False  |
| CPI_FOMC | FADE  |   1.5 |  15 |         26 |     13 | -0.364 |    -1.818 |   0.552 |   0.231 | -0.997 |      11 |  -0.238 |     -1.189 |    0.69  |    0.273 |  -0.563 | False  |
| CPI_FOMC | FADE  |   1   |  15 |         26 |     15 | -0.056 |    -0.28  |   0.92  |   0.333 | -0.148 |      11 |  -0.511 |     -2.553 |    0.409 |    0.182 |  -1.395 | False  |
| NFP      | FADE  |   1.5 |  15 |         16 |      6 | -0.056 |    -0.28  |   0.92  |   0.333 | -0.089 |       6 |  -0.556 |     -2.78  |    0.368 |    0.167 |  -1.112 | False  |
| NFP      | FADE  |   1   |  15 |         16 |      9 | -0.056 |    -0.28  |   0.92  |   0.333 | -0.112 |       6 |  -0.556 |     -2.78  |    0.368 |    0.167 |  -1.112 | False  |

Files: PREREG.md (444, sha256), run.py, results.csv, out.txt. Shared prep `_r227_229/prep.py`, engine `_r227_229/eng.py`.
