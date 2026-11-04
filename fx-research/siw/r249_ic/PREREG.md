# R249 PREREG — SIW v2 entry + Exit v4 on IC BID XAUUSD M5
Code: ../siw.py unchanged (detect(), outcome_v4(), defaults: modes abc, pin wick≥0.50/body≤0.35, star body≤0.40 tol $0.30, engulf tol $0.10, leg lookback 12, max_ext $10, EMA21/55 on close). Spec ../SPEC.md (Exit v4: SL $10, TP $20 cap, exit close of L+2; SL before TP; gap fills at open).
Data: IC BID `data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv` 2025-05-14→2026-10-09 = longest IC XAU file on box (data/from_parquet_m1 2019+ is Dukascopy mid, not IC → not used). Timestamps: label = server−3h; server = label+3h; true UTC = label (US-DST summer) / label+1h (winter) (verified: label+1h aligns with Dukascopy UTC in Dec–Feb, median |Δclose| $0.08). ICT = true UTC+7. siw.load()'s Nov-2026 srv rule NOT used.
Split 60/40 by server day (IS < 2026-03-19). Cost $0.28/0.01 per trade; stress 1.5× ($0.42). All signals traded independently (no position overlap filter), as in the Dukascopy study.
Counted cells (4): side {SELL, BUY} × dedupe {1 (off), 3 (same-side, 3 bars)}. N 6642 → 6646.
Descriptive (uncounted): per pattern (A_PIN, A_STAR, B_ENGULF, C_*), by session (true-UTC Asia 00–07, London 07–12, NY 12–21, Late 21–24) and hour, per-month E/total.
Gate: OOS n≥100, OOS E>0, IS E>0, OOS Z ≥ Z_BONF(6646), 1.5× cost OOS E>0.
Watch-only; no trading.
