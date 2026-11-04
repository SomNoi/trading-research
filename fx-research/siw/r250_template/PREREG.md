# R250 PREREG — SIW v2 "top-3 of Nov 3" template match (Exit v4) — written 2026-11-04 ICT before any IC outcome was viewed
Watch-only research. No trading.

## Templates (hindsight-picked; outcomes of Nov 3 ARE known — that is the caveat)
Source for Nov 3: Dukascopy BID M5 (duka_xau_m5_bid_refreshed.csv) = SUBSTITUTE source (IC data ends label 2026-10-09 17:55, does not cover Nov 3).
68 SIW v2 signals (detect() default, dedupe=1) on ICT day 2026-11-03; Exit v4 (SL10/TP20/close L+2, $0.28). Top 3 by $:
- T1 SELL A_PIN  conf 13:35 ICT  +8.41
- T2 BUY  B_ENGULF conf 00:50 ICT +5.90
- T3 SELL B_ENGULF conf 15:30 ICT +5.74
Fingerprints in templates.csv. Features (at L, ATR14 Wilder): body/uw/lw fraction of range, colour, colours of L-1,L-2, rng/ATR,
(EMA21-EMA55)/ATR, 3-bar slope EMA21/ATR & EMA55/ATR, (close-EMA21)/ATR, leg/ATR, ICT hour. Directional features are sign-flipped for BUY (dir-adjusted: sg=-1 S,+1 B... we store sg*value).
For mirror shape, "rejection wick" = uw for SELL, lw for BUY; "other wick" = opposite.

## Matching tolerances (fixed now)
TIGHT: same side, same kind (A_PIN / B_ENGULF), same L colour, same L-1 and L-2 colours; |body|±0.15, rej wick ±0.20, other wick ±0.20;
rng/ATR ±0.40; dir-adj gap ±0.75; dir-adj s21 ±0.25; dir-adj s55 ±0.20; dir-adj d21 ±0.50; leg/ATR ±0.50; ICT hour ±2 (circular).
LOOSE: same side, same kind; body ±0.20; ICT hour ±2; dir-adj gap ±1.0; dir-adj d21 ±0.75; leg/ATR ±0.75.
A bar matches the set if it matches ANY of T1..T3 (union). Candidate bars = SIW v2 signals in IC history (detect default).

## Data / rules
IC BID XAUUSD M5 data/ic-mt5-2026-10-10 (≈17 mo). Timestamps exactly as R249 run.py (true UTC = label (+1h winter); ICT = UTC+7).
Exit v4 entry open L+1, SL before TP, close at close L+2. Cost $0.28/0.01 lot; 1.5x check ($0.42). IS/OOS 60/40 by server day, cut 2026-03-18/19 (same as R249).
Caps: 1, 2, 3 trades/day = first matches of the (server) day.
Baselines: R249 all-SIW (results_main.csv); RANDOM: 500 draws, per matched trade a random IC bar with same side, same ICT hour, same EMA21/55 sign, same split — mean E and pct of draws ≥ observed.

## Counted cells (added to N): 2 tiers × 3 caps (union) = 6, + 2 tiers × 3 templates (cap1) = 6 → 12. Bonferroni Z at alpha .05 / new N.
## Gate (PASS only if all): OOS n≥100, IS E>0, OOS E>0, OOS E at 1.5x cost >0, OOS Z ≥ Bonferroni Z. Else verdict ไม่เจอ (no edge).
