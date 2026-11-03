# R247 PREREG — xau_m5_ma_pb_pa_20261103
Data IC BID XAUUSD M5 (2025-05-14→2026-10-09), label = server−3h (R246 audit); ICT = server+4h summer/+5h winter. 60/40 split by server day (cut 2026-03-19). Cost $0.28/0.01, stress 1.5×.
SHORT signal bar i (completed): EMAf_i<EMAs_i; H_i ≥ min(EMAf,EMAs)_i − $1 (high within $1 of/touching either EMA); C_i < min(EMAf,EMAs)_i; candle = bearish engulfing (C<O, prev C>O, O_i≥C_{i-1}, C_i≤O_{i-1}) OR shooting star (upper wick ≥2×body, close in lower third of range, range>0). LONG mirror (L ≤ max EMA + $1, C > max EMA, bullish engulf or hammer).
Entry open i+1; SL = signal high + $0.30 (long: low − $0.30).
Grid 16 counted: EMA (fast/slow) {9/21,10/20,20/50,5/20} × exit {TP1.5R cap 24 bars, TP2R cap 24, time 6 bars (30m) w/ SL, time 12 bars (60m) w/ SL}. SL-first on same bar. One position at a time (main stats).
Gate: OOS E>0, IS E>0, OOS n≥100, OOS Z(per-trade $) ≥ Z_BONF(N=6630), 1.5× cost OOS E>0.
Descriptive (uncounted), computed per trade WITHOUT the one-position filter for all three sets: (a) same PA candles, no MA context; (b) MA-context bars (trend + touch + close beyond both, any candle), 200 bootstrap draws of size n_signal per split; report lift (signal E − baseline E) and percentile of signal E in the bootstrap distribution. Pattern breakdown engulf vs star.
