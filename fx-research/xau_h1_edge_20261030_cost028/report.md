# XAU H1 edge hunt (cost $0.28) — VERDICT: NO EDGE (ไม่เจอ)
- Data: Dukascopy XAUUSD M1 → 1h, BKK, 2022-01-01 → 2026-10-10 03:00 BKK (28,245 bars). htf H1 parquet not used (ends 2025-10-09).
- PREREG locked + sha256 before run. SL $3.5 / TP 1.5R / time stop 25 H1, kept for parity.
- **0/25 pass kill bar.** 0 base survivors → no grid.
- Best OOS PF: 04_EQL_SWEEP PF 1.17, n=85 (<150), WR 47.1%, net +$28.7/oz, maxDD $37.8 (>net), IS PF 0.70, sens min 0.16 → fails n, PF, WR, DD, sens.
- Next: 02_ASIA_L_SWEEP 0.70, 14_DOUBLE_EXP_FADE 0.70, 03_EQH_SWEEP 0.68. Most OOS PF 0.40–0.65.
- OOS trades all hyps: 9,722; ~70% hit SL, ~30% TP. $3.5 SL is noise on H1 bars (median range is many $), so WR ~30% < 40% breakeven at 1.5R. Wider SL not tested (not preregistered).
- vs M1 (best PF 1.02) / M5 (best PF 1.09): H1 worse under same SL; no TF shows edge.
- Trials +125 → N_TRIALS 1455, Z_BONF 3.981.
- Charts: charts/oos_equity_top6.png, charts/oos_equity_all25.png. NOT a live signal.
