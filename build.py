# -*- coding: utf-8 -*-
# Builds the v2 site: a short landing page (index.html) plus one page per topic.
# Study facts live in data.py (copied verbatim from v1). v1 is kept in old/ for rollback.
import html, os
import data, charts as C
C.TSCALE = 1.12
E = html.escape
D = os.path.dirname(os.path.abspath(__file__))
NE, PR, PS, EX = data.NE, data.PR, data.PS, data.EX
G = {gid: studies for gid, _, studies in data.groups}

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Pridi:wght@400;600&family=Sarabun:wght@400;600&family=Sriracha&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">')

CSS = r"""
:root{--paper:#f7f3ea;--paper2:#efe8da;--ink:#24211c;--mut:#5b554b;--soft:#7a7366;--rule:#d9d1c0;--acc:#b03a1f;--pen:#22507f;--gross:#6f8a5e}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.75 Sarabun,"Noto Sans Thai",Tahoma,sans-serif}
a{color:var(--pen);text-underline-offset:3px;text-decoration-thickness:1px}
.mono,.num{font-family:"IBM Plex Mono",ui-monospace,monospace}
h1,h2,h3,.head{font-family:Pridi,"Noto Serif Thai",serif;font-weight:600;line-height:1.35}
.page{max-width:1080px;margin:0 auto;padding:0 20px}
.top{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding:18px 0 10px;border-bottom:1px solid var(--ink);font-size:15px}
.top .brand{font-family:Pridi,serif;font-weight:600;color:var(--ink);text-decoration:none}
.top .stamp{color:var(--mut)}
.note{font-family:Sriracha,cursive;color:var(--pen);font-size:19px;line-height:1.45}
/* landing */
.intro{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,3fr);gap:40px;padding:44px 0 26px;
  background-image:linear-gradient(var(--rule) 1px,transparent 1px);background-size:100% 34px;background-position:0 33px}
.intro h1{font-size:clamp(28px,4.6vw,46px);margin:0 0 18px;max-width:17em}
.intro h1 .hl{background:linear-gradient(transparent 62%,#f0c9a9 62%)}
.intro p{margin:0 0 12px;max-width:38em;background:var(--paper)}
.intro .side{align-self:end;transform:rotate(-1.5deg);border-left:2px solid var(--pen);padding:4px 0 4px 14px;background:var(--paper)}
.ledger{display:flex;flex-wrap:wrap;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);margin:6px 0 38px}
.ledger div{padding:12px 22px 12px 0;margin-right:22px;border-right:1px solid var(--rule)}
.ledger div:last-child{border-right:0}
.ledger b{display:block;font:600 26px/1.2 "IBM Plex Mono",monospace}
.ledger span{font-size:14px;color:var(--mut)}
.ledger .red b{color:var(--acc)}
.toc-h{display:flex;align-items:baseline;gap:16px;margin:0 0 6px}
.toc-h h2{font-size:26px;margin:0}
.toc-h p{margin:0;color:var(--mut);font-size:15px}
.toc{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));column-gap:28px}
.entry{display:block;color:inherit;text-decoration:none;border-top:1px solid var(--ink);padding:16px 0 22px;grid-column:span 2}
.entry.w4{grid-column:span 4}.entry.w3{grid-column:span 3}
.entry .n{font:600 13px "IBM Plex Mono",monospace;color:var(--soft)}
.entry h3{font-size:21px;margin:2px 0 6px}
.entry:hover h3,.entry:focus h3{text-decoration:underline;text-decoration-color:var(--acc);text-underline-offset:5px}
.entry p{margin:0 0 10px;font-size:16px;color:#3a362f}
.entry .k{font:600 15px "IBM Plex Mono",monospace}
.entry .k em{font-style:normal;color:var(--acc)}
.entry .meta{font-size:14px;color:var(--mut);margin-top:6px}
.entry svg,.entry svg.chart{display:block;width:auto;max-width:100%;height:auto;margin:6px 0 8px}
.entry.main{display:grid;grid-template-columns:minmax(0,1fr) 220px;column-gap:24px}
.entry.main .n,.entry.main h3,.entry.main p{grid-column:1}
.entry.main .aside{grid-column:2;grid-row:1/span 5;align-self:center}
.tag{display:inline-block;white-space:nowrap;margin:2px 0;font-size:13px;padding:0 8px;border:1px solid currentColor;border-radius:2px;line-height:1.7}
.tag.ne{color:var(--acc)}.tag.pr{color:#8a6412}.tag.ps{color:#3f6b36}.tag.ex{color:var(--mut)}
footer{margin:46px 0 0;padding:18px 0 50px;border-top:1px solid var(--ink);font-size:14px;color:var(--mut)}
footer p{margin:0 0 6px;max-width:60em}
/* topic pages */
.crumb{padding:22px 0 0;font-size:15px}
.crumb a{text-decoration:none}.crumb a:hover{text-decoration:underline}
.thead{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:28px;align-items:start;padding:14px 0 18px;border-bottom:1px solid var(--rule)}
.thead .n{font:600 14px "IBM Plex Mono",monospace;color:var(--soft)}
.thead h1{font-size:clamp(26px,4.2vw,40px);margin:2px 0 12px}
.thead p{margin:0 0 10px;max-width:40em}
.verdict{border:2px solid var(--acc);color:var(--acc);padding:10px 16px 12px;transform:rotate(1.5deg);max-width:250px;margin-top:30px;background:var(--paper)}
.verdict small{display:block;font-size:13px;letter-spacing:.04em;color:var(--mut)}
.verdict b{font-family:Pridi,serif;font-size:22px;display:block;line-height:1.3}
.verdict span{display:block;font-size:14px;color:var(--ink);margin-top:4px;line-height:1.5}
.verdict.pr{border-color:#8a6412;color:#8a6412}
.ground{background:var(--paper2);border-left:3px solid var(--ink);padding:10px 16px;margin:22px 0;font-size:16px;max-width:46em}
.ground p{margin:4px 0}
.figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:26px 36px;margin:28px 0}
figure{margin:0}
.fig-scroll{overflow-x:auto}
svg.chart{width:100%;height:auto;display:block;font-family:Sarabun,"Noto Sans Thai",sans-serif}
svg.chart .mono{font-family:"IBM Plex Mono",monospace}
svg.chart .head{font-family:Pridi,serif}
figcaption{font-size:14px;color:var(--mut);margin-top:8px;border-top:1px solid var(--rule);padding-top:6px}
figcaption b{color:var(--ink);font-weight:600}
h2.sec{font-size:24px;margin:40px 0 4px}
.sec-sub{color:var(--mut);margin:0 0 10px;font-size:15px}
.study{display:grid;grid-template-columns:150px minmax(0,1fr);gap:4px 24px;border-top:1px solid var(--rule);padding:18px 0}
.study .d{font:400 13px/1.6 "IBM Plex Mono",monospace;color:var(--mut)}
.study .d .tag{margin-top:8px;font-family:Sarabun,sans-serif}
.study h3{font-size:19px;margin:0 0 4px}
.study .q{margin:0 0 6px}
.study ul{margin:6px 0 4px;padding-left:20px}.study li{margin:2px 0}
.study details{font-size:15px;color:#3a362f;margin:4px 0}
.study summary{cursor:pointer;color:var(--pen)}
.study .src{font:12px "IBM Plex Mono",monospace;color:var(--soft);word-break:break-all;margin:6px 0 0}
.pn{display:flex;justify-content:space-between;gap:16px;border-top:1px solid var(--ink);margin-top:40px;padding:14px 0;font-size:15px}
.pn a{text-decoration:none}.pn a:hover{text-decoration:underline}
.lesson{border-top:1px solid var(--rule);padding:14px 0}
.lesson h3{font-size:20px;margin:0 0 4px}
.lesson p{margin:0 0 8px;max-width:44em}
.formula{font:600 clamp(17px,3vw,22px) "IBM Plex Mono",monospace;margin:8px 0;padding:8px 0;border-top:1px dashed var(--rule);border-bottom:1px dashed var(--rule)}
.tl{list-style:none;margin:0;padding:0}
.tl li{display:grid;grid-template-columns:110px minmax(0,1fr);gap:16px;border-top:1px solid var(--rule);padding:8px 0;font-size:16px}
.tl li span:first-child{font:600 14px "IBM Plex Mono",monospace;color:var(--acc);padding-top:2px}
ol.steps{padding-left:24px}ol.steps li{margin:0 0 12px;max-width:46em}
dl.gl{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:4px 32px;margin:0}
dl.gl div{border-top:1px solid var(--rule);padding:8px 0}
dl.gl dt{font-weight:600}dl.gl dd{margin:2px 0 0;font-size:15px;color:#3a362f}
@media (max-width:820px){
 .intro{grid-template-columns:1fr;gap:18px;padding-top:28px}
 .intro .side{align-self:start;max-width:22em}
 .toc{grid-template-columns:1fr}.entry,.entry.w3,.entry.w4{grid-column:auto}
 .entry.main{grid-template-columns:1fr}.entry.main .aside{grid-column:1;grid-row:auto}
 .thead{grid-template-columns:1fr}.verdict{margin-top:0;transform:rotate(-1deg)}
 .study{grid-template-columns:1fr}.study .d{display:flex;gap:12px;align-items:center;flex-wrap:wrap}.study .d .tag{margin-top:0}
 .ledger div{padding-right:14px;margin-right:14px}
 .top{flex-direction:column;gap:0}.top .stamp{font-size:13px}
 .toc-h{display:block}.toc-h p{margin-top:2px}
 .tl li{grid-template-columns:1fr;gap:0}
}
@media (max-width:420px){body{font-size:16px}.page{padding:0 16px}.ledger b{font-size:22px}}
"""

