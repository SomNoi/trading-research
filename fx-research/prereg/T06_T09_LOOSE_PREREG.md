# T06 / T09 base and looser variants: pre-registration (written BEFORE any T09 test or loose-variant test)

The registration timestamp is the `registered_utc` value recorded with the sha256 in results/prereg_hashes.txt.

This file inherits all common conventions from prereg/TRACK3_DEFINITIONS.md (sha256 e563e30f…):
- Closed-bar decisions, entry at the next M5 open.
- One position at a time.
- FLAT 1% risk.
- Kai's cost file at 1x/1.5x/2x.
- Entry block 20:30–24:00 UTC and at weekends.
- Minimum stop XAU $1 / FX 5 pips.
- 24 h safety time-exit.
- Walk-forward: IS 24 months / OOS 6 months, 10 non-overlapping OOS windows 2021-01..2025-10-09.
- Holdout ≥ 2025-10-10 is never loaded.
- Symbols:
  - XAUUSD with the source's USD constants.
  - EURUSD, GBPUSD, USDJPY and AUDUSD with constants ATR-normalised as (c / 2.0) × ATR14(M5).

Each variant below is a single fixed parameter set, i.e. one trial per symbol. There is no grid and no tuning, and the variants are not combined with each other. The pass bar is unchanged.

## T09 VSA absorption, base: source /workspace/xau_lab_review/xau_lab/tech/T09_vsa.py
Not tested before.

Volume source: Dukascopy M1 bid volume summed to M5. The source uses broker tick_volume, so this is a proxy. Only its ratio to the 20-bar average is used.

Signal on a closed M5 bar s, with the reference window being the previous 20 bars:
- avgV = mean volume of the previous 20 bars; avgR = mean range of the previous 20 bars.
- Buy when all of these hold:
  - V(s) ≥ 1.5 × avgV;
  - |close − open| ≤ 0.25 × max(range(s), avgR);
  - low(s) ≤ min low of the previous 10 bars;
  - close(s) > low(s) + 0.6 × range(s).
- Sell is the mirror image: high(s) ≥ max high of the previous 10 bars and close(s) < high(s) − 0.6 × range(s).
- SL = low − $0.20 (buy) or high + $0.20 (sell). Distance from the entry is clamped to [$0.8, $3.0]; the engine minimum of $1 still applies.
- TP 1R.

## T09 looser variants (each relaxes ONE condition of the T09 base)
- **T09_L1_vol12:** volume threshold 1.5 → 1.2 × avgV.
- **T09_L2_body40:** body threshold 0.25 → 0.40 × max(range, avgR).
- **T09_L3_ext5:** swing-extreme lookback 10 → 5 bars (new 5-bar low/high instead of 10-bar).

## T06 AsiaBreak retest: looser variants
Reference base is the source configuration: unlimited trades per day, TP 1R. It was already tested in Track 3 as part of the 4-combo grid; see prereg/TRACK3_DEFINITIONS.md.
- **T06_L1_tol50:** retest tolerance $0.15 → $0.50. The retest bar's low only needs to come within AH + $0.50 (mirror for sells).
- **T06_L2_tokyo:** Asia range window 06:00–13:55 ICT → 09:00–13:55 ICT (02:00–06:55 UTC; Tokyo morning only). The minimum bar count scales 20 → 12. The signal window is unchanged.
- **T06_L3_noprev:** drop the condition that the previous bar also closed beyond the range. The previous bar may have closed back inside; only the retest bar must close outside.

Trials added: (1 base + 3) × 5 symbols for T09, plus 3 × 5 for T06, = 35. All are logged in results/trials.csv. The deflated Sharpe and Bonferroni thresholds are recomputed over all trials.
