# R242 REPORT
PREREG locked (sha256 in PREREG.sha256). Cut 2026-03-18.

- R242 xau_m5_er_compress_burst_20261101 — Kaufman ER10 compression (≥nq/8 bars ER<0.2, box<1.2·ATR50, box≥minbox) → ER10≥0.6 close outside box, CONT/FADE, SL box side (mirrored for FADE), TP1/2R T12, 07–20 UTC — ไม่เจอ. best nq=6 minbox=2.5 TPm=1 arm=CONT OOS E+0.979R ($+12.87/0.01lot) PFnan znan n1 (IS E+0.354R n3); OOS>0 8/16; gate-PASS 0/16; Z_bonf 4.323; N=6486.

```
    nq  minbox  TPm   arm  n_IS   E_IS  Eusd_IS  PF_IS  WR_IS   z_IS  n_OOS  E_OOS  Eusd_OOS  PF_OOS  WR_OOS  z_OOS   PASS
0    6     2.5    2  CONT     2  0.689    3.110  3.418  0.500    NaN      1  0.159      2.09     NaN     1.0    NaN  False
1    6     2.5    2  FADE     3 -0.428   -3.787  0.279  0.333 -0.908      1 -1.021    -13.43     0.0     0.0    NaN  False
2    6     2.5    1  CONT     3  0.354    3.227  2.863  0.667  0.756      1  0.979     12.87     NaN     1.0    NaN  False
3    6     2.5    1  FADE     3 -0.428   -3.787  0.279  0.333 -0.908      1 -1.021    -13.43     0.0     0.0    NaN  False
4    6     3.5    2  CONT     2  0.689    3.110  3.418  0.500    NaN      1  0.159      2.09     NaN     1.0    NaN  False
5    6     3.5    2  FADE     3 -0.428   -3.787  0.279  0.333 -0.908      1 -1.021    -13.43     0.0     0.0    NaN  False
6    6     3.5    1  CONT     3  0.354    3.227  2.863  0.667  0.756      1  0.979     12.87     NaN     1.0    NaN  False
7    6     3.5    1  FADE     3 -0.428   -3.787  0.279  0.333 -0.908      1 -1.021    -13.43     0.0     0.0    NaN  False
8    7     2.5    2  CONT     1  1.948   10.500    NaN  1.000    NaN      1  0.159      2.09     NaN     1.0    NaN  False
9    7     2.5    2  FADE     1 -1.052   -5.670  0.000  0.000    NaN      1 -1.021    -13.43     0.0     0.0    NaN  False
10   7     2.5    1  CONT     1  0.948    5.110    NaN  1.000    NaN      1  0.979     12.87     NaN     1.0    NaN  False
11   7     2.5    1  FADE     1 -1.052   -5.670  0.000  0.000    NaN      1 -1.021    -13.43     0.0     0.0    NaN  False
12   7     3.5    2  CONT     1  1.948   10.500    NaN  1.000    NaN      1  0.159      2.09     NaN     1.0    NaN  False
13   7     3.5    2  FADE     1 -1.052   -5.670  0.000  0.000    NaN      1 -1.021    -13.43     0.0     0.0    NaN  False
14   7     3.5    1  CONT     1  0.948    5.110    NaN  1.000    NaN      1  0.979     12.87     NaN     1.0    NaN  False
15   7     3.5    1  FADE     1 -1.052   -5.670  0.000  0.000    NaN      1 -1.021    -13.43     0.0     0.0    NaN  False
```
 Setup+trigger nearly mutually exclusive: n_IS 1–3, n_OOS 1 per cell → untestable/thin.