def badge(v): return f'<span class="tag {v}">{E(data.BADGE[v])}</span>'
def clean_src(s): return s.replace("/workspace/", "")

def study_html(s):
    li = "".join(f"<li>{E(x)}</li>" for x in s["k"])
    return (f'<article class="study"><div class="d">{E(s["d"])}<br>{badge(s["v"])}</div><div>'
            f'<h3>{E(s["t"])}</h3><p class="q">{E(s["q"])}</p><ul>{li}</ul>'
            f'<details><summary>วิธีทดสอบ</summary><p>{E(s["m"])}</p></details>'
            f'<p class="src">ที่มา {E(clean_src(s["src"]))}</p></div></article>')

def fig(svg, cap, src=""):
    srcp = f" ที่มา {E(src)}" if src else ""
    return f'<figure><div class="fig-scroll">{svg}</div><figcaption>{cap}{srcp}</figcaption></figure>'

def shell(title, body, desc):
    return f"""<!DOCTYPE html>
<html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">{FONTS}<style>{CSS}</style></head>
<body><div class="page">
<div class="top"><a class="brand" href="index.html">สมุดวิจัยเทรด ของส้มน้อย</a><span class="stamp">ทดสอบย้อนหลังและบัญชีเดโม · อัปเดต 17 ต.ค. 2026</span></div>
{body}
<footer><p>ตัวเลขทุกตัวคัดลอกจากไฟล์รายงานของงานแต่ละชิ้น ไม่ได้คำนวณใหม่ ยกเว้นสัดส่วนสัญญาณสด 99/192 ที่นับจาก signals.csv และเส้นจุดคุ้มทุนในหน้าบทเรียนที่คำนวณจากสูตร</p>
<p>ทั้งหมดเป็นการทดสอบย้อนหลังหรือบัญชีเดโม (IC Markets MT5 demo และ IQ Option PRACTICE) ไม่มีการเทรดเงินจริง และไม่ใช่คำแนะนำการลงทุน</p>
<p><a href="old/index_v1.html">หน้าเวอร์ชันเก่า (ยาวหน้าเดียว)</a></p></footer>
</div></body></html>"""

# ------------------------------------------------------------------ topics
T = []  # (slug, num, title, short, keyline, studies, verdict_cls, verdict_text, page_body_fn)

def S(gid, *idx): return [G[gid][i] for i in idx]

