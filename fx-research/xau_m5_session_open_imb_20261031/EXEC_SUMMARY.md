# Report — xau-m5-session-open-imb-20261031 (IC MT5 BID XAUUSD M5)
Verdict: **ไม่เจอ (NO EDGE)**. 0/24 pass. PREREG sha256 fd5a18f9… (results/prereg_hashes.txt).
- Split 60/40 at 2026-03-19 03:05 UTC (10:05 ICT). Session events: 685 (both sessions).
- The n_OOS≥150 gate cannot be met: the max OOS n is 78 (NY |I|≥0.8). The frame is structurally under-powered at ~1 trade/session/day with |I|≥0.8.
- Best OOS PF: LDN_CONT_t0.8_F1, PF 1.50 at n=18, but IS PF is 0.73 (noise). Best with n≥50: LDN_CONT_t0.8_F0, PF 1.08 at n=58, IS PF 0.71, sens_min 0.95.
- 21 of 24 OOS PFs are below 1.1. FADE fails sensitivity everywhere (min ≤0.17). IS and OOS ranks do not agree.
- N_TRIALS 2751→2775, Z_BONF 4.132. Full table: summary.csv. Chart: results/best_equity.png.
Distinction: SOX traded range expansion. This round trades signed open-window return / ATR (imbalance) with CONT/FADE arms, an ATR percentile gate and an H1 EMA55 soft filter. It uses no BOS/CHoCH, no motif codes and no shape clusters.
