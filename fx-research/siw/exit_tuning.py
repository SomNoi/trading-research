import pandas as pd, numpy as np, siw
df=siw.load('duka_xau_m5_bid.csv'); C=0.28; TO=siw.P['timeout']
O,H,Lo,Cl=df.o.values,df.h.values,df.l.values,df.c.values
L=["11-03 13:50","11-03 12:00","11-03 04:55","11-02 23:50","11-02 23:15","11-02 22:05","11-02 19:50","11-02 14:05","11-02 11:10","11-02 10:00","11-02 06:00","10-30 18:00","10-30 14:05","10-30 05:15","10-29 23:55","10-29 18:35","10-29 15:15","10-29 10:10","10-29 08:20","10-29 04:45"]
idx={t:i for i,t in df.srv.items()}
his=pd.DataFrame([dict(i=idx[pd.Timestamp('2026-'+x)]) for x in L]); his['dir']=['B' if df.e21[i]>df.e55[i] else 'S' for i in his.i]
his['conf_srv']=df.srv[his.i].values
allv=pd.read_csv('siw2_signals_oct29_nov3.csv',parse_dates=['conf_srv'])
def sltp(i,d,sl,tp,to=TO):
    e=O[i+1]
    for j in range(i+1,min(i+1+to,len(df))):
        fav=(e-Lo[j]) if d=='S' else (H[j]-e); adv=(H[j]-e) if d=='S' else (e-Lo[j])
        if adv>=sl: return -sl-C
        if fav>=tp: return tp-C
    j=min(i+to,len(df)-1); return ((e-Cl[j]) if d=='S' else (Cl[j]-e))-C
def timex(i,d,n,sl=None):
    e=O[i+1]; mae=0
    for j in range(i+1,min(i+1+n,len(df))):
        adv=(H[j]-e) if d=='S' else (e-Lo[j]); mae=max(mae,adv)
        if sl and adv>=sl: return -sl-C,mae
    j=min(i+n,len(df)-1); return ((e-Cl[j]) if d=='S' else (Cl[j]-e))-C,mae
rows=[];out=[]
def grid(s,lab):
    for sl in range(1,11):
        for tp in range(1,16):
            p=np.array([sltp(r.i,r.dir,sl,tp) for r in s.itertuples()])
            rows.append(dict(set=lab,sl=sl,tp=tp,n=len(p),win=(p>0).mean(),net=p.sum()))
    g=pd.DataFrame([r for r in rows if r['set']==lab])
    out.append(f"\n### {lab} (n={len(s)})\nTop by win rate (tiebreak net):\n"+g.sort_values(['win','net'],ascending=False).head(5).to_markdown(index=False,floatfmt='.2f')+"\nTop by net $:\n"+g.sort_values('net',ascending=False).head(5).to_markdown(index=False,floatfmt='.2f'))
    return g
for nm,S in [('his20',his),('allv2',allv)]:
    for d in 'SB':
        s=S[S.dir==d]; grid(s,f'{nm}_{d}')
        tr=s[s.conf_srv<'2026-10-31']; te=s[s.conf_srv>='2026-11-01']
        if len(tr) and len(te):
            g=grid(tr,f'{nm}_{d}_train_oct29-30'); b=g.sort_values('net',ascending=False).iloc[0]; bw=g.sort_values(['win','net'],ascending=False).iloc[0]
            for lab,bb in [('best-net',b),('best-win',bw)]:
                p=np.array([sltp(r.i,r.dir,int(bb.sl),int(bb.tp)) for r in te.itertuples()])
                out.append(f"\nOOS {nm}_{d} {lab} SL{int(bb.sl)}/TP{int(bb.tp)} train win {bb.win:.0%} net {bb.net:+.2f} -> test Nov2-3 n={len(p)} win {(p>0).mean():.0%} net {p.sum():+.2f}")
pd.DataFrame(rows).to_csv('exit_tuning_sltp_grid.csv',index=False)
tr=[];out.append('\n## B) Time exit (no TP/SL), entry next open, exit close of Nth bar\n')
for nm,S in [('his20',his),('allv2',allv)]:
    for d in 'SB':
        s=S[S.dir==d]
        for n,sl in [(1,None),(2,None),(3,None),(4,None),(6,None),(3,5)]:
            r=[timex(x.i,x.dir,n,sl) for x in s.itertuples()]; p=np.array([a for a,_ in r]); m=max(b for _,b in r)
            tr.append(dict(set=nm,dir=d,bars=n,minutes=5*n,safetySL=sl or '',n=len(p),win=(p>0).mean(),avg=p.mean(),median=np.median(p),net=p.sum(),worst=p.min(),maxMAE=m))
T=pd.DataFrame(tr);T.to_csv('exit_tuning_time.csv',index=False);out.append(T.to_markdown(index=False,floatfmt='.2f'))
open('exit_tuning.md','w').write(f"# SIW v2 exit tuning (Dukascopy BID, Oct29-Nov3, cost $0.28/0.01, $ per 0.01 lot = price $)\nTimeout for SL/TP grid = {TO} bars; same-bar both-hit = SL. IN-SAMPLE, tiny n: overfit.\n## A) SL/TP grid\n"+'\n'.join(out))
print('\n'.join(out))
