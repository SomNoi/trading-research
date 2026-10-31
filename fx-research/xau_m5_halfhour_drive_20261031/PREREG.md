# R191 PREREG — Half-hour open drive (:00/:30) CONT/FADE, XAU M5, LDN∪NY 07–16 UTC
DATA: SUBSTITUTE data/from_parquet_m1/XAUUSD_M5.csv (≠ IC BID).
Signal bar i: minute∈{0,30}, hour 7–16 UTC, drive=C−O, |drive|≥λ·ATR14 (ATR through bar i), drive≠0. Entry next bar open (must be contiguous +5m).
CONT s=sign(drive); FADE s=−sign. SL $3.5, TP $5.25 (1.5R), time exit close of bar T. Cost $0.28 (also report $0.42).
Grid 16: λ{0.15,0.30}×Arm{CONT,FADE}×Hold{T3,T6}×Which{both(:00+:30),:00_only}. Max 1 trade per slot; no overlap.
Split 60/40 by bar index. N 5682→5698, Bonferroni Z.
PASS: OOS n≥100, OOS PF≥1.2, OOS E>0, IS PF>1, full t≥Z. Related R175 (hour-open, every hour); this = half-hour + session-gated.
