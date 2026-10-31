# PREREG — m5-motif5-novel-20261031 (fleet task m5-motif5-novel-20261031)
Data: IC Markets MT5 BID XAUUSD M5, /workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv. Times UTC -> Asia/Bangkok (ICT).
Sessions by ENTRY bar open time (ICT): ASIA 05:00–13:00, LDN 14:00–19:00, NY 19:30–23:30.
## Alphabet (per closed bar, R=high-low; R==0 -> D)
body=|c-o|/R, up=(h-max(o,c))/R, lo=(min(o,c)-l)/R. Order of rules:
1. body<=0.15 -> D
2. up>=0.60 -> W+ (upper pin) ; lo>=0.60 -> W- (lower pin)
3. body>=0.50 -> B+ if c>o else B-
4. else S+ if c>o else S-  (7 symbols)
Motif = codes of bars t-4..t.
## Split: first 60% bars IS, last 40% OOS. Mining/selection IS only; OOS evaluated once.
## Mining (IS, HINDSIGHT): F=close[t+5]-close[t]. Keep motif if fires/day (IS trading days) in [0.5,2.0],
|mean(sign F)|>=0.15 and sign(mean F)==sign(mean sign F). Rank by |mean F|, K=30 logged, top 15 traded.
## Trade: direction = sign(IS mean F). Primary Entry B: when bars t-4,t-3 (motif bars 1,2) match motif prefix, enter at next open (bar3 open).
Exit at open of bar after motif bar5 (i.e. bar t+1 open; max hold 3 bars) or SL $3.5 / TP $5.25 (1.5R) intrabar (SL first if both). Cost $0.28 RT. 1 position at a time per config. 0.01 lot = 1 oz => $ = price units.
Note (locked, honest): entry fires on 2-bar prefix match; full motif need not complete.
## Context grid: session {any,LDN,NY} x ATR14 {any,Q4 (>= IS 75th pct)} = 6 per motif -> 90 trials; + Entry A (k=1) variant at any/any for 15 motifs = 15. N=105.
## Pass (OOS): PF>1.25, WR>48% (R:R 1.5), MDD<25% of net profit, n>150, sensitivity (entry k-1/k+1 and SL 3.0/4.0, TP=1.5×SL) all PF>1.15. Else ไม่เจอ.
N_TRIALS prior 2630 -> 2735. Z_BONF=norm.ppf(1-0.05/2735).
