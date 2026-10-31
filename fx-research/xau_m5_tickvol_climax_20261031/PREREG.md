# PREREG — xau_m5_tickvol_climax_20261031 (fleet xau-m5-tickvol-climax-20261031)
Round 6 (pivot from Asia-range LDN break: collides with T06 AsiaBreak FAIL CLEAR).
Data: IC MT5 BID XAUUSD_M5.csv (data/ic-mt5-2026-10-10). Split 60/40 by bar index.
RelVol = tick_volume / SMA(tick_volume,48) (SMA includes current bar). ATR14 = Wilder EWM of TR.
Climax bar t: RelVol>=λ AND (high-low)>=0.8·ATR14[t]; doji (close==open) skipped. dir=sign(close-open).
Arms: MR enters -dir at open[t+1]; CONT enters +dir at open[t+1]. One position at a time.
Grid (16): Arm{MR,CONT} × λ{2,3} × Sess{any, LDN∪NY = UTC 07:00–16:30 on signal bar} × ATR_confirm{any, range>=1.0·ATR14}.
Exit: SL $3.5, TP 1.5R ($5.25), time stop 5 bars (close of 5th), SL first if both hit. Cost $0.28 RT.
Pass (all OOS): PF>=1.25, n>=150, E>0, PF>1 at $0.42, sensitivity PF>1 for SL{3,4}×R{1.25,1.75}, MDD<=25% at 1% risk, IS PF>1. Else ไม่เจอ.
Distinct from R1–R5 (open-imbalance, VWAP band, ATR-regime impulse, NR-K break, composite): trigger is relative tick-volume, not price range/structure. N_TRIALS +16 (2833->2849).
