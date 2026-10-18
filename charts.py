# -*- coding: utf-8 -*-
# Inline SVG charts and diagrams for v2. Every number comes from data.py / the v1 page.
# Diagram rules follow the diagram-design skill: accent on 1-2 elements, no shadows,
# orthogonal connectors, masked arrow labels, 4px grid, <title>/<desc> on every svg.
import html
E = html.escape

INK, MUTED, SOFT, RULE, PAPER, PAPER2 = "#24211c", "#5b554b", "#7a7366", "#d9d1c0", "#f7f3ea", "#efe8da"
ACC, PEN, GROSS = "#b03a1f", "#22507f", "#6f8a5e"

def svg_open(slug, w, h, title, desc):
    return (f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-labelledby="{slug}-title {slug}-desc" '
            f'style="max-width:{w}px"><title id="{slug}-title">{E(title)}</title><desc id="{slug}-desc">{E(desc)}</desc>'
            f'<defs><marker id="{slug}-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker>'
            f'<marker id="{slug}-arra" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker></defs>')

TSCALE = 1.0  # bumped per chart for phone legibility

def t(x, y, s, size=15, fill=INK, anchor="start", cls="", weight=None):
    size = round(size * TSCALE, 1)
    w = f' font-weight="{weight}"' if weight else ""
    c = f' class="{cls}"' if cls else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}{c}>{E(str(s))}</text>'

def fmt_pct(v): return f"{v:.1f}%"

# ------------------------------------------------------------------ win rate vs breakeven
def breakeven(slug, rows, title):
    """rows: (label, actual %, breakeven %)."""
    W, L, R = 480, 8, 60
    rowh, top = 54, 44
    H = top + rowh * len(rows) + 8
    lo, hi = 20.0, 65.0
    def X(p): return L + (p - lo) / (hi - lo) * (W - L - R)
    s = [svg_open(slug, W, H, title, "แต่ละแถวคือ win rate ที่ได้จริง เทียบกับ win rate ขั้นต่ำที่ต้องได้เพื่อไม่ขาดทุน")]
    s.append(f'<rect x="{L}" y="10" width="22" height="10" fill="{MUTED}"/>' + t(L + 28, 20, "ชนะจริง", 14, MUTED))
    s.append(f'<rect x="{L+100}" y="6" width="3" height="18" fill="{ACC}"/>' + t(L + 110, 20, "จุดคุ้มทุน ต้องเกินเส้นนี้", 14, ACC))
    for i, (lab, act, be) in enumerate(rows):
        y = top + i * rowh
        s.append(t(L, y + 12, lab, 14, INK))
        s.append(f'<rect x="{L}" y="{y+20}" width="{W-L-R}" height="14" fill="{PAPER2}"/>')
        s.append(f'<rect x="{L}" y="{y+20}" width="{X(act)-L:.1f}" height="14" fill="{MUTED}"/>')
        s.append(f'<rect x="{X(be)-1.5:.1f}" y="{y+15}" width="3" height="24" fill="{ACC}"/>')
        s.append(t(X(act) - 5, y + 31.5, fmt_pct(act), 12, PAPER, "end", "mono", 600))
        s.append(t(X(be) + 7, y + 31.5, fmt_pct(be), 12, ACC, "start", "mono", 600))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ gross vs net, diverging
def diverging(slug, rows, maxabs, title, desc):
    """rows: (label, gross, net). Bars grow left from zero when negative."""
    W, L, R = 480, 8, 8
    rowh, top = 62, 44
    H = top + rowh * len(rows) + 26
    zero = W - R - 86
    sc = (zero - L - 4) / float(maxabs)
    s = [svg_open(slug, W, H, title, desc)]
    s.append(f'<rect x="{L}" y="10" width="14" height="10" fill="{GROSS}"/>' + t(L + 20, 20, "ก่อนหักต้นทุน", 14, MUTED))
    s.append(f'<rect x="{L+140}" y="10" width="14" height="10" fill="{ACC}"/>' + t(L + 160, 20, "หลังหักต้นทุน", 14, MUTED))
    s.append(f'<line x1="{zero}" y1="{top-6}" x2="{zero}" y2="{H-22}" stroke="{INK}" stroke-width="1"/>')
    s.append(t(zero, H - 6, "0 เท่าทุน", 12, MUTED, "middle"))
    for i, (lab, g, n) in enumerate(rows):
        y = top + i * rowh
        s.append(t(L, y + 12, lab, 14, INK))
        for j, (v, col) in enumerate(((g, GROSS), (n, ACC))):
            yy = y + 20 + j * 18
            w = max(abs(v) * sc, 1.5)
            x = zero - w if v < 0 else zero
            s.append(f'<rect x="{x:.1f}" y="{yy}" width="{w:.1f}" height="14" fill="{col}"/>')
            txt = (f"+{v:,.2f}" if v > 0 else f"{v:,.2f}").replace(".00", "")
            s.append(t(zero + 6 + (w if v > 0 else 0), yy + 12, txt, 12, col, "start", "mono", 600))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ slopegraph: search period vs unseen period
