# R241 REPORT
PREREG locked (sha256 in PREREG.sha256). Cut 2026-03-18.

- R241 xau_m5_monthend_fix_fade_20261101 — Month-end WM/R 16:00 London fix: M=C1600−C1530 ≥k·ATR20 → FADE at 16:05, SL 15:30–16:05 extreme+0.30, TP 50% retrace/1.5R, exit 17:00; DayType ME/control/QE ×k1/1.5 (12 cells) — ไม่เจอ. best daytype=non_ME_control k=1.5 tp=1.5R OOS E+0.052R ($+1.93/0.01lot) PF1.10 z0.27 n35 (IS E-0.139R n38); OOS>0 1/12; gate-PASS 0/12; Z_bonf 4.322; N=6470.

```
           daytype    k          tp  SLbuf  n_IS   E_IS  Eusd_IS  PF_IS  WR_IS   z_IS  n_OOS  E_OOS  Eusd_OOS  PF_OOS  WR_OOS  z_OOS   PASS
0        month_end  1.0  50%retrace    0.3     1 -1.304   -1.200  0.000  0.000    NaN      4 -0.913    -2.563   0.034   0.250 -2.523  False
1        month_end  1.0        1.5R    0.3     2  1.332    7.070    NaN  1.000    NaN      5 -1.010    -4.302   0.000   0.000 -4.665  False
2        month_end  1.5  50%retrace    0.3     1 -1.304   -1.200  0.000  0.000    NaN      3 -0.873    -0.527   0.047   0.333 -1.717  False
3        month_end  1.5        1.5R    0.3     2  1.332    7.070    NaN  1.000    NaN      4 -1.004    -3.210   0.000   0.000 -3.594  False
4   non_ME_control  1.0  50%retrace    0.3    85 -0.310   -0.587  0.583  0.353 -1.939     57 -0.097    -0.232   0.830   0.474 -0.530  False
5   non_ME_control  1.0        1.5R    0.3    88 -0.291   -0.577  0.592  0.386 -2.333     61 -0.121     0.255   0.799   0.426 -0.836  False
6   non_ME_control  1.5  50%retrace    0.3    38 -0.060   -0.132  0.913  0.421 -0.204     34 -0.214    -0.143   0.640   0.471 -1.060  False
7   non_ME_control  1.5        1.5R    0.3    38 -0.139   -0.243  0.778  0.447 -0.722     35  0.052     1.932   1.101   0.514  0.266  False
8      quarter_end  1.0  50%retrace    0.3     0    NaN      NaN    NaN    NaN    NaN      1 -1.220    -1.550   0.000   0.000    NaN  False
9      quarter_end  1.0        1.5R    0.3     1  1.468   13.040    NaN  1.000    NaN      2 -0.721    -2.840   0.000   0.000    NaN  False
10     quarter_end  1.5  50%retrace    0.3     0    NaN      NaN    NaN    NaN    NaN      1 -1.220    -1.550   0.000   0.000    NaN  False
11     quarter_end  1.5        1.5R    0.3     1  1.468   13.040    NaN  1.000    NaN      2 -0.721    -2.840   0.000   0.000    NaN  False
```
 ME arm: n_OOS 3–5, E_OOS −0.87…−1.01R all 4 cells (18 ME days total, 6 QE); control ≈ flat/neg → no ME-specific edge.
