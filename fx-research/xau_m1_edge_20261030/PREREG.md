# PREREG — xau-m1-edge-20261030 (locked before any stats)
Data: /workspace/fx-research/data/XAUUSD_M1.parquet (Dukascopy mid M1), study window 2022-01-01 ICT → data end (2026-10-09 UTC last bar; no extension fetched). Index → Asia/Bangkok.
Rules: HYPOTHESES.md (sha recorded alongside). Signals from closed bars; entry next bar open; one open position per hypothesis (signals during an open trade ignored).
Primary screen (25 trials): SL=$3.50 from entry, TP=1.5R=$5.25, time stop = exit at close of 25th bar after entry. Same-bar SL&TP touch → SL (pessimistic). PnL per 1 oz in $.
Cost: $0.65 per trade round-turn (spread 0.45 + slip 0.15 + comm 0.05), USER model (not Kai IC model).
Splits by entry time ICT: IS 2022-01-01..2023-12-31; OOS 2024-01-01..end; Recent OOS 2025-01-01..end (secondary). NOTE: OOS overlaps fleet HOLDOUT (2025-10-10+) — documented.
KILL (all on OOS): PF>1.25; WR>48% (R=1.5≥1.3); MaxDD (peak-to-trough of cumulative net $ equity) < 0.25 × OOS net profit (net≤0 → fail); N>150;
 sensitivity: entry shifted -2 and +2 bars (signal shift), SL 3.0 and 4.0 (TP kept 1.5R) → each PF>1.15 on OOS.
Sensitivity is run for every hypothesis (4 trials each = 100) so trials = 125. Small grid SL{2.5,3.5,4.5}×TP{1.2,1.5,2.0} (9, minus overlap) run ONLY for hyps passing the 4 OOS base criteria.
Phase 4 (MC shuffle 1000, WFA 6m/2m, Tue–Thu) only if ≥1 passes full kill.