be_rows_all = [
    ("SL $2 / TP $5 ทุกสัญญาณ (2019-2025)", 31.47, 32.6), ("SL $2 / TP $5 + ตัวกรอง H1", 30.6, 32.6),
    ("TP $5 / SL ปลายแท่งสัญญาณ", 25.17, 31.5), ("TP $5 / SL $3", 40.27, 46.49), ("TP $5 / SL $7", 47.42, 52.68),
    ("7 ปี: SL 2.59 / TP 2.19 (ช่วงทดสอบ)", 53.5, 59.5), ("7 ปี: SL 2.59 / TP 3.74 (ช่วงทดสอบ)", 41.4, 46.1),
    ("7 ปี: SL 2.59 / TP 5.74 (ช่วงทดสอบ)", 34.3, 38.1), ("SMC M5 (zz3, TP 1.5R, ช่วงทดสอบ)", 41.3, 44.9)]

topics = [
 dict(slug="engulf", title="แท่งกลืนกินทอง M5", studies=S("gold-engulf", 0, 1, 2, 3),
      short="สัญญาณปิดทะลุ T1/T2 บนทอง กราฟ 5 นาที ย้อนหลัง 2019 ถึง 2025 ราวๆ 35 สัญญาณต่อวัน ราคาวิ่งไปทางเรากับวิ่งสวนพอๆ กัน",
      key='ชนะ 31.5% <em>ต้องได้ 32.6%</em>', w="w4 main",
      verdict=(NE, "ไม่มีเอดจ์", "ทุก SL ที่ลอง ชนะต่ำกว่าจุดคุ้มทุน ขาดทุนทุกปี")),
 dict(slug="mae-mfe", title="MAE / MFE 7 ปี", studies=S("gold-engulf", 6),
      short="วัดสัญญาณแท่งกลืนกิน 62,599 ครั้ง แล้วตั้ง SL/TP จากสถิติจริง ล็อกค่าไว้ก่อนเปิดดูช่วงทดสอบ",
      key='ก่อนต้นทุน -$4 <em>หลัง -$3,311</em>', w="",
      verdict=(NE, "ไม่มีเอดจ์", "ก่อนหักต้นทุนเกือบเท่าทุน หลังหักขาดทุนทุกคู่ SL/TP")),
 dict(slug="live-week", title="สัปดาห์ 12-17 ต.ค. สัญญาณสด และ ENG5", studies=S("gold-engulf", 4, 5),
      short="ตัวเฝ้าสัญญาณนับแท่งกลืนกินจริงทั้งสัปดาห์ (ไม่ส่งคำสั่ง) แล้วทดสอบย้อนหลังสัปดาห์เดียวกัน 4 แบบ",
      key='ถูกทาง <em>51.6%</em>', w="w3",
      verdict=(NE, "ไม่มีเอดจ์", "ใกล้โยนเหรียญ และ 4 แบบติดลบตั้งแต่ก่อนหักต้นทุน")),
 dict(slug="patterns", title="ขุดรูปแบบจากอดีต และ SMC", studies=S("gold-pattern", 0, 1, 2, 3, 4, 5),
      short="ลองค้นรูปแบบ 37,682 แบบ กับโครงสร้าง SMC บน M5, H1, H4 รูปแบบที่ดูชนะในอดีตร่วงเมื่อเจอข้อมูลใหม่",
      key='71.6% <em>→ 46.7%</em>', w="w3",
      verdict=(NE, "ไม่มีเอดจ์", "ก่อนหักต้นทุนราว 0R ทุกกรอบเวลา")),
 dict(slug="gold-systems", title="ระบบอื่นบนทอง (EMA55, REB-H4, แม่ปลาฯ, ACME)", studies=S("gold-other", *range(9)),
      short="9 ระบบที่ไม่ใช่แท่งกลืนกิน ส่วนใหญ่ลงทะเบียนล่วงหน้า ใกล้สุดคือ REB-H4 PF 1.026 แต่ t = 0.14",
      key='PF สูงสุด <em>1.026</em>', w="w4",
      verdict=(NE, "ไม่มีเอดจ์", "ไม่มีตัวไหนถึงเกณฑ์ PF 1.2 หลังหักต้นทุน")),
 dict(slug="forex", title="ฟอเร็กซ์ และบอทเดโม", studies=S("fx", *range(7)),
      short="ระบบมาตรฐานหลายตระกูลบนหลายคู่เงิน ทดสอบในวันเดียว (11 ต.ค.) และพบว่ากำไรของบอทเดโมมาจาก martingale",
      key='ผ่าน <em>0 จาก 29</em>', w="",
      verdict=(NE, "ไม่มีเอดจ์", "ไม่มีระบบผ่าน มีแค่การตรวจข้อมูลราคาที่ผ่าน")),
 dict(slug="iq-option", title="IQ Option (บัญชี PRACTICE)", studies=S("iq", *range(8)),
      short="ออปชัน 1 ถึง 5 นาที ต้องชนะราว 52-54% ถึงคุ้ม ช่วงตลาดปกติไม่มีกฎผ่าน มี 2 อย่างที่มีแวว",
      key='spike fade 58.1% <em>เข้าช้าเหลือ 54-55%</em>', w="w3",
      verdict=(PR, "มีแววแต่ยังไม่พอ", "2 จาก 8 งานมีแวว ที่เหลือไม่มีเอดจ์")),
 dict(slug="lessons", title="บทเรียน วิธีทดสอบ และขั้นต่อไป", studies=[],
      short="ทำไม win rate อย่างเดียวหลอกตา ทำไมต้องล็อกข้อมูลทดสอบ ต้นทุนกับการเทรดถี่ ไทม์ไลน์ และคำศัพท์",
      key='จุดคุ้มทุน = SL ÷ (SL + TP)', w="w3", verdict=None),
]
for i, tp in enumerate(topics): tp["num"] = f"{i+1:02d}"
assert sum(len(tp["studies"]) for tp in topics) == 37

