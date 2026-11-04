"""SIW v2 exit v4 backtest: SL $10 / TP $20 cap / close at close of L+2 (10 min). Refreshed Dukascopy CSV."""
import pandas as pd, numpy as np, siw
df=siw.load('duka_xau_m5_bid_refreshed.csv')
HIS=["11-03 13:50","11-03 12:00","11-03 04:55","11-02 23:50","11-02 23:15","11-02 22:05","11-02 19:50","11-02 14:05","11-02 11:10","11-02 10:00","11-02 06:00","10-30 18:00","10-30 14:05","10-30 05:15","10-29 23:55","10-29 18:35","10-29 15:15","10-29 10:10","10-29 08:20","10-29 04:45"]
idx={t:i for i,t in df.srv.items()}
his=pd.DataFrame([dict(i=idx[pd.Timestamp('2026-'+x)]) for x in HIS]); his['dir']=['B' if df.e21[i]>df.e55[i] else 'S' for i in his.i]
allv=siw.detect(df)
today=pd.DataFrame([dict(i=int(df.index[df.ict==pd.Timestamp(s)][0]),dir='B') for s in ['2026-11-04 06:45','2026-11-04 09:30'] if (df.ict==pd.Timestamp(s)).any()])
rows=[];det=[]
for nm,S in [('all SIW v2',allv),('his 20 picks',his),('his 2 buys Nov4',today)]:
  for d in ['S','B','all']:
    s=S if d=='all' else S[S.dir==d]; s=s[s.i+2<len(df)]
    if not len(s): continue
    r=[siw.outcome_v4(df,int(x.i)+1,x.dir) for x in s.itertuples()]; p=np.array([b for _,b in r]); k=pd.Series([a for a,_ in r]).value_counts().to_dict()
    rows.append(dict(set=nm,dir=d,n=len(p),win=f"{(p>0).mean():.0%}",total=p.sum(),avg=p.mean(),worst=p.min(),best=p.max(),exits=' '.join(f"{a}:{b}" for a,b in k.items())))
for x in today.itertuples():
    k,p=siw.outcome_v4(df,x.i+1,'B'); det.append(f"- confirm {df.ict[x.i]:%m-%d %H:%M} ICT, entry {df.o[x.i+1]:.2f} @ {df.ict[x.i+1]:%H:%M}, exit by {df.ict[x.i+2]+pd.Timedelta(minutes=5):%H:%M} ICT -> {k} {p:+.2f} (EMA21>EMA55: {df.e21[x.i]>df.e55[x.i]}, SIW detects: {x.i in set(allv.i)})")
T=pd.DataFrame(rows)
md=(f"# SIW v2 exit v4 — SL $10 / TP $20 cap / time exit 10 min\nData: Dukascopy XAU/USD BID M5 {df.ict.iloc[0]:%Y-%m-%d %H:%M} → {df.ict.iloc[-1]:%Y-%m-%d %H:%M} ICT ({len(df)} bars). "
"Entry = open of L+1; per bar SL checked before TP (worst case); else exit at close of L+2. $ per 0.01 lot after $0.28 cost. all SIW v2 = detect() default (dedupe=1).\n\n"
"**IN-SAMPLE, ~1 week, rules tuned on the same data. Not proof of edge.**\n\n"+T.to_markdown(index=False,floatfmt='.2f')+"\n\n## His 2 buys Nov 4\n"+"\n".join(det)+"\n")
open('exit_v4.md','w').write(md); T.to_csv('exit_v4.csv',index=False); print(md)
