# PREREG r223 (IC BID)
DATA=IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv
Cost $0.28; SL$2 TP$6 (3R) + time T; entry next open; one position at a time; 60/40 chrono split by day.
PASS: OOS E>0, PF>=1.2, n>=50, IS E>0. 16 trials. N before=6170.
For UTC hour h: mu,sigma of all M5 closes in hour h over previous D trading days (excl current day). z=(C-mu)/sigma. Signal |z|>=theta, max 1 per hour, re-arm when |z|<theta/2; FADE sign -z; entry next open. Grid D{10,20}xtheta{1.5,2}xSess{any,LDNNY 07-20}xT{5,10}. NOT VWAP. Related R96/R192/R54.
Code: run.py + eng.py (sha below, frozen before run).
