# PREREG xau_m5_atr_regime_lib_20261031 (fleet xau-m5-atr-regime-lib-20261031)
Written 2026-10-31 (ICT) before any backtest.
Data: data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv (IC MT5 BID). Cost $0.28/oz RT.
Split: first 60% of bars by time = IS, last 40% = OOS. Nothing is selected on OOS.
Regime: ATR14 (Wilder, M5). Causal percentile rank of the current ATR within the trailing 5520 bars (~20 trading days), excluding the current bar. Q1: pct<=25. Q4: pct>=75. Mid: no trade.
Patterns (signal on close of bar t, entry at open of t+1):
- IMP_UP: close[t]>close[t-1]>close[t-2]>close[t-3] and close[t]-open[t-2] >= k*ATR14[t]. IMP_DN mirrors this.
- EXH: bars t-3..t-1 form an IMP and bar t closes opposite, reclaiming >=50% of the impulse move (close[t-1]-open[t-3]).
Arms: CONT = trade in the impulse direction after IMP. FADE = trade against the impulse after EXH.
Grid (16): Regime{Q1,Q4} x Arm{CONT,FADE} x k{0.8,1.2} x Session{any, LDN∪NY = 07:00-20:59 UTC by signal bar}.
Exit: SL $3.5, TP $5.25 (1.5R), time stop at the close of the 5th bar held. If SL and TP fall in the same bar, count SL. One position at a time. No daily cap.
Pass (all required, OOS): PF>=1.25, n>=150, E>0 after cost, PF>1 at 1.5x cost ($0.42), sensitivity PF>1 for every SL{3.0,4.0} x TP R{1.25,1.75}, MDD<=25% at 1% fixed-fractional risk, and IS PF>1.
Selection: "best" is reported by OOS PF only for description. A pass needs every criterion. N_TRIALS +16.
Fail verdict: ไม่เจอ.
