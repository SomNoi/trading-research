# XAU M1 edge — 25 human-behavior hypotheses (task xau-m1-edge-20261030)
All rules: bar t = signal bar (closed). Entry = open[t+1]. Times = bar open time in Asia/Bangkok (ICT).
Session gate: signal bar AND entry bar must lie in ASIA 05:00–12:59, LONDON 14:00–18:59 or NY 19:30–23:29 ICT.
"short/long" = fade direction. rng = high-low. ICT day = calendar date in ICT.
## A Liquidity sweep
1 ASIA_H_SWEEP: AH = max high of ICT-day bars 05:00–12:59. Bar t in LONDON/NY same day: high>AH & close<AH -> SHORT. First per day.
2 ASIA_L_SWEEP: mirror (low<AL & close>AL) -> LONG. First per day.
3 EQH_SWEEP: H30 = max(high[t-30..t-1]); n = count(high[t-30..t-1] >= H30-0.30) >= 2; high[t]>H30 & close[t]<H30 -> SHORT.
4 EQL_SWEEP: mirror -> LONG.
5 PDH_FAKE: PDH = prior ICT-day high. high>PDH & close<PDH -> SHORT. First per day.
6 PDL_FAKE: mirror -> LONG. First per day.
7 FRACTAL_HUNT: fractal high at k: high[k]>high[k-1] & high[k]>high[k+1], known from bar k+1; SH = last known. high[t]>SH & close[t]<SH -> SHORT; mirror with fractal low -> LONG.
## B Volatility exhaustion
8 BIG_BAR_REJ: rng[t-1]>3.5; t-1 bull & close[t]<=mid(t-1) -> SHORT; t-1 bear & close[t]>=mid(t-1) -> LONG.
9 RUN3_REJ: close[t-1]-close[t-4]>5 & close[t]<open[t] -> SHORT; mirror (<-5 & bull bar) -> LONG.
10 PIN: rng>=1.0; upper wick>=0.7*rng & close<=low+rng/3 -> SHORT; lower wick>=0.7*rng & close>=high-rng/3 -> LONG.
11 UPWICK_AFTER_UP: close[t-1]-close[t-6]>3 & upper wick[t]>=0.5*rng[t] & rng[t]>=0.5 -> SHORT.
12 LOWWICK_AFTER_DN: mirror -> LONG.
13 EXPANSION_FADE: rng[t]>2*median(rng[t-20..t-1]) & rng[t]>=1; bull bar -> SHORT, bear -> LONG.
14 DOUBLE_EXP_FADE: bars t-1 and t both expansion (def 13) same color -> fade.
## C Session-open imbalance
15 LDN_FVG: first 3-bar FVG with gap>=0.30 whose bar t in 14:02–14:29: low[t]>high[t-2] -> SHORT; high[t]<low[t-2] -> LONG. First per session.
16 NY_FVG: same, bar t in 19:32–19:59.
17 LDN_DRIVE: d = close(14:14) - open(14:00); d>2 -> SHORT, d<-2 -> LONG. Signal bar 14:14.
18 NY_DRIVE: close(19:44)-open(19:30), |d|>2.
19 ASIA_DRIVE: close(05:14)-open(05:00), |d|>1.5.
20 OPEN_GAP_FILL: at session first bar (05:00/14:00/19:30): g = open - prior bar close; g>0.5 -> SHORT, g<-0.5 -> LONG; signal on that bar (entry 1st bar after).
## D Time & mean reversion
21 EMA_1p5ATR: EMA20(close), ATR14 = SMA14(TR). (close-EMA)>1.5ATR and not true at t-1 -> SHORT; mirror LONG.
22 VWAP_1p5ATR: session VWAP of typical price weighted by volume from session start; same rule, 1.5 ATR.
23 EMA_2p5ATR: as 21 with 2.5.
24 ATR_CHANNEL: close > EMA20+2*ATR14 (first bar) -> SHORT; < EMA-2ATR -> LONG.
25 STREAK8: 8 consecutive close>prev close ending at t (exactly 8th) -> SHORT; mirror LONG.
