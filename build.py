# -*- coding: utf-8 -*-
# Builds /workspace/research-site/index.html. Every number below is copied from the source reports (path noted per card).
import html, os
OUT = "/workspace/research-site/index.html"
E = html.escape

# ---------------------------------------------------------------- charts (inline SVG)
FONT = "font-family=\"Sarabun,'Noto Sans Thai','Leelawadee UI',Tahoma,sans-serif\""

def chart_breakeven():
    rows = [
        ("SL $2 / TP $5 ทุกสัญญาณ (2019-2025)", 31.47, 32.6),
        ("SL $2 / TP $5 + ตัวกรอง H1", 30.6, 32.6),
        ("TP $5 / SL ปลายแท่งสัญญาณ", 25.17, 31.5),
        ("TP $5 / SL $3", 40.27, 46.49),
        ("TP $5 / SL $7", 47.42, 52.68),
        ("7 ปี: SL 2.59 / TP 2.19 (ช่วงทดสอบ)", 53.5, 59.5),
        ("7 ปี: SL 2.59 / TP 3.74 (ช่วงทดสอบ)", 41.4, 46.1),
        ("7 ปี: SL 2.59 / TP 5.74 (ช่วงทดสอบ)", 34.3, 38.1),
        ("SMC M5 (zz3, TP 1.5R, ช่วงทดสอบ)", 41.3, 44.9),
    ]
    W, L, R = 440, 10, 56
    rowh = 58
    top = 50
    H = top + rowh * len(rows) + 20
    scale = (W - L - R) / 70.0
    s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="win rate จริง เทียบ จุดคุ้มทุน" {FONT}>']
    s.append(f'<rect x="{L}" y="12" width="14" height="14" rx="3" fill="#f5a524"/><text x="{L+20}" y="24" fill="#e6e9ef" font-size="15">ชนะจริง</text>')
    s.append(f'<line x1="{L+100}" y1="12" x2="{L+100}" y2="28" stroke="#ff5d73" stroke-width="4"/><text x="{L+110}" y="24" fill="#e6e9ef" font-size="15">จุดคุ้มทุน (ต้องชนะเกินเส้นนี้)</text>')
    for i, (lab, act, be) in enumerate(rows):
        y = top + i * rowh
        s.append(f'<text x="{L}" y="{y+14}" fill="#c9d1e0" font-size="15">{E(lab)}</text>')
        s.append(f'<rect x="{L}" y="{y+22}" width="{(W-L-R):.1f}" height="20" rx="4" fill="#232a3a"/>')
        s.append(f'<rect x="{L}" y="{y+22}" width="{act*scale:.1f}" height="20" rx="4" fill="#f5a524"/>')
        bx = L + be * scale
        s.append(f'<line x1="{bx:.1f}" y1="{y+17}" x2="{bx:.1f}" y2="{y+47}" stroke="#ff5d73" stroke-width="4"/>')
        s.append(f'<text x="{L+act*scale-6:.1f}" y="{y+37}" fill="#1a1300" font-size="13" text-anchor="end" font-weight="700">{act:.1f}%</text>')
        s.append(f'<text x="{bx+7:.1f}" y="{y+37}" fill="#ff8b9a" font-size="13" font-weight="700">{be:.1f}%</text>')
    s.append('</svg>')
    return "".join(s)

def chart_diverging(rows, maxabs, unit_note, aria):
    # rows: (label, gross, net)
    W, L, R = 440, 10, 10
    rowh = 74
    top = 46
    H = top + rowh * len(rows) + 30
    zero = W - R - 74
    scale = (zero - L - 10) / float(maxabs)
    s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{E(aria)}" {FONT}>']
    s.append(f'<rect x="{L}" y="12" width="14" height="14" rx="3" fill="#5ad19a"/><text x="{L+20}" y="24" fill="#e6e9ef" font-size="15">ก่อนหักต้นทุน (gross)</text>')
    s.append(f'<rect x="{L+215}" y="12" width="14" height="14" rx="3" fill="#ff5d73"/><text x="{L+235}" y="24" fill="#e6e9ef" font-size="15">หลังหักต้นทุน (net)</text>')
    s.append(f'<line x1="{zero}" y1="{top-6}" x2="{zero}" y2="{H-24}" stroke="#8892a6" stroke-width="1.5" stroke-dasharray="4 3"/>')
    s.append(f'<text x="{zero}" y="{H-8}" fill="#8892a6" font-size="13" text-anchor="middle">0 (เท่าทุน)</text>')
    for i, (lab, g, n) in enumerate(rows):
        y = top + i * rowh
        s.append(f'<text x="{L}" y="{y+14}" fill="#c9d1e0" font-size="15">{E(lab)}</text>')
        for j, (v, col) in enumerate(((g, "#5ad19a"), (n, "#ff5d73"))):
            yy = y + 22 + j * 22
            w = abs(v) * scale
            if v < 0:
                x = zero - w
                s.append(f'<rect x="{x:.1f}" y="{yy}" width="{max(w,1.5):.1f}" height="18" rx="3" fill="{col}"/>')
            else:
                s.append(f'<rect x="{zero}" y="{yy}" width="{max(w,1.5):.1f}" height="18" rx="3" fill="{col}"/>')
            txt = (f"+{v:,.2f}" if v > 0 else f"{v:,.2f}").replace(".00", "")
            s.append(f'<text x="{zero+8+(w if v>0 else 0):.1f}" y="{yy+14}" fill="{col}" font-size="13" font-weight="700">{txt}</text>')
    s.append('</svg>')
    return "".join(s) + f'<p class="note">{unit_note}</p>'

def chart_hindsight():
    rows = [(("4 รูปแบบ", "ที่ชนะ ≥70%"), 71.6, 46.7), (("ชุด 4.5/วัน", "(≥62%)"), 64.2, 49.5), (("ชุด 4.5/วัน", "(≥58%)"), 62.6, 49.9)]
    W, H = 440, 330
    base, top = 260, 70
    scale = (base - top) / 80.0
    s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="ผลขุดรูปแบบ ก่อนและหลัง" {FONT}>']
    s.append('<rect x="10" y="12" width="14" height="14" rx="3" fill="#7aa2ff"/><text x="30" y="24" fill="#e6e9ef" font-size="15">ช่วงที่ใช้ค้นหา (เห็นข้อสอบแล้ว)</text>')
    s.append('<rect x="10" y="36" width="14" height="14" rx="3" fill="#ff5d73"/><text x="30" y="48" fill="#e6e9ef" font-size="15">ช่วงที่ไม่เคยเห็น</text>')
    y50 = base - 50 * scale
    s.append(f'<line x1="10" y1="{y50:.1f}" x2="{W-10}" y2="{y50:.1f}" stroke="#8892a6" stroke-dasharray="5 4"/>')
    s.append(f'<text x="{W-10}" y="{y50+16:.1f}" fill="#8892a6" font-size="13" text-anchor="end">เส้น 50% = โยนเหรียญ</text>')
    gw = (W - 20) / 3.0
    for i, (lab, a, b) in enumerate(rows):
        gx = 10 + i * gw
        for j, (v, col) in enumerate(((a, "#7aa2ff"), (b, "#ff5d73"))):
            x = gx + 14 + j * 52
            h = v * scale
            s.append(f'<rect x="{x:.1f}" y="{base-h:.1f}" width="46" height="{h:.1f}" rx="4" fill="{col}"/>')
            s.append(f'<text x="{x+23:.1f}" y="{base-h-6:.1f}" fill="#e6e9ef" font-size="14" text-anchor="middle" font-weight="700">{v:.1f}%</text>')
        cx = gx + 14 + 49
        s.append(f'<text x="{cx:.1f}" y="{base+22}" fill="#c9d1e0" font-size="14" text-anchor="middle">{E(lab[0])}</text>')
        s.append(f'<text x="{cx:.1f}" y="{base+41}" fill="#c9d1e0" font-size="14" text-anchor="middle">{E(lab[1])}</text>')
    s.append('</svg>')
    return "".join(s)

