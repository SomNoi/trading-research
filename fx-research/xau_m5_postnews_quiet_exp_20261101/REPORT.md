# R232 REPORT — xau_m5_postnews_quiet_exp_20261101
Post-news (NFP/CPI/FOMC real cal) quiet t0+15→+30/45m (all bars<1·ATR) → first expansion ≥λ·ATR CONT, SL$2/4 TP3×SL T12

## Verdict
ไม่เจอ. best quietEnd=30 lam=1.0 SL=2 event=NFP_CPI OOS E+nanR ($+nan/0.01lot) PFnan znan n0 (IS E-1.140R n1); OOS>0 0/16; gate-PASS 0/16; Z_bonf 4.317; N=6330.

## Notes
Untestable: post-release bars almost never quiet (<1·pre-event ATR14) — 1 trade total at quietEnd+30, 0 at +45 across 42 events (16 NFP/15 CPI/11 FOMC). Not loosened post-hoc (prereg locked). Thicker n than R228 NOT achieved.

## Full grid (sorted by OOS E)
|   quietEnd |   lam |   SL | event   |   n_is |   E_is |   Eusd_is |   PF_is |   WR_is |   z_is |   n_oos |   E_oos |   Eusd_oos |   PF_oos |   WR_oos |   z_oos | PASS   |
|-----------:|------:|-----:|:--------|-------:|-------:|----------:|--------:|--------:|-------:|--------:|--------:|-----------:|---------:|---------:|--------:|:-------|
|         30 |   1   |    2 | NFP_CPI |      1 |  -1.14 |     -2.28 |       0 |       0 |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         30 |   1   |    2 | ALL     |      1 |  -1.14 |     -2.28 |       0 |       0 |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         30 |   1   |    4 | NFP_CPI |      1 |  -1.07 |     -4.28 |       0 |       0 |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         30 |   1   |    4 | ALL     |      1 |  -1.07 |     -4.28 |       0 |       0 |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         30 |   1.5 |    2 | NFP_CPI |      1 |  -1.14 |     -2.28 |       0 |       0 |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         30 |   1.5 |    2 | ALL     |      1 |  -1.14 |     -2.28 |       0 |       0 |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         30 |   1.5 |    4 | NFP_CPI |      1 |  -1.07 |     -4.28 |       0 |       0 |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         30 |   1.5 |    4 | ALL     |      1 |  -1.07 |     -4.28 |       0 |       0 |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         45 |   1   |    2 | NFP_CPI |      0 | nan    |    nan    |     nan |     nan |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         45 |   1   |    2 | ALL     |      0 | nan    |    nan    |     nan |     nan |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         45 |   1   |    4 | NFP_CPI |      0 | nan    |    nan    |     nan |     nan |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         45 |   1   |    4 | ALL     |      0 | nan    |    nan    |     nan |     nan |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         45 |   1.5 |    2 | NFP_CPI |      0 | nan    |    nan    |     nan |     nan |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         45 |   1.5 |    2 | ALL     |      0 | nan    |    nan    |     nan |     nan |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         45 |   1.5 |    4 | NFP_CPI |      0 | nan    |    nan    |     nan |     nan |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |
|         45 |   1.5 |    4 | ALL     |      0 | nan    |    nan    |     nan |     nan |    nan |       0 |     nan |        nan |      nan |      nan |     nan | False  |

Files: PREREG.md (444, sha256), run.py, results.csv, out.txt. Shared prep `_r227_229/prep.py`, engine `_r227_229/eng.py`.
