import pandas as pd,numpy as np
d=pd.read_csv('/workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv')
o,h,l,c=(d[x].values for x in('open','high','low','close'));n=len(d)
srv=(pd.to_datetime(d.time_utc.str[:19])+pd.Timedelta('3h')).dt.date.values
ud=np.unique(srv);cut=ud[int(len(ud)*.6)]
T=pd.read_csv('trades.csv');B=pd.read_csv('../r249_ic/trades.csv').assign(variant='BASE_R249')
A=pd.concat([B,T]);R=[]
for r in A.itertuples():
  s=1 if r.side=='BUY' else -1;e=o[r.i+1];k=0;j=r.i+1
  while j<n and s*(c[j]-o[j])>0: k+=1;j+=1
  last=r.i+max(k,1)  # run 0: use L+1 (the opposite bar)
  ex=(h[r.i+1:last+1].max()-e) if s>0 else (e-l[r.i+1:last+1].min())
  R.append((k,s*(c[last]-e),ex))
A[['run','move','mfe']]=R;A['bucket']=A.run.clip(upper=5).map(lambda x:'5+' if x==5 else str(int(x)))
A['split']=np.where(A.IS,'IS','OOS')
g=A.groupby(['variant','dedupe','side','split','bucket'])
F=g.agg(count=('run','size'),move_mean=('move','mean'),move_med=('move','median'),mfe_mean=('mfe','mean'),mfe_med=('mfe','median')).reset_index()
F['pct']=F['count']/F.groupby(['variant','dedupe','side','split'])['count'].transform('sum')
F=F[['variant','dedupe','side','split','bucket','count','pct','move_mean','move_med','mfe_mean','mfe_med']];F.round(3).to_csv('followthrough.csv',index=False)
P=[]
for (v,dd,sd),x in A.groupby(['variant','dedupe','side']):
  cnt=x.groupby(srv[x.i.values]).size().reindex(ud,fill_value=0)
  for sp,m in(('IS',ud<cut),('OOS',ud>=cut)):
    y=cnt[m];hs=y.clip(upper=4).value_counts().reindex(range(5),fill_value=0)
    P.append(dict(variant=v,dedupe=dd,side=sd,split=sp,days=len(y),mean=y.mean(),median=y.median(),max=y.max(),**{('d4+' if i==4 else f'd{i}'):hs[i] for i in range(5)}))
P=pd.DataFrame(P);P.round(2).to_csv('signals_per_day.csv',index=False)
pd.set_option('display.width',250);pd.set_option('display.max_rows',500)
print(F[F.dedupe==1].round(2).to_string(index=False));print(P.round(2).to_string(index=False))
