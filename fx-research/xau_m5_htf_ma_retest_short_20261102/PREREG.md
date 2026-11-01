# R244 PREREG — Below slow HTF MA, retest from below → short
Written 2026-11-02 ~01:30 ICT before any outcome scoring. Data IC BID XAUUSD_M5.csv (time_utc as UTC). HTF bars (H1/H4/D1 UTC) resampled from the same M5; an HTF bar is usable only from the first M5 bar after its close (no lookahead). Cost $0.28/0.01lot RT. 60/40 split by unique UTC day (same cut as R237–R242). Entry at bar OPEN; SL/TP intrabar, both in same bar → SL first; time exit at close of last bar. One position at a time. Soft PASS: PF_OOS≥1.2, n_OOS≥50, E_IS>0, E_OOS>0. Z one-sided norm.isf(0.05/N). Prefer ไม่เจอ. No demo.
MA: SMA50 or EMA50 of closes on completed D1 or H4 (value of last completed bar, held constant until next completes). Condition: prior M5 close < MA.
Touch: M5 bar t with H_t ≥ MA and H_{t−1} < MA. Reject: C_t < (H_t+L_t)/2 or C_t < MA. Short at OPEN t+1. SL = max(H_t, MA)+0.50. TP = m·R. Time stop T12 M5.
Grid 16 = MA{SMA50,EMA50} × TF{D1,H4} × m{1.5,2.0} × Sess{any, LDNNY = touch bar 07:00–19:55 UTC}.
N 6502 → 6518. ≠ R216 PA@SR, ≠ engulf confirm.
