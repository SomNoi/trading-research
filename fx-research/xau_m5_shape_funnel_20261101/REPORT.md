# R220 REPORT — M5 shape funnel (KMeans K=8) + session gate, 3R — DATA: IC BID
Prereg sha256 in PREREG.sha256 (locked 444 before run). Grid 16 cells (W{3,5}×p{.55,.60}×H{3,5}×Sess{any,LDNNY}).
Result: IS funnel kept **0/8 bins in every cell** → 0 trades IS and OOS. OOS evaluated once (empty).
IS bin P(sign r_{t+1}=sign r_t): W3 max 0.502, W5 max 0.508 (all 0.47–0.51) — M5 shape clusters show no continuation, slight mean-reversion tilt. See diag_IS.txt, results.csv.
Verdict: **ไม่เจอ**. No post-hoc p_min relaxation (would be data-snooping). N_TRIALS 6122→6138.
WARNING: DATA = IC BID only.
