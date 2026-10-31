# report — m5-motif5-novel-20261031 (Source: IC Markets MT5 BID XAUUSD M5, 99,964 bars, $0.28 RT, times in ICT)
**Result: ไม่เจอ (no edge). 0/105 configurations pass.**
- Primary PREREG (sha 9e97e1a4…): no motif occurs ≥0.5 times/day. The highest is 0.22/day, with 7^5 codes over 264 IS days. That leaves 0 trials, so the result is ไม่เจอ by construction.
- AMEND1 (frequency filter lowered to [0.10, 2.0]; written before seeing any F or P&L): this run is EXPLORATORY-AMENDED. The top 15 HINDSIGHT motifs were tested with entry k=2 × session {any, LDN, NY} × ATR {any, Q4}, plus 15 runs with entry k=1. Total 105 trials.
- Best OOS PF is 0.98: prefix B+|B- long, LDN session, n=462, WR 45.0%, net −$14.4/oz, sensitivity min PF 0.55. The IS PF for that same row was 0.68.
- Median OOS PF is 0.79. Correlation between IS PF and OOS PF is −0.04.
- Why it fails: the mined forward move F (close[t+5]−close[t]) happens after the motif ends. The tradeable window (bar 3 → bar t+1) is a different window, so even the IS trades have PF<1. Prefix entries also collapse many motifs onto the same 1–2 bar prefix, which is why duplicate rows appear in summary.csv.
- N_TRIALS 2630→2735, Z_BONF=4.128.
- Charts: charts/near_miss_*.png. Full table: summary.csv. Mined motifs: motif_list_IS.csv (tagged HINDSIGHT).
