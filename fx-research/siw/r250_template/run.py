import sys;sys.path.insert(0,'..');sys.path.insert(0,'../../scripts');import siw,pandas as pd,numpy as np,json
from scipy.stats import norm;from fleet import fx
def feats(df):
  tr=np.maximum(df.h-df.l,np.maximum(abs(df.h-df.c.shift()),abs(df.l-df.c.shift())));a=tr.ewm(alpha=1/14,adjust=False).mean()
  rng=(df.h-df.l).clip(lower=1e-9);top=np.maximum(df.o,df.c);bot=np.minimum(df.o,df.c)
  F=pd.DataFrame(dict(body=(df.c-df.o).abs()/rng,uw=(df.h-top)/rng,lw=(bot-df.l)/rng,g=df.c>df.o,rng_atr=rng/a,gap=(df.e21-df.e55)/a,
   s21=(df.e21-df.e21.shift(3))/a,s55=(df.e55-df.e55.shift(3))/a,d21=(df.c-df.e21)/a,atr=a,hr=df.ict.dt.hour))
  F['g1']=F.g.shift(1);F['g2']=F.g.shift(2);return F
def fp(df,F,s):
  X=F.loc[s.i].reset_index(drop=True);sg=np.where(s.dir.values=='S',-1,1)
  X['side']=s.dir.values;X['kind']=s.kind.values;X['rej']=np.where(sg<0,X.uw,X.lw);X['oth']=np.where(sg<0,X.lw,X.uw)
  for c in['gap','s21','s55','d21']:X[c+'_a']=X[c]*sg
  X['leg_atr']=s.leg_dist.values/X.atr;X['i']=s.i.values;return X
# templates from Dukascopy
dk=siw.load('../duka_xau_m5_bid_refreshed.csv');Fd=feats(dk);tp=pd.read_csv('templates.csv')
sd=siw.detect(dk);sd=sd[sd.i.isin(tp.i)];TP=fp(dk,Fd,sd).set_index('i').loc[tp.i].reset_index();TP['name']=['T1','T2','T3']
TP.to_csv('templates_fingerprint.csv',index=False)
# IC data (as R249)
d=pd.read_csv('/workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv')
lab=pd.to_datetime(d.time_utc.str[:19]);srv=lab+pd.Timedelta('3h')
dst=srv.dt.tz_localize('America/New_York',ambiguous=True,nonexistent='shift_forward').map(lambda x:x.dst()!=pd.Timedelta(0)).values
utc=lab+pd.to_timedelta(np.where(dst,0,1),unit='h')
df=pd.DataFrame(dict(o=d.open,h=d.high,l=d.low,c=d.close,srv=srv,utc=utc,ict=utc+pd.Timedelta('7h')))
df['e21']=df.c.ewm(span=21,adjust=False).mean();df['e55']=df.c.ewm(span=55,adjust=False).mean()
days=df.srv.dt.date.values;ud=np.unique(days);cut=ud[int(len(ud)*.6)];F=feats(df)
fx('progress','R250 IC loaded, detecting',task='R250',pct=45)
s=siw.detect(df);s=s[s.i+2<len(df)].reset_index(drop=True);X=fp(df,F,s)
fx('heartbeat','R250 detect done',task='R250',status='ok')
hd=lambda a,b:np.minimum(abs(a-b),24-abs(a-b))
def match(t,tier):
  m=(X.side==t.side)&(X.kind==t.kind)&(abs(X.body-t.body)<=(.15 if tier=='TIGHT' else .2))&(hd(X.hr,t.hr)<=2)
  if tier=='TIGHT':
    m&=(X.g==t.g)&(X.g1==t.g1)&(X.g2==t.g2)&(abs(X.rej-t.rej)<=.2)&(abs(X.oth-t.oth)<=.2)&(abs(X.rng_atr-t.rng_atr)<=.4)&(abs(X.gap_a-t.gap_a)<=.75)&(abs(X.s21_a-t.s21_a)<=.25)&(abs(X.s55_a-t.s55_a)<=.2)&(abs(X.d21_a-t.d21_a)<=.5)&(abs(X.leg_atr-t.leg_atr)<=.5)
  else: m&=(abs(X.gap_a-t.gap_a)<=1)&(abs(X.d21_a-t.d21_a)<=.75)&(abs(X.leg_atr-t.leg_atr)<=.75)
  return m.values
pnl=np.array([siw.outcome_v4(df,i+1,dd)[1] for i,dd in zip(s.i,s.dir)]);X['pnl']=pnl;X['day']=days[s.i];X['IS']=X.day<cut;X['srv']=df.srv[s.i].values
newN=6646+12;zb=norm.isf(.05/newN)
def st(p):
  if len(p)==0:return dict(n=0)
  g=p[p>0].sum();b=-p[p<0].sum();return dict(n=len(p),win=(p>0).mean(),E=p.mean(),E15=(p-.14).mean(),PF=g/b if b else np.nan,Z=p.mean()/p.std()*np.sqrt(len(p)) if len(p)>1 else np.nan)
rng_=np.random.default_rng(250);key=lambda A:list(zip(A.side,A.hr,A.gap>0,A.IS))
# random pool: all IC bars with features
B=F.copy();B['IS']=days<cut;B=B.iloc[60:-3]
def randomE(M):
  E=[];grp={}
  for k in set(key(M)):
    sd_,hr,gp,IS=k;grp[k]=B.index[(B.hr==hr)&((B.gap>0)==gp)&(B.IS==IS)].values
  ks=key(M);out=[]
  for _ in range(500):
    tot=[]
    for k in ks:
      i=rng_.choice(grp[k]);tot.append(siw.outcome_v4(df,i+1,k[0])[1])
    out.append(np.mean(tot))
  return np.array(out)
rows=[];allm=[]
for tier in['TIGHT','LOOSE']:
  ms={t.name:match(t,tier) for t in TP.itertuples()}
  for nm,m in list(ms.items())+[('UNION',np.any(list(ms.values()),axis=0))]:
    M=X[m].sort_values('i');M=M.assign(tier=tier,set=nm);allm.append(M)
    caps=(1,2,3) if nm=='UNION' else (1,)
    for cap in caps:
      C=M.groupby('day').head(cap);r=dict(tier=tier,set=nm,cap=cap,days=C.day.nunique(),tpd=len(C)/max(C.day.nunique(),1))
      for lab_,g in(('IS',C[C.IS]),('OOS',C[~C.IS]),('FULL',C)):r.update({f'{lab_}_{a}':v for a,v in st(g.pnl.values).items()})
      if len(C[~C.IS]):rd=randomE(C[~C.IS]);r['RAND_OOS_E']=rd.mean();r['RAND_p_ge_obs']=(rd>=r['OOS_E']).mean()
      r['gate']='PASS' if r.get('OOS_n',0)>=100 and r.get('IS_E',-1)>0 and r.get('OOS_E',-1)>0 and r.get('OOS_E15',-1)>0 and r.get('OOS_Z',0)>=zb else 'fail'
      rows.append(r);fx('heartbeat',f'R250 {tier} {nm} cap{cap} done',task='R250',status='ok')
R=pd.DataFrame(rows);R.to_csv('results_main.csv',index=False);pd.concat(allm).to_csv('matches.csv',index=False)
pd.set_option('display.width',320);print('zb',zb,'newN',newN,'cut',cut);print(R.round(3).to_string())
