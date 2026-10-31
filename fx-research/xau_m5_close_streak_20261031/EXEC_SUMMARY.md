# R9 xau_m5_close_streak_20261031 — ไม่เจอ
XAUUSD M5 IC BID, $0.28 RT, 60/40 (OOS from 2026-03-19 10:05 ICT), SL3.5 TP1.5R T5. Grid 12 (PREREG.md, sha in PREREG.sha256).
- 0/12 pass. 11/12 cells have OOS PF<1; IS PF<1 in 11/12.
- Best OOS PF 1.52 = k8 CONT ATR Q4, n=35 (needs 150), IS PF 0.85 → noise.
- Best with n≥150: k5 FADE any, PF 0.86, n=1116, E −$0.29/trade.
- CONT and FADE lose about equally, so the streak has no directional information after costs.
- Versus R3: R3 needed |move|≥κ·ATR over 3 bars. R9 counts consecutive higher (or lower) closes only, with no size condition. Neither works.
Full table: results/summary.csv; equity: results/best_equity.png.
