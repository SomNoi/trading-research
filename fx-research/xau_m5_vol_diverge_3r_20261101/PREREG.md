# R215 PREREG — Body×volume DIVERGE → FADE, IC BID XAUUSD M5
Data: IC BID /workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv
med=median(tickvol[t-W..t-1]). UP_FALL: C>O & vol<med → short. DOWN_RISE: C<O & vol>med → long. Gate |C-O|/(H-L)>=β.
Entry next open. SL$2 TP$6 (SL first if both), time exit close T3/T5. Cost $0.28. No overlap.
Grid β{0.0,0.5}×W{20,40}×Hold{3,5}×Sess{any,LDN∪NY 07-20 UTC}=16. Split 60/40 chrono.
Pass: OOS mean>0 AND OOS one-sided Z > norm.ppf(1-0.05/6058), global N=6042+16=6058. Else ไม่เจอ.