def chart_be_curve():
    W, H = 440, 300
    L, B, T, Rr = 50, 245, 30, 20
    xs = [0.5, 1, 1.5, 2, 2.5, 3]
    xmax = 3.2
    def px(r): return L + (r - 0.3) / (xmax - 0.3) * (W - L - Rr)
    def py(p): return B - p / 80.0 * (B - T)
    s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="จุดคุ้มทุนตามอัตรา TP ต่อ SL" {FONT}>']
    for p in (20, 40, 60, 80):
        s.append(f'<line x1="{L}" y1="{py(p):.1f}" x2="{W-Rr}" y2="{py(p):.1f}" stroke="#2c3446"/><text x="{L-8}" y="{py(p)+5:.1f}" fill="#8892a6" font-size="13" text-anchor="end">{p}%</text>')
    pts = []
    r = 0.3
    while r <= xmax + 1e-9:
        pts.append(f"{px(r):.1f},{py(100/(1+r)):.1f}")
        r += 0.05
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#f5a524" stroke-width="3"/>')
    for r in xs:
        p = 100 / (1 + r)
        s.append(f'<circle cx="{px(r):.1f}" cy="{py(p):.1f}" r="5" fill="#f5a524"/>')
        s.append(f'<text x="{px(r):.1f}" y="{py(p)-10:.1f}" fill="#e6e9ef" font-size="13" text-anchor="middle">{p:.1f}%</text>')
        s.append(f'<text x="{px(r):.1f}" y="{B+20}" fill="#c9d1e0" font-size="13" text-anchor="middle">1:{r:g}</text>')
    s.append(f'<text x="{(L+W-Rr)/2:.0f}" y="{B+42}" fill="#8892a6" font-size="13" text-anchor="middle">SL : TP (ยังไม่รวมต้นทุน)</text>')
    s.append('</svg>')
    return "".join(s)

# ---------------------------------------------------------------- studies
NE, PR, PS, EX = "ne", "pr", "ps", "ex"
BADGE = {NE: "ไม่มีเอดจ์", PR: "มีแววแต่ยังไม่พอ", PS: "ผ่าน", EX: "แค่สำรวจ สรุปไม่ได้"}

groups = []

groups.append(("gold-engulf", "ทองคำ M5: แท่งกลืนกิน / ปิดทะลุ (เรื่องหลักของเรา)", [
 dict(t="สแกนแท่งกลืนกิน 1 วัน (15 ต.ค.)", d="15-16 ต.ค. 2026", q="วันที่ 15 ต.ค. แท่งกลืนกินบน M5 วิ่งไปทางสัญญาณไกลแค่ไหน",
      m="ใช้ข้อมูล Dukascopy ของวันนั้นวันเดียว (276 แท่ง M5) นับแท่งกลืนกินแบบ 1 แท่งเล็ก และ 2 แท่งเล็ก แล้วดูว่าราคาวิ่งต่อกี่จุดใน 12 แท่ง",
      k=["เจอ 7 สัญญาณ (ซื้อ 6 ขาย 1)", "สัญญาณซื้อวิ่งไปทางเราเฉลี่ย 2,000 ถึง 2,600 จุด (จุดละ $0.01)", "แต่วันนั้นทองผันผวนมาก (วิ่ง $20 ถึง $50) ไม่ใช่วันปกติ"],
      v=EX, src="results/reports/XAU_ENGULF_20261015_REPORT.md"),
 dict(t="ปิดทะลุ + TP $5 (ย้อนหลัง 6.8 ปี)", d="ราว 16 ต.ค. 2026", q="ถ้าเข้าทุกสัญญาณปิดทะลุ T1/T2 แล้วตั้ง TP $5 จะกำไรไหม",
      m="ข้อมูล 2019 ถึง 9 ต.ค. 2025 (2,107 วัน) ลอง SL 4 แบบ: ปลายแท่งสัญญาณ, $3, $5, $7 หักต้นทุน $0.28 ต่อ 0.01 lot",
      k=["73,958 สัญญาณ (ราว 35 ครั้งต่อวัน)", "SL ปลายแท่ง: ชนะ 25.2% แต่ต้องชนะ 31.5% ถึงจะเท่าทุน", "SL $7: ชนะ 47.4% แต่ต้องชนะ 52.7%", "ขาดทุนราว -$0.24 ถึง -$0.50 ต่อไม้ ทุก SL ทุกปี"],
      v=NE, src="results/reports/XAU_CLOSEBREAK_TP5_REPORT.md"),
 dict(t="MFE / MAE ของสัญญาณปิดทะลุ", d="ราว 16 ต.ค. 2026", q="หลังสัญญาณ ราคาวิ่งไปทางเรามากกว่าวิ่งสวนไหม",
      m="วัดระยะที่ราคาวิ่งไปทางเรา (MFE) และวิ่งสวน (MAE) ใน 6, 12, 24 แท่ง ของทุกสัญญาณ 2019 ถึง 2025",
      k=["24 แท่ง: MFE กลาง $2.34 เทียบ MAE กลาง $2.42 แทบเท่ากัน", "วิ่งไปทางเรา ≥$5: 23.4% วิ่งสวน ≥$5: 23.7%", "ราคาสวนก่อนถึงจุดสูงสุดราว 48% ของครั้ง", "หน้าตาเหมือนการสุ่ม ไม่มีแรงส่งต่อ"],
      v=NE, src="results/reports/XAU_ENGULF_MFE_MAE_REPORT.md"),
 dict(t="SL $2 / TP $5 และตัวกรอง H1", d="ราว 16 ต.ค. 2026", q="SL $2 TP $5 (เสี่ย 1 ได้ 2.5) จะชนะพอไหม ถ้าใส่ตัวกรองเทรนด์ H1 + ย่อตัว M15 จะดีขึ้นไหม",
      m="ทุกสัญญาณ 2019 ถึง 2025 ถือได้สูงสุด 48 แท่ง หักต้นทุน $0.28 แล้วลองแบบมีตัวกรอง H1 BOS + ย่อ 40-60% บน M15",
      k=["จุดคุ้มทุน = (2+0.28)/(5+2) = 32.6%", "ไม่กรอง: ชนะ 31.5% ขาดทุนรวม -$24,208 (0.01 lot) ติดลบทุกปี", "กรอง H1: สัญญาณเหลือ 2.2 ต่อวัน ชนะ 30.6% ยังต่ำกว่าคุ้มทุน", "ฝั่งซื้อปี 2024-25 พอเสมอตัว (+$13 จาก 914 ไม้) น่าจะมาจากทองขาขึ้น"],
      v=NE, src="results/reports/XAU_SL2_TP5_REPORT.md"),
 dict(t="เฝ้าสัญญาณสด 1 สัปดาห์", d="12-17 ต.ค. 2026", q="สัปดาห์นี้ สัญญาณแท่งกลืนกินไปถูกทางกี่ %",
      m="ตัวเฝ้าสัญญาณอ่านราคา Dukascopy ทุกชั่วโมง นับแท่ง T1/T2 แล้วดูราคาปิดแท่งที่ 24 (2 ชั่วโมง) ว่าไปทางสัญญาณไหม ไม่มีการส่งคำสั่งจริง",
      k=["197 สัญญาณ มีผลครบ 192", "ไปทางสัญญาณ 99 ครั้ง = 51.6% (ใกล้โยนเหรียญ)", "ซื้อ 44.2% (95 ครั้ง) ขาย 58.8% (97 ครั้ง)", "ยังไม่หักต้นทุน และแค่ 1 สัปดาห์"],
      v=NE, src="engulf_watch/signals.csv"),
 dict(t="ทดสอบย้อนหลัง 1 สัปดาห์ 4 แบบ", d="17 ต.ค. 2026", q="สัปดาห์ 12-17 ต.ค. ถ้าเทรดตามกฎ 4 แบบจะได้เท่าไร",
      m="ENG5 (ถือ 5 นาที), SMA21 5 นาที, SMA21 15 นาที + ออกก่อน (MAIN), ไม่กรอง 15 นาที เข้าแท่งถัดไป หักต้นทุน $0.28",
      k=["ENG5: 213 ไม้ ชนะ 43.2% สุทธิ -$73.97", "SMA21 5 นาที: 139 ไม้ ชนะ 44.6% สุทธิ -$67.13", "MAIN SMA21 15 นาที: 131 ไม้ ชนะ 38.9% สุทธิ -$88.67", "ไม่กรอง 15 นาที: 195 ไม้ ชนะ 37.4% สุทธิ -$98.21"],
      v=NE, src="engulf_watch/bt_week_20261017.md"),
 dict(t="MAE/MFE 7 ปี 62,599 สัญญาณ + ทดสอบ SL/TP", d="17 ต.ค. 2026", q="ถ้าตั้ง SL/TP จากสถิติ MAE/MFE จริง จะได้ระบบที่กำไรไหม",
      m="แบ่ง 70% แรกไว้ค้นหา 30% หลังเก็บไว้ทดสอบ ล็อก SL/TP (บันทึก hash) ก่อนเปิดดูช่วงทดสอบ SL $2.59 ลอง TP 4 ค่า",
      k=["ทุกคู่ SL/TP ขาดทุน ทั้งช่วงค้นหาและช่วงทดสอบ ทุกปี", "ก่อนหักต้นทุนเกือบเท่าทุน (ช่วงทดสอบ -$4 ถึง +$63)", "หลังหักต้นทุน: ช่วงทดสอบ -$2,431 ถึง -$3,311", "win rate ต่ำกว่าคุ้มทุน 4-6 จุด, PF 0.73-0.85", "ไม้แพ้ไม่ได้มี MAE ลึกกว่าไม้ชนะ (AUC 0.42) จึงตั้ง SL แยกไม่ได้"],
      v=NE, src="engulf_watch/maemfe/REPORT.md"),
]))

