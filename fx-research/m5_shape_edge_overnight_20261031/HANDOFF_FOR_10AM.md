# HANDOFF 10:00 ICT — XAUUSD M5 bar-shape edge (both runs) — **ไม่เจอ**
Data: IC Markets MT5 BID XAUUSD M5, 99,964 bars, 2025-05-14→2026-10-09 UTC. No live trading.
| Run | Split | Trials | Pass | Best OOS PF (n>150 / overall) | Path |
|---|---|---|---|---|---|
| A | 70/30 | 360 | 0 | 1.47, but n=147, WR 44.9%, IS PF 0.86 | exec_run_A_7030/ |
| B | 60/40, prereg-locked | 440 | 0 | 1.19 (w4_t0.85_c39 MR, n=163, WR 47.2%, sens min 0.91) | fx_run_B_6040/ |
- Run B: shape clusters and bar sequences are not stable from IS to OOS. Sequence lift sign agrees only 55% of the time, with correlation 0.08. Median OOS PF is about 0.85.
- multiple_testing.json: N_TRIALS 1830 → 2630 (+440 B, +360 A), Z_BONF 4.12. Run A should NOT bump it again.
- GitHub: skipped, because gh is not authenticated. Notion: skipped.
Thai line: "ทดสอบรูปทรงแท่งเทียน XAUUSD M5 2 รอบ (800 trials) — ผ่าน 0 สรุป ไม่เจอ edge; PF OOS ดีสุด ~1.19 ยังไม่ผ่านเกณฑ์"
