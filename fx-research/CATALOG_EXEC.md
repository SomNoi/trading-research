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
Still never studied as a dedicated system: **morning star / evening star**. (Engulfing was studied earlier: NO EDGE.)