groups.append(("gold-pattern", "ทองคำ: ขุดรูปแบบ และโครงสร้าง SMC", [
 dict(t="ขุดรูปแบบแบบเห็นคำตอบก่อน (hindsight)", d="ราว 16 ต.ค. 2026", q="มีรูปแบบไหนชนะ 70% ขึ้นไปไหม ถ้าเลือกจากอดีตเต็มที่",
      m="ลอง 37,682 แบบ (วัน, เวลา, สีแท่ง, ขนาดแท่ง, high/low เมื่อวาน, EMA55) TP = SL = 1 ATR ค้นหาใน 70% แรก แล้วแช่แข็งไปทดสอบ 30% หลัง",
      k=["เจอแค่ 4 รูปแบบที่ชนะ ≥70% (รวม 0.35 สัญญาณต่อวัน)", "ช่วงค้นหา: ชนะ 71.6%", "ช่วงที่ไม่เคยเห็น: เหลือ 46.7% ขาดทุน -$27.7", "ชุด 4.5 สัญญาณต่อวัน: เหลือ 49.5% และ 49.9%"],
      v=NE, src="results/reports/XAU_HINDSIGHT_MINE_REPORT.md"),
 dict(t="ตัวอย่างสอน: การโกงด้วยการแอบดูอนาคต", d="16 ต.ค. 2026", q="ถ้าแอบดูอนาคตเพื่อตัดไม้แพ้ทิ้ง ผลจะดูดีแค่ไหน และของจริงเป็นอย่างไร",
      m="จงใจเลือกรูปแบบจาก 6 เดือนที่เทรนด์แรงที่สุด แล้วตัดไม้แพ้ทิ้ง (ผิดโดยตั้งใจ) เทียบกับการทดสอบแบบซื่อตรง",
      k=["แบบโกง: ชนะ 100% กำไร +$33.40 ไม่มีขาดทุนเลย", "แบบซื่อตรง: 372 ไม้ ชนะ 41.7% สุทธิ -$127.97 PF 0.19", "ห้ามเทรดรูปแบบนี้ เป็นแค่บทเรียน"],
      v=NE, src="results/reports/XAU_BIAS_DEMO_REPORT.md"),
 dict(t="รูปแบบคล้าย (fuzzy pattern) M5", d="16 ต.ค. 2026", q="จับคู่รูปแบบแบบหยาบๆ แล้วเทรดถี่ 4-5 ครั้งต่อวัน ได้ไหม",
      m="ลงทะเบียนกฎล่วงหน้า ค้นหาปี 2019-2022 ทดสอบ 2023 ถึง 9 ต.ค. 2025 ครั้งเดียว",
      k=["96 แบบในช่วงค้นหา ติดลบหมดในปี 2022", "ตัวสุดท้าย: 974 ไม้ -$0.33 ต่อไม้ PF 0.75 ติดลบทุกปี", "ต้นทุน $0.28-0.32 ต่อไม้ ใหญ่กว่าการเคลื่อนไหวที่ทายได้"],
      v=NE, src="results/reports/XAU_FUZZY_REPORT.md"),
 dict(t="โครงสร้าง SMC บน M5", d="ราว 16 ต.ค. 2026", q="BOS + ย่อ 30-70% + กวาด liquidity + แท่งยืนยัน (กลืนกิน / impulse / ChoCh) ใช้ได้ไหม",
      m="480 แบบ (zigzag 3 ค่า x ตัวกรอง 10 x การยืนยัน 4 x TP 4) ค้นหาก่อน 4 ต.ค. 2023 ทดสอบหลังจากนั้น",
      k=["ไม่มีแบบไหนกำไรในช่วงค้นหาเลย (0%)", "ก่อนหักต้นทุน ราว 0R (+0.001R ถึง -0.011R)", "ผลช่วงค้นหากับช่วงทดสอบไม่สัมพันธ์กัน (-0.05) = สุ่ม", "แบบที่ดีที่สุดในช่วงค้นหา: ช่วงทดสอบชนะ 39.2% คุ้มทุน 43.6%"],
      v=NE, src="results/reports/XAU_SMC_STRUCT_REPORT.md"),
 dict(t="โครงสร้าง SMC บน H1 / H4", d="ราว 16 ต.ค. 2026", q="ถ้าขึ้นไปกรอบใหญ่ ต้นทุนเทียบ R เล็กลง จะมีเอดจ์ไหม",
      m="กฎเดียวกับ M5 แต่ใช้ H1 และ H4 อีก 960 แบบ",
      k=["ต้นทุนเหลือแค่ 0.04R (H1) และ 0.02R (H4)", "แต่ก่อนหักต้นทุนยังราว 0R", "H4 zz3 บวกเล็กน้อยทั้ง 2 ช่วง แต่แค่ 86 + 39 ไม้ t ราว 0.6 = เสียงรบกวน", "H1 ช่วงลอนดอน (14-19 น.) บวกทั้ง 2 ช่วง ควรทดสอบใหม่แบบลงทะเบียนล่วงหน้า"],
      v=NE, src="results/reports/XAU_SMC_STRUCT_HTF_REPORT.md"),
 dict(t="CHoCH M5 (งานทีมเก่า)", d="5 ต.ค. 2026", q="เข้า limit ที่ย่อ 62% หลัง CHoCH, TP 2R ใช้ได้ไหม",
      m="ข้อมูล 1 ปี (ต.ค. 2025 ถึง ก.ย. 2026) คุ้มทุนที่ 2R = 33.3%",
      k=["70% แรก: ถึง TP 31.5% (-0.055R ต่อไม้)", "30% หลัง: 36.0% (+0.08R ต่อไม้)", "รวมๆ ราวเท่าทุน และข้อมูลแค่ 1 ปี"],
      v=NE, src="NOTES.md (choch-research)"),
]))

