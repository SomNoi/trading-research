# PREREG r222 (IC BID)
DATA=IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv
Cost $0.28; SL$2 TP$6 (3R) + time T; entry next open; one position at a time; 60/40 chrono split by day.
PASS: OOS E>0, PF>=1.2, n>=50, IS E>0. 16 trials. N before=6154.
Bias=last completed H1 close vs EMA55_H1 (available only after H1 close). M5 pivots L confirmed at k+L; reset on bias flip; need HH+HL (long) / LH+LL (short) post-flip. Signal: first later bar with low<=lastHL+phi*ATR14(t-1) (short: high>=lastLH-phi*ATR); entry next open CONT; re-arm on new pivot. Grid L{2,3}xphi{.25,.5}xSess{any,LDNNY 07-20}xT{6,12}. Related R101/R8/R198.
Code: run.py + eng.py (sha below, frozen before run).
