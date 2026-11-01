# R230 PREREG — XAU M5 minute-of-hour bucket IS-sign CONT + tickvol confirm, LDN∪NY (2026-11-01)
Locked before any result. N_before=6282 (+16 → 6298), Z_bonf=norm.ppf(1−0.05/6298) one-sided.
## Rule
- Bucket bar b = M5 bar starting at minute m∈bucket set, hour 07–19 UTC (LDN∪NY 07–20). Bucket sets: A={:00,:30}, B={:15,:45}.
- IS μ_m = mean(close−open) of bucket bars with minute m on IS days only (LDN∪NY). Direction for minute m = sign(IS μ_m) (CONT IS-sign), locked from IS, applied unchanged to OOS.
- Signal at close of bar i = bar immediately preceding bucket bar (contiguous 5-min). Confirm: tickvol[i] ≥ median(tickvol[i−20..i−1]). Entry = open of bucket bar (= next open).
- SL $SL, TP=TPmult·SL, time exit at close of bar entry+T−1 (T bars held).
- Grid 16: bucket{A,B} × SL{$4,$8} × TPmult{1.5,2.0} × T{6,12}. Sess fixed LDN∪NY. Arm CONT only.
- Novelty: ≠ R127 (IS-locked MoH residual z FADE/CONT on any bar) — here only quarter-hour buckets, raw IS mean sign, tickvol gate. ≠ session-drive (R55/58/76/165/217).
Data XAU IC Markets MT5 BID (2025-05-14→2026-10-09). Cost $0.28/0.01 lot per trade; R=(pnl−0.28)/SL; engine `_r227_229/eng.py` sim (entry next open, SL checked before TP intrabar, one position at a time). Split 60/40 chronological by calendar day. PASS(soft): OOS E>0, PF≥1.2, n≥50, IS E>0. EDGE requires PASS and z_oos ≥ Z_bonf (one-sided), and no IS/OOS side-flip; default verdict ไม่เจอ. No demo. R94/R227 untouched (watch-only).
