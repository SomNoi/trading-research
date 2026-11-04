import pandas as pd,numpy as np
from scipy.stats import norm
d=pd.read_csv('/workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv');lo=d.low.values;hi=d.high.values
T=pd.read_csv('../r249_ic/trades.csv');B=T[T.dedupe==1].copy()
def keep(i,side,K,mode):
  if i-2-K<0: return False
  if mode=='SET':
    if side=='BUY': return lo[i-2:i+1].min()<=lo[i-2-K:i-2].min()
    return hi[i-2:i+1].max()>=hi[i-2-K:i-2].max()
  if side=='BUY': return lo[i]<=lo[i-K:i].min()
  return hi[i]>=hi[i-K:i].max()
def dd3(x):
  out=[];last={}
  for idx,r in x.sort_values('i').iterrows():
    if r.i-last.get(r.side,-99)>=3: out.append(idx);last[r.side]=r.i
  return x.loc[out]
def st(x):
  if len(x)==0: return dict(n=0)
  g=x.pnl[x.pnl>0].sum();b=-x.pnl[x.pnl<0].sum()
  return dict(n=len(x),win=(x.pnl>0).mean(),E=x.pnl.mean(),E15=x.pnl15.mean(),PF=g/b,tot=x.pnl.sum(),tot15=x.pnl15.sum(),Z=x.pnl.mean()/x.pnl.std()*np.sqrt(len(x)))
N=6670;zb=norm.isf(.05/N);rows=[];allT=[]
vars_=[('BASE_R249',0,None),('SET_K5',5,'SET'),('SET_K6',6,'SET'),('LONLY_K5',5,'L')]
for nm,K,m in vars_:
  x=B if m is None else B[[keep(r.i,r.side,K,m) for r in B.itertuples()]]
  for dd in(1,3):
    y=x if dd==1 else dd3(x)
    if m: allT.append(y.assign(variant=nm,dedupe=dd))
    for sd in('BUY','SELL'):
      z=y[y.side==sd];r=dict(variant=nm,dedupe=dd,side=sd,counted=m is not None)
      for p,g in(('IS',z[z.IS]),('OOS',z[~z.IS])): r.update({f'{p}_{a}':v for a,v in st(g).items()})
      r['gate']='baseline' if m is None else ('PASS' if r['OOS_n']>=100 and r['IS_E']>0 and r['OOS_E']>0 and r['OOS_Z']>=zb and r['OOS_E15']>0 else 'fail')
      rows.append(r)
M=pd.DataFrame(rows);M.to_csv('results_main.csv',index=False);pd.concat(allT).to_csv('trades.csv',index=False)
print('zb',round(zb,3));pd.set_option('display.width',300)
print(M[['variant','dedupe','side','IS_n','IS_win','IS_E','IS_PF','IS_tot','IS_E15','IS_Z','OOS_n','OOS_win','OOS_E','OOS_PF','OOS_tot','OOS_E15','OOS_tot15','OOS_Z','gate']].round(3).to_string())
