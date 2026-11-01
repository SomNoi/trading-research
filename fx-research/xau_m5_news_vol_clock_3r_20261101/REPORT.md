# R221 REPORT — News/high-vol clock windows (NFP/CPI/FOMC proxy, LDN-NY overlap ATRQ4) first big bar CONT/FADE
DATA=IC BID XAUUSD M5 (ic-mt5-2026-10-10). Cost $0.28, SL$2/TP$6 (3R)+T, next-open entry, 1 position, 60/40 chrono (cut 2026-03-18).

Verdict: **ไม่เจอ** (0/16 pass PF≥1.2,n≥50,OOS&IS E>0). best OOS window=NFP_CPI_FOMC arm=CONT lam=0.5 T=6 E+0.222R PF1.30 z0.70 n36 (IS E-0.088); OOS>0 cells 2/16. Z_bonf=4.311 @N=6154. related R76/R165/Track11; engine µs-timestamp bug fixed (AMENDMENT.md).

```
      window  arm  lam  T  n_is   E_is  PF_is   z_is  n_oos  E_oos  PF_oos  z_oos  PASS
NFP_CPI_FOMC CONT  0.5  6    52 -0.088  0.883 -0.397     36  0.222   1.303  0.700 False
NFP_CPI_FOMC CONT  0.5 12    52  0.054  1.070  0.218     36  0.193   1.254  0.607 False
  OVERLAP_Q4 FADE  1.0 12   111 -0.311  0.656 -2.013    123 -0.164   0.809 -1.057 False
  OVERLAP_Q4 FADE  1.0  6   111 -0.311  0.656 -2.013    123 -0.164   0.809 -1.057 False
NFP_CPI_FOMC CONT  1.0  6    45 -0.105  0.865 -0.428     29 -0.174   0.798 -0.539 False
NFP_CPI_FOMC CONT  1.0 12    45 -0.060  0.926 -0.228     29 -0.174   0.798 -0.539 False
  OVERLAP_Q4 CONT  1.0  6   111 -0.527  0.454 -3.840    123 -0.197   0.774 -1.281 False
  OVERLAP_Q4 CONT  1.0 12   111 -0.527  0.454 -3.840    123 -0.197   0.774 -1.281 False
  OVERLAP_Q4 FADE  0.5 12   129 -0.241  0.728 -1.631    141 -0.204   0.767 -1.424 False
  OVERLAP_Q4 FADE  0.5  6   129 -0.270  0.697 -1.851    141 -0.204   0.767 -1.424 False
  OVERLAP_Q4 CONT  0.5  6   129 -0.458  0.516 -3.443    141 -0.204   0.767 -1.424 False
  OVERLAP_Q4 CONT  0.5 12   129 -0.458  0.516 -3.443    141 -0.204   0.767 -1.424 False
NFP_CPI_FOMC FADE  1.0  6    45 -0.270  0.667 -1.208     29 -0.242   0.721 -0.785 False
NFP_CPI_FOMC FADE  1.0 12    45 -0.134  0.834 -0.535     29 -0.312   0.654 -1.020 False
NFP_CPI_FOMC FADE  0.5  6    52 -0.521  0.421 -2.861     36 -0.584   0.405 -2.500 False
NFP_CPI_FOMC FADE  0.5 12    52 -0.497  0.461 -2.542     36 -0.584   0.405 -2.500 False
```