def slope_hindsight(slug):
    rows = [("4 รูปแบบที่ชนะ ≥70%", 71.6, 46.7), ("ชุด 4.5/วัน (≥62%)", 64.2, 49.5), ("ชุด 4.5/วัน (≥58%)", 62.6, 49.9)]
    W, H = 480, 320
    x1, x2, top, bot = 204, 344, 60, 290
    def Y(p): return bot - (p - 44) / (74 - 44) * (bot - top)
    s = [svg_open(slug, W, H, "รูปแบบที่ขุดจากอดีต ก่อนและหลังเจอข้อมูลใหม่",
                  "win rate ในช่วงที่ใช้ค้นหา เทียบกับช่วงที่ไม่เคยเห็น ทุกชุดร่วงลงต่ำกว่า 50%")]
    s.append(t(x1, 28, "ช่วงที่ใช้ค้นหา", 14, MUTED, "middle"))
    s.append(t(x2, 28, "ช่วงที่ไม่เคยเห็น", 14, MUTED, "middle"))
    s.append(f'<line x1="{x1}" y1="{top-16}" x2="{x1}" y2="{bot}" stroke="{RULE}"/>')
    s.append(f'<line x1="{x2}" y1="{top-16}" x2="{x2}" y2="{bot}" stroke="{RULE}"/>')
    s.append(f'<line x1="{x1-20}" y1="{Y(50):.1f}" x2="{W-8}" y2="{Y(50):.1f}" stroke="{MUTED}" stroke-dasharray="5 4"/>')
    s.append(t(x1 - 26, Y(50) + 5, "50% = โยนเหรียญ", 13, MUTED, "end"))
    for i, (lab, a, b) in enumerate(rows):
        col = ACC if i == 0 else MUTED
        s.append(f'<line x1="{x1}" y1="{Y(a):.1f}" x2="{x2}" y2="{Y(b):.1f}" stroke="{col}" stroke-width="{2.5 if i == 0 else 1.5}"/>')
        s.append(f'<circle cx="{x1}" cy="{Y(a):.1f}" r="4" fill="{col}"/><circle cx="{x2}" cy="{Y(b):.1f}" r="4" fill="{col}"/>')
    s.append(t(x1 - 10, Y(71.6) + 5, "71.6%", 13, ACC, "end", "mono", 600))
    s.append(t(x1 - 64, Y(71.6) + 5, "4 รูปแบบที่ชนะ ≥70%", 13, ACC, "end"))
    s.append(t(x1 - 10, Y(64.2) + 2, "64.2%", 13, MUTED, "end", "mono", 600))
    s.append(t(x1 - 10, Y(62.6) + 12, "62.6%", 13, MUTED, "end", "mono", 600))
    s.append(t(x1 - 64, Y(64.2) + 2, "ชุด 4.5 สัญญาณ", 13, MUTED, "end"))
    s.append(t(x1 - 64, Y(62.6) + 12, "ต่อวัน (2 ชุด)", 13, MUTED, "end"))
    s.append(t(x2 + 10, Y(49.9) - 8, "49.9% / 49.5%", 13, MUTED, "start", "mono", 600))
    s.append(t(x2 + 10, Y(46.7) + 5, "46.7%", 13, ACC, "start", "mono", 600))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ PF dot plot
