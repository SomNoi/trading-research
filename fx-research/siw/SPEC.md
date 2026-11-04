# SIW v2 — XAUUSD M5 (2026-11-04). Research only, no live trading.
Times: IC server (UTC+3 until Nov 1 2026, UTC+2 after). Decide on CLOSED bars only.
Bar L = CONFIRM bar (= the trader's listed time). Entry = OPEN of L+1.

## Rules (sell; buy = mirror)
1. Direction (only filter): EMA21 < EMA55 at L → sells only; EMA21 > EMA55 → buys only. (EMA21 touch: optional, default OFF — made no difference.)
2. L is valid if any enabled mode is true:
   - A: L is a pin/shooting star (upper wick ≥50% of range, body ≤35%) or a small body (≤40%) sitting inside L-1's upper wick (±$0.30).
   - B: Engulfing: L red, L-1 green, open(L) ≥ close(L-1)−$0.10 and close(L) ≤ open(L-1)+$0.10.
   - C: original SIW: L-1 is pin/star-in-wick and L closes red.
3. Leg filter: ext = highest high of last 12 bars (incl. L) − close(L). ext > $10 → SKIP (no reverse trade). Buy: close − lowest low.
   Optional pullback zone: ext ≤ $3 (default OFF; it cuts catch from 17 to 3 of 20).
4. Dedupe: OFF by default (dedupe=1 = consecutive bars may both signal). dedupe=3 hid 11 of his 20 picks because a pattern fired 1 bar earlier. Note: this inflates signal count (clusters).
5. Trade: TP $10, SL $5 from entry; same-bar both → SL; timeout 48 bars (close at market); cost $0.28 per 0.01.

## ไทย
1. ทิศทาง: EMA21 > EMA55 รอเฉพาะ Buy; EMA21 < EMA55 รอเฉพาะ Sell (ไม่บังคับแตะ EMA21).
2. แท่งที่ลิสต์ = แท่งคอนเฟิร์ม (L) เข้าออเดอร์ที่ราคาเปิดแท่งถัดไป. L ใช้ได้ถ้า
   A) L เป็นพินบาร์/Shooting star/Hammer หรือเนื้อเทียนสั้นอยู่ในไส้ของแท่งก่อนหน้า
   B) L เป็น Engulfing ตามเทรนด์ (Sell: แท่งแดงกลืนแท่งเขียวก่อนหน้า)
   C) แท่งก่อนหน้าเป็นพิน/สตาร์ในไส้ และ L ปิดสีตามทิศ (SIW เดิม)
3. วัดระยะจาก High สูงสุด (Sell) / Low ต่ำสุด (Buy) ของขาปัจจุบัน (12 แท่ง) ถึงราคาปิด L: ถ้าห่างเกิน $10 = ข้าม ไม่เข้า ไม่กลับทาง. โซน $2-3 เป็นตัวเลือก (ปิดไว้).
4. TP $10 / SL $5 จากราคาเข้า, ชนทั้งคู่ในแท่งเดียวนับ SL, หมดเวลา 48 แท่ง, ค่าใช้จ่าย $0.28 ต่อ 0.01 ล็อต.
ทุกตัวเลขปรับได้ใน P (siw.py) / inputs (Pine, MQL5).

## Exit v3 (2026-11-04) / ทางออก v3
SL $5 / TP $20 from entry. After 3 bars (15 min) still open → trailing stop = best price since entry ∓ trail ($2/$3/$5), never looser than SL; optional BE (stop ≥ entry). Bar-by-bar, SL before TP in same bar. Results: exit_v3.md.
ไทย: SL $5 / TP $20, ครบ 15 นาทียังไม่ปิด → เปิด Trailing stop ตามราคาที่ดีที่สุดตั้งแต่เข้า (ห่าง $2/$3/$5), ตัวเลือกเลื่อน SL ไปจุดทุน.
Run: `python3 siw.py duka_xau_m5_bid.csv --exit v3 --trail 3 [--be]`

## Exit v4 (2026-11-04, CURRENT) / ทางออก v4 (ใช้ปัจจุบัน)
SL $10 / TP $20 (safety cap) from entry (= open of L+1). Close by time at the CLOSE of bar L+2 (10 min after entry), whichever comes first. Bar by bar over L+1, L+2: SL checked before TP (worst case); gap through a level fills at bar open. Cost $0.28 per 0.01. Replaces v3 for alerts/app. Results: exit_v4.md (in-sample).
ไทย: SL $10 / TP $20 (กันไว้) จากราคาเข้า (เปิดแท่ง L+1). ครบ 10 นาที = ปิดที่ราคาปิดแท่ง L+2 (แท่งที่ 2 หลังเข้า) อะไรถึงก่อนปิดก่อน. แท่งเดียวชนทั้ง SL/TP นับ SL.
Run: `python3 siw.py duka_xau_m5_bid_refreshed.csv --exit v4` · `python3 exit_v4.py`
