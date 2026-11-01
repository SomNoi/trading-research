# R242 PREREG — Kaufman ER compression → burst
Written 2026-11-01 ~22:45 ICT before any outcome scoring. Data IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv (time_utc treated as UTC); London clock via zoneinfo Europe/London (DST-aware; bar start London = UTC→London). Cost $0.28/0.01lot RT. Split 60/40 by unique UTC day (same cut as R237–R239). Entry at bar OPEN; SL/TP intrabar, both in same bar → SL first; else time exit at stated bar close. R=PnL/SL-distance. Soft PASS: PF_OOS≥1.2, n_OOS≥50, E_IS>0, E_OOS>0. Z one-sided vs Z_BONF(N). Prefer ไม่เจอ. No demo.
Session: signal bar start 07:00–19:55 UTC. ER10_t = |C_t−C_{t−10}| / Σ_{j=t−9..t}|C_j−C_{j−1}|. ATR50 = SMA50 TR.
Setup at trigger bar t, evaluated on prior 8 closed bars t−8..t−1: count(ER10<0.2) ≥ nq; box = [min L, max H] over t−8..t−1; height < 1.2·ATR50_{t−1} and height ≥ minbox.
Trigger: ER10_t ≥ 0.6 and C_t > boxH (up) or C_t < boxL (down). Entry OPEN t+1. CONT: dir=breakout, SL = opposite box side; FADE: dir=−breakout, SL distance = same as CONT risk |O_{t+1}−opposite side| placed beyond entry. Skip if risk ≤0. TP = m·R, time stop T12 (close of 12th bar). One position at a time.
Grid 16 = nq{6,7} × minbox{2.5,3.5} × TP m{2,1} × Arm{CONT,FADE}. ER_low 0.2, ATR_box 1.2, session fixed.
N 6470 → 6486. Distinct from R66/R? Kaufman ER regime alone, R239 VR, R237 tickvol, shapes (box+ER-burst trigger).