groups.append(("gold-other", "ทองคำ: ระบบอื่นที่ทดสอบ", [
 dict(t="EMA55 ย่อตัว M5", d="15 ต.ค. 2026", q="ย่อมาแตะ EMA55 แล้วเข้าตามเทรนด์ ใช้ได้ไหม",
      m="ลงทะเบียนล่วงหน้า walk-forward 72 แบบ ไม่แตะช่วงเก็บไว้ทดสอบ",
      k=["1,154 ไม้ PF 0.69 หลังต้นทุน (0.92 ก่อนต้นทุน)", "ทั้ง 72 แบบติดลบหลังต้นทุน"], v=NE, src="results/reports/XAU_EMA55_PB_REPORT.md"),
 dict(t="EMA55 กรอบใหญ่", d="15 ต.ค. 2026", q="ใช้กรอบใหญ่ขึ้นเพื่อลดต้นทุนต่อ R ช่วยไหม",
      m="ลงทะเบียนล่วงหน้า walk-forward อีก 30 แบบ",
      k=["306 ไม้ PF 0.93 (1.005 ก่อนต้นทุน)", "ต้นทุนลดจาก 0.17R เหลือ 0.04-0.11R แต่ไม่มีเอดจ์ก่อนต้นทุน"], v=NE, src="results/reports/XAU_EMA55_HTF_REPORT.md"),
 dict(t="เบรก swing high + อ่านกราฟเช้า 15 ต.ค.", d="15 ต.ค. 2026", q="ซื้อเมื่อทะลุ swing high ล่าสุด ได้ผลไหม",
      m="walk-forward 12 แบบ บนข้อมูล 2019-2025",
      k=["1,026 ไม้ PF 1.009 (+0.003R ต่อไม้) = เท่าทุน", "การอ่านกราฟเช้าวันนั้นไม่ใช่การอ่านแบบปิดตาจริง ใช้สรุปไม่ได้"], v=NE, src="results/reports/XAU_BLINDREAD_SWINGBO_REPORT.md"),
 dict(t="แท่งขยายตัวตอนเปิดตลาด (SOX)", d="15 ต.ค. 2026", q="หลังตลาดเงียบ แท่งใหญ่ตอนเปิดเซสชันจะวิ่งต่อไหม",
      m="ลงทะเบียนล่วงหน้า 2 รอบ 20 แบบ",
      k=["ทั้ง 20 แบบติดลบตั้งแต่ก่อนหักต้นทุน", "215 ไม้ -$0.53 ต่อไม้ PF 0.70"], v=NE, src="results/reports/XAU_SOX_REPORT.md"),
 dict(t="กรอบราคาต่อวัน (ADR)", d="15 ต.ค. 2026", q="ทองวิ่งวันละราว ADR คงที่ไหม เทรดตามได้ไหม",
      m="ดูสถิติก่อน แล้ว walk-forward 18 แบบ",
      k=["มีแค่ 36.8% ของวันที่อยู่ใน ±20% ของ ADR", "1,086 ไม้ PF 0.92 บวกแค่ 1 ใน 5 ปี"], v=NE, src="results/reports/XAU_ADR_REPORT.md"),
 dict(t="REB-H4 บนทองคำ", d="11 ต.ค. 2026", q="ระบบ range breakout + กรอบ H4 ใช้กับทองได้ไหม",
      m="ลงทะเบียนล่วงหน้า ทดสอบนอกตัวอย่างอิสระ",
      k=["382 ไม้ PF 1.026 (1.5x ต้นทุน 0.979) t = 0.14", "DD -23.7% บวก 4 ใน 7 ปี"], v=NE, src="results/reports/REB_H4_XAU_REPORT.md"),
 dict(t="ระบบแม่ปลาปากกาเขียว (แกนกลไก)", d="11 ต.ค. 2026", q="แกนกฎจากหนังสือ (Sig H1/H4, SL ที่ไส้, TP ระยะคงที่) ทำกำไรไหม",
      m="เขียนกฎตามหนังสือ ลงทะเบียนล่วงหน้า 2 แบบ ทดสอบ 2019-2025 และช่วงเก็บไว้ทดสอบ 1 ครั้ง",
      k=["H1: 2,762 ไม้ ชนะ 22.2% PF 0.87 พอร์ตแตก", "H4: 443 ไม้ PF 0.97 DD -53% (1% ต่อไม้)", "ก่อนต้นทุน H1 PF 1.06 ต้นทุนราว 0.1R ตัดสินผล", "ส่วนที่ต้องใช้ดุลยพินิจไม่ได้ทดสอบ"],
      v=NE, src="mae-pla/REPORT.md"),
 dict(t="ACME 8 ข้อ (เข้าอย่างเดียว SL ตายตัว)", d="11 ต.ค. 2026", q="ลำดับ 8 ข้อของผู้ใช้ เมื่อทำให้เป็นกฎตายตัว ใช้ได้ไหม",
      m="ลงทะเบียนล่วงหน้า 2 แบบ (M15/H4 และ H1/D1) ไม่มีการแก้ไม้",
      k=["สัญญาณน้อยมาก: 12 ไม้ใน 5 ปี (ต้องการ ≥300)", "PF 0.27 -0.62R ต่อไม้", "ระบบ ACME เต็มยังคลุมเครือเกินจะทดสอบ"],
      v=NE, src="acme-9step/REPORT.md"),
 dict(t="ค้นหาระบบทองรุ่นแรก (888 แบบ + ML)", d="4 ต.ค. 2026", q="มีกฎผสม 888 แบบ หรือ LightGBM ตัวไหนผ่านเกณฑ์ไหม",
      m="ข้อมูล ม.ค. 2024 ถึง ก.ย. 2026 เกณฑ์ PF ≥1.10 ทั้งช่วงทดสอบและช่วงเก็บ",
      k=["PF กลางก่อนต้นทุนราว 1.01", "ผ่าน 0 แบบ", "ML: ฝึก PF 1.36 แต่ทดสอบ 1.02 (overfit)"], v=NE, src="NOTES.md (xau_research)"),
]))

groups.append(("fx", "ฟอเร็กซ์และระบบรวมหลายคู่เงิน (11 ต.ค.)", [
 dict(t="Walk-forward 29 ระบบ x คู่เงิน", d="11 ต.ค. 2026", q="ระบบมาตรฐาน 6 ตระกูล บน 5 คู่ (รวมทอง) ผ่านเกณฑ์ไหม",
      m="Donchian, Asian MR, session breakout, Kaze, TSMOM, seasonality หักต้นทุน IC จริง",
      k=["ผ่าน 0 จาก 29", "ใกล้สุด: USDJPY NY breakout PF 1.26 แต่ DD -26% และ t 2.69 < 3.54", "ทอง: ต้นทุนราว $0.29 ต่อไม้ กลืนเอดจ์ระบบระยะสั้นหมด"],
      v=NE, src="REPORT.md"),
 dict(t="NYBO M15 ลงทะเบียนล่วงหน้า (คู่ใหม่)", d="11 ต.ค. 2026", q="ตัวที่เกือบผ่าน (NY breakout) ใช้ได้กับคู่เงินอื่นไหม",
      m="ทดสอบ 5 คู่ที่ไม่เคยใช้ กฎตายตัว",
      k=["PF รวม 0.904 ติดลบทุกปี 2021-2025", "ผ่าน 0 จาก 5 ข้อ"], v=NE, src="results/reports/NYBO_M15_4h_prereg_REPORT.md"),
 dict(t="Track 2: ตระกูลใหม่ 24 ตัว", d="11 ต.ค. 2026", q="ORB โตเกียว/แฟรงก์เฟิร์ต, London fix, ข่าว ฯลฯ ใช้ได้ไหม",
      m="walk-forward หลังต้นทุน", k=["ผ่าน 0 จาก 24", "ดีสุด: ทอง fix flow PF 1.03 (115 ไม้)"], v=NE, src="results/reports/TRACK2_SUMMARY.md"),
 dict(t="Track 3: เทคนิคบอทเดโม (T01/T06/T08/T15)", d="11 ต.ค. 2026", q="เทคนิคที่บอทเดโมใช้ ทำกำไรจริงไหม และกำไรในเดโมมาจากไหน",
      m="ทดสอบที่ความเสี่ยงคงที่ 1% และวิเคราะห์ประวัติดีลเดโม (ปรับทุกไม้เป็น lot คงที่)",
      k=["PF 0.61 ถึง 0.86 ทุกเทคนิค", "กำไรในเดโมมาจากการเพิ่ม lot หลังแพ้ (martingale)", "เช่น MCM1 +$340.60 ถ้า lot คงที่เป็น -$41.27"],
      v=NE, src="REPORT.md, results/kai_demo_analysis.md"),
 dict(t="Track A / Track B", d="11 ต.ค. 2026", q="ระบบกรอบใหญ่รวม 13 คู่ (A) และ M5 ฟอเร็กซ์ต้นทุนต่ำ (B) ผ่านไหม",
      m="walk-forward รวมหลายคู่", k=["Track A: ผ่าน 0 จาก 6 (PF 0.64-0.96)", "Track B: ผ่าน 0 จาก 12 ใกล้สุด USDJPY B2 PF 1.28 แต่ DD -31%"], v=NE, src="results/reports/TRACKA_REPORT.md, TRACKB_REPORT.md"),
 dict(t="USDJPY REB + REB-H4 คู่อื่น", d="11 ต.ค. 2026", q="range breakout + ตัวกรองกรอบใหญ่ ใช้ได้ไหม",
      m="ลงทะเบียนล่วงหน้า", k=["USDJPY: ไม่มีตัวผ่าน (V3 PF 1.56 แต่แค่ 207 ไม้)", "คู่อื่นรวม: 895 ไม้ PF 0.90 DD -98%"], v=NE, src="results/reports/USDJPY_REB_HTF_REPORT.md, REB_H4_XPAIR_REPORT.md"),
 dict(t="ตรวจข้อมูล Dukascopy เทียบ IC Markets", d="11 ต.ค. 2026", q="ข้อมูลฟรีที่เราใช้ ต่างจากราคา IC มากไหม",
      m="เทียบแท่ง M5 ทีละแท่งก่อน 10 ต.ค. 2025",
      k=["เวลาตรงกัน ไม่มีเลื่อนชั่วโมง", "ทอง: ราคา bid IC ต่างจาก mid Dukascopy แค่ -$0.04", "สหสัมพันธ์ผลตอบแทน 5 นาที 0.976-0.996"],
      v=PS, src="results/dukascopy_vs_ic.md"),
]))

