# R238 REPORT
PREREG locked (sha256 in PREREG.sha256). Cut 2026-03-18.

- R238 xau_m5_asia_ldn_gapfill_20261101 — Asia 06:55 close→LDN 07:00 open gap |G|≥λ·ATR, FADE on first 07:xx close crossing C_asia+f·G, SL beyond open/0.5|G|, TP1.5/2×SL T12, 1/day — ไม่เจอ. best lam=0.3 f=0.5 SLmode=beyond_open TPm=1.5 OOS E+nanR ($+nan/0.01lot) PFnan znan n0 (IS E+nanR n0); OOS>0 0/16; gate-PASS 0/16; Z_bonf 4.321; N=6426.

```
    lam    f       SLmode  TPm  n_IS  E_IS  Eusd_IS  PF_IS  WR_IS  z_IS  n_OOS  E_OOS  Eusd_OOS  PF_OOS  WR_OOS  z_OOS   PASS
0   0.3  0.5  beyond_open  1.5     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
1   0.3  0.5  beyond_open  2.0     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
2   0.3  0.5     half_gap  1.5     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
3   0.3  0.5     half_gap  2.0     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
4   0.3  0.7  beyond_open  1.5     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
5   0.3  0.7  beyond_open  2.0     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
6   0.3  0.7     half_gap  1.5     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
7   0.3  0.7     half_gap  2.0     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
8   0.6  0.5  beyond_open  1.5     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
9   0.6  0.5  beyond_open  2.0     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
10  0.6  0.5     half_gap  1.5     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
11  0.6  0.5     half_gap  2.0     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
12  0.6  0.7  beyond_open  1.5     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
13  0.6  0.7  beyond_open  2.0     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
14  0.6  0.7     half_gap  1.5     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
15  0.6  0.7     half_gap  2.0     0   NaN      NaN    NaN    NaN   NaN      0    NaN       NaN     NaN     NaN    NaN  False
```
Structural: XAU trades continuously through 07:00 UTC; 06:55-close→07:00-open |G|/ATR14 median 0.006, p99 0.156, max 0.187 over 362 days → λ≥0.3 never triggers; n=0 all 16 cells.
