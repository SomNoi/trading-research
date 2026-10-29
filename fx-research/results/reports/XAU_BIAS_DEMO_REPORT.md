# DELIBERATELY BIASED STUDY - NOT A STRATEGY
Educational demo of overfitting and lookahead bias, written 2026-10-16 ICT. **Do not trade this.**

**Data:** Dukascopy XAU/USD M5 bars resampled from M1, **mid** price, timestamps in UTC (shown here in ICT). Range 2019-01-01 to 2025-10-09 only.
**Holdout excluded:** the reserved holdout (2025-10-10 onward) was deliberately NOT loaded, even though more recent data was offered. This protects it for real pre-registered candidates.
**Units:** 0.01 lot XAU = 1 oz, so $ per 0.01 lot = $/oz.

**Costs (Kai's IC model, round trip):** p90 spread for the session + $0.05/oz/side slippage + $0.07/oz commission ($3.50/lot/side). By session:
| Session (UTC) | Round-trip cost ($/oz) |
|---|---|
| Asia 00–07 | 0.29 |
| London 07–12 | 0.28 |
| London/NY overlap 12–16 | 0.27 |
| NY 16–20:30 | 0.32 |
| Rollover 20:30–24 | 0.57 |
In the honest control, each trade's cost is the average of the entry-time and exit-time session spreads, plus the fixed parts.

**Target and stop:** target = $0.20 net + $0.28 reference cost (London) = **$0.48/oz**. Stop is **symmetric at $0.48/oz**. If TP and SL are touched in the same bar, it counts as SL.

## Step 1: overfit pattern selection (data-mined)
- **How it was chosen:**
  - Pick the 6 strongest-trending calendar months by |close−open|/open: 2025-09, 2020-07, 2024-03, 2025-03, 2022-11, 2023-03.
  - Encode every 3-bar M5 sequence. Each bar gets a direction (bull/bear), a body/range bucket (<1/3, 1/3–2/3, >2/3) and whether upper wick > lower wick. That gives 12 states per bar and 1,728 patterns × 2 directions.
  - Keep the pattern/direction with the best (TP-first − SL-first) rate inside those 6 months, with at least 30 matches.
- **Locked pattern (code 14):**
  - Bar t−2: bear, body <1/3 of range, lower wick ≥ upper.
  - Bar t−1: bear, body <1/3, upper wick > lower.
  - Bar t: bear, body 1/3–2/3, lower wick ≥ upper.
  - Action: **LONG** at the open of t+1.
- **Inside the mined months:** 32 matches, 68.8% hit TP first.

## Step 2: lookahead filter (BIASED BY DESIGN, not a trial)
- **Method:** for each match from 2019-01 to 2025-10-09 (one position at a time), peek at bars +1..+3 and keep only matches that hit +$0.48 before −$0.48. Losers are dropped.
- **Matches kept:** 167, which is **0.08 per trading day**. By year: 2019 23 | 2020 24 | 2021 25 | 2022 33 | 2023 25 | 2024 23 | 2025 14.
- **Sample week:** the busiest week was 2019-08-26 (ICT) with Mon 1, Tue 0, Wed 0, Thu 1, Fri 1. The suggested week of 2024-03-04 had 0 every day.
- **Top hours (ICT):** 10:00 (15), 09:00 (13), 16:00 (12), 11:00 (12), 18:00 (11).
- **By session (UTC):** Asia 55, London 39, NY 32, London/NY overlap 29, rollover 12.
- **Cumulative "profit":** 167 × $0.20 = **+$33.40 per 0.01 lot**, with a 100% win rate and zero drawdown. This is impossible in real life.
- **Examples** (date, ICT entry time, entry mid price; these are not a reference for trading):
  - 2019-08-14 16:20 ICT, 1500.22
  - 2020-05-27 17:45 ICT, 1706.39
  - 2020-11-18 07:10 ICT, 1881.99
  - 2021-01-26 21:10 ICT, 1856.12
  - 2021-10-01 17:10 ICT, 1754.59
  - 2022-03-30 00:05 ICT, 1913.74
  - 2024-06-27 17:25 ICT, 2313.26
  - 2024-09-25 20:35 ICT, 2663.16

## Step 3: honest control (no peeking, all matches, IC costs)
- **Rules:** entry at the **open of the next M5 bar** after the pattern. Exit at TP or SL ($0.48 each), or a **time stop at the close of the 3rd bar after entry** (15 min). One position at a time.
- **Logged as trials:** 2 rows in trials.csv labelled BIAS_DEMO. N_TRIALS is now 821.

| Run | Trades/day | Win % (net>0) | TP-hit % | Gross $/trade | Net $/trade (0.01 lot) | Cumulative $ | PF | Max DD $ |
|---|---|---|---|---|---|---|---|---|
| Full span 2019–2025-10-09 (pattern above) | 0.18 (372) | 41.7 | 44.9 | −0.02 | −0.34 | −127.97 | 0.19 | −127.78 |
| Split: re-mined on 2019–22 months, in-sample 2019–22 | 0.15 (191) | 41.4 | 45.5 | −0.01 | −0.34 | −63.89 | 0.19 | −63.16 |
| Split: same pattern, out-of-sample 2023–2025-10-09 | 0.15 (129) | 36.4 | 42.6 | −0.06 | −0.39 | −50.19 | 0.15 | −50.40 |

**Split pattern (mined on 2020-07, 2022-11, 2021-05, 2019-08, 2021-06, 2020-04):** bear body 1/3–2/3 with upper wick > lower, then bear body <1/3 with upper wick > lower, then bull body >2/3 with upper wick > lower → SHORT. It scored 71% TP-first inside those months (31 matches).

**Why it fails:**
- Before costs the pattern is a coin flip, with gross close to $0.
- A win nets only about +$0.16 after costs; a loss costs about −$0.80.

## Side by side
- **BIASED (lookahead):** 167 trades, 100% wins, +$33.40 per 0.01 lot, 0 drawdown.
- **HONEST (same pattern, full span):** 372 trades, 42% wins, −$127.97 per 0.01 lot, PF 0.19.
- **HONEST (locked 2019–22, tested 2023–25):** 129 trades, 36% wins, −$50.19 per 0.01 lot, PF 0.15.

Script: scripts/xau_bias_demo.py. Data: results/xau_bias_demo.json.
