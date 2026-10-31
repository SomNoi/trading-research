# Round 10 — IS-only feature stump / ridge logistic → threshold entry (XAU M5, IC MT5 BID, $0.28)
Verdict: **FAIL — ไม่เจอ** (0/9 pass). PREREG.md locked (sha256 in PREREG.sha256) before fit. OOS start 2026-03-19 10:05 ICT.
| cell | IS n/PF | OOS n/PF | note |
|---|---|---|---|
| ridge0.1 τ0.55 | 1857 / 0.77 | 1301 / 0.71 (E −$0.70, MDD 93%) | best OOS by PF with n≥150 |
| ridge1.0 τ0.55 | 1859 / 0.77 | 1302 / 0.71 | ≈ identical (C irrelevant, 7 features) |
| ridge τ0.60 | 4 / 0 | 7 / 0.22 | almost no signals |
| ridge τ0.65, stump all τ | 0 | 0 | p never leaves [0.35,0.65] / [0.40,0.60] |
Model quality: ridge IS AUC 0.522 → OOS 0.508; stump picked atr_pct (IS AUC 0.517 → OOS 0.503). Largest coef atr_pct (+, i.e. high-vol → long bias = gold uptrend drift), r12 (−, mild MR). Signal ~ noise; cannot pay SL3.5/TP1.5R/T5 + $0.28.
Leakage controls: z-score mu/sd from IS rows only (index < cut−5); labels t+5 so last 5 IS bars dropped; fit on IS only; OOS scored once with frozen params/scaler; features use only bars ≤ t; entry at open t+1; atr_pct trailing window excludes current from rank base.
vs archive LightGBM (xau_research, NO EDGE): that was a large nonlinear search over many features/hyperparams (high multiple testing); this is 7 locked features, linear/1-D model, 9 cells. Both find ~0.5 AUC → consistent: no exploitable M5 direction signal at 5-bar horizon.
Files: PREREG.md, main.py, results/summary.csv, results/model_info.json.
