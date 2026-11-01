# R220 PREREG — M5 multi-bin shape funnel + session gate — DATA: IC BID
Data: IC BID XAUUSD_M5.csv (2025-05→2026-10). IS = first 60% bars by time, OOS = rest. OOS run ONCE.
Bar features: signed body/range, upper wick/range, lower wick/range, range/ATR14 (ATR on prior-inclusive TR, completed bars). Window W bars ending at t (bar1 = bar t). Vector 4W, z-scored with IS mean/std.
Clustering: KMeans K=8 fixed, seed 0, n_init 10, fit on IS windows only.
Funnel (IS only): keep bin if P(sign r_{t+1}=sign r_t) ≥ p_min AND P(sign(C_{t+H}-C_t)=sign r_t) > 0.5 (continuation through H).
Trade: at close of bar t if bin kept & gate passes & body≠0: enter CONT dir sign(C_t-O_t) at open t+1. SL $2, TP $6, else exit at close of bar t+H. Same-bar SL&TP → SL. Cost $0.28/trade. One position at a time.
Gate: Sess{any, LDN∪NY 07:00–20:00 UTC on signal bar}.
Grid (16): W{3,5} × p_min{0.55,0.60} × H{3,5} × Sess{any,LDNNY}. K=8 fixed.
PASS: OOS E>0 after cost, PF≥1.2, n≥50, IS E>0, OOS t not ≪2. Otherwise ไม่เจอ. N_TRIALS 6122→6138.