groups.append(("iq", "IQ Option (ออปชันระยะสั้น บัญชี PRACTICE)", [
 dict(t="บันทึกพื้นฐาน IQ Blitz 1 นาที", d="1 ต.ค. 2026", q="ต้องชนะกี่ % ถึงคุ้ม และมีงานวิจัยไหนยืนยันว่าชนะได้",
      m="สรุปงานวิจัยและข้อมูลหน่วยงานกำกับ", k=["payout 91% ต้องชนะ 52.36%", "ESMA พบบัญชีรายย่อย 74-87% ขาดทุน", "martingale ไม่เปลี่ยนค่าคาดหวัง"], v=EX, src="/workspace/iq_research.md"),
 dict(t="ค้นหาเทคนิค 6 คู่เงิน 1-5 นาที", d="4 ต.ค. 2026", q="มีเทคนิคไหนชนะเกิน 56% ทุกคู่ไหม",
      m="31 กฎ x 4 expiry + spike fade 240 แบบ ทดสอบปี 2025 ด้วย", k=["ผ่าน 0 แบบ", "spike fade ปี 2025 ได้ 53.3-53.9% ต่ำกว่าคุ้มทุน 54.05%", "ทุกแบบเคยแพ้ติด 8-17 ไม้"], v=NE, src="/workspace/iq_tech_search/REPORT.md"),
 dict(t="IQ ระยะสั้น + walk-forward (spike fade)", d="11 ต.ค. 2026", q="กฎไหนชนะเกินจุดคุ้มทุน 54.35% จริงนอกตัวอย่าง",
      m="ราว 1,880 แบบ walk-forward รายไตรมาส ข้อมูล 2024 ถึง ต.ค. 2026 ทดสอบความหน่วงเวลาเข้าด้วยข้อมูล 1 วินาที",
      k=["กฎที่ใช้ทดสอบอยู่ตอนนั้นแพ้: 52.3% และ 51.3%", "spike fade (แท่ง > 4 ATR เข้าสวน): 58.1% นอกตัวอย่าง (5,315 ไม้) 8 ใน 8 ไตรมาส", "แต่ถ้าเข้าช้า 7-8 วินาที เหลือราว 54-55% = เท่าทุน", "ครึ่งหลังปี 2024 ต่ำกว่าคุ้มทุน"],
      v=PR, src="/workspace/iq-research/REPORT.md"),
 dict(t="Blitz 1 นาที 7,488 แบบ", d="ต้น ต.ค. 2026 (ไม่ระบุวันในไฟล์)", q="ช่วงเวลาไหน กฎไหน ชนะเกิน 54.1%",
      m="208 กฎ x 9 ช่วงเวลา x 4 ระดับความผันผวน + ML", k=["ช่วงตลาดปกติ: ไม่มีกฎผ่าน (50-53%)", "ML: 62% ในตัวอย่าง เหลือ 49-51%", "ช่วง rollover (04:00-04:59 น. ไทย) RSI2: 60.8% นอกตัวอย่าง แต่ยังไม่ยืนยันกับราคา IQ"], v=PR, src="/workspace/iq_research2/report.md"),
 dict(t="รอบ 3: expiry 5 นาที", d="ต้น ต.ค. 2026 (ไม่ระบุวันในไฟล์)", q="5 เทคนิค 47 แบบ ผ่าน 53.5% ไหม",
      m="ค้นหา เม.ย.-ก.ค. 2026 ทดสอบ ส.ค.-ก.ย. 2026 + ปี 2025 + คู่อื่น", k=["ไม่มีเทคนิคผ่านอย่างมั่นคง (ส่วนใหญ่ 48-52%)", "วิธี EMA26 pullback (T1): 48-50% แพ้ติดยาวสุด 7-13 ไม้"], v=NE, src="/workspace/iq_research3/report.md"),
 dict(t="รอบ 4: แพ้ติดกัน และตัวกรองห้ามเข้า", d="ต้น ต.ค. 2026 (ไม่ระบุวันในไฟล์)", q="การแพ้ติดกันเกิดบ่อยผิดปกติไหม กรองได้ไหม",
      m="36 ชุด (6 เทคนิค x 6 ช่วงข้อมูล)", k=["แพ้ติดกันเกิดเท่ากับการสุ่ม", "ไม่มีปัจจัยไหนแยกไม้แพ้ได้ (|ρ| ≤ 0.06)", "ไม่มีตัวกรองไหนลดแพ้ติดยาวสุดเหลือ ≤4 ไม้"], v=NE, src="/workspace/iq_research4/report.md"),
 dict(t="รอบ 5: martingale 3 ไม้ เทียบ 1% คงที่", d="ต้น ต.ค. 2026 (ไม่ระบุวันในไฟล์)", q="martingale ช่วยให้กำไรมากขึ้นไหม",
      m="228 เคส เริ่ม $10,000", k=["martingale ชนะ 1% คงที่แค่ 40 จาก 228 เคส", "พอร์ตแตก: martingale 114 เคส, 1% คงที่ 79 เคส", "ผลต่อเงินที่ลงเกือบเท่ากัน (-7.3% กับ -6.9%)"], v=NE, src="/workspace/iq_research5/report.md"),
 dict(t="EUR/USD 1 นาที: colorbig / round", d="ต้น ต.ค. 2026 (ไม่ระบุวันในไฟล์)", q="ตามสีแท่งใหญ่ หรือเลขกลม ชนะเกิน 53.5% ไหม",
      m="158 วันเทรด 188k แท่ง", k=["colorbig ตามสี: 48-49%", "roundbreak: 45.6%", "roundfade5: 49.9% (โยนเหรียญ)"], v=NE, src="/workspace/iq_fast/backtest/results.md"),
]))

# ---------------------------------------------------------------- HTML pieces
def card(s):
    li = "".join(f"<li>{E(x)}</li>" for x in s["k"])
    return f'''<article class="card" data-v="{s['v']}">
<div class="card-top"><span class="badge b-{s['v']}">{BADGE[s['v']]}</span><span class="date">{E(s['d'])}</span></div>
<h3>{E(s['t'])}</h3>
<p><b>คำถาม:</b> {E(s['q'])}</p>
<p><b>วิธี:</b> {E(s['m'])}</p>
<div class="nums"><b>ตัวเลขสำคัญ</b><ul>{li}</ul></div>
<p class="src">ที่มา: {E(s['src'])}</p>
</article>'''

counts = {NE: 0, PR: 0, PS: 0, EX: 0}
sections = []
for gid, gtitle, studies in groups:
    for s in studies: counts[s["v"]] += 1
    sections.append(f'<section class="grp" id="{gid}"><h2 class="gh">{E(gtitle)}</h2><div class="grid">' + "".join(card(s) for s in studies) + "</div></section>")
total = sum(counts.values())

