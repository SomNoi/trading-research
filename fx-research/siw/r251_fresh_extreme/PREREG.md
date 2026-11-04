# R251 PREREG — SIW v2 + "fresh extreme" left-window filter (IC BID XAUUSD M5)
Base: R249 unchanged (../siw.py detect(dedupe=1) + outcome_v4; EMA21/55 dir, patterns A/B/C, leg ≤$10/12 bars; entry open L+1; Exit v4 SL $10 / TP $20 / time exit close L+2). Data IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv 2025-05-14→2026-10-09; time_utc label = server−3h (R249 mapping). Split 60/40 by server day, IS ≤2026-03-18, OOS ≥2026-03-19. Cost $0.28/0.01; stress 1.5× ($0.42). No lookahead: filter uses only bars ≤ L (known at L close).
Filter (set = bars L-2..L, order inside set irrelevant):
- SET_K5 / SET_K6: BUY keep if min(low[L-2..L]) <= min(low[L-2-K..L-3]); SELL keep if max(high[L-2..L]) >= max(high[L-2-K..L-3]).
- LONLY_K5 (contrast): BUY low[L] <= min(low[L-5..L-1]); SELL high[L] >= max(high[L-5..L-1]).
Dedupe 3: applied AFTER filter, same side, keep a signal only if ≥3 bars since last kept same-side signal.
Counted cells (12): variant {SET_K5, SET_K6, LONLY_K5} × side {BUY, SELL} × dedupe {1,3}. N 6658 → 6670; Z_BONF = norm.isf(0.05/6670).
Gate: OOS n≥100, IS E>0, OOS E>0, OOS Z ≥ Z_BONF, OOS E at 1.5× cost >0. Comparison vs R249 baseline (same side/dedupe) descriptive. If 0 pass → ไม่เจอ. Watch-only.
