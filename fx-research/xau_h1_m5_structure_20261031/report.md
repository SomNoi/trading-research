# Report — H1 structure bias + M5 trigger, XAUUSD (IC MT5 BID M5)
Prereg: PREREG.md sha256 757d47d02d138df5688851c2814911f3829524e261e587baad95725547c54d19 (hashed + chmod a-w before run). Split 60/40 by M5 bar. Cost $0.28 RT /0.01 lot.
H1 events (full sample): bull BOS 218, bear BOS 178, bull CHoCH 155, bear CHoCH 162.

**Verdict: ไม่เจอ (no edge). 0/16 pass.**
- Best OOS PF: CHoCH_flip|ENGULF|E2|any — PF 0.998, n=663, WR 40.0%, exp −$0.008/trade, PF@1.5x cost 0.97, MDD 51% at 1% risk, sens 0.95–1.03.
- Next: BOS_cont|ENGULF|E2|any PF 0.92 (n=1065; IS 1.09 did not hold).
- Median OOS PF ≈ 0.81. Session gate LDN∪NY made every arm worse. E1 (fixed $3.5) worse than E2 (ATR) in all pairs.
- No trial reaches PF 1.0 at 1.5x cost; Bonferroni bar (Z 4.13) is moot.
Full table: summary.csv. Chart: chart_top3_oos.png.
