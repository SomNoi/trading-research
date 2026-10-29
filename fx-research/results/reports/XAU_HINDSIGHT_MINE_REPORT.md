# XAUUSD M5 hindsight pattern mine (deliberate in-sample / lookahead, research only)
**Read this first.** These patterns were chosen with full hindsight, which is like seeing the exam answers before the test. The in-sample numbers are not evidence of edge. The honest check is in section 3.

## Setup
- **Data:** Dukascopy XAU/USD M1 mid resampled to M5, 2019-01-01 to 2025-10-09. The holdout from 2025-10-10 on was not touched.
- **Mining (IS):** the first 70% of eligible bars, up to 2023-10-04 02:55 UTC (1,229 days).
- **Honest check (OOS):** the last 30%, from 2023-10-04 to 2025-10-09 (521 days).
- **Trade:** enter at the next bar's open. TP and SL are both 1×ATR14, so 1R = ATR. Time exit after 12 bars (60 min).
- **Costs:** $0.28/oz round trip (IC), subtracted in R. The rollover block is on. 0.01 lot = 1 oz.
- **"Hit"** means net R > 0 after costs.
- **Pattern families:** every combination of 2 or 3 discrete features, in both directions:
  - hour or half-hour (UTC) and weekday
  - 3-bar candle colour sequence
  - range expansion bucket and body bucket (both in ATR)
  - level touch of the prior-day high or low
  - side of EMA55
- **Minimum sample:** 40 per cell.
- **Script:** scripts/xau_hindsight.py. Output: results/xau_hindsight_*.json.

## 4. Trial count
- This mine tested 37,682 cell×direction combinations.
- The cumulative total is now 917 + 37,682 = **38,599**.
- With this many trials, roughly 2–3% of 40–150-sample cells will show ≥70% hits by chance alone.

## 1. Top patterns at ≥70% in-sample (all of them; only 4 out of 37,132 eligible cells)
| Pattern (plain words) | Dir | IS n | /day | IS hit | IS avg R net |
|---|---|---|---|---|---|
| Thursday, 07:30–08:00 UTC, bar trades below the prior-day low | Short | 150 | 0.12 | 72.7% | +0.17 |
| Thursday, 01:30–02:00 UTC, bar below the prior-day low | Short | 84 | 0.07 | 71.4% | +0.13 |
| 05:30–06:00 UTC, green bar after 2 red bars, small range (<0.7 ATR) | Short | 77 | 0.06 | 71.4% | +0.06 |
| Thursday, 03:30–04:00 UTC, bar below the prior-day low | Short | 125 | 0.10 | 70.4% | +0.05 |

Even with full hindsight and 1:1 R, the ≥70% patterns together give only **0.35 signals/day** (436 trades in total). Their IS hit rate is 71.6%, avg +0.11 R, and net **+$58.6** at 0.01 lot.

## 2. Combined set at ~4.5 signals/day (hindsight)
To reach 4–5 signals/day I had to relax the per-pattern threshold. Patterns were then picked greedily by IS avg R, without overlap.

| Per-pattern threshold | Patterns | IS /day | IS hit | IS avg R | IS net (0.01 lot) |
|---|---|---|---|---|---|
| ≥62% | 57 qualified | 4.54 | 64.2% | −0.01 | +$416 |
| ≥58% | 333 qualified | 4.52 | 62.6% | +0.04 | +$730 |

**Conclusion:** no hindsight set at 4–5 signals/day reaches 70% with sensible 1:1 R exits. A 70% hit rate at that frequency only appears if you skew TP/SL, for example a small TP and a wide SL. That raises the breakeven hit rate by the same amount, so it is not an edge.

## 3. HONEST CHECK: the same patterns, frozen, on the last 30% (unseen)
| Set | OOS n | /day | OOS hit | OOS avg R | OOS net (0.01 lot) |
|---|---|---|---|---|---|
| ≥70% patterns (4) | 169 | 0.32 | **46.7%** | −0.17 | **−$27.7** |
| 4.5/day set (≥62%) | 2,673 | 5.13 | **49.5%** | −0.17 | **−$692** |
| 4.5/day set (≥58%) | 2,428 | 4.66 | **49.9%** | −0.12 | **−$609** |

Hit rates fall back to a coin flip, and costs make the result net negative. The patterns do not hold. The best single pattern (Thursday 07:30 short below the prior-day low) held up best at 59% OOS and +0.08 R, but that is on n = 54, which is noise-level.