def pf_dots(slug, rows, title, focal):
    """rows: (label, pf after cost). focal = label to highlight."""
    W, L = 480, 150
    rowh, top = 30, 44
    H = top + rowh * len(rows) + 36
    lo, hi = 0.2, 1.38
    def X(v): return L + (v - lo) / (hi - lo) * (W - L - 16)
    s = [svg_open(slug, W, H, title, "PF หลังหักต้นทุนของแต่ละระบบ เทียบเส้นเท่าทุน 1.0 และเกณฑ์ 1.2")]
    for v, lab, dash in ((1.0, "1.0 เท่าทุน", "4 3"), (1.2, "1.2 เกณฑ์", "")):
        s.append(f'<line x1="{X(v):.1f}" y1="{top-12}" x2="{X(v):.1f}" y2="{H-30}" stroke="{INK if v==1.2 else MUTED}" stroke-dasharray="{dash}"/>')
        s.append(t(X(v) + (-5 if v == 1.0 else 5), top - 18, lab, 12, MUTED, "end" if v == 1.0 else "start"))
    for v in (0.4, 0.6, 0.8):
        s.append(t(X(v), H - 12, f"{v:.1f}", 12, SOFT, "middle", "mono"))
    for i, (lab, v) in enumerate(rows):
        y = top + i * rowh + 14
        f = lab == focal
        s.append(f'<line x1="{L}" y1="{y}" x2="{W-16}" y2="{y}" stroke="{RULE}" stroke-width="0.8"/>')
        s.append(t(L - 10, y + 5, lab, 14, ACC if f else INK, "end", "", 600 if f else None))
        s.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="{6 if f else 5}" fill="{ACC if f else PAPER}" stroke="{ACC if f else INK}" stroke-width="1.5"/>')
        tx = X(v) - 10 if v > 1.0 else X(v) + 10
        s.append(t(tx, y - 7, f"{v:g}", 12, ACC if f else MUTED, "end" if v > 1.0 else "start", "mono", 600))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ IQ ranges vs breakeven