# ------------------------------------------------------------------ per-topic body
def body_engulf(tp):
    g = ('<div class="ground"><p><b>จุดคุ้มทุน</b> คือ win rate ขั้นต่ำที่ไม่ขาดทุน คิดจาก (SL + ต้นทุน) ÷ (SL + TP) '
         'เช่น SL $2 TP $5 ต้นทุน $0.28 ต่อไม้ (0.01 lot) ได้ 2.28 ÷ 7 = 32.6% ระบบต้องชนะเกินตัวเลขนี้ถึงจะกำไร</p></div>')
    f = ('<div class="figs">' + fig(C.engulf_rule("engulf-rule"), "<b>กฎสัญญาณที่ทดสอบ</b> วาดแบบสมุด แท่งทึบคือแท่งลง (แดง) แท่งโปร่งคือแท่งขึ้น (เขียว)")
         + fig(C.breakeven("engulf-be", be_rows_all[:5], "แท่งกลืนกิน ชนะจริงเทียบจุดคุ้มทุน"),
               "<b>ทุกแถวไม่ถึงเส้นแดง</b> win rate จะสูงหรือต่ำขึ้นกับระยะ SL แต่จุดคุ้มทุนก็ขยับตาม",
               "XAU_SL2_TP5_REPORT.md, XAU_CLOSEBREAK_TP5_REPORT.md") + '</div>')
    return g + f

def body_maemfe(tp):
    g = ('<div class="ground"><p><b>MAE</b> คือระยะที่ราคาวิ่งสวนเราไกลที่สุดระหว่างถือไม้ ใช้คิดว่า SL ควรห่างแค่ไหน</p>'
         '<p><b>MFE</b> คือระยะที่ราคาวิ่งไปทางเราไกลที่สุด ใช้คิดว่า TP ควรอยู่ตรงไหน</p></div>')
    mm = C.diverging("maemfe-net", [
        ("SL 2.59 / TP 2.19 ช่วงค้นหา", -1093, -6696), ("SL 2.59 / TP 2.19 ช่วงทดสอบ", -4, -3311),
        ("SL 2.59 / TP 3.74 ช่วงค้นหา", -514, -5215), ("SL 2.59 / TP 3.74 ช่วงทดสอบ", 3, -2786),
        ("SL 2.59 / TP 3.82 ช่วงค้นหา", -525, -5195), ("SL 2.59 / TP 3.82 ช่วงทดสอบ", 16, -2760),
        ("SL 2.59 / TP 5.74 ช่วงค้นหา", -314, -4548), ("SL 2.59 / TP 5.74 ช่วงทดสอบ", 63, -2431),
    ], 6696, "กำไรก่อนและหลังต้นทุน 7 ปี", "แท่งเขียวก่อนหักต้นทุนแทบเป็นศูนย์ แท่งแดงหลังหักต้นทุนติดลบหลายพันดอลลาร์")
    f = ('<div class="figs">' + '<div>' + fig(C.split_bar("maemfe-split"), "<b>แบ่งข้อมูลก่อนเริ่ม</b> ล็อก SL/TP และบันทึก hash ก่อนเปิดดูช่วงทดสอบ ช่วงทดสอบเปิดดูครั้งเดียว")
         + '<div style="height:26px"></div>'
         + fig(C.breakeven("maemfe-be", be_rows_all[5:8], "7 ปี ชนะจริงเทียบจุดคุ้มทุน (ช่วงทดสอบ)"),
               "<b>ต่ำกว่าคุ้มทุน 4-6 จุดทุกค่า TP</b>") + '</div>'
         + fig(mm, "<b>ต้นทุนคือส่วนที่ทำให้ขาดทุนเกือบทั้งหมด</b> หน่วยดอลลาร์รวม ที่ 0.01 lot ต่อไม้",
               "engulf_watch/maemfe/REPORT.md") + '</div>')
    return g + f

def body_live(tp):
    wk = C.diverging("week-net", [
        ("ENG5 ไม่กรอง ถือ 5 นาที (213 ไม้)", -14.33, -73.97), ("SMA21 ถือ 5 นาที (139 ไม้)", -28.21, -67.13),
        ("MAIN SMA21 15 นาที + ออกก่อน (131 ไม้)", -52.0, -88.67), ("ไม่กรอง 15 นาที + ออกก่อน (195 ไม้)", -43.61, -98.21),
    ], 98.21, "สัปดาห์ 12-17 ต.ค. ก่อนและหลังต้นทุน 4 แบบ", "ทุกแบบติดลบตั้งแต่ก่อนหักต้นทุน")
    return ('<div class="figs">' + fig(C.watcher("watcher"), "<b>ตัวเฝ้าสัญญาณ</b> ข้อมูลแค่ 1 สัปดาห์ ยังไม่หักต้นทุน", "engulf_watch/signals.csv")
            + fig(wk, "<b>ทดสอบย้อนหลังสัปดาห์เดียวกัน</b> หน่วยดอลลาร์รวม ที่ 0.01 lot ใช้ดูภาพรวมเท่านั้น", "engulf_watch/bt_week_20261017.md") + '</div>')

def body_patterns(tp):
    return ('<div class="ground"><p>ถ้าลองหลายหมื่นแบบ ย่อมมีบางแบบดูชนะ 70% โดยบังเอิญ วิธีเช็กคือแช่แข็งรูปแบบไว้ แล้วเอาไปเจอข้อมูลช่วงที่ไม่เคยเห็น</p></div>'
            '<div class="figs">' + fig(C.slope_hindsight("hindsight"), "<b>ร่วงลงต่ำกว่าโยนเหรียญทุกชุด</b> ลองทั้งหมด 37,682 แบบ", "XAU_HINDSIGHT_MINE_REPORT.md")
            + fig(C.breakeven("smc-be", be_rows_all[8:], "SMC M5 ชนะจริงเทียบจุดคุ้มทุน"),
                  "<b>SMC M5 แบบที่ดีที่สุดในช่วงค้นหา</b> พอไปช่วงทดสอบชนะ 41.3% ต้องได้ 44.9%", "XAU_SMC_STRUCT_REPORT.md") + '</div>')

