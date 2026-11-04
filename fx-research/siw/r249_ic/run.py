import sys;sys.path.insert(0,'..');import siw,pandas as pd,numpy as np
from scipy.stats import norm
d=pd.read_csv('/workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv')
lab=pd.to_datetime(d.time_utc.str[:19]);srv=lab+pd.Timedelta('3h')
dst=srv.dt.tz_localize('America/New_York',ambiguous=True,nonexistent='shift_forward').map(lambda x:x.dst()!=pd.Timedelta(0)).values
utc=lab+pd.to_timedelta(np.where(dst,0,1),unit='h')
df=pd.DataFrame(dict(o=d.open,h=d.high,l=d.low,c=d.close,srv=srv,utc=utc,ict=utc+pd.Timedelta('7h')))
df['e21']=df.c.ewm(span=21,adjust=False).mean();df['e55']=df.c.ewm(span=55,adjust=False).mean()
days=df.srv.dt.date.values;ud=np.unique(days);cut=ud[int(len(ud)*.6)]
out=[]
for dd in(1,3):
  s=siw.detect(df,dict(dedupe=dd))
  for _,r in s.iterrows():
    if r.i+2>=len(df): continue
    k,p=siw.outcome_v4(df,r.i+1,r.dir);u=df.utc[r.i]
    out.append(dict(dedupe=dd,i=r.i,side='SELL' if r.dir=='S' else 'BUY',kind=r.kind,pat=r.kind[0] if r.kind[0]!='A' else r.kind,conf_srv=r.conf_srv,entry_srv=r.entry_srv,entry_ict=df.ict[r.i+1],entry=r.entry,exit=k,pnl=p,pnl15=p-.14,IS=days[r.i]<cut,hr=u.hour,month=r.conf_srv.strftime('%Y-%m')))
T=pd.DataFrame(out);T['sess']=pd.cut(T.hr,[-1,6,11,20,24],labels=['Asia','London','NY','Late']);T.to_csv('trades.csv',index=False)
def st(x):
  if len(x)==0: return dict(n=0)
  g=x.pnl[x.pnl>0].sum();b=-x.pnl[x.pnl<0].sum();eq=x.pnl.cumsum()
  return dict(n=len(x),win=(x.pnl>0).mean(),E=x.pnl.mean(),E15=x.pnl15.mean(),tot=x.pnl.sum(),PF=g/b if b else np.nan,DD=(eq.cummax()-eq).max(),Z=x.pnl.mean()/x.pnl.std()*np.sqrt(len(x)))
zb=norm.isf(.05/6646);rows=[]
for dd in(1,3):
  for sd in['SELL','BUY','ALL']:
    x=T[(T.dedupe==dd)&((T.side==sd)|(sd=='ALL'))];r=dict(dedupe=dd,side=sd)
    for nm,g in(('IS',x[x.IS]),('OOS',x[~x.IS]),('FULL',x)): r.update({f'{nm}_{a}':v for a,v in st(g).items()})
    m=x.groupby('month').pnl.sum();r['months_pos']=f'{(m>0).sum()}/{len(m)}'
    r['gate']='n/a' if sd=='ALL' else ('PASS' if r['OOS_n']>=100 and r['OOS_E']>0 and r['IS_E']>0 and r['OOS_Z']>=zb and r['OOS_E15']>0 else 'fail')
    rows.append(r)
M=pd.DataFrame(rows);M.to_csv('results_main.csv',index=False)
def brk(col):
  L=[]
  for (dd,sd,v),x in T.groupby(['dedupe','side',col],observed=True):
    r=dict(dedupe=dd,side=sd,**{col:v});[r.update({f'{nm}_{a}':b for a,b in st(g).items()}) for nm,g in(('IS',x[x.IS]),('OOS',x[~x.IS]))];L.append(r)
  return pd.DataFrame(L)
P=brk('pat');S=brk('sess');H=brk('hr');P.to_csv('by_pattern.csv',index=False);S.to_csv('by_session.csv',index=False);H.to_csv('by_hour.csv',index=False)
MO=T.groupby(['dedupe','side','month']).pnl.agg(['count','sum','mean']).reset_index();MO.to_csv('by_month.csv',index=False)
pd.set_option('display.width',300);pd.set_option('display.max_rows',200)
print('zb',zb,'cut',cut)
print(M[['dedupe','side','IS_n','IS_win','IS_E','IS_PF','OOS_n','OOS_win','OOS_E','OOS_E15','OOS_PF','OOS_Z','OOS_DD','FULL_tot','FULL_DD','months_pos','gate']].round(3).to_string())
c=['dedupe','side',None,'IS_n','IS_E','OOS_n','OOS_win','OOS_E','OOS_PF']
for nm,X in(('pat',P),('sess',S)): print(X[[nm if a is None else a for a in c]].round(3).to_string())
print(H[H.dedupe==1][['side','hr','IS_n','IS_E','OOS_n','OOS_E']].round(2).to_string())
print(MO[MO.dedupe==1].pivot(index='month',columns='side',values='sum').round(1).to_string())
print(T.exit.value_counts())
