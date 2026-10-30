# FX-Research catalog — executive summary (2026-10-29 ICT)
**No system passed the full pass bar.** No finalist exists, so the 2025-10-10 UTC holdout was never used for selection.
Totals: 925 trials logged (Bonferroni z ≈ 3.87). Data is Dukascopy mid, which differs from IC MT5. Costs follow Kai's IC model. Full map: INDEX.md.

## Families and verdicts
- Track 1 (Donchian, Asian mean reversion, session breakout, Kaze, TS momentum, seasonality) across 5 symbols: FAIL, 0 passes (best OOS PF ≈ 1.28, no robust edge).
- Track 2 (Tokyo/Frankfurt ORB, fix flow, cross-pair residual, news shock): FAIL, 0 of 24 pass.
- Track 3 Kai techniques (T01 SMC sweep, T06 Asia break, T08 multi-TF, T09 VSA, T15 Preda-v5, plus loose variants): CLEAR FAIL, PF 0.57–0.86.
- Track A (6 higher-TF systems pooled across 13 symbols): CLEAR FAIL, PF 0.64–0.96.
- Track B (M5 FX): FAIL. Near-miss: USDJPY B2 range breakout (PF 1.28, n 996), which failed on its 31% drawdown and a losing 2023.
- USDJPY REB + HTF filters: FAIL. Near-miss: V3 PF 1.56, but only 207 trades (300 needed).
- REB-H4: FAIL on other pairs (PF 0.90), on gold (PF 1.03, t 0.14) and as a binary option. The demo EA handoff is a forward test only, not a pass.
- NYBO M15 (NY breakout): CLEAR FAIL, pooled PF 0.90.
- Gold (XAU) studies (EMA55 pullback, EMA55 higher TF, swing breakout, session-open scalp, ADR, fuzzy, close-break TP5/SL2): all NO EDGE, PF 0.69–1.01 after costs.
- Engulfing (engulf_watch, MAE/MFE brackets): NO EDGE. Before costs it is about zero; the $0.28 cost makes it negative.
- SMC structure (M5, H1/H4): NO EDGE. The SMC folder holds definitions and vocabulary only, not a strategy.
- CHoCH (archived study): about breakeven before commission, and the first 70% of the data was negative. FAIL.
- Mae-pla book patterns: FAIL, OOS PF 0.87–0.97.
- ACME: the full system is TOO-VAGUE to test, and the 8-rule entry-only version FAILs (n 12, PF 0.27).
- Hindsight mine, bias demo, daily-range oracle: LOOKAHEAD. These are teaching aids and upper bounds, NOT strategies.

## Classic candles Track B (2026-10-29)
Pin bar (V0/V1), inside bar, doji on XAUUSD M5: **FAIL / NO EDGE** (hold PF 0.77–0.86 after $0.28; hit≈50%; MFE≈MAE). See classic_candles/REPORT.md. Trials 925→937.
Morning/evening star (MES_V0, MES_V1 EMA5 trend filter) XAUUSD M5: **FAIL / NO EDGE** (hold PF 0.76–0.80 after $0.28; hit≈49%; MFE≈MAE). See classic_candles/MES_REPORT.md. Trials 937→943.
No classic candle pattern remains unstudied (engulfing earlier: NO EDGE).
## Combo MTF (2026-10-29)
H1 EMA55 bias + M5 pin/engulf ± RSI14 XAUUSD: **FAIL / NO EDGE** (hold PF 0.72–0.85 after $0.28). Does stacking help? **No** — same losing PF band as stand-alone candles. See combo_mtf/REPORT.md. Trials 943→955.
- 2026-10-30 xau_m1_edge_20261030 (25 human-behavior M1 hyps, $0.65 cost): **NO EDGE**, 0/25 pass, best OOS PF 0.83 (PDL fake-break); +125 trials.
- 2026-10-30 xau_m1_edge_20261030_cost028 (same 25 hyps, $0.28 cost): **NO EDGE**, 0/25 pass, best OOS PF 1.018 (PDL fake, n=253, +$8.2/oz, sens min 0.83); +125 trials (1080→1205).
- 2026-10-30 xau_m5_edge_20261030_cost028 (25 hyps on M5, $0.28): **NO EDGE**, 0/25 pass, best OOS PF 1.09 (LDN FVG, n=350, +$62.5/oz, WR 46.6%, sens min 0.08, IS PF 0.85); +125 trials (1205→1330).
- 2026-10-30 xau_m15_edge_20261030_cost028 (25 hyps on M15, $0.28): **NO EDGE**, 0/25 pass, best OOS PF 1.13 (Asia drive, n=171, +$44.9/oz, WR 46.2%, maxDD 133% of net, sens min 0.02, IS PF 1.13); +125 trials; combined M15+H1 → N_TRIALS 1580.
- 2026-10-30 xau_h1_edge_20261030_cost028 (25 hyps on H1, $0.28): **NO EDGE**, 0/25 pass, best OOS PF 1.17 (EQL sweep, n=85, +$28.7/oz, WR 47.1%, sens min 0.16, IS PF 0.70); ~70% SL hits; +125 trials; N_TRIALS now 1580 after M15+H1.
- 2026-10-30 ic_mt5_xau_edge_20261030 (25 hyps on **IC MT5 BID** M5 then M1, $0.28, 60/40 split): **NO EDGE / ไม่เจอ**, 0/50 pass. M5 best OOS PF with n>150 is 0.86 (EQH sweep, n=379). M1 best is 0.97 (VWAP dev, n=706). +250 trials → N_TRIALS 1830, Z_BONF 4.035. Demo deals 52946518: at constant 0.01 lot PF 0.92 (Daily Confirmation) and 0.68 (kai probe). drive-xauusd best_config is INVALID (1e242 return).
| 2026-10-31 | m5_shape_edge_overnight_20261031 | XAUUSD M5 3–5 bar shape clusters+codes, 370 patterns/360 BT | **ไม่เจอ** — 0 pass, median OOS PF 0.76 | m5_shape_edge_overnight_20261031/exec_run_A_7030/EXEC_SUMMARY.md (run A; a parallel 60/40 prereg run may exist in the root of the same folder) |
- 2026-10-31 m5_shape_edge_overnight_20261031 (XAU M5 bar shapes; run A 70/30 and run B 60/40 prereg): **ไม่เจอ**. 0/800 pass. B best OOS PF 1.19 (n=163, WR 47.2%, sens min 0.91). Seq IS→OOS lift corr 0.08. N_TRIALS 1830→2630, Z_BONF 4.12.
