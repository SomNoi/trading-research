# Run B — XAUUSD M5 bar-shape edge (IS 60 / OOS 40)
Source: IC Markets MT5 BID XAUUSD M5 export, 99,964 bars from 2025-05-14 to 2026-10-09 UTC. The split falls at 2026-03-19 03:05 UTC (10:05 ICT).
Prereg: ../PREREG.md, sha256 bea9dcc0…876addf, locked before any backtest.
## Clusters (IS discovery; kept clusters have ≥20 members)
| cfg | protos | kept | IS cover | OOS assigned |
|---|---|---|---|---|
| w3 0.85 | 98 | 54 | 99.6% | 99.4% |
| w3 0.90 | 267 | 122 | 98.8% | 98.6% |
| w4 0.85 | 211 | 87 | 99.1% | 99.0% |
| w4 0.90 | 662 | 194 | 96.1% | 96.0% |
| w5 0.85 | 380 | 120 | 97.7% | 97.4% |
| w5 0.90 | 1369 | 263 | 92.2% | 92.2% |
## Sequences
- Top 40 IS sequences by |lift| at N=3 with n≥100. In OOS, 55% keep the same lift sign, and the IS-to-OOS lift correlation is 0.08. That is noise.
## Backtests
- 440 trials: (180 clusters + 40 sequences) × continuation and mean-reversion. Each uses $0.28 cost, SL $3.5, TP 1.5R, and a 25-bar time stop.
- **0 / 440 PASS.** Median OOS PF is 0.85 for clusters and 0.84 for sequences. 358 trials have n>150; only 6.7% of them have OOS PF>1. IS PF and OOS PF correlate at 0.05.
| near-miss | mode | IS PF | OOS n | OOS PF | WR | net $/oz | MDD | sens min PF |
|---|---|---|---|---|---|---|---|---|
| w4_t0.85_c39 | MR | 0.88 | 163 | 1.19 | 47.2% | +61.2 | 30.9 | 0.91 |
| w5_t0.9_c43 | MR | 1.12 | 191 | 1.19 | 47.6% | +69.9 | 55.7 | 0.85 |
| w5_t0.9_c32 | cont | 0.90 | 210 | 1.17 | 47.1% | +72.5 | 48.6 | 0.99 |
| w4_t0.85_c25 | MR | 0.90 | 208 | 1.17 | 47.1% | +71.3 | 29.5 | 0.29 |
| w5_t0.9_c15 | MR | 0.68 | 193 | 1.15 | 46.6% | +58.0 | 48.8 | 0.04 |
Every near-miss fails PF>1.25, WR>48%, MDD<25% of net, and sensitivity. OOS t is about 1.1, far below Z_BONF 4.12. Verdict: **ไม่เจอ**.
Session gate: skipped, as declared in the prereg. Charts: eq_*.png (top 5 by OOS PF; the red line marks the split).