def iq_ranges(slug):
    rows = [
        ("spike fade นอกตัวอย่าง", 58.1, 58.1, 54.35),
        ("spike fade ถ้าเข้าช้า 7-8 วิ", 54, 55, 54.35),
        ("RSI2 ช่วง rollover นอกตัวอย่าง", 60.8, 60.8, 54.1),
        ("Blitz ML ในตัวอย่าง", 62, 62, 54.1),
        ("Blitz ML นอกตัวอย่าง", 49, 51, 54.1),
        ("Blitz ช่วงตลาดปกติ", 50, 53, 54.1),
        ("spike fade ปี 2025 (6 คู่)", 53.3, 53.9, 54.05),
        ("expiry 5 นาที ส่วนใหญ่", 48, 52, 53.5),
        ("EUR/USD colorbig", 48, 49, 53.5),
        ("EUR/USD roundbreak", 45.6, 45.6, 53.5),
    ]
    W, L, R = 480, 8, 16
    rowh, top = 44, 44
    H = top + rowh * len(rows) + 30
    lo, hi = 44.0, 64.0
    def X(p): return L + (p - lo) / (hi - lo) * (W - L - R)
    s = [svg_open(slug, W, H, "IQ Option: win rate เทียบจุดคุ้มทุนของแต่ละงาน",
                  "จุดหรือช่วงคือ win rate ที่ได้ ขีดแดงคือจุดคุ้มทุนของงานนั้น มีแค่ผลในตัวอย่างหรือผลที่ยังไม่ยืนยันที่เกินเส้น")]
    s.append(f'<circle cx="{L+6}" cy="15" r="5" fill="{INK}"/>' + t(L + 16, 20, "ชนะจริง (จุดหรือช่วง)", 14, MUTED))
    s.append(f'<rect x="{L+190}" y="6" width="3" height="18" fill="{ACC}"/>' + t(L + 200, 20, "จุดคุ้มทุนของงานนั้น", 14, ACC))
    for p in (46, 50, 54, 58, 62):
        s.append(f'<line x1="{X(p):.1f}" y1="{top-4}" x2="{X(p):.1f}" y2="{H-26}" stroke="{RULE}" stroke-width="0.8"/>')
        s.append(t(X(p), H - 10, f"{p}%", 12, SOFT, "middle", "mono"))
    for i, (lab, a, b, be) in enumerate(rows):
        y = top + i * rowh
        s.append(t(L, y + 12, lab, 13, INK))
        cy = y + 28
        s.append(f'<rect x="{X(be)-1.5:.1f}" y="{cy-10}" width="3" height="20" fill="{ACC}"/>')
        if a == b:
            s.append(f'<circle cx="{X(a):.1f}" cy="{cy}" r="5" fill="{INK}"/>')
            lab_v = fmt_pct(a) if a % 1 else f"{a:g}%"
        else:
            s.append(f'<line x1="{X(a):.1f}" y1="{cy}" x2="{X(b):.1f}" y2="{cy}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
            lab_v = f"{a:g}-{b:g}%"
        right = max(a, b)
        if right > be or X(min(a, b)) - L < 60:
            s.append(t(X(right) + 10, cy + 4, lab_v, 12, INK, "start", "mono", 600))
        else:
            s.append(t(X(min(a, b)) - 10, cy + 4, lab_v, 12, INK, "end", "mono", 600))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ breakeven curve
def be_curve(slug):
    W, H = 480, 290
    L, B, T, Rr = 50, 235, 24, 20
    xmax = 3.2
    def px(r): return L + (r - 0.3) / (xmax - 0.3) * (W - L - Rr)
    def py(p): return B - p / 80.0 * (B - T)
    s = [svg_open(slug, W, H, "จุดคุ้มทุนตามอัตรา SL ต่อ TP", "ยิ่ง TP ไกลกว่า SL win rate ที่ต้องได้ยิ่งต่ำ คำนวณจากสูตร SL หารด้วย SL บวก TP ยังไม่รวมต้นทุน")]
    for p in (20, 40, 60, 80):
        s.append(f'<line x1="{L}" y1="{py(p):.1f}" x2="{W-Rr}" y2="{py(p):.1f}" stroke="{RULE}"/>' + t(L - 8, py(p) + 5, f"{p}%", 12, SOFT, "end", "mono"))
    pts, r = [], 0.3
    while r <= xmax + 1e-9:
        pts.append(f"{px(r):.1f},{py(100/(1+r)):.1f}"); r += 0.05
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="2"/>')
    for r in (0.5, 1, 1.5, 2, 2.5, 3):
        p = 100 / (1 + r)
        s.append(f'<circle cx="{px(r):.1f}" cy="{py(p):.1f}" r="4" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
        s.append(t(px(r), py(p) - 10, fmt_pct(p), 12, INK, "middle", "mono"))
        s.append(t(px(r), B + 20, f"1:{r:g}", 12, MUTED, "middle", "mono"))
    s.append(t((L + W - Rr) / 2, B + 44, "SL : TP (ยังไม่รวมต้นทุน)", 13, MUTED, "middle"))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ fx tally (0 passed out of N)
def tally(slug):
    rows = [("Walk-forward ระบบมาตรฐาน", 29), ("Track 2 ตระกูลใหม่", 24), ("Track B M5 ฟอเร็กซ์", 12), ("Track A กรอบใหญ่", 6)]
    W, top, rowh = 480, 16, 64
    H = top + rowh * len(rows)
    s = [svg_open(slug, W, H, "ฟอเร็กซ์: ระบบที่ผ่านเกณฑ์", "ทุกช่องคือ 1 ระบบที่ทดสอบ ช่องว่างคือไม่ผ่าน ทุกชุดผ่าน 0 ระบบ")]
    for i, (lab, n) in enumerate(rows):
        y = top + i * rowh
        s.append(t(8, y + 14, lab, 14, INK) + t(W - 8, y + 14, f"ผ่าน 0 จาก {n}", 13, ACC, "end", "mono", 600))
        for k in range(n):
            x = 8 + k * 16
            s.append(f'<rect x="{x}" y="{y+24}" width="12" height="12" fill="none" stroke="{MUTED}" stroke-width="1"/>')
            s.append(f'<line x1="{x+2}" y1="{y+34}" x2="{x+10}" y2="{y+26}" stroke="{SOFT}" stroke-width="0.8"/>')
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ diagram helpers
def node(x, y, w, h, name, sub="", tag="", focal=False, dashed=False):
    stroke = ACC if focal else INK
    fill = "#f6e6df" if focal else PAPER
    d = ' stroke-dasharray="4 3"' if dashed else ""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{PAPER}"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{1.5 if focal else 1}"{d}/>']
    cx = x + w / 2
    if tag:
        tw = 10 + len(tag) * 8
        out.append(f'<rect x="{x+8}" y="{y+8}" width="{tw}" height="16" rx="2" fill="none" stroke="{stroke}" stroke-opacity=".45" stroke-width=".8"/>')
        out.append(t(x + 8 + tw / 2, y + 20, tag, 11, stroke, "middle", "mono"))
    if sub:
        out.append(t(cx, y + h / 2 - 2, name, 15, INK, "middle", "", 600))
        out.append(t(cx, y + h / 2 + 17, sub, 12, MUTED, "middle", "mono" if sub.isascii() else ""))
    else:
        out.append(t(cx, y + h / 2 + 5, name, 15, INK, "middle", "", 600))
    return "".join(out)

def vline(slug, x, y1, y2, accent=False, label="", side="right"):
    col = ACC if accent else MUTED
    m = f"{slug}-arra" if accent else f"{slug}-arr"
    out = f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2-1}" stroke="{col}" stroke-width="1.4" marker-end="url(#{m})"/>'
    if label:
        lw = 12 + len(label) * 8
        my = (y1 + y2) / 2
        lx = x + 8 if side == "right" else x - 8 - lw
        out += f'<rect x="{lx}" y="{my-9}" width="{lw}" height="18" fill="{PAPER}"/>' + t(lx + lw / 2, my + 4, label, 12, col, "middle")
    return out

def elbow(slug, x1, y1, x2, y2, label=""):
    """down from (x1,y1), then across, then down to (x2,y2). r=8 corners."""
    ym = (y1 + y2) / 2
    sx = 1 if x2 > x1 else -1
    d = (f"M{x1},{y1} V{ym-8} Q{x1},{ym} {x1+8*sx},{ym} H{x2-8*sx} Q{x2},{ym} {x2},{ym+8} V{y2-1}")
    out = f'<path d="{d}" fill="none" stroke="{MUTED}" stroke-width="1.4" marker-end="url(#{slug}-arr)"/>'
    if label:
        lw = 12 + len(label) * 8
        lx = (x1 + x2) / 2 - lw / 2
        out += f'<rect x="{lx}" y="{ym-30}" width="{lw}" height="18" fill="{PAPER}"/>' + t(lx + lw / 2, ym - 17, label, 12, MUTED, "middle")
    return out

# ------------------------------------------------------------------ diagram: engulf rule T1/T2
def engulf_rule(slug):
    W, H = 480, 268
    s = [svg_open(slug, W, H, "กฎแท่งกลืนกินแบบปิดทะลุ T1 และ T2",
                  "ฝั่งซื้อ T1 แท่งเขียวปิดเหนือ high ของแท่งแดงก่อนหน้า T2 แท่งเขียวปิดเหนือ high สูงสุดของแท่งแดง 2 แท่ง")]
    def candle(cx, hi, op, cl, lo, up):
        top, bot = min(op, cl), max(op, cl)
        out = f'<line x1="{cx}" y1="{hi}" x2="{cx}" y2="{lo}" stroke="{INK}" stroke-width="1.4"/>'
        out += f'<rect x="{cx-12}" y="{top}" width="24" height="{bot-top}" fill="{PAPER if up else INK}" stroke="{INK}" stroke-width="1.4"/>'
        return out
    # panel frames
    for x0, name in ((8, "ซื้อ T1"), (248, "ซื้อ T2")):
        s.append(f'<rect x="{x0}" y="8" width="224" height="216" rx="6" fill="none" stroke="{RULE}"/>')
        s.append(t(x0 + 14, 34, name, 17, INK, "start", "head", 600))
    # T1
    s.append(f'<line x1="28" y1="96" x2="216" y2="96" stroke="{MUTED}" stroke-dasharray="5 4"/>')
    s.append(f'<rect x="132" y="101" width="88" height="18" fill="{PAPER}"/>' + t(176, 114, "high แท่งแดง", 12, MUTED, "middle"))
    s.append(candle(72, 96, 112, 176, 196, False))
    s.append(candle(116, 64, 176, 76, 204, True))
    s.append(f'<line x1="132" y1="76" x2="160" y2="76" stroke="{ACC}" stroke-width="1.5" marker-end="url(#{slug}-arra)"/>')
    s.append(t(166, 72, "ปิดเหนือเส้น", 12, ACC) + t(166, 88, "= สัญญาณ", 12, ACC))
    # T2
    s.append(f'<line x1="268" y1="104" x2="456" y2="104" stroke="{MUTED}" stroke-dasharray="5 4"/>')
    s.append(f'<rect x="392" y="148" width="76" height="34" fill="{PAPER}"/>' + t(430, 160, "high สูงสุด", 12, MUTED, "middle") + t(430, 176, "ของ 2 แท่ง", 12, MUTED, "middle"))
    s.append(f'<line x1="430" y1="140" x2="430" y2="108" stroke="{MUTED}" stroke-width="0.8"/>')
    s.append(candle(296, 104, 116, 160, 176, False))
    s.append(candle(332, 132, 144, 192, 204, False))
    s.append(candle(372, 72, 192, 84, 212, True))
    s.append(f'<line x1="388" y1="84" x2="404" y2="84" stroke="{ACC}" stroke-width="1.5" marker-end="url(#{slug}-arra)"/>')
    s.append(t(408, 80, "ปิดเหนือ", 12, ACC) + t(408, 96, "= สัญญาณ", 12, ACC))
    s.append(f'<line x1="8" y1="236" x2="472" y2="236" stroke="{RULE}" stroke-width=".8"/>')
    s.append(f'<rect x="8" y="248" width="12" height="12" fill="{INK}"/>' + t(26, 259, "แท่งลง (แดง)", 12, MUTED))
    s.append(f'<rect x="124" y="248" width="12" height="12" fill="{PAPER}" stroke="{INK}"/>' + t(142, 259, "แท่งขึ้น (เขียว)", 12, MUTED))
    s.append(t(472, 259, "ฝั่งขายใช้กฎกลับด้าน", 12, MUTED, "end"))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ diagram: test pipeline (flowchart)
def pipeline(slug):
    W, H = 480, 548
    x, w, h = 90, 300, 52
    ys = [8, 88, 168, 248, 328]
    names = [("ข้อมูลราคา M5 ปี 2019 ถึง 9 ต.ค. 2025", "Dukascopy", "1"),
             ("ค้นหากฎในข้อมูลส่วนแรก", "in-sample", "2"),
             ("จดกฎ SL/TP และเกณฑ์ผ่านลงไฟล์", "ลงทะเบียนล่วงหน้า + hash", "3"),
             ("เปิดข้อมูลส่วนที่ล็อกไว้ ทดสอบครั้งเดียว", "out-of-sample", "4"),
             ("หักต้นทุน $0.28 ต่อไม้ แล้วเช็ก", "ชนะเกินจุดคุ้มทุน และ PF ≥ 1.2 ?", "5")]
    s = [svg_open(slug, W, H, "ขั้นตอนทดสอบกฎเทรดของเรา",
                  "ค้นหาในข้อมูลส่วนแรก จดกฎก่อน แล้วทดสอบกับข้อมูลที่ล็อกไว้ครั้งเดียวหลังหักต้นทุน ไม่ผ่านก็จบ")]
    # arrows first
    for a, b in zip(ys, ys[1:]):
        s.append(vline(slug, x + w / 2, a + h, b))
    s.append(vline(slug, 190, 380, 436, label="ผ่าน", side="left"))
    s.append(vline(slug, 290, 380, 436, accent=True, label="ไม่ผ่าน"))
    for (n, sub, tag), y in zip(names, ys):
        s.append(node(x, y, w, h, n, sub, "", focal=(tag == "3")))
    s.append(node(28, 436, 200, 60, "ทดสอบต่อในบัญชีเดโม", "ยังไม่มีระบบไหนมาถึง", dashed=True))
    s.append(node(252, 436, 200, 60, "จบ ไม่แก้กฎแล้วลองซ้ำ", "บนข้อมูลชุดเดิม", focal=True))
    s.append(t(240, 528, "ข้อมูลตั้งแต่ 10 ต.ค. 2025 ยังล็อกไว้ ไม่ได้ใช้ (ยกเว้นงานแม่ปลาฯ และ ACME)", 12, MUTED, "middle"))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ diagram: live watcher
def watcher(slug):
    W, H = 480, 420
    x, w, h = 90, 300, 52
    ys = [8, 88, 168, 248]
    names = [("อ่านราคา Dukascopy ทุกชั่วโมง", "ทอง M5", ""),
             ("หาแท่ง T1 / T2", "ซื้อหรือขาย", ""),
             ("รอ 24 แท่ง", "= 2 ชั่วโมง", ""),
             ("ราคาปิดแท่งที่ 24 ไปทางสัญญาณไหม", "นับถูก / ผิด", "")]
    s = [svg_open(slug, W, H, "ตัวเฝ้าสัญญาณแท่งกลืนกิน ทำงานอย่างไร",
                  "อ่านราคาทุกชั่วโมง หาแท่ง T1 T2 รอ 24 แท่งแล้วดูว่าราคาไปทางสัญญาณไหม ไม่มีการส่งคำสั่ง")]
    for a, b in zip(ys, ys[1:]):
        s.append(vline(slug, x + w / 2, a + h, b))
    s.append(vline(slug, x + w / 2, 300, 336, accent=True))
    for (n, sub, tag), y in zip(names, ys):
        s.append(node(x, y, w, h, n, sub, tag))
    s.append(node(x, 336, w, 56, "ถูกทาง 99 จาก 192 = 51.6%", "12-17 ต.ค. 2026", focal=True))
    s.append(t(240, 412, "ไม่มีการส่งคำสั่งซื้อขายจริง แค่นับผล", 12, MUTED, "middle"))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ diagram: where demo bot profit came from
def martingale(slug):
    W, H = 480, 300
    s = [svg_open(slug, W, H, "กำไรของบอทเดโมมาจากไหน",
                  "เทคนิคเดียวกัน ถ้าเพิ่ม lot หลังแพ้ได้บวก 340.60 ดอลลาร์ ถ้าใช้ lot คงที่ได้ลบ 41.27 ดอลลาร์")]
    s.append(elbow(slug, 200, 64, 124, 112))
    s.append(elbow(slug, 280, 64, 356, 112))
    s.append(vline(slug, 124, 164, 208))
    s.append(vline(slug, 356, 164, 208, accent=True))
    s.append(node(90, 8, 300, 56, "เทคนิคของบอท T01 / T06 / T08 / T15", "PF 0.61 ถึง 0.86 ที่ความเสี่ยงคงที่"))
    s.append(node(24, 112, 200, 52, "เพิ่ม lot หลังแพ้", "martingale"))
    s.append(node(256, 112, 200, 52, "lot คงที่ทุกไม้", "ปรับประวัติดีลใหม่"))
    s.append(node(24, 208, 200, 56, "MCM1  +$340.60", "ที่เห็นในบัญชีเดโม"))
    s.append(node(256, 208, 200, 56, "MCM1  -$41.27", "กำไรจริงของเทคนิค", focal=True))
    s.append(t(240, 290, "ที่มา: REPORT.md, results/kai_demo_analysis.md", 12, MUTED, "middle"))
    s.append("</svg>")
    return "".join(s)

# ------------------------------------------------------------------ diagram: 7-year data split
def split_bar(slug):
    W, H = 480, 132
    segs = [("ค้นหา 70%", "2019 ถึง ก.ย. 2023", 4.7, PAPER2, INK),
            ("ทดสอบ 30%", "ก.ย. 2023 ถึง 9 ต.ค. 2025", 2.1, "#f6e6df", ACC),
            ("ยังล็อกไว้", "ตั้งแต่ 10 ต.ค. 2025", 1.0, PAPER, MUTED)]
    tot = sum(s_[2] for s_ in segs)
    s = [svg_open(slug, W, H, "การแบ่งข้อมูล 7 ปีของงาน MAE/MFE",
                  "70 เปอร์เซ็นต์แรกใช้ค้นหา 30 เปอร์เซ็นต์หลังใช้ทดสอบหลังล็อก SL TP ข้อมูลหลัง 10 ต.ค. 2025 ยังไม่ได้ใช้")]
    x = 8
    for i, (name, dates, yrs, fill, stroke) in enumerate(segs):
        w = (W - 16) * yrs / tot
        dash = ' stroke-dasharray="4 3"' if i == 2 else ""
        s.append(f'<rect x="{x:.1f}" y="40" width="{w-4:.1f}" height="40" fill="{fill}" stroke="{stroke}"{dash}/>')
        if i < 2:
            s.append(t(x + 8, 65, name, 14, stroke, "start", "", 600))
            s.append(t(x + 2, 100, dates, 12, MUTED, "start"))
        else:
            s.append(t(W - 8, 28, name + " ↓", 14, stroke, "end", "", 600))
            s.append(t(W - 8, 118, dates, 12, MUTED, "end"))
        x += w
    s.append("</svg>")
    return "".join(s)
