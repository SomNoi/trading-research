# R94 REPORT — OR-pool PDH∪PWH first CONT break, XAU M5
**DATA WARNING: SUBSTITUTE parquet M1→M5 mid (`data/from_parquet_m1/XAUUSD_M5.csv`) — NOT IC BID.**
PREREG sha256 1d4b06308d6c1044c7853a7677fe175073de61a93a5b1df978feeb6ca78ec1ae (chmod 444, written before run).

Signals 1279 days (PDH 1022, PWH 185, BOTH 72). Cost $0.28, SL$3.5 TP1.5R, 60/40 by day.

**Verdict: prereg PASS 1/16 — fragile, NOT Bonferroni-significant.**
- PASS: MonTue H24 ATR-any — IS n=303 PF 1.126 E+0.17; OOS n=213 PF 1.317 E+0.54; @$0.42 PF 1.226. OOS t≈1.92 vs Z_BONF≈4.23 (N=4226).
- Neighbours: MonTue H12 any OOS 1.187 (n=213); MonTue Q4 OOS 1.41–1.48 but n=53. WedThu all OOS<1. any-day OOS 1.08–1.17.
- LevelTag (pass cell OOS): PDH n=183 PF 1.262, PWH n=13 1.247, BOTH n=17 2.143 — edge is mostly PDH; PWH-only breaks weak in any-day (OOS 0.90–1.00).
- vs R93 (PDH-only, H16 MonTue OOS 1.203 n=209): union + crossing definition + H24 lifts to 1.317 — same family, near-duplicate trades. vs R92 (PWH, n≤94): pool adds sample but PWH tag alone doesn't carry.
Results: results/results.json
