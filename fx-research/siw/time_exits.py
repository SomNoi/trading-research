import sys, pandas as pd, numpy as np
sys.path.append('/workspace/siw-alert/engine'); import fetch as F
import siw
raw=pd.read_csv('duka_xau_m5_bid.csv')
try:
    nb=pd.DataFrame(F.closed_only(F.fetch(500)))[['t','o','h','l','c','v']]
    raw=pd.concat([raw,nb]).drop_duplicates('t',keep='last').sort_values('t'); raw.to_csv('duka_xau_m5_bid_refreshed.csv',index=False)
except Exception as e: print('refresh failed',e)
raw.to_csv('/tmp/r.csv',index=False); df=siw.load('/tmp/r.csv')
# fix srv offset: siw.load uses Nov1 boundary; fine
C=0.28; O,H,Lo,Cl=df.o.values,df.h.values,df.l.values,df.c.values
def tx(i,d,n,sl=5.0):
    e=O[i+1]
    for j in range(i+1,min(i+1+n,len(df))):
        adv=(H[j]-e) if d=='S' else (e-Lo[j])
        if adv>=sl: return -sl-C,'SL'
    j=min(i+n,len(df)-1); return ((e-Cl[j]) if d=='S' else (Cl[j]-e))-C,'T'
allv=siw.detect(df)  # dedupe=1 research default
from exit_tuning import L as HIS
idx={t:i for i,t in df.srv.items()}
his=pd.DataFrame([dict(i=idx[pd.Timestamp('2026-'+x)]) for x in HIS]); his['dir']=['B' if df.e21[i]>df.e55[i] else 'S' for i in his.i]
# his 2 buys today: confirm 09:30 and 06:45 ICT Nov 4
t2=[]
for s in ['2026-11-04 06:45','2026-11-04 09:30']:
    m=df.index[df.ict==pd.Timestamp(s)]
    if len(m): t2.append(dict(i=int(m[0]),dir='B',ict=s))
today=pd.DataFrame(t2)
rows=[]
for nm,S in [('allv2',allv),('his20',his),('his_buys_nov4',today)]:
  for d in ['S','B','all']:
    s=S if d=='all' else S[S.dir==d]
    s=s[s.i+3<len(df)] if len(s) else s
    if not len(s): continue
    for n in (1,2,3):
      r=[tx(int(x.i),x.dir,n) for x in s.itertuples()]; p=np.array([a for a,_ in r])
      rows.append(dict(set=nm,dir=d,exit=f'{5*n}min',n=len(p),win=f"{(p>0).mean():.0%}",total=p.sum(),avg=p.mean(),worst=p.min(),best=p.max(),sl_hits=sum(b=='SL' for _,b in r)))
T=pd.DataFrame(rows)
det=[]
for x in today.itertuples():
    e=O[x.i+1]; det.append(f"- confirm {x.ict} ICT ({'' if df.e21[x.i]>df.e55[x.i] else 'NOTE: EMA21<EMA55 = counter-trend, '}detected by SIW: {x.i in set(allv.i)}) entry {e:.2f} @ {df.ict[x.i+1]:%H:%M} ICT: "+", ".join(f"{5*n}m {tx(x.i,'B',n)[0]:+.2f}" for n in (1,2,3)))
rng=f"{df.ict.iloc[0]:%Y-%m-%d %H:%M} → {df.ict.iloc[-1]:%Y-%m-%d %H:%M} ICT"
md=f"""# SIW v2 time exits: close at 5 / 10 / 15 min
Data: Dukascopy XAU/USD BID M5, {rng} ({len(df)} bars, refreshed with latest Dukascopy bars).
Entry = open of bar after the confirm bar. Exit = close of bar 1/2/3 after entry (5/10/15 min), hard SL $5 checked first in each bar (worst-case intrabar).
$ = price move per 0.01 lot (1 oz: $1 move = $1), minus $0.28 cost per trade (same convention as exit_v3.py). allv2 = all SIW v2 signals (modes abc, dedupe=1).

**IN-SAMPLE, small n, ~1 week of data. The rules were tuned on this same week. Treat it as a description of the data, not proof of an edge.**

{T.to_markdown(index=False,floatfmt='.2f')}

## His 2 buys today (Nov 4)
"""+"\n".join(det)+"\n"
open('time_exits_5_10_15.md','w').write(md); print(md)
