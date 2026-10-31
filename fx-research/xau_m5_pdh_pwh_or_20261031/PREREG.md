# R94 PREREG — OR-pool PDH∪PWH first CONT break, XAU M5 (DATA SUBSTITUTE parquet M5 ≠ IC BID)
- Data: /workspace/fx-research/data/from_parquet_m1/XAUUSD_M5.csv (parquet M1->M5 mid, NOT IC BID)
- PDH = prior UTC-day High; PWH = prior ISO-week High.
- Break event at bar i (day d): C[i]>L and C[i-1]<=L for L in {PDH,PWH}. Signal = first break of either level on day d (1 trade/day). LevelTag = PDH / PWH / BOTH.
- Long only, entry next bar open, SL $3.5, TP 1.5R ($5.25), time exit H bars. Cost $0.28/trade (also report $0.42).
- Grid 16: Day{any,MonTue,WedThu,TueWedThu} × H{12,24} × ATR{any,Q4 (ATR14 pct over 2880 bars ≥0.75)}.
- Split 60/40 by day. PASS: OOS n≥150, OOS PF≥1.25, OOS E>0, IS PF>1. No loosening.
- Distinct from R73/R74/R92/R93 (union pool, crossing definition, H{12,24}).
