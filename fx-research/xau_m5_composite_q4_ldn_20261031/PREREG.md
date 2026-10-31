# PREREG — xau_m5_composite_q4_ldn_20261031 (Round 5 composite; fleet xau-m5-composite-q4-ldn-20261031)
Frozen 2026-10-31 before any P&L. Data: data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv (IC MT5 BID). Cost $0.28/oz RT. Split: first 60% bars IS, last 40% OOS (chrono).
Shared context (all arms): decision bar in London ICT 14:00-18:59 (UTC 07:00-11:59); ATR14 (Wilder) causal pct rank >=75 within trailing 5520 bars (~20 trading days).
Exit: entry next bar open; SL $3.5, TP $5.25 (1.5R), time stop close of 5th bar after entry; SL wins same-bar tie; one position at a time.
Triggers (fade/MR only):
1. VWAP_MR: session VWAP = cumsum(typical*tick_volume)/cumsum(tick_volume) reset at 07:00 UTC; d=(close-VWAP)/ATR14; |d|>=beta -> trade toward VWAP. beta in {1.0,1.5}.
2. NR7_FAILFADE: bar t range = min of last 7; first close beyond [low_t,high_t] in t+1..t+3 = break at b; if b+1 or b+2 closes back inside -> enter opposite the break. Fixed.
3. EXH_FADE: bars t-2,t-1,t each close beyond prior close in same direction, |close_t-open_{t-2}|>=kappa*ATR14; within t+1..t+3 first close retracing >=50% of the impulse (from close_t toward open_{t-2}) -> enter in reclaim direction. kappa in {0.8,1.2}.
TOD levels: full_LDN (07:00-11:59 UTC) or early60 (07:00-07:59 UTC), applied to the signal (entry-decision) bar.
Grid: VWAP 2x2 + NR7 1x2 + EXH 2x2 = 10 trials. No expansion after P&L.
Pass (all OOS): PF>=1.25, n>=150, E>0, PF>1 at $0.42, sensitivity PF>1 for SL{3,4} x R{1.25,1.75}, MDD<=25% at 1% risk, IS PF>1. Else ไม่เจอ. N_TRIALS +10 (2823->2833).