def body_gold(tp):
    rows = [("EMA55 ย่อตัว M5", 0.69), ("EMA55 กรอบใหญ่", 0.93), ("เบรก swing high", 1.009), ("SOX เปิดตลาด", 0.70),
            ("ADR กรอบต่อวัน", 0.92), ("REB-H4", 1.026), ("แม่ปลาฯ H1", 0.87), ("แม่ปลาฯ H4", 0.97), ("ACME 8 ข้อ", 0.27)]
    return ('<div class="ground"><p><b>PF (Profit Factor)</b> คือกำไรรวม ÷ ขาดทุนรวม มากกว่า 1 คือกำไร เกณฑ์ของเราต้องการ 1.2 ขึ้นไป หลังหักต้นทุน</p></div>'
            '<div class="figs">' + fig(C.pf_dots("gold-pf", rows, "ระบบอื่นบนทอง PF หลังหักต้นทุน", "REB-H4"),
                                      "<b>ไม่มีจุดไหนถึงเส้น 1.2</b> REB-H4 สูงสุดในกราฟนี้ แต่ 382 ไม้ t = 0.14 ยังแยกจากความบังเอิญไม่ได้ "
                                      "ACME มีแค่ 12 ไม้ใน 5 ปี", "รายงานแต่ละงานด้านล่าง") + '</div>')

def body_fx(tp):
    return ('<div class="figs">' + fig(C.tally("fx-tally"), "<b>แต่ละช่องคือ 1 ระบบ</b> ใกล้สุดคือ USDJPY NY breakout PF 1.26 แต่ DD -26%",
                                      "REPORT.md, TRACK2_SUMMARY.md, TRACKA_REPORT.md, TRACKB_REPORT.md")
            + fig(C.martingale("bot-profit"), "<b>เทคนิคเดียวกัน ต่างกันแค่ขนาด lot</b> 4 ใน 5 เทคนิคติดลบเมื่อใช้ lot คงที่") + '</div>')

def body_iq(tp):
    return ('<div class="ground"><p><b>จุดคุ้มทุนของออปชัน</b> ขึ้นกับ payout เช่น payout 91% ต้องชนะ 52.36% '
            'แต่ละงานด้านล่างใช้จุดคุ้มทุนของตัวเอง (53.5% ถึง 54.35%) ตามสินทรัพย์และ expiry ที่ทดสอบ</p>'
            '<p><b>spike fade</b> คือเข้าสวนแท่งที่ใหญ่กว่า 4 ATR</p></div>'
            '<div class="figs">' + fig(C.iq_ranges("iq-range"), "<b>ผลที่เกินเส้นแดง</b> เป็นผลในตัวอย่าง หรือยังไม่ได้ยืนยันกับราคา IQ จริง "
                                      "spike fade ถ้าเข้าช้า 7-8 วินาทีก็เหลือแค่เท่าทุน", "iq-research/REPORT.md, iq_research2/report.md และรายงานรอบอื่น") + '</div>')

