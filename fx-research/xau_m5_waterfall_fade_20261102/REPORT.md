# R243 REPORT
PREREG locked (sha256 in PREREG.sha256). Cut 2026-03-18.

- R243 xau_m5_waterfall_fade_20261102 — HTF waterfall (≥N consecutive bear bars body/range≥0.6 on H1/H4) → FADE long on first M5 small-body≤0.4 or lower-wick≥0.6 in next TF bar, SL low−0.5, TP1.5/2R T12 — ไม่เจอ. best TF=1h N=4 trig=wick60 TPm=1.5 OOS E+nanR ($+nan/0.01lot) PFnan znan n0 (IS E+nanR n0); OOS>0 0/16; gate-PASS 0/16; Z_bonf 4.323; N=6502.

```
    TF  N     trig  TPm  n_IS   E_IS  Eusd_IS  PF_IS  WR_IS  z_IS  n_OOS  E_OOS  Eusd_OOS  PF_OOS  WR_OOS  z_OOS   PASS
0   1h  4   wick60  1.5     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
1   1h  4   wick60  2.0     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
2   1h  4  small40  1.5     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
3   1h  4  small40  2.0     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
4   1h  5   wick60  1.5     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
5   1h  5   wick60  2.0     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
6   1h  5  small40  1.5     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
7   1h  5  small40  2.0     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
8   4h  4   wick60  1.5     1 -1.097    -3.16    0.0    0.0   NaN      0    NaN       NaN     NaN     NaN    NaN  False
9   4h  4   wick60  2.0     1 -1.097    -3.16    0.0    0.0   NaN      0    NaN       NaN     NaN     NaN    NaN  False
10  4h  4  small40  1.5     1  1.418     4.82    NaN    1.0   NaN      0    NaN       NaN     NaN     NaN    NaN  False
11  4h  4  small40  2.0     1  1.918     6.52    NaN    1.0   NaN      0    NaN       NaN     NaN     NaN    NaN  False
12  4h  5   wick60  1.5     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
13  4h  5   wick60  2.0     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
14  4h  5  small40  1.5     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
15  4h  5  small40  2.0     0    NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
```
Note: streak counts (β0.6) H1 len1/2/3/≥4 = 1091/154/14/0; H4 = 273/35/4/1 → N≥4 waterfall almost never occurs on XAU (≤1 arm in 17 months) → untestable.
