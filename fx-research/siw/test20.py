import pandas as pd, siw
df = siw.load('duka_xau_m5_bid.csv')
L = ["11-03 13:50","11-03 12:00","11-03 04:55","11-02 23:50","11-02 23:15","11-02 22:05","11-02 19:50","11-02 14:05","11-02 11:10","11-02 10:00","11-02 06:00","10-30 18:00","10-30 14:05","10-30 05:15","10-29 23:55","10-29 18:35","10-29 15:15","10-29 10:10","10-29 08:20","10-29 04:45"]
L = [pd.Timestamp('2026-'+x) for x in L]; idx = {t: i for i, t in df.srv.items()}
def window(s): return s[(s.conf_srv >= '2026-10-29') & (s.conf_srv < '2026-11-04')]
def stats(rows, p={}):
    if not len(rows): return 'n=0'
    o = [siw.outcome(df, r.i+1, r.dir, p) for _, r in rows.iterrows()]; res = [x[0] for x in o]; pnl = sum(x[1] for x in o)
    w = res.count('TP'); return f"n={len(o)} TP{w}/SL{res.count('SL')}/TO{res.count('TO')} win {w/len(o):.0%} net ${pnl:+.2f}/0.01"
def split(rows, p={}):
    return ' | '.join(f"{d}: {stats(rows[rows.dir==d], p)}" for d in 'SB')
configs = [('abc', {}), ('abc dd3', {'dedupe':3}), ('bc', {'modes':'bc'}), ('a', {'modes':'a'}), ('b', {'modes':'b'}), ('c', {'modes':'c'}), ('ab', {'modes':'ab'}), ('ac', {'modes':'ac'}), ('bc', {'modes':'bc'}),
           ('abc+zone3', {'zone_max':3}), ('abc+touch', {'touch':True}), ('abc+zone3+touch', {'zone_max':3,'touch':True}), ('abc ext5', {'max_ext':5}), ('abc ext15', {'max_ext':15})]
for lab, p in configs:
    s = window(siw.detect(df, p)); ex = sum(any(s.i == idx[t]) for t in L); n1 = sum(any((s.i-idx[t]).abs() <= 1) for t in L)
    print(f"[{lab:16s}] signals {len(s):3d} (S{sum(s.dir=='S')}/B{sum(s.dir=='B')})  catch exact {ex}/20 ±1 {n1}/20 | all: {stats(s)} || {split(s)}")
s = window(siw.detect(df, {})); print('\nPer pick (abc default):')
for t in L:
    i = idx[t]; b = df.loc[i]; d = 'B' if b.e21 > b.e55 else 'S'; m = s[s.i == i]; m1 = s[(s.i-i).abs() <= 1]
    why = ''
    if m.empty:
        k = siw.classify(df, i, d, siw.P); w = df.loc[i-11:i]; dist = (w.h.max()-b.c) if d=='S' else (b.c-w.l.min())
        why = f"pattern={k} legdist={dist:.2f} EMAdir={d} bar o{b.o:.2f} h{b.h:.2f} l{b.l:.2f} c{b.c:.2f} | prev o{df.loc[i-1].o:.2f} h{df.loc[i-1].h:.2f} l{df.loc[i-1].l:.2f} c{df.loc[i-1].c:.2f}"
        if k and dist > 10: why = 'EXT>10 ' + why
        elif not k: why = 'NO PATTERN ' + why
        else: why = 'DEDUPE ' + why
    print(t.strftime('%m-%d %H:%M'), d, 'Y '+m.iloc[0].kind if len(m) else ('±1 '+m1.iloc[0].kind+' @'+m1.iloc[0].conf_srv.strftime('%H:%M') if len(m1) else '-'), why)
rows = pd.DataFrame([dict(i=idx[t], dir=('B' if df.loc[idx[t]].e21 > df.loc[idx[t]].e55 else 'S')) for t in L])
print('\nHis 20 as given (entry = open of listed+1, dir = EMA rule):', stats(rows), '||', split(rows))
c = s[s.i.isin(rows.i)]; o = s[~s.i.isin(rows.i)]
print('v2 signals matching his picks:', stats(c)); print('v2 signals NOT in his picks:', stats(o)); print('ALL v2 abc:', stats(s), '||', split(s))
for lab, p in configs[7:10]:
    print(f"{lab}: ", stats(window(siw.detect(df, p))))
window(siw.detect(df, {})).to_csv('siw2_signals_oct29_nov3.csv', index=False)
