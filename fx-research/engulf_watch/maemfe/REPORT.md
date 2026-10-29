# XAUUSD M5 engulf T1/T2: MAE/MFE study and SL/TP bracket test
**Source for every number:** Dukascopy free feed (**mid**), not IC MT5. XAU/USD M1 aggregated to M5 (UTC). Signals from 2019-01-02 to 2025-10-09. The project holdout (2025-10-10+) was never loaded.
Research only; no orders were placed.

## Method
- **Signals:** engulf T1/T2 as in engulf_watch (each bar counted once, T2 takes precedence). There were 74,434 signal bars, of which **62,599 are eligible**:
  - the next bar is contiguous;
  - the 24-bar window has no daily-break or weekend gap;
  - entry is not between 20:30 and 24:00 UTC or on a weekend (the IC cost-file block).
- **Measurement:** entry at the next M5 open. The 24 M5 bars are scanned on M1 bars.
  - MFE = max favourable move from entry; the first M1 bar that reaches it is the peak.
  - MAE-before-peak = max adverse move from the entry minute up to and including the peak minute.
  - Total MAE covers all 24 bars.
  - Outcome is decided by the bar-24 close vs entry; a flat close counts against.
- **Split:** chronological by signal. **Discovery** = first 70% (43,819 signals, 2019-01-02 to 2023-09-07 06:25 UTC). **Holdout** = last 30% (18,780 signals, 2023-09-07 06:50 to 2025-10-09).
- **Freeze before holdout:** SL/TP were fixed in MAEMFE_PREREG.md (sha256 d35aa556…, hashed 2026-10-17T06:29:25Z) before any holdout statistic was computed.
- **Bracket rules:** if SL and TP fall in the same M1 bar, SL counts first. Otherwise exit at the bar-24 close. One trade at a time. Cost $0.28/oz round trip, size 1 oz (0.01 lot).

## Discovery: distributions ($/oz)
- **Outcome at bar 24:** 48.8% went the signal's way (21,404 winners, 22,415 losers).
- **MAE before peak, p50/p70/p80/p90:** winners 0.95 / 1.69 / **2.29** / 3.40; losers 0.65 / 1.24 / 1.76 / 2.76.
- **Separation is poor and inverted.**
  - Only 13.8% of losers exceed the winner p80, against 20% of winners by construction.
  - AUC(loser > winner) = 0.42, below 0.5: losers show *less* pre-peak heat, because their peak comes early (median bar 4 vs 19 for winners).
  - Total MAE over 24 bars separates well (AUC 0.84), but that is only known after the fact.
- **MFE, p50/p70/p90:** all signals 2.19 / 3.74 / 7.59; winners 3.82 / 5.74 / 10.24.
- **By side (information only):** winner MAE-before-peak p80 is 2.31 for BUY and 2.27 for SELL; all-signal MFE p50 is 2.19 / 2.20; win rate at bar 24 is 49.6% / 48.1%.
- **Frozen levels:** **SL = 2.29 + $0.30 buffer = $2.59.** TP combos, each counted as a trial:
  - P_all50 = 2.19 (primary)
  - P_all70 = 3.74
  - S_win50 = 3.82
  - S_win70 = 5.74
- These SL/TP are fixed $ amounts, while gold's $-volatility roughly doubled over the span. Holdout MFE p50 was 3.44 against 2.19 in discovery.

## Results ($ per 0.01 lot, after $0.28 cost)
| combo (SL/TP) | set | trades | win % | breakeven win % | avg win | avg loss | net $ | gross $ | PF | max losing streak |
|---|---|---|---|---|---|---|---|---|---|---|
| P_all50 2.59/2.19 | discovery | 20014 | 50.7 | 58.5 | 1.79 | −2.52 | −6696 | −1093 | 0.73 | 15 |
| | holdout | 11809 | 53.5 | 59.5 | 1.88 | −2.76 | −3311 | −4 | 0.78 | 13 |
| P_all70 2.59/3.74 | discovery | 16786 | 41.6 | 47.6 | 2.72 | −2.47 | −5215 | −514 | 0.78 | 16 |
| | holdout | 9961 | 41.4 | 46.1 | 3.20 | −2.73 | −2786 | +3 | 0.83 | 14 |
| S_win50 2.59/3.82 | discovery | 16679 | 41.3 | 47.3 | 2.75 | −2.47 | −5195 | −525 | 0.79 | 16 |
| | holdout | 9915 | 41.0 | 45.6 | 3.26 | −2.73 | −2760 | +16 | 0.83 | 14 |
| S_win70 2.59/5.74 | discovery | 15124 | 37.6 | 42.9 | 3.25 | −2.44 | −4548 | −314 | 0.80 | 19 |
| | holdout | 8907 | 34.3 | 38.1 | 4.42 | −2.72 | −2431 | +63 | 0.85 | 18 |

**Primary P_all50, BUY vs SELL net $ (PF):**
- Discovery: BUY −3427 (0.73) / SELL −3269 (0.73).
- Holdout: BUY −1559 (0.80) / SELL −1751 (0.77).

**P_all50 per year, net $:**
| year | discovery | holdout |
|---|---|---|
| 2019 | −940 | — |
| 2020 | −1828 | — |
| 2021 | −1481 | — |
| 2022 | −1600 | — |
| 2023 | −848 (to Sep 7) | −449 (from Sep 7) |
| 2024 | — | −1640 |
| 2025 | — | −1222 |

Every year is negative for every combo. Full per-year and per-side tables are in discovery.json and holdout.json.

**Holdout distributions (descriptive):**
- MAE before peak, p50/p70/p80/p90: winners 1.46 / 2.61 / 3.53 / 5.36; losers 0.95 / 1.82 / 2.65 / 4.13.
- AUC 0.415.
- Win rate at bar 24: 49.1%.

## Verdict: NO EDGE
- Before costs the brackets are roughly zero: discovery −$0.02 to −$0.05 per trade, holdout about $0.00 to +$0.01.
- The $0.28 cost makes every combo lose on both sets. The win rate sits 4–6 points below breakeven.
- Losers do not sit deeper in MAE before the peak than winners, so this SL rule does not use any real separation.

**Multiple testing:** 4 trials logged (engulf-maemfe). The project total is now **925 trials**, so the **Bonferroni bar is z ≈ 3.87**.

## Files
- maemfe.py
- MAEMFE_PREREG.md
- discovery_signals.csv
- holdout_signals.csv
- discovery_trades.csv
- holdout_trades.csv
- discovery.json
- holdout.json
