# R240 REPORT
PREREG locked (sha256 in PREREG.sha256). Cut 2026-03-18.

- R240 xau_m5_ldn_auction_drift_20261101 — LBMA PM auction 15:00 London (DST-aware) M5 bar |body|≥λ·ATR → CONT at 15:05, SL bar far end ±0.30, TP1.5R or 15:30 exit, ×arm×ATR14/20; post-2015 e-auction only — ไม่เจอ. best lam=0.5 arm=SHORT_only tp=1.5R ATR=14 OOS E+0.107R ($+0.05/0.01lot) PF1.29 z0.66 n37 (IS E-0.097R n54); OOS>0 4/16; gate-PASS 0/16; Z_bonf 4.322; N=6458.

```
    lam         arm              tp  ATR  n_IS   E_IS  Eusd_IS  PF_IS  WR_IS   z_IS  n_OOS  E_OOS  Eusd_OOS  PF_OOS  WR_OOS  z_OOS   PASS
0   0.3   CONT_both            1.5R   14   147 -0.033    0.203  0.934  0.435 -0.382    105 -0.050    -0.820   0.899   0.448 -0.496  False
1   0.3   CONT_both            1.5R   20   146 -0.026    0.310  0.948  0.438 -0.297    105 -0.051    -0.788   0.898   0.448 -0.501  False
2   0.3   CONT_both  exit_1530_only   14   147 -0.011    0.420  0.980  0.401 -0.099    105 -0.147    -1.318   0.723   0.400 -1.368  False
3   0.3   CONT_both  exit_1530_only   20   146 -0.035    0.439  0.934  0.404 -0.340    105 -0.152    -1.291   0.715   0.400 -1.415  False
4   0.3  SHORT_only            1.5R   14    68 -0.082   -1.289  0.852  0.397 -0.620     52 -0.045    -0.658   0.902   0.462 -0.328  False
5   0.3  SHORT_only            1.5R   20    68 -0.081   -1.214  0.854  0.397 -0.611     51  0.023    -0.293   1.055   0.490  0.167  False
6   0.3  SHORT_only  exit_1530_only   14    68 -0.086   -1.274  0.855  0.353 -0.536     52 -0.131    -1.145   0.726   0.442 -0.954  False
7   0.3  SHORT_only  exit_1530_only   20    68 -0.098   -1.241  0.833  0.353 -0.622     51 -0.114    -0.992   0.757   0.451 -0.818  False
8   0.5   CONT_both            1.5R   14   106  0.010    0.961  1.022  0.453  0.102     76  0.002    -0.855   1.004   0.474  0.016  False
9   0.5   CONT_both            1.5R   20   106  0.026    1.024  1.055  0.462  0.250     79 -0.087    -1.356   0.824   0.430 -0.768  False
10  0.5   CONT_both  exit_1530_only   14   106  0.051    1.241  1.105  0.443  0.423     76 -0.033    -1.060   0.932   0.447 -0.245  False
11  0.5   CONT_both  exit_1530_only   20   106  0.045    1.251  1.092  0.443  0.372     79 -0.109    -1.511   0.786   0.405 -0.854  False
12  0.5  SHORT_only            1.5R   14    54 -0.097   -1.262  0.824  0.389 -0.665     37  0.107     0.054   1.287   0.541  0.660  False
13  0.5  SHORT_only            1.5R   20    54 -0.053   -1.047  0.902  0.407 -0.355     40 -0.013    -0.490   0.969   0.475 -0.085  False
14  0.5  SHORT_only  exit_1530_only   14    54 -0.074   -1.190  0.869  0.370 -0.422     37  0.071    -0.228   1.189   0.541  0.414  False
15  0.5  SHORT_only  exit_1530_only   20    54 -0.071   -1.078  0.874  0.370 -0.407     40 -0.040    -0.796   0.904   0.475 -0.254  False
```
 Data 2025-05→2026-10 = post-2015 e-auction only. SHORT_only IS<0 all cells.
