import sys;sys.path.insert(0,'/workspace/fx-research')
from _r237_239_eng import *
lt=t.dt.tz_convert('Europe/London') if t.dt.tz is not None else t.dt.tz_localize('UTC').dt.tz_convert('Europe/London')
lhm=(lt.dt.hour*100+lt.dt.minute).values;ldate=lt.dt.date.values
def atrL(L): return np.r_[np.nan,pd.Series(tr).rolling(L).mean().values[:-1]]
def simlv(trades,cost=.28):
  # trades: (e,dir,sl_level,tp_level or nan,x_last)
  out=[];busy=-1
  for e,dr,sll,tpl,xl in trades:
    if e<=busy or xl>=n: continue
    en=o[e];R=abs(en-sll)
    if R<=0 or (dr>0 and sll>=en) or (dr<0 and sll<=en): continue
    p=None
    for k in range(e,xl+1):
      if dr>0:
        if l[k]<=sll: p=sll-en;break
        if tpl==tpl and h[k]>=tpl: p=tpl-en;break
      else:
        if h[k]>=sll: p=en-sll;break
        if tpl==tpl and l[k]<=tpl: p=en-tpl;break
    if p is None: p=dr*(c[k]-en)
    busy=k;out.append((e,(p-cost)/R,p-cost))
  return np.array(out).reshape(-1,3)
def bar_at(hm):  # dict ldate->index of bar with London start hm
  idx=np.where(lhm==hm)[0];return dict(zip(ldate[idx],idx))
