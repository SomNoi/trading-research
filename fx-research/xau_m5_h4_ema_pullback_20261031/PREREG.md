# PREREG xau_m5_h4_ema_pullback_20261031 (fleet xau-m5-h4-ema-pullback-20261031) — Round 8
Written 2026-10-31 (ICT) before any backtest.
Data: data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv (IC MT5 BID). Cost $0.28/oz RT. Split: first 60% of M5 bars = IS, last 40% = OOS.
Distinct from combo_mtf (H1 EMA55 bias + M5 pin/engulf): this round uses an H4 EMA50 bias, and the entry is an M5 EMA20 touch-and-reclaim with no candle pattern. Distinct from XAU_EMA55_PB (single-TF M5 EMA55 pullback) and 4_kaze (EMA9/21 cross): it uses an HTF bias filter, EMA20 and a touch-depth δ.
H4: resample M5 to 4h bars (label=left, closed=left, UTC). EMA50 (adjust=False) on H4 close. An H4 bar starting at T becomes usable only at M5 bars with time_utc >= T+4h (completed only, merge_asof backward). Bias +1 if H4 close > EMA50, -1 if below, 0 if equal or warm-up.
Signal at M5 bar t, with E=EMA20(close, adjust=False) and ATR14 Wilder: LONG if bias=+1 and low_t <= E_t and close_t > E_t. SHORT mirrors this (high_t >= E_t and close_t < E_t).
δ: any, or 0.5, which requires the touch depth |E_t - low_t| (long) or |high_t - E_t| (short) to be <= 0.5·ATR14_t.
Slope: off, or on, which requires sign(E_t - E_{t-2}) = bias.
Entry: open[t+1]. SL $3.5, TP $5.25 (1.5R), time stop at the close of the H-th bar after entry, H in {5,12}. SL wins a same-bar tie. One position at a time.
Session: any, or LDN∪NY = decision bar UTC 07:00-16:29.
Grid 16 = δ{any,0.5} × H{5,12} × Sess{any,LDNNY} × Slope{off,on}.
Pass (all OOS): PF>=1.25, n>=150, E>0, PF>1 at $0.42, sensitivity PF>1 for SL{3,4}×R{1.25,1.75}, MDD<=25% at 1% risk, IS PF>1. Otherwise the verdict is ไม่เจอ. N_TRIALS +16 (2865->2881).