timeline = [
 ("1 ต.ค.", "IQ Option: บันทึกพื้นฐาน จุดคุ้มทุน 52.36% ที่ payout 91%"),
 ("ต้น ต.ค.", "IQ Option: รอบ 2 ถึง 5 และ EUR/USD 1 นาที (ไฟล์ไม่ระบุวันแน่ชัด)"),
 ("4 ต.ค.", "ทอง: ค้นหารุ่นแรก 888 แบบ + ML / IQ: ค้นหาเทคนิค 6 คู่"),
 ("5 ต.ค.", "ทอง: CHoCH M5 (งานทีมเก่า)"),
 ("11 ต.ค.", "วันใหญ่: walk-forward 29 ระบบ, NYBO, Track 2/3/A/B, REB-H4, แม่ปลาฯ, ACME, IQ spike fade, ตรวจข้อมูล IC"),
 ("15 ต.ค.", "ทอง: EMA55, swing breakout, SOX, ADR, สแกนแท่งกลืนกินวันที่ 15"),
 ("16 ต.ค.", "ตัวอย่างสอนเรื่องโกงอนาคต, fuzzy pattern แล้วต่อด้วย (ราว 16 ต.ค.) ขุดรูปแบบ hindsight, SMC M5/H1/H4, ปิดทะลุ TP $5, MFE/MAE, SL $2 / TP $5"),
 ("12-17 ต.ค.", "เฝ้าสัญญาณแท่งกลืนกินสด (ไม่ส่งคำสั่ง) 197 สัญญาณ"),
 ("17 ต.ค.", "ทดสอบย้อนหลัง 1 สัปดาห์ 4 แบบ (09:48 น.) และ MAE/MFE 7 ปี 62,599 สัญญาณ (13:29 น.)"),
]
tl = "".join(f'<li><span class="tld">{E(a)}</span><span>{E(b)}</span></li>' for a, b in timeline)

c_be = chart_breakeven()
c_mm = chart_diverging([
    ("SL 2.59 / TP 2.19 ช่วงค้นหา", -1093, -6696), ("SL 2.59 / TP 2.19 ช่วงทดสอบ", -4, -3311),
    ("SL 2.59 / TP 3.74 ช่วงค้นหา", -514, -5215), ("SL 2.59 / TP 3.74 ช่วงทดสอบ", 3, -2786),
    ("SL 2.59 / TP 3.82 ช่วงค้นหา", -525, -5195), ("SL 2.59 / TP 3.82 ช่วงทดสอบ", 16, -2760),
    ("SL 2.59 / TP 5.74 ช่วงค้นหา", -314, -4548), ("SL 2.59 / TP 5.74 ช่วงทดสอบ", 63, -2431),
], 6696, "หน่วย: ดอลลาร์รวม ที่ 0.01 lot ต่อไม้ ช่วงค้นหา 2019 ถึง ก.ย. 2023, ช่วงทดสอบ ก.ย. 2023 ถึง 9 ต.ค. 2025 ที่มา: engulf_watch/maemfe/REPORT.md", "กำไรก่อนและหลังต้นทุน 7 ปี")
c_wk = chart_diverging([
    ("ENG5 ไม่กรอง ถือ 5 นาที (213 ไม้)", -14.33, -73.97),
    ("SMA21 ถือ 5 นาที (139 ไม้)", -28.21, -67.13),
    ("MAIN SMA21 15 นาที + ออกก่อน (131 ไม้)", -52.0, -88.67),
    ("ไม่กรอง 15 นาที + ออกก่อน (195 ไม้)", -43.61, -98.21),
], 98.21, "หน่วย: ดอลลาร์รวม ที่ 0.01 lot สัปดาห์ 12-17 ต.ค. 2026 ที่มา: engulf_watch/bt_week_20261017.md", "กำไรก่อนและหลังต้นทุน 1 สัปดาห์")
c_hs = chart_hindsight()
c_curve = chart_be_curve()

CSS = r"""
:root{--bg:#0e1119;--card:#161b27;--line:#262e40;--tx:#e6e9ef;--mut:#9aa4b8;--acc:#f5a524;--red:#ff5d73;--grn:#5ad19a;--yel:#ffd166;--blu:#7aa2ff}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--tx);font-family:Sarabun,"Noto Sans Thai","Leelawadee UI",Tahoma,sans-serif;font-size:17px;line-height:1.65}
a{color:var(--blu)}
.wrap{max-width:1100px;margin:0 auto;padding:0 16px}
nav{position:sticky;top:0;z-index:5;background:rgba(14,17,25,.94);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
nav .wrap{display:flex;gap:6px;overflow-x:auto;padding:10px 16px;white-space:nowrap;scrollbar-width:none}
nav a{color:var(--mut);text-decoration:none;font-size:15px;padding:5px 11px;border:1px solid var(--line);border-radius:999px}
nav a:hover{color:var(--tx);border-color:var(--acc)}
.hero{padding:44px 0 26px}
.kicker{color:var(--acc);font-weight:700;letter-spacing:.3px;font-size:15px}
.hero h1{font-size:clamp(26px,5.4vw,42px);line-height:1.3;margin:8px 0 14px}
.hero h1 em{color:var(--red);font-style:normal}
.hero p.sub{color:var(--tx);font-size:clamp(18px,3.4vw,22px);font-weight:600}
.hero p{color:var(--mut);margin:6px 0;max-width:820px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:22px 0 4px}
.stat{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px}
.stat b{display:block;font-size:26px;color:var(--acc);line-height:1.2}
.stat span{color:var(--mut);font-size:14px}
.demo{display:inline-block;margin-top:14px;background:#1f2a1f;border:1px solid #2f5a3a;color:#9fe0b4;padding:6px 12px;border-radius:10px;font-size:15px}
section{padding:26px 0}
h2{font-size:clamp(22px,4vw,30px);margin:0 0 14px}
h2.gh{font-size:clamp(19px,3.4vw,24px);border-left:4px solid var(--acc);padding-left:10px}
.tl{list-style:none;margin:0;padding:0;border-left:2px solid var(--line)}
.tl li{position:relative;padding:8px 0 12px 22px;display:flex;flex-direction:column}
.tl li:before{content:"";position:absolute;left:-7px;top:15px;width:12px;height:12px;border-radius:50%;background:var(--acc)}
.tld{font-weight:700;color:var(--acc)}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:4px 0 6px}
.filters button{background:var(--card);color:var(--tx);border:1px solid var(--line);border-radius:999px;padding:7px 13px;font:inherit;font-size:15px;cursor:pointer}
.filters button.on{border-color:var(--acc);color:var(--acc)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 16px 12px;display:flex;flex-direction:column}
.card h3{margin:8px 0 8px;font-size:19px;line-height:1.4}
.card p{margin:4px 0;font-size:16px}
.card-top{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
.date{color:var(--mut);font-size:14px}
.badge{font-size:14px;font-weight:700;padding:3px 10px;border-radius:999px}
.b-ne{background:#3a1820;color:#ff8b9a;border:1px solid #6b2a37}
.b-pr{background:#3a2f12;color:var(--yel);border:1px solid #6b5520}
.b-ps{background:#13341f;color:var(--grn);border:1px solid #23613a}
.b-ex{background:#232a3a;color:#b8c2d6;border:1px solid #3a4560}
.nums{background:#11151f;border-radius:10px;padding:8px 12px;margin:8px 0;font-size:16px}
.nums ul{margin:4px 0 0;padding-left:20px}.nums li{margin:2px 0}
.src{color:#6f7a90;font-size:13px;margin-top:auto!important;padding-top:6px;word-break:break-all}
.chart{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px;margin:0 0 16px}
.chart h3{margin:0 0 6px;font-size:19px}
.chart .lead{color:var(--mut);margin:0 0 10px;font-size:16px}
.chart svg{width:100%;max-width:640px;height:auto;display:block;margin:0 auto}
.note{color:#6f7a90;font-size:13px;margin:8px 0 0}
.lesson{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px;margin-bottom:12px}
.lesson h3{margin:0 0 6px;font-size:19px;color:var(--acc)}
.formula{font-size:clamp(18px,3.6vw,24px);background:#11151f;border-radius:10px;padding:12px;text-align:center;margin:10px 0;font-weight:700}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.steps{counter-reset:s;list-style:none;padding:0;margin:0}
.steps li{counter-increment:s;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 14px 14px 58px;margin-bottom:10px;position:relative}
.steps li:before{content:counter(s);position:absolute;left:14px;top:14px;width:32px;height:32px;border-radius:50%;background:var(--acc);color:#1a1300;font-weight:800;display:flex;align-items:center;justify-content:center}
dl.gl{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;margin:0}
dl.gl div{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:12px 14px}
dl.gl dt{font-weight:800;color:var(--acc)}dl.gl dd{margin:4px 0 0;color:var(--tx);font-size:16px}
footer{color:#6f7a90;font-size:14px;padding:30px 0 50px;border-top:1px solid var(--line);margin-top:20px}
@media (max-width:520px){body{font-size:16px}.grid{grid-template-columns:1fr}.card{padding:14px}}
"""

