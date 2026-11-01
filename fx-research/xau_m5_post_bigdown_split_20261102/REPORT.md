# R245 REPORT
PREREG locked (sha256 in PREREG.sha256). Cut 2026-03-18.

- R245 xau_m5_post_bigdown_split_20261102 — Post big down D1 (r<0, |r|≥p90 trailing60 lagged) next UTC day: A FADE long 07–10 / B CONT short 12–16, entry window open (λ0) or after first |C−O|≥0.3ATR bar, SL$4/8 TP1.5/2×SL, exit window end — ไม่เจอ. best arm=A_fade_ldn lam=0.0 SL=4 TPm=2.0 OOS E+0.930R ($+3.72/0.01lot) PF3.61 z1.47 n6 (IS E-1.070R n6); OOS>0 8/16; gate-PASS 0/16; Z_bonf 4.324; N=6534.

```
             arm  lam  SL  TPm  n_IS   E_IS  Eusd_IS  PF_IS  WR_IS   z_IS  n_OOS  E_OOS  Eusd_OOS  PF_OOS  WR_OOS  z_OOS   PASS
0     A_fade_ldn  0.0   4  1.5     6 -1.070   -4.280  0.000  0.000   -inf      6  0.597     2.387   2.673   0.667  1.132  False
1     A_fade_ldn  0.0   4  2.0     6 -1.070   -4.280  0.000  0.000   -inf      6  0.930     3.720   3.607   0.667  1.470  False
2     A_fade_ldn  0.0   8  1.5     6 -1.035   -8.280  0.000  0.000   -inf      6  0.493     3.947   2.430   0.667  0.985  False
3     A_fade_ldn  0.0   8  2.0     6 -1.035   -8.280  0.000  0.000   -inf      6  0.743     5.947   3.155   0.667  1.238  False
4     A_fade_ldn  0.3   4  1.5     6 -0.237   -0.947  0.668  0.333 -0.449      6 -0.237    -0.947   0.668   0.333 -0.449  False
5     A_fade_ldn  0.3   4  2.0     6 -0.570   -2.280  0.361  0.167 -1.140      6 -0.070    -0.280   0.902   0.333 -0.111  False
6     A_fade_ldn  0.3   8  1.5     6 -0.202   -1.613  0.708  0.333 -0.383      6  0.410     3.282   2.189   0.667  0.816  False
7     A_fade_ldn  0.3   8  2.0     6 -0.035   -0.280  0.949  0.333 -0.055      6  0.160     1.282   1.310   0.500  0.267  False
8   B_cont_ldnny  0.0   4  1.5     6 -0.237   -0.947  0.668  0.333 -0.449      6 -0.653    -2.613   0.267   0.167 -1.568  False
9   B_cont_ldnny  0.0   4  2.0     6 -0.070   -0.280  0.902  0.333 -0.111      6 -0.570    -2.280   0.361   0.167 -1.140  False
10  B_cont_ldnny  0.0   8  1.5     6 -0.202   -1.613  0.708  0.333 -0.383      6 -0.202    -1.613   0.708   0.333 -0.383  False
11  B_cont_ldnny  0.0   8  2.0     6 -0.035   -0.280  0.949  0.333 -0.055      6 -0.035    -0.280   0.949   0.333 -0.055  False
12  B_cont_ldnny  0.3   4  1.5     6  0.597    2.387  2.673  0.667  1.132      6  0.180     0.720   1.336   0.500  0.322  False
13  B_cont_ldnny  0.3   4  2.0     6  0.930    3.720  3.607  0.667  1.470      6  0.430     1.720   1.804   0.500  0.641  False
14  B_cont_ldnny  0.3   8  1.5     6  0.632    5.053  2.831  0.667  1.199      6 -0.202    -1.613   0.708   0.333 -0.383  False
15  B_cont_ldnny  0.3   8  2.0     6  0.465    3.720  1.899  0.500  0.693      6 -0.035    -0.280   0.949   0.333 -0.055  False
```
Note: only 18 big down days in sample → n=6 IS / 6 OOS per cell; untestable/thin; IS/OOS signs flip.