def body_lessons(tp):
    tl = "".join(f'<li><span>{E(a)}</span><span>{E(b)}</span></li>' for a, b in data.timeline)
    gl = [("MAE (Maximum Adverse Excursion)", "ระยะที่ราคาวิ่งสวนเราไกลที่สุดระหว่างถือไม้ ใช้ช่วยคิดว่า SL ควรห่างแค่ไหน"),
          ("MFE (Maximum Favorable Excursion)", "ระยะที่ราคาวิ่งไปทางเราไกลที่สุดระหว่างถือไม้ ใช้ช่วยคิดว่า TP ควรอยู่ตรงไหน"),
          ("Holdout (ข้อมูลที่ล็อกไว้)", "ข้อมูลส่วนที่เก็บไว้ ห้ามดูระหว่างค้นหากฎ ใช้ทดสอบจริงครั้งเดียวตอนท้าย เหมือนข้อสอบที่ยังไม่เคยเห็น"),
          ("PF (Profit Factor)", "กำไรรวม ÷ ขาดทุนรวม มากกว่า 1 คือกำไร น้อยกว่า 1 คือขาดทุน เกณฑ์ของเราต้องการ 1.2 ขึ้นไป"),
          ("R:R (Risk : Reward)", "เสี่ยงเท่าไร ได้เท่าไร เช่น SL $2 TP $5 คือ 1 : 2.5 ส่วน R คือหน่วยของความเสี่ยง 1 ไม้ (1R = ระยะ SL)"),
          ("จุดคุ้มทุน (Breakeven win rate)", "win rate ขั้นต่ำที่ทำให้ไม่ขาดทุน = SL ÷ (SL + TP) บวกผลของต้นทุน"),
          ("In-sample / Out-of-sample", "ข้อมูลที่ใช้ค้นหากฎ / ข้อมูลที่ไม่ได้ใช้ค้นหา ใช้ตรวจว่ากฎยังได้ผลไหม"),
          ("Gross / Net", "กำไรก่อนหักต้นทุน / กำไรหลังหักต้นทุน (spread ค่าคอม slippage)"),
          ("Walk-forward", "ค้นหากฎในช่วงหนึ่ง แล้วทดสอบช่วงถัดไป เลื่อนไปเรื่อยๆ เหมือนเทรดจริงที่ไม่รู้อนาคต"),
          ("ลงทะเบียนล่วงหน้า (Pre-registration)", "จดกฎและเกณฑ์ผ่านลงไฟล์ล็อกก่อนทดสอบ เพื่อกันการแก้กฎหลังเห็นผล"),
          ("แท่งกลืนกิน T1 / T2 (แบบปิดทะลุ)", "ซื้อ T1 แท่งก่อนเป็นแท่งแดง แท่งเขียวปิดเหนือ high ของแท่งนั้น ซื้อ T2 2 แท่งก่อนเป็นแท่งแดง แท่งเขียวปิดเหนือ high สูงสุดของ 2 แท่ง ขายกลับด้าน"),
          ("Martingale", "เพิ่มขนาดไม้หลังแพ้เพื่อเอาคืน ทำให้ดูกำไรบ่อย แต่เสี่ยงพอร์ตแตกเมื่อแพ้ติดกันยาว")]
    gls = "".join(f"<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>" for a, b in gl)
    return f"""
<div class="figs">
<div>
<div class="lesson"><h3>1. win rate ขึ้นกับ TP/SL ไม่ได้วัดฝีมือ</h3>
<p>ตั้ง TP ใกล้ SL ไกล จะชนะบ่อย ตั้ง TP ไกล SL ใกล้ จะชนะน้อย แต่จุดคุ้มทุนก็ขยับตามเสมอ</p>
<div class="formula">จุดคุ้มทุน = SL ÷ (SL + TP)</div>
<p>รวมต้นทุนด้วยเป็น (SL + ต้นทุน) ÷ (TP + SL) เช่น SL $2 TP $5 ต้นทุน $0.28 ได้ 2.28 ÷ 7 = 32.6% แต่ระบบชนะจริง 31.5% จึงขาดทุน</p></div>
{fig(C.be_curve("be-curve"), "<b>เส้นจุดคุ้มทุน</b> คำนวณจากสูตร ยังไม่รวมต้นทุน")}
</div>
{fig(C.pipeline("pipeline"), "<b>ขั้นตอนที่ใช้กับทุกงานตั้งแต่ 11 ต.ค.</b> กล่องแดงคือ 2 ขั้นที่ข้ามไม่ได้")}
</div>
<div class="lesson"><h3>2. ลองหลายแบบ ต้องเจอผู้ชนะปลอม</h3><p>ลอง 37,682 แบบ ย่อมมีบางแบบดูชนะ 70% โดยบังเอิญ (รายงานประเมินราว 2-3% ของกลุ่มเล็ก) พอเจอข้อมูลใหม่ก็กลับมาราว 50% ยิ่งลองมาก ยิ่งต้องมีหลักฐานแรงขึ้น ตอนนี้ลองไป 925 ชุดในบันทึก เกณฑ์ Bonferroni z ราว 3.87 (ดู<a href="patterns.html">หน้าขุดรูปแบบ</a>)</p></div>
<div class="lesson"><h3>3. ต้องล็อกข้อมูลทดสอบไว้ก่อน</h3><p>แบ่งข้อมูลเป็นส่วนค้นหากับส่วนที่ล็อกไว้ ห้ามแอบดู ตั้งกฎและจดลงไฟล์ (พร้อม hash) ก่อนเปิดดูส่วนที่ล็อก ข้อมูลตั้งแต่ 10 ต.ค. 2025 ยังเก็บไว้ ไม่ได้ใช้ ยกเว้นงานแม่ปลาฯ และ ACME ที่ใช้ไปแล้ว 1 ครั้ง</p></div>
<div class="lesson"><h3>4. ต้นทุนคือศัตรูของการเทรดถี่</h3><p>ทอง M5 ราคาวิ่งเฉลี่ยแค่ไม่กี่ดอลลาร์ ต้นทุน $0.28 ต่อไม้ (spread ค่าคอม และ slippage) กินกำไรทั้งหมด เทรด 35 ครั้งต่อวันก็ยิ่งจ่ายต้นทุนมาก กรอบใหญ่ (H1/H4) ต้นทุนเทียบ R เล็กลง แต่ก็ยังไม่เจอเอดจ์</p></div>
<div class="lesson"><h3>5. martingale ไม่สร้างกำไร</h3><p>กำไรในบัญชีเดโมของบอทมาจากการเพิ่ม lot หลังแพ้ ถ้าใช้ lot คงที่ 4 ใน 5 เทคนิคติดลบ งาน IQ รอบ 5 ก็พบว่า martingale แค่ขยายความผันผวน และทำให้พอร์ตแตกบ่อยขึ้น (ดู<a href="forex.html">หน้าฟอเร็กซ์</a>)</p></div>

<h2 class="sec">ขั้นต่อไป</h2>
<ol class="steps">
<li><b>ใช้แท่งกลืนกินเป็นแค่จังหวะเข้า หลังกรองด้วย H1</b><br>แท่งกลืนกินเดี่ยวๆ ไม่มีเอดจ์ ให้ดูทิศ H1 ก่อน แล้วรอแท่งกลืนกิน M5 ทางเดียวกัน ตัวกรอง H1 แบบที่ลองแล้ว (BOS + ย่อ 40-60%) ยังไม่ผ่าน จึงต้องเขียนกฎ H1 ของส้มน้อยเองให้ชัด แล้วลงทะเบียนล่วงหน้าก่อนทดสอบ</li>
<li><b>ทดสอบกับข้อมูลที่ล็อกไว้แค่ครั้งเดียว</b><br>ตั้งกฎ ตั้ง SL/TP และเกณฑ์ผ่านให้เสร็จก่อน แล้วค่อยเปิดข้อมูลที่ล็อกไว้ ถ้าไม่ผ่านก็ถือว่าไม่ผ่าน ห้ามปรับกฎแล้วลองใหม่บนข้อมูลชุดเดิม</li>
<li><b>จดบันทึกการเทรดมือ (journal) ในบัญชีเดโม</b><br>ทุกไม้จดเวลา ทิศ H1 เหตุผลที่เข้า SL TP ผลลัพธ์ และ MAE/MFE ถ้าดูได้ ใช้ lot คงที่ ไม่เพิ่ม lot หลังแพ้ เมื่อได้หลายร้อยไม้จะเห็นว่าดุลยพินิจของเราดีกว่ากฎตายตัวไหม</li>
<li><b>คิดต้นทุนทุกครั้ง</b><br>ก่อนเชื่อผลทดสอบใด ถามว่าหลังหัก $0.28 ต่อไม้แล้วยังกำไรไหม และ win rate เกินจุดคุ้มทุนของ TP/SL นั้นหรือยัง</li>
</ol>

<h2 class="sec">ไทม์ไลน์ (ปี 2026)</h2>
<p class="sec-sub">วันที่มาจากบันทึกการทดสอบ (results/trials.csv), STATUS.md และหัวรายงาน รายการที่เขียนว่า "ราว" เรียงตามลำดับจำนวนการทดสอบสะสม เพราะไฟล์ไม่ได้บอกเวลาตรงๆ</p>
<ul class="tl">{tl}</ul>

<h2 class="sec">คำศัพท์</h2>
<dl class="gl">{gls}</dl>
"""

BODY = {"engulf": body_engulf, "mae-mfe": body_maemfe, "live-week": body_live, "patterns": body_patterns,
        "gold-systems": body_gold, "forex": body_fx, "iq-option": body_iq, "lessons": body_lessons}

