# PREREG r221 (IC BID)
DATA=IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv
Cost $0.28; SL$2 TP$6 (3R) + time T; entry next open; one position at a time; 60/40 chrono split by day.
PASS: OOS E>0, PF>=1.2, n>=50, IS E>0. 16 trials. N before=6138.
Windows UTC: NFP-proxy 1st Fri 12:30-13:30; CPI-proxy Wed wom2/3 12:30-13:30; FOMC-proxy Wed dom>=15 18:00-19:30; OVERLAP_Q4 12-16 & ATR14(t-1)>=IS p80. Signal first bar |C-O|>=lam*ATR14(t-1), 1/window-day. Grid Window{NFP_CPI_FOMC,OVERLAP_Q4}xArm{CONT,FADE}xlam{0.5,1}xT{6,12}. Related R76/R165/Track11 (not redo).
Code: run.py + eng.py (sha below, frozen before run).
