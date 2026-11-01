import sys;sys.path.insert(0,'/workspace/fx-research');from _r237_239_eng import *
mid=(h+l)/2;dr=np.sign(c-mid);res=[]
pv=np.r_[np.nan,v[:-1]];ppv=np.r_[np.nan,np.nan,v[:-2]]
for A in(2,3):
  m=(v>pv)&(dr!=0)
  if A==3: m&=(pv>ppv)
  for S in(4,8):
    for tm in(1.5,2.0):
      for se in('any','LDNNY'):
        mm=m&(ldnny if se=='LDNNY' else True);sig=np.where(mm)[0];sig=sig[sig>3]
        res.append(stats(sim(sig,dr[sig],np.full(len(sig),S),tm),dict(accel=A,SL=S,TPm=tm,sess=se)))
finish(res,6410,'R237','xau_m5_tv_accel_mid_20261101','M5 tickvol accel (2/3 rising bars) + close side of mid CONT, SL$4/8 TP1.5/2×SL T12 ×sess',['accel','SL','TPm','sess'])