LONG = {
 "engulf": ["เรื่องหลักของเรา สัญญาณปิดทะลุ (แท่งกลืนกิน T1/T2) บนทอง XAUUSD กราฟ 5 นาที ทดสอบย้อนหลัง 2019 ถึง 2025 ได้ 73,958 สัญญาณ ราว 35 ครั้งต่อวัน",
            "หลังสัญญาณ ราคาวิ่งไปทางเรากับวิ่งสวนพอๆ กัน (MFE กลาง $2.34 เทียบ MAE กลาง $2.42) ลอง SL/TP หลายแบบ ทุกแบบชนะต่ำกว่าจุดคุ้มทุน ใส่ตัวกรอง H1 ก็ยังไม่พอ"],
 "mae-mfe": ["งานล่าสุด (17 ต.ค.) วัดสัญญาณแท่งกลืนกิน 62,599 ครั้งย้อนหลัง 7 ปี แล้วตั้ง SL/TP จากสถิติจริง ล็อกค่าและบันทึก hash ก่อนเปิดดูช่วงทดสอบ",
             "ก่อนหักต้นทุนเกือบเท่าทุนทุกคู่ พอหักต้นทุน $0.28 ต่อไม้ก็ขาดทุนหลายพันดอลลาร์ ไม้แพ้ก็ไม่ได้มี MAE ลึกกว่าไม้ชนะ จึงตั้ง SL แยกไม้แพ้ออกไม่ได้"],
 "live-week": ["12 ถึง 17 ต.ค. 2026 ตัวเฝ้าสัญญาณอ่านราคาทุกชั่วโมงแล้วนับแท่งกลืนกิน ไม่ส่งคำสั่งจริง จาก 192 สัญญาณที่มีผลครบ ไปถูกทาง 99 ครั้ง",
               "พอเอาสัปดาห์เดียวกันมาทดสอบย้อนหลัง 4 แบบ รวม ENG5 ที่ถือ 5 นาที ติดลบทุกแบบตั้งแต่ก่อนหักต้นทุน ข้อมูลแค่สัปดาห์เดียว ใช้ดูภาพรวมเท่านั้น"],
 "patterns": ["ค้นหารูปแบบจากอดีตแบบเต็มที่ 37,682 แบบ ทั้งวัน เวลา สีแท่ง ขนาดแท่ง ฯลฯ และโครงสร้าง SMC บน M5 อีก 480 แบบ บน H1/H4 อีก 960 แบบ",
              "รูปแบบที่ชนะ 71.6% ในช่วงที่ใช้ค้นหา เหลือ 46.7% ในช่วงที่ไม่เคยเห็น SMC ก่อนหักต้นทุนราว 0R ทุกกรอบเวลา มีตัวอย่างสอนเรื่องการแอบดูอนาคตไว้ด้วย"],
 "gold-systems": ["ระบบอื่นที่ทดสอบบนทอง 9 เรื่อง ตั้งแต่ EMA55, เบรก swing high, SOX, ADR, REB-H4 ไปจนถึงกฎจากหนังสือแม่ปลาปากกาเขียว ลำดับ ACME 8 ข้อ และการค้นหารุ่นแรก 888 แบบ + ML",
                  "ส่วนใหญ่ PF ต่ำกว่า 1 หลังหักต้นทุน ตัวที่บวกเล็กน้อยก็มีไม้น้อยหรือ t ต่ำเกินกว่าจะเชื่อ"],
 "forex": ["11 ต.ค. 2026 ทดสอบระบบมาตรฐาน 6 ตระกูลบนหลายคู่เงิน ตามด้วยตระกูลใหม่อีก 24 ตัว และ Track A/B หักต้นทุน IC จริงทั้งหมด ไม่มีระบบไหนผ่าน",
           "เทคนิคของบอทเดโมก็ PF ต่ำกว่า 1 ทุกตัว กำไรที่เห็นในเดโมมาจากการเพิ่ม lot หลังแพ้ ส่วนข้อมูลฟรี Dukascopy ที่ใช้ทั้งหมด ตรวจแล้วใกล้ราคา IC Markets มาก"],
 "iq-option": ["ออปชันระยะสั้น 1 ถึง 5 นาที ใน IQ Option บัญชี PRACTICE ทดสอบ 8 รอบ ช่วงตลาดปกติไม่มีกฎไหนชนะเกินจุดคุ้มทุน ML ที่ได้ 62% ในตัวอย่างก็เหลือ 49-51%",
               "มี 2 อย่างที่มีแวว spike fade ได้ 58.1% นอกตัวอย่าง แต่ถ้าเข้าช้า 7-8 วินาทีเหลือราว 54-55% และ RSI2 ช่วง rollover 04:00-04:59 น. ได้ 60.8% แต่ยังไม่ยืนยันกับราคา IQ ส่วน martingale ไม่ช่วย"],
 "lessons": ["สิ่งที่ได้จาก 37 งาน เขียนไว้กันลืม ทั้งเรื่องจุดคุ้มทุน ผู้ชนะปลอม การล็อกข้อมูล ต้นทุน และ martingale ต่อด้วยขั้นต่อไป ไทม์ไลน์ และคำศัพท์"],
}

def topic_page(i, tp):
    prev_t = topics[i - 1] if i > 0 else None
    next_t = topics[i + 1] if i + 1 < len(topics) else None
    v = tp["verdict"]
    vbox = (f'<div class="verdict {v[0]}"><small>ผลสรุป</small><b>{E(v[1])}</b><span>{E(v[2])}</span></div>' if v else "")
    paras = "".join(f"<p>{E(p)}</p>" for p in LONG[tp["slug"]])
    studies = ""
    if tp["studies"]:
        studies = (f'<h2 class="sec">งานในหัวข้อนี้ ({len(tp["studies"])} เรื่อง)</h2><p class="sec-sub">กด "วิธีทดสอบ" เพื่อดูรายละเอียด</p>'
                   + "".join(study_html(s) for s in tp["studies"]))
    pn = '<div class="pn">'
    pn += f'<a href="{prev_t["slug"]}.html">← {E(prev_t["title"])}</a>' if prev_t else '<a href="index.html">← สารบัญ</a>'
    pn += f'<a href="{next_t["slug"]}.html">{E(next_t["title"])} →</a>' if next_t else '<a href="index.html">กลับสารบัญ →</a>'
    pn += '</div>'
    body = (f'<div class="crumb"><a href="index.html">← กลับสารบัญ</a></div>'
            f'<header class="thead"><div><div class="n">หัวข้อ {tp["num"]} / {len(topics):02d}</div><h1>{E(tp["title"])}</h1>{paras}</div>{vbox}</header>'
            + BODY[tp["slug"]](tp) + studies + pn)
    return shell(f'{tp["title"]} · สมุดวิจัยเทรด', body, tp["short"])

