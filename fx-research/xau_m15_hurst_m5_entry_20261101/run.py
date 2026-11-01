import sys;sys.path.insert(0,'/workspace/fx-research');from _r237_239_eng import *
s=pd.Series(c,index=t);m15=s.resample('15min',label='left').last().dropna()
lr=np.log(m15).diff();r4=np.log(m15).diff(4)
sma=pd.Series(c).rolling(20).mean().values;sd=pd.Series(c).rolling(20).std().values;z=(c-sma)/sd;pz=np.r_[np.nan,z[:-1]]
slope=sma-np.r_[[np.nan]*3,sma[:-3]]
ph=np.r_[np.nan,h[:-1]];pph=np.r_[np.nan,np.nan,h[:-2]];pl=np.r_[np.nan,l[:-1]];ppl=np.r_[np.nan,np.nan,l[:-2]];pcl=np.r_[np.nan,c[:-1]]
bl=(c>ph)&~(pcl>pph)&(slope>0);bs=(c<pl)&~(pcl<ppl)&(slope<0);res=[]
for W in(64,128):
  vr=(r4.rolling(W).var()/(4*lr.rolling(W).var()))
  # bar M15 starting at T completes at T+15; available for M5 bars whose close>=T+15 i.e. M5 start>=T+10
  vr.index=vr.index+pd.Timedelta('10min')
  VR=vr.reindex(t,method='ffill').values
  MR=VR<=.9;TR=VR>=1.1
  for th in(2.0,2.5):
    fm=MR&(np.abs(z)>=th)&(np.abs(pz)<th);fd=-np.sign(z)
    for S in(4,8):
      for se in('any','LDNNY'):
        g=ldnny if se=='LDNNY' else np.ones(n,bool)
        dirs=np.where(fm&g,fd,np.where(TR&bl&g,1,np.where(TR&bs&g,-1,0)));sig=np.where(dirs!=0)[0];sig=sig[sig>30]
        tr_=sim(sig,dirs[sig],np.full(len(sig),S),2.0);row=dict(W=W,theta=th,SL=S,sess=se)
        if len(tr_):
          e=tr_[:,0].astype(int)-1;row['nMR_OOS']=int((fm[e]&~IS[e]).sum());row['nTR_OOS']=int((~fm[e]&~IS[e]).sum())
          oo=~IS[e];row['E_MR_OOS']=tr_[oo&fm[e],1].mean();row['E_TR_OOS']=tr_[oo&~fm[e],1].mean()
        res.append(stats(tr_,row))
finish(res,6442,'R239','xau_m15_hurst_m5_entry_20261101','M15 Lo-MacKinlay VR(q4) W64/128 regime (MR≤0.9 / TREND≥1.1) → M5 MR FADE first |z20|≥θ2/2.5, TREND CONT first prior-H/L break w/ SMA20 slope, SL$4/8 TP2×SL T12 ×sess',['W','theta','SL','sess'])
