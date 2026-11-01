# R236 REPORT — ไม่เจอ
PREREG sha256 2ce5138d… (chmod 444, locked before outcomes). setups_IS.json locked (444) before OOS BT. IC BID XAU M5, cost $0.28, 60/40 by day (cut 2026-03-18).
## Selection (IS, big-target bars |body|≥5 or range≥5)
Strongest consistent (≥3/4 families) direction deviation: hour==03 UTC hit 0.444 (−5.6pp, n378); next hour 09 +3.2pp, hour 04 +2.8pp, tvr q40–60 −2.1pp, uw q20–40 +1.9pp. Everything else <2pp ⇒ pre-entry features carry ~no directional info. Full table: selection_IS.csv.
## Direction hit (CONT = ref-bar color)
| entry | gate | IS all | OOS all | IS big | OOS big | P(rng≥5) IS/OOS |
|---|---|---|---|---|---|---|
| B2 | none | 0.492 | 0.489 | 0.502 | 0.492 | 0.281/0.418 |
| B2 | G1 | 0.497 | 0.503 | 0.444 | 0.501 | 0.146/0.248 |
| B2 | G2 | 0.461 | 0.472 | 0.467 | 0.345 | 0.182/0.403 |
| B3 | none/G1/G2 | ≈ same as B2 (same ref→next-bar relation, one bar later) | | | | |
Gates *lower* size (Asia hour) and do not move OOS direction off 50%.
## Backtest 16 cells
0/16 PASS; OOS>0 2/16 (B2/B3 G2 FADE TP5 SL4, E+0.014R $+0.06, n72, PF1.04, z0.15). G1 cells all OOS E −0.05…−0.08R ($−0.26…−0.32), z ≈ −4…−5. Cost 1.5×: all negative. Target $5–10/0.01 not approached.
## Caveats
B2 family consistency used col0×col1 (pre-entry) since col1×col2 makes CONT hit degenerate — documented deviation. B2 and B3 are near-duplicate tests (≈ same samples shifted) — effective independent trials ≈8, N still bumped by 16.
## Verdict
ไม่เจอ — direction ≈50% with or without gates; size≠direction confirmed again (R233–R236).
- R236 xau_m5_common_feat_dir_20261101 — Shared pre-entry features (hour, sess, tvr, rng/ATR, bf, wicks, streak, PDH/PDL dist, moh, same/size2/1) selected IS for DIRECTION on large-move bars, pooled + ≥3/4 families; gates G1=hour03 UTC, G2=hour03∧tvr q40–60 → entry bar2/bar3 OPEN CONT/FADE, TP5/SL4 & TP10/SL5, single-bar — ไม่เจอ. best B2 G2 FADE TP5 SL4 OOS E+0.014R ($+0.06/0.01lot) PF1.04 z0.15 n72 (IS E-0.037R n165); OOS>0 2/16; gate-PASS 0/16; Z_bonf 4.319; N=6394. Direction hit: baseline IS 0.492/OOS 0.489 (big-target 0.502/0.492); G1 OOS 0.503 (big 0.501); max IS lift 5.6pp did not survive OOS.