# ------------------------------------------------------------------ landing
def mini_bar(a, b, la, lb, maxv):
    W = 220
    wa, wb = a / maxv * (W - 70), b / maxv * (W - 70)
    return (f'<svg viewBox="0 0 {W} 56" width="{W}" aria-hidden="true" class="chart">'
            f'<rect x="0" y="6" width="{wa:.1f}" height="14" fill="#5b554b"/><text x="{wa+6:.1f}" y="18" font-size="12" class="mono" fill="#24211c">{la}</text>'
            f'<rect x="0" y="32" width="{wb:.1f}" height="14" fill="#b03a1f"/><text x="{wb+6:.1f}" y="44" font-size="12" class="mono" fill="#b03a1f">{lb}</text></svg>')

def landing():
    counts = {NE: 0, PR: 0, PS: 0, EX: 0}
    for tp in topics:
        for s in tp["studies"]: counts[s["v"]] += 1
    entries = []
    for tp in topics:
        n = len(tp["studies"])
        meta = f'{n} งาน · ' + " ".join(sorted({badge(s["v"]) for s in tp["studies"]})) if n else "บทเรียน ไทม์ไลน์ คำศัพท์"
        aside = ""
        if tp["slug"] == "engulf":
            aside = ('<div class="aside">' + mini_bar(31.5, 32.6, "ชนะจริง 31.5%", "ต้องได้ 32.6%", 40)
                     + '<div class="note" style="font-size:16px">ขาดไปนิดเดียว แต่ขาดทุกปี</div></div>')
        if tp["slug"] == "patterns":
            aside = ('<svg viewBox="0 0 260 64" width="260" aria-hidden="true" class="chart">'
                     '<line x1="40" y1="52" x2="250" y2="52" stroke="#d9d1c0"/>'
                     '<line x1="60" y1="10" x2="200" y2="44" stroke="#b03a1f" stroke-width="2"/>'
                     '<circle cx="60" cy="10" r="4" fill="#b03a1f"/><circle cx="200" cy="44" r="4" fill="#b03a1f"/>'
                     '<text x="52" y="14" font-size="12" text-anchor="end" class="mono" fill="#24211c">71.6%</text>'
                     '<text x="208" y="48" font-size="12" class="mono" fill="#b03a1f">46.7%</text>'
                     '<text x="60" y="64" font-size="11" text-anchor="middle" fill="#5b554b">ช่วงค้นหา</text>'
                     '<text x="200" y="64" font-size="11" text-anchor="middle" fill="#5b554b">ข้อมูลใหม่</text></svg>')
        if tp["slug"] == "forex":
            sq = "".join(f'<rect x="{1+k%15*14}" y="{1+k//15*14}" width="10" height="10" fill="none" stroke="#5b554b"/>' for k in range(29))
            aside = f'<svg viewBox="0 0 212 30" width="212" aria-hidden="true" class="chart">{sq}</svg>'
        cls = f'entry {tp["w"]}'.strip()
        entries.append(f'<a class="{cls}" href="{tp["slug"]}.html"><span class="n">{tp["num"]}</span><h3>{E(tp["title"])}</h3>'
                       + (f'<p>{E(tp["short"])}</p><p class="k">{tp["key"]}</p><p class="meta">{meta}</p>{aside}</a>' if tp["slug"] == "engulf" else
                        f'<p>{E(tp["short"])}</p>{aside}<p class="k">{tp["key"]}</p><p class="meta">{meta}</p></a>'))
    body = f"""
<section class="intro"><div>
<h1>ทดสอบมา 37 เรื่อง <span class="hl">ยังไม่มีกฎไหนชนะตลาดได้จริงหลังหักต้นทุน</span></h1>
<p>ส่วนใหญ่เป็นทองคำ XAUUSD กราฟ 5 นาที ใช้ข้อมูลราคาฟรีจาก Dukascopy (ตรวจแล้วว่าใกล้ราคา IC Markets มาก) และต้นทุนจริงของ IC Markets ราว $0.28 ต่อ 0.01 lot ต่อไม้</p>
<p>แท่งกลืนกินทอง M5 ก่อนหักต้นทุนแค่เสมอตัว ต้นทุนคือส่วนที่ทำให้ขาดทุนเกือบทั้งหมด ทั้งหมดเป็นการทดสอบย้อนหลังและบัญชีเดโม ไม่มีเงินจริง</p>
</div><div class="side note">ถ้าจะจำได้เรื่องเดียว<br>ถามทุกครั้งว่า "หัก $0.28 แล้วยังเหลือไหม" ✏️</div></section>
<div class="ledger">
<div><b>37</b><span>งานวิจัย</span></div>
<div class="red"><b>0</b><span>ระบบที่ผ่านเกณฑ์</span></div>
<div><b>925</b><span>ชุดกฎในบันทึก</span></div>
<div><b>62,599</b><span>สัญญาณ 7 ปีที่วัดผล</span></div>
<div><b>51.6%</b><span>สัญญาณสดสัปดาห์นี้ถูกทาง 🎲</span></div>
</div>
<div class="toc-h"><h2>เลือกหัวข้อ</h2><p>แต่ละหัวข้อมีหน้าของตัวเอง สรุป กราฟ และผลสรุป</p></div>
<nav class="toc" aria-label="หัวข้อ">{''.join(entries)}</nav>
"""
    return shell("สมุดวิจัยเทรด ของส้มน้อย", body, "สรุปงานทดสอบระบบเทรด 37 เรื่อง ทองคำ ฟอเร็กซ์ และ IQ Option บนบัญชีเดโม"), counts

if __name__ == "__main__":
    html_idx, counts = landing()
    open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(html_idx)
    for i, tp in enumerate(topics):
        open(os.path.join(D, tp["slug"] + ".html"), "w", encoding="utf-8").write(topic_page(i, tp))
    print("pages:", ["index.html"] + [tp["slug"] + ".html" for tp in topics], counts)
