import pandas as pd, numpy as np, siw
from exit_tuning import his, allv, df   # reuses his 20 picks + all v2 signals
rows=[]
vs=[('T2',2,False),('T3',3,False),('T5',5,False),('T2+BE',2,True),('T3+BE',3,True),('T5+BE',5,True)]
for nm,S in [('his20',his),('allv2',allv)]:
  for d in ['S','B','all']:
    s=S if d=='all' else S[S.dir==d]
    if not len(s): continue
    for lab,t,be in vs:
      r=[siw.outcome_v3(df,int(x.i)+1,x.dir,dict(v3_trail=t,v3_be=be)) for x in s.itertuples()]
      p=np.array([b for _,b in r]); k=pd.Series([a for a,_ in r]).value_counts().to_dict()
      rows.append(dict(set=nm,dir=d,exit=lab,n=len(p),win=f"{(p>0).mean():.0%}",net=p.sum(),avg=p.mean(),worst=p.min(),best=p.max(),exits=' '.join(f"{a}:{b}" for a,b in k.items())))
T=pd.DataFrame(rows); T.to_csv('exit_v3.csv',index=False)
prev=pd.read_csv('exit_tuning_time.csv'); prev=prev[(prev.bars==3)&(prev.safetySL.isna())]
md=("# SIW v2 exit v3 (SL $5 / TP $20, trailing after 15 min)\nDukascopy BID XAUUSD M5 Oct29-Nov3, entry next open, cost $0.28/0.01, $ = per 0.01 lot. "
"Trail from best price since entry, activated after 3 bars; stop never looser than SL; stop checked before TP in a bar; best updated after the bar. Timeout 48 bars. IN-SAMPLE, small n.\n\n"
+T.to_markdown(index=False,floatfmt='.2f')+"\n\n## Previous: 15-min time exit (close of bar 3, no SL)\n"+prev[['set','dir','n','win','net','avg','worst']].to_markdown(index=False,floatfmt='.2f'))
open('exit_v3.md','w').write(md); print(md)
