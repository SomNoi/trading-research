# R248 Step 3 PREREG — IC BID backtest of CHECKLIST.md (unchanged)
CHECKLIST.md sha256 49a4c9d37780a5ceb3aa3c8d98b797bafd54bcbea97b1388beaedff715364301 — rules used verbatim (items 1–9, trade/exit rules). SHORT only.
Data IC BID XAUUSD M5 2025-05-14→2026-10-09. Label = server−3h. True UTC = label (US-DST summer) / label+1h (winter). 60/40 by server day (cut 2026-03-19). Cost $0.28/0.01, stress 1.5×.
Counted cells (12): {CORE (1–9), CORE+Asia (true-UTC hour of signal bar ∈[0,6)), CORE+prior-star (bar i−1 upper wick ≥2×body & close in lower third)} × {TP1.5R cap 2h, TP2R cap 2h, T30m w/ SL, T60m w/ SL}. N 6630 → 6642.
EMA = close EMA (adjust=False); ATR14 = rolling mean TR, value at signal bar i. Lower-high: max high of bars i−36..i−1. One position at a time.
Gate: OOS n≥30 else UNTESTABLE; pass needs OOS E>0, IS E>0, OOS Z ≥ Z_BONF(6642), 1.5× cost OOS E>0.
Descriptive baseline (uncounted): random bars meeting items 1,2,4,5 only, 200 draws matched n per split, same exits, no one-position filter (signals also unfiltered for that comparison); report lift & percentile.
