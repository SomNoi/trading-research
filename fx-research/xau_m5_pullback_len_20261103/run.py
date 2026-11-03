import sys;sys.path.insert(0,'/workspace/fx-research')
from _r237_239_eng import d,o,h,l,c,n,IS,t
import numpy as np,pandas as pd
e21=pd.Series(c).ewm(span=21,adjust=False).mean().values;e55=pd.Series(c).ewm(span=55,adjust=False).mean().values
body=np.abs(c-o);rng=h-l;uw=h-np.maximum(o,c);lw=np.minimum(o,c)-l
def sigs(dr):
  pc,po=np.r_[np.nan,c[:-1]],np.r_[np.nan,o[:-1]]
  if dr<0:
    star=(uw>=2*body)&(lw<=body)&(rng>0)&(np.minimum(o,c)<=l+rng/3)
    eng=(c<o)&(pc>po)&(o>=pc)&(c<=po)
    ema=(c<o)&(h>=e21)&(c<e21)
    trend=e21<e55
  else:
    star=(lw>=2*body)&(uw<=body)&(rng>0)&(np.maximum(o,c)>=h-rng/3)
    eng=(c>o)&(pc<po)&(o<=pc)&(c>=po)
    ema=(c>o)&(l<=e21)&(c>e21)
    trend=e21>e55
  return (star|eng|ema)&trend
def run(dr,T=48,cost=.28):
  S=sigs(dr);ev=[];busy=-1
  for s in range(60,n-1):
    if not S[s]: continue
    # count pullback bars back from s-1
    k=0;j=s-1
    while j>0 and ((dr<0 and (h[j]>h[j-1] or c[j]>o[j])) or (dr>0 and (l[j]<l[j-1] or c[j]<o[j]))):
      k+=1;j-=1
    # j = leg bar: must be a full trend bar making new extreme
    leg=(dr<0 and c[j]<o[j] and l[j]<l[j-1]) or (dr>0 and c[j]>o[j] and h[j]>h[j-1])
    if not leg or k==0: continue
    e=s+1
    if e<=busy or e+T>n: continue
    en=o[e];sl=(h[s]+.30) if dr<0 else (l[s]-.30);R=abs(en-sl)
    if (dr<0 and sl<=en) or (dr>0 and sl>=en): continue
    tp=en-dr*1.5*R if False else en+dr*1.5*R;p=None
    for q in range(e,e+T):
      if dr<0:
        if h[q]>=sl: p=-R;break
        if l[q]<=tp: p=1.5*R;break
      else:
        if l[q]<=sl: p=-R;break
        if h[q]>=tp: p=1.5*R;break
    if p is None: p=dr*(c[q]-en)
    busy=q;ev.append(dict(dir='short' if dr<0 else 'long',k=min(k,5),k_raw=k,t=str(t.iloc[s]),IS=bool(IS[s]),R=R,usd=p-cost,r=(p-cost)/R))
  return ev
E=pd.DataFrame(run(-1)+run(1));E.to_csv('events.csv',index=False)
rows=[]
for (dr,k),g in E.groupby(['dir','k']):
  row=dict(dir=dr,len='5+' if k==5 else str(k))
  for nm,m in(('IS',g.IS),('OOS',~g.IS)):
    x=g[m];row.update({f'n_{nm}':len(x),f'hit_{nm}':round((x.usd>0).mean(),3),f'E$_{nm}':round(x.usd.mean(),2),f'ER_{nm}':round(x.r.mean(),3)})
  rows.append(row)
R=pd.DataFrame(rows);R.to_csv('results.csv',index=False);print(R.to_string(index=False))
print(E.groupby('dir').k.value_counts(normalize=True).round(3).unstack())
print('span',t.iloc[0],t.iloc[-1],'medR',E.groupby('dir').R.median())
