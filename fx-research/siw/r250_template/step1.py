import sys;sys.path.insert(0,'..');import siw,pandas as pd,numpy as np
df=siw.load('../duka_xau_m5_bid_refreshed.csv')
tr=np.maximum(df.h-df.l,np.maximum(abs(df.h-df.c.shift()),abs(df.l-df.c.shift())));df['atr14']=tr.ewm(alpha=1/14,adjust=False).mean()
s=siw.detect(df);s['ict_conf']=df.ict[s.i].values
s=s[(s.ict_conf>=pd.Timestamp('2026-11-03'))&(s.ict_conf<pd.Timestamp('2026-11-04'))&(s.i+2<len(df))]
R=[]
for r in s.itertuples():
  k,p=siw.outcome_v4(df,r.i+1,r.dir);L=df.loc[r.i];rng=L.h-L.l;top,bot=max(L.o,L.c),min(L.o,L.c)
  R.append(dict(i=r.i,conf_ict=r.ict_conf,dir=r.dir,kind=r.kind,entry=r.entry,exit=k,pnl=round(p,2),body=abs(L.c-L.o)/rng,uw=(L.h-top)/rng,lw=(bot-L.l)/rng,green=L.c>L.o,rng=rng,
   atr=L.atr14,rng_atr=rng/L.atr14,gap_atr=(L.e21-L.e55)/L.atr14,s21_atr=(L.e21-df.e21[r.i-3])/L.atr14,s55_atr=(L.e55-df.e55[r.i-3])/L.atr14,d21_atr=(L.c-L.e21)/L.atr14,leg=r.leg_dist,leg_atr=r.leg_dist/L.atr14,
   p1=('G' if df.c[r.i-1]>df.o[r.i-1] else 'R'),p2=('G' if df.c[r.i-2]>df.o[r.i-2] else 'R'),p3=('G' if df.c[r.i-3]>df.o[r.i-3] else 'R'),
   net3_atr=(df.c[r.i-1]-df.o[r.i-3])/L.atr14,hr_utc=df.utc[r.i].hour))
T=pd.DataFrame(R).sort_values('pnl',ascending=False);T.to_csv('nov3_signals.csv',index=False)
pd.set_option('display.width',300);print(len(T));print(T.round(3).to_string())
