import sys;sys.path.insert(0,'/workspace/fx-research');from _r237_239_eng import *
idx=np.where((hr==7)&(mi==0))[0];idx=idx[idx>20]
ok=(hr[idx-1]==6)&(mi[idx-1]==55)&(day[idx-1]==day[idx]);idx=idx[ok];res=[];cnt={}
for lam in(.3,.6):
 for f in(.5,.7):
  for sm in('beyond_open','half_gap'):
   for tm in(1.5,2.0):
    sig=[];drs=[];sls=[]
    for i in idx:
      Ca=c[i-1];Ol=o[i];G=Ol-Ca;A=atr[i-1]
      if np.isnan(A) or abs(G)<lam*A or G==0: continue
      F=Ca+f*G
      for k in range(i,i+12):
        if (G>0 and c[k]<=F) or (G<0 and c[k]>=F):
          if k+1>=n: break
          dr=-np.sign(G);en=o[k+1]
          sl=max(abs((Ol+np.sign(G)*.25*A)-en),1) if sm=='beyond_open' else max(.5*abs(G),1)
          sig.append(k);drs.append(dr);sls.append(sl);break
    res.append(stats(sim(sig,drs,sls,tm),dict(lam=lam,f=f,SLmode=sm,TPm=tm)))
finish(res,6426,'R238','xau_m5_asia_ldn_gapfill_20261101','Asia 06:55 close→LDN 07:00 open gap |G|≥λ·ATR, FADE on first 07:xx close crossing C_asia+f·G, SL beyond open/0.5|G|, TP1.5/2×SL T12, 1/day',['lam','f','SLmode','TPm'])
