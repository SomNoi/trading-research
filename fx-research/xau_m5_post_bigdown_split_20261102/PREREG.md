# R245 PREREG — Post big down-day session split
Written 2026-11-02 ~01:30 ICT before any outcome scoring. Data IC BID XAUUSD_M5.csv (time_utc as UTC). HTF bars (H1/H4/D1 UTC) resampled from the same M5; an HTF bar is usable only from the first M5 bar after its close (no lookahead). Cost $0.28/0.01lot RT. 60/40 split by unique UTC day (same cut as R237–R242). Entry at bar OPEN; SL/TP intrabar, both in same bar → SL first; time exit at close of last bar. One position at a time. Soft PASS: PF_OOS≥1.2, n_OOS≥50, E_IS>0, E_OOS>0. Z one-sided norm.isf(0.05/N). Prefer ไม่เจอ. No demo.
D1 (UTC) log-return r=ln(C_d/C_{d−1}). Big down day: r<0 and |r| ≥ p90 of the trailing 60 completed D1 |r| (days d−60..d−1). Trade only the next UTC trading day.
Arm A_fade_ldn: LONG; window 07:00–09:55 UTC; λ=0 → enter at 07:00 bar OPEN; λ=0.3 → first M5 bar in window with |C−O| ≥ 0.3·ATR14 (any colour), enter next OPEN (if within window). 
Arm B_cont_ldnny: SHORT; window 12:00–15:55 UTC; same λ rule (λ=0 → 12:00 OPEN).
SL fixed $4 or $8; TP = m·SL; exit at window end (close of last window bar) if neither hit.
Grid 16 = Arm{A,B} × λ{0,0.3} × SL{4,8} × m{1.5,2.0}.
N 6518 → 6534. ≠ news-clock, ≠ opening-drive, ≠ quiet-Asia.
