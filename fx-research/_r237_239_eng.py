import pandas as pd,numpy as np
from scipy.stats import norm
d=pd.read_csv('/workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv',parse_dates=['time_utc'])
o,h,l,c,v=[d[k].values.astype(float) for k in['open','high','low','close','tick_volume']]
t=d.time_utc;day=t.dt.date.values;hr=t.dt.hour.values;mi=t.dt.minute.values
days=np.array(sorted(set(day)));cut=days[int(len(days)*.6)];IS=day<cut
pc=np.r_[np.nan,c[:-1]];tr=np.nanmax(np.c_[h-l,np.abs(h-pc),np.abs(l-pc)],1)
atr=pd.Series(tr).rolling(14).mean().values;n=len(o);ldnny=(hr>=7)&(hr<=19)
def sim(sig,dirs,sld,tpm,T=12,cost=.28):
  out=[];busy=-1
  for s,dr,sl in zip(sig,dirs,sld):
    e=s+1
    if e<=busy or e+T>n: continue
    en=o[e];tp=tpm*sl;p=None
    for k in range(e,e+T):
      if dr>0:
        if l[k]<=en-sl: p=-sl;break
        if h[k]>=en+tp: p=tp;break
      else:
        if h[k]>=en+sl: p=-sl;break
        if l[k]<=en-tp: p=tp;break
    if p is None: p=dr*(c[k]-en)
    busy=k;out.append((e,(p-cost)/sl,p-cost))
  return np.array(out).reshape(-1,3)
def stats(tr,row):
  for k in('IS','OOS'):
    m=IS[tr[:,0].astype(int)] if k=='IS' else ~IS[tr[:,0].astype(int)] if len(tr) else np.array([],bool)
    x=tr[m,1] if len(tr) else np.array([]);u=tr[m,2] if len(tr) else np.array([]);gl=-x[x<0].sum()
    row.update({f'n_{k}':len(x),f'E_{k}':x.mean() if len(x) else np.nan,f'Eusd_{k}':u.mean() if len(u) else np.nan,
      f'PF_{k}':x[x>0].sum()/gl if gl>0 else np.nan,f'WR_{k}':(x>0).mean() if len(x) else np.nan,
      f'z_{k}':x.mean()/x.std(ddof=1)*np.sqrt(len(x)) if len(x)>2 else np.nan})
  row['PASS']=bool(row['PF_OOS']>=1.2 and row['n_OOS']>=50 and row['E_IS']>0 and row['E_OOS']>0);return row
def zb(N): return round(float(norm.isf(.05/N)),3)
def finish(res,N,rid,folder,desc,keys):
  import json,os
  r=pd.DataFrame(res);r.to_csv('results.csv',index=False)
  b=r.sort_values('E_OOS',ascending=False).iloc[0];Z=zb(N);P=int(r.PASS.sum());op=int((r.E_OOS>0).sum())
  verdict='ไม่เจอ' if (P==0 or b.z_OOS<Z) else 'soft-pass (below Bonferroni)'
  if P>0 and b.z_OOS<Z: verdict='ไม่เจอ (soft-pass cells %d but z<Z_bonf)'%P
  bk=' '.join(f'{k}={b[k]}' for k in keys)
  line=f"- {rid} {folder} — {desc} — {verdict}. best {bk} OOS E{b.E_OOS:+.3f}R (${b.Eusd_OOS:+.2f}/0.01lot) PF{b.PF_OOS:.2f} z{b.z_OOS:.2f} n{int(b.n_OOS)} (IS E{b.E_IS:+.3f}R n{int(b.n_IS)}); OOS>0 {op}/16; gate-PASS {P}/16; Z_bonf {Z}; N={N}."
  json.dump(dict(N_TRIALS=N,Z_BONF=Z,added=16,**{'pass':P}),open('multiple_testing.json','w'),indent=1)
  pd.set_option('display.width',250)
  open('REPORT.md','w').write(f"# {rid} REPORT\nPREREG locked (sha256 in PREREG.sha256). Cut {cut}.\n\n{line}\n\n```\n{r.round(3).to_string()}\n```\n")
  open('EXEC_SUMMARY.md','w').write(f"# {rid} EXEC SUMMARY\n{line}\n")
  print(line);print(r.round(3).to_string());return line
