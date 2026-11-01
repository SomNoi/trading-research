# R214 PREREG — Large body + tickvol > median → CONT, IC BID XAUUSD M5
Data: IC BID /workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv
body_frac=|C-O|/(H-L+1e-9). Signal at t: body_frac>=β AND tickvol_t > median(tickvol[t-W..t-1]). Dir=sign(C-O) (CONT only). Entry next open.
SL$2 TP$6 (SL first if both in bar), time exit close of bar T3/T5. Cost $0.28/trade. No overlap: new signal ignored while a trade is open.
Grid β{0.50,0.70}×W{20,40}×Hold{3,5}×Sess{any,LDN∪NY 07-20 UTC hours incl}=16. Split 60/40 chrono by signal bar.
Pass: OOS mean>0 AND OOS one-sided Z > Z_BONF=norm.ppf(1-0.05/6042) global N=6026+16=6042. Else ไม่เจอ.