JS = r"""
document.querySelectorAll('.filters button').forEach(function(b){b.addEventListener('click',function(){
 document.querySelectorAll('.filters button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
 var f=b.getAttribute('data-f');document.querySelectorAll('.card').forEach(function(c){c.style.display=(f==='all'||c.getAttribute('data-v')===f)?'':'none'});
});});
"""

page = f"""<!DOCTYPE html>
<html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>สรุปงานวิจัยเทรด สำหรับส้มน้อย</title><style>{CSS}</style></head><body>
<nav><div class="wrap">
<a href="#top">สรุป</a><a href="#timeline">ไทม์ไลน์</a><a href="#studies">ทุกงานวิจัย</a><a href="#charts">กราฟ</a><a href="#lessons">บทเรียน</a><a href="#next">ขั้นต่อไป</a><a href="#glossary">คำศัพท์</a>
</div></nav>
<header class="hero" id="top"><div class="wrap">
<div class="kicker">สรุปงานวิจัยเทรด สำหรับส้มน้อย (อัปเดต 17 ต.ค. 2026)</div>
<h1>สรุปสั้นๆ: <em>ยังไม่มีกฎไหนชนะตลาดได้จริงหลังหักต้นทุน</em></h1>
<p class="sub">แท่งกลืนกินทอง M5 ก่อนหักต้นทุนแค่เสมอตัว ค่าใช้จ่ายราว $0.28 ต่อไม้ (0.01 lot) คือส่วนที่ทำให้ขาดทุนเกือบทั้งหมด</p>
<p>ทองคำ XAUUSD กราฟ 5 นาทีเป็นหลัก ข้อมูลราคาฟรีจาก Dukascopy (ตรวจแล้วว่าใกล้ราคา IC Markets มาก) ต้นทุนใช้ตัวเลขจริงของ IC Markets: ราว $0.28 ต่อ 0.01 lot ต่อไม้</p>
<p>ทุกอย่างในหน้านี้เป็นการทดสอบย้อนหลังหรือบัญชีเดโมเท่านั้น ไม่มีการเทรดเงินจริง</p>
<div class="stats">
<div class="stat"><b>{total}</b><span>งานวิจัยในหน้านี้</span></div>
<div class="stat"><b>0</b><span>ระบบเทรดที่ผ่านเกณฑ์</span></div>
<div class="stat"><b>925</b><span>ชุดกฎที่บันทึกการทดสอบ (ไม่รวมการขุดรูปแบบ)</span></div>
<div class="stat"><b>62,599</b><span>สัญญาณแท่งกลืนกิน 7 ปีที่วัดผล</span></div>
<div class="stat"><b>51.6%</b><span>สัญญาณสดสัปดาห์นี้ไปถูกทาง (เหมือนโยนเหรียญ)</span></div>
</div>
<span class="demo">บริบท: บัญชีเดโม IC Markets MT5 และ IQ Option PRACTICE เท่านั้น</span>
</div></header>

<main class="wrap">
<section id="timeline"><h2>ไทม์ไลน์งานวิจัย (ปี 2026)</h2><ul class="tl">{tl}</ul>
<p class="note">วันที่มาจากบันทึกการทดสอบ (results/trials.csv), STATUS.md และหัวรายงาน รายการที่เขียนว่า "ราว" คือเรียงตามลำดับจำนวนการทดสอบสะสม เพราะไฟล์ไม่ได้บอกเวลาตรงๆ</p></section>

<section id="studies"><h2>ทุกงานวิจัย ({total} เรื่อง)</h2>
<p style="color:var(--mut);margin-top:0">กดปุ่มเพื่อกรองตามผล: ไม่มีเอดจ์ {counts[NE]} เรื่อง, มีแววแต่ยังไม่พอ {counts[PR]} เรื่อง, ผ่าน {counts[PS]} เรื่อง (เป็นการตรวจข้อมูล ไม่ใช่ระบบเทรด), แค่สำรวจ {counts[EX]} เรื่อง</p>
<div class="filters"><button class="on" data-f="all">ทั้งหมด</button><button data-f="ne">ไม่มีเอดจ์</button><button data-f="pr">มีแววแต่ยังไม่พอ</button><button data-f="ps">ผ่าน</button><button data-f="ex">แค่สำรวจ</button></div>
{''.join(sections)}
</section>

<section id="charts"><h2>กราฟ (สร้างจากตัวเลขจริงในรายงาน)</h2>
<div class="chart"><h3>1. ชนะจริง เทียบ จุดคุ้มทุน</h3><p class="lead">win rate สูงหรือต่ำไม่สำคัญ ที่สำคัญคือแท่งสีส้มต้องยาวเกินเส้นแดง ทุกแถวยังไม่ถึงเส้นแดง</p>{c_be}<p class="note">ที่มา: XAU_SL2_TP5_REPORT.md, XAU_CLOSEBREAK_TP5_REPORT.md, engulf_watch/maemfe/REPORT.md, XAU_SMC_STRUCT_REPORT.md</p></div>
<div class="chart"><h3>2. ก่อนหักต้นทุน เทียบ หลังหักต้นทุน (7 ปี 62,599 สัญญาณ)</h3><p class="lead">แท่งเขียว (ก่อนต้นทุน) แทบเป็นศูนย์ แท่งแดง (หลังต้นทุน) ติดลบหลายพันดอลลาร์ แปลว่าต้นทุน $0.28 ต่อไม้คือที่มาของการขาดทุนเกือบทั้งหมด</p>{c_mm}</div>
<div class="chart"><h3>3. สัปดาห์ 12-17 ต.ค.: ก่อนและหลังต้นทุน 4 แบบ</h3><p class="lead">ทุกแบบติดลบตั้งแต่ก่อนหักต้นทุน และต้นทุนทำให้ลบมากขึ้นอีก (ข้อมูลแค่ 1 สัปดาห์ ใช้ดูภาพรวมเท่านั้น)</p>{c_wk}</div>
<div class="chart"><h3>4. ขุดรูปแบบจากอดีต: ช่วงที่เห็นแล้ว เทียบ ช่วงที่ไม่เคยเห็น</h3><p class="lead">รูปแบบที่ดูชนะ 70% ร่วงเหลือต่ำกว่า 50% เมื่อเจอข้อมูลใหม่</p>{c_hs}<p class="note">ที่มา: results/reports/XAU_HINDSIGHT_MINE_REPORT.md (ลองทั้งหมด 37,682 แบบ)</p></div>
</section>

<section id="lessons"><h2>บทเรียนที่ได้</h2>
<div class="lesson"><h3>1. win rate ขึ้นกับ TP/SL ไม่ใช่ตัววัดฝีมือ</h3>
<p>ตั้ง TP ใกล้ SL ไกล จะชนะบ่อย ตั้ง TP ไกล SL ใกล้ จะชนะน้อย แต่จุดคุ้มทุนก็ขยับตามเสมอ</p>
<div class="formula">จุดคุ้มทุน = SL ÷ (SL + TP)</div>
<p>รวมต้นทุนด้วย: (SL + ต้นทุน) ÷ (TP + SL) เช่น SL $2 TP $5 ต้นทุน $0.28 = 2.28 ÷ 7 = <b>32.6%</b> แต่ระบบชนะจริง 31.5% จึงขาดทุน</p>
<div class="chart" style="margin-top:10px">{c_curve}</div></div>
<div class="two">
<div class="lesson"><h3>2. ลองหลายแบบ ต้องเจอ "ผู้ชนะปลอม"</h3><p>ลอง 37,682 แบบ ย่อมมีบางแบบดูชนะ 70% โดยบังเอิญ (รายงานประเมินราว 2-3% ของกลุ่มเล็ก) พอเจอข้อมูลใหม่ก็กลับมาราว 50% ยิ่งลองมาก ยิ่งต้องมีหลักฐานแรงขึ้น (ตอนนี้ลองไป 925 ชุดในบันทึก เกณฑ์ Bonferroni z ราว 3.87)</p></div>
<div class="lesson"><h3>3. ต้องล็อกข้อมูลทดสอบไว้ก่อน</h3><p>แบ่งข้อมูล: ส่วนแรกไว้ค้นหา ส่วนหลังล็อกไว้ ห้ามแอบดู ตั้งกฎและจดลงไฟล์ (พร้อม hash) ก่อนเปิดดูส่วนที่ล็อก ข้อมูลตั้งแต่ 10 ต.ค. 2025 ยังเก็บไว้ ไม่ได้ใช้ (ยกเว้นงานแม่ปลาฯ และ ACME ที่ใช้ไปแล้ว 1 ครั้ง)</p></div>
<div class="lesson"><h3>4. ต้นทุนคือศัตรูของการเทรดถี่</h3><p>ทอง M5 ราคาวิ่งเฉลี่ยแค่ไม่กี่ดอลลาร์ ต้นทุน $0.28 ต่อไม้ (spread + ค่าคอม + slippage) กินกำไรทั้งหมด เทรด 35 ครั้งต่อวันยิ่งจ่ายต้นทุนมาก กรอบใหญ่ (H1/H4) ต้นทุนเทียบ R เล็กลง แต่ก็ยังไม่เจอเอดจ์</p></div>
<div class="lesson"><h3>5. martingale ไม่สร้างกำไร</h3><p>กำไรในบัญชีเดโมของบอทมาจากการเพิ่ม lot หลังแพ้ ถ้าใช้ lot คงที่ 4 ใน 5 เทคนิคติดลบ งาน IQ รอบ 5 ก็พบว่า martingale แค่ขยายความผันผวน และทำให้พอร์ตแตกบ่อยขึ้น</p></div>
</div></section>

<section id="next"><h2>ขั้นต่อไป</h2><ol class="steps">
<li><b>ใช้แท่งกลืนกินเป็นแค่ "จังหวะเข้า" หลังกรองด้วย H1</b><br>แท่งกลืนกินเดี่ยวๆ ไม่มีเอดจ์ ให้ดูทิศ H1 ก่อน แล้วรอแท่งกลืนกิน M5 ทางเดียวกัน ตัวกรอง H1 แบบที่เราลองแล้ว (BOS + ย่อ 40-60%) ยังไม่ผ่าน จึงต้องเขียนกฎ H1 ของส้มน้อยเองให้ชัด แล้วลงทะเบียนล่วงหน้าก่อนทดสอบ</li>
<li><b>ทดสอบกับข้อมูลที่ล็อกไว้แค่ครั้งเดียว</b><br>ตั้งกฎ ตั้ง SL/TP และเกณฑ์ผ่านให้เสร็จก่อน แล้วค่อยเปิดข้อมูลที่ล็อกไว้ ถ้าไม่ผ่านก็ถือว่าไม่ผ่าน ห้ามปรับกฎแล้วลองใหม่บนข้อมูลชุดเดิม</li>
<li><b>จดบันทึกการเทรดมือ (journal) ในบัญชีเดโม</b><br>ทุกไม้จด: เวลา, ทิศ H1, เหตุผลที่เข้า, SL, TP, ผลลัพธ์, MAE/MFE ถ้าดูได้ ใช้ lot คงที่ ไม่เพิ่ม lot หลังแพ้ เมื่อได้หลายร้อยไม้จะเห็นว่าดุลยพินิจของเราดีกว่ากฎตายตัวไหม</li>
<li><b>คิดต้นทุนทุกครั้ง</b><br>ก่อนเชื่อผลทดสอบใด ถามเสมอว่า "หลังหัก $0.28 ต่อไม้แล้วยังกำไรไหม" และ win rate เกินจุดคุ้มทุนของ TP/SL นั้นหรือยัง</li>
</ol></section>

<section id="glossary"><h2>คำศัพท์</h2><dl class="gl">
<div><dt>MAE (Maximum Adverse Excursion)</dt><dd>ระยะที่ราคาวิ่ง "สวน" เราไกลที่สุดระหว่างถือไม้ ใช้ช่วยคิดว่า SL ควรห่างแค่ไหน</dd></div>
<div><dt>MFE (Maximum Favorable Excursion)</dt><dd>ระยะที่ราคาวิ่ง "ไปทาง" เราไกลที่สุดระหว่างถือไม้ ใช้ช่วยคิดว่า TP ควรอยู่ตรงไหน</dd></div>
<div><dt>Holdout (ข้อมูลที่ล็อกไว้)</dt><dd>ข้อมูลส่วนที่เก็บไว้ ห้ามดูระหว่างค้นหากฎ ใช้ทดสอบจริงครั้งเดียวตอนท้าย เหมือนข้อสอบที่ยังไม่เคยเห็น</dd></div>
<div><dt>PF (Profit Factor)</dt><dd>กำไรรวม ÷ ขาดทุนรวม มากกว่า 1 คือกำไร น้อยกว่า 1 คือขาดทุน เกณฑ์ของเราต้องการ 1.2 ขึ้นไป</dd></div>
<div><dt>R:R (Risk : Reward)</dt><dd>เสี่ยงเท่าไร ได้เท่าไร เช่น SL $2 TP $5 คือ 1 : 2.5 ส่วน "R" คือหน่วยของความเสี่ยง 1 ไม้ (1R = ระยะ SL)</dd></div>
<div><dt>จุดคุ้มทุน (Breakeven win rate)</dt><dd>win rate ขั้นต่ำที่ทำให้ไม่ขาดทุน = SL ÷ (SL + TP) บวกผลของต้นทุน</dd></div>
<div><dt>In-sample / Out-of-sample</dt><dd>ข้อมูลที่ใช้ค้นหากฎ / ข้อมูลที่ไม่ได้ใช้ค้นหา ใช้ตรวจว่ากฎยังได้ผลไหม</dd></div>
<div><dt>Gross / Net</dt><dd>กำไรก่อนหักต้นทุน / กำไรหลังหักต้นทุน (spread ค่าคอม slippage)</dd></div>
<div><dt>Walk-forward</dt><dd>ค้นหากฎในช่วงหนึ่ง แล้วทดสอบช่วงถัดไป เลื่อนไปเรื่อยๆ เหมือนเทรดจริงที่ไม่รู้อนาคต</dd></div>
<div><dt>ลงทะเบียนล่วงหน้า (Pre-registration)</dt><dd>จดกฎและเกณฑ์ผ่านลงไฟล์ล็อกก่อนทดสอบ เพื่อกันการแก้กฎหลังเห็นผล</dd></div>
<div><dt>แท่งกลืนกิน T1 / T2 (แบบปิดทะลุ)</dt><dd>ซื้อ T1: แท่งก่อนเป็นแท่งแดง แท่งเขียวปิดเหนือ high ของแท่งนั้น ซื้อ T2: 2 แท่งก่อนเป็นแท่งแดง แท่งเขียวปิดเหนือ high สูงสุดของ 2 แท่ง ขายกลับด้าน</dd></div>
<div><dt>Martingale</dt><dd>เพิ่มขนาดไม้หลังแพ้เพื่อเอาคืน ทำให้ดูกำไรบ่อย แต่เสี่ยงพอร์ตแตกเมื่อแพ้ติดกันยาว</dd></div>
</dl></section>
</main>
<footer><div class="wrap">หน้านี้สรุปจากไฟล์รายงานใน /workspace/fx-research และโฟลเดอร์งาน IQ บน workspace ตัวเลขทุกตัวคัดลอกจากรายงาน ไม่ได้คำนวณใหม่ ยกเว้นสัดส่วนสัญญาณสด 99/192 ที่นับจาก signals.csv และเส้นจุดคุ้มทุนในบทเรียนข้อ 1 ที่คำนวณจากสูตร ไม่ใช่คำแนะนำการลงทุน</div></footer>
<script>{JS}</script></body></html>"""

open(OUT, "w", encoding="utf-8").write(page)
print("written", len(page), "bytes;", total, "studies", counts)
