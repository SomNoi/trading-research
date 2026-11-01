# R244 REPORT
PREREG locked (sha256 in PREREG.sha256). Cut 2026-03-18.

- R244 xau_m5_htf_ma_retest_short_20261102 — Below slow HTF MA (SMA/EMA50 on completed D1/H4): M5 first touch from below (H≥MA, prior H<MA, prior C<MA) + reject (C<mid or C<MA) → short next open, SL max(H,MA)+0.5, TP1.5/2R T12 — ไม่เจอ. best MA=SMA50 TF=4h TPm=2.0 sess=LDNNY OOS E-0.075R ($+0.38/0.01lot) PF0.90 z-0.33 n39 (IS E-0.203R n67); OOS>0 0/16; gate-PASS 0/16; Z_bonf 4.324; N=6518.

```
       MA  TF  TPm   sess  n_IS   E_IS  Eusd_IS  PF_IS  WR_IS   z_IS  n_OOS  E_OOS  Eusd_OOS  PF_OOS  WR_OOS  z_OOS   PASS
0   SMA50  1D  1.5    any    37 -0.409   -0.860  0.492  0.297 -2.134     22 -0.173     1.274   0.740   0.409 -0.680  False
1   SMA50  1D  1.5  LDNNY    24 -0.127   -0.525  0.815  0.417 -0.490     15 -0.210     2.222   0.689   0.400 -0.685  False
2   SMA50  1D  2.0    any    36 -0.442   -1.021  0.485  0.250 -2.104     22 -0.150     1.290   0.789   0.364 -0.519  False
3   SMA50  1D  2.0  LDNNY    23 -0.188   -0.790  0.753  0.348 -0.648     15 -0.076     3.003   0.887   0.400 -0.213  False
4   SMA50  4h  1.5    any   108 -0.217   -0.200  0.690  0.380 -1.902     61 -0.172    -0.185   0.749   0.377 -1.107  False
5   SMA50  4h  1.5  LDNNY    68 -0.260   -0.807  0.642  0.353 -1.804     39 -0.096     0.292   0.853   0.410 -0.485  False
6   SMA50  4h  2.0    any   106 -0.137   -0.035  0.810  0.358 -1.035     61 -0.150    -0.111   0.797   0.328 -0.845  False
7   SMA50  4h  2.0  LDNNY    67 -0.203   -0.695  0.730  0.328 -1.226     39 -0.075     0.379   0.895   0.359 -0.329  False
8   EMA50  1D  1.5    any    28 -0.264   -0.588  0.645  0.357 -1.142     49 -0.251    -0.422   0.653   0.347 -1.470  False
9   EMA50  1D  1.5  LDNNY    21 -0.331   -0.969  0.570  0.333 -1.267     29 -0.173    -0.534   0.745   0.379 -0.772  False
10  EMA50  1D  2.0    any    28 -0.230   -0.500  0.707  0.321 -0.878     49 -0.381    -1.473   0.536   0.245 -2.104  False
11  EMA50  1D  2.0  LDNNY    21 -0.214   -0.825  0.722  0.333 -0.711     29 -0.392    -2.112   0.512   0.241 -1.720  False
12  EMA50  4h  1.5    any   109 -0.222   -0.293  0.682  0.376 -1.958     76 -0.220    -1.191   0.684   0.355 -1.615  False
13  EMA50  4h  1.5  LDNNY    64 -0.408   -1.176  0.484  0.312 -2.899     44 -0.123    -0.811   0.812   0.386 -0.667  False
14  EMA50  4h  2.0    any   106 -0.159   -0.010  0.782  0.349 -1.206     76 -0.361    -1.784   0.549   0.250 -2.488  False
15  EMA50  4h  2.0  LDNNY    63 -0.309   -0.904  0.615  0.302 -1.856     44 -0.146    -1.087   0.799   0.318 -0.696  False
```
Note: all 16 cells E_IS<0 and E_OOS<0 (PF 0.51–0.95) → shorting HTF-MA retest from below is negative on XAU.
