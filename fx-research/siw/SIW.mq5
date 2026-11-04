// SIW v2 — MQL5 SKETCH (signals/alerts only, no order sending). Compile & verify in MetaEditor.
#property indicator_chart_window
#property indicator_plots 0
input bool UseA=true, UseB=true, UseC=true, UseZone=false;
input double StarBody=0.40, PinWick=0.50, PinBody=0.35, WickTol=0.30, EngTol=0.10, MaxExt=10.0, ZoneMax=3.0;
input int LegLen=12;
input double V3SL=5.0, V3TP=20.0, V3Trail=3.0; input int V3AfterBars=3; input bool V3BE=false; // v3 exit (alert text only; manage manually)
int h21, h55; datetime lastBar=0;
int OnInit(){ h21=iMA(_Symbol,PERIOD_M5,21,0,MODE_EMA,PRICE_CLOSE); h55=iMA(_Symbol,PERIOD_M5,55,0,MODE_EMA,PRICE_CLOSE); return INIT_SUCCEEDED; }
double O(int k){return iOpen(_Symbol,PERIOD_M5,k);} double H(int k){return iHigh(_Symbol,PERIOD_M5,k);}
double L(int k){return iLow(_Symbol,PERIOD_M5,k);}  double C(int k){return iClose(_Symbol,PERIOD_M5,k);}
bool Rej(int k,bool sell){
  double rng=MathMax(H(k)-L(k),1e-9), top=MathMax(O(k),C(k)), bot=MathMin(O(k),C(k)), bp=(top-bot)/rng;
  double ptop=MathMax(O(k+1),C(k+1)), pbot=MathMin(O(k+1),C(k+1));
  if(sell) return ((H(k)-top)/rng>=PinWick && bp<=PinBody) || (bp<=StarBody && bot>=ptop-WickTol && top<=H(k+1)+WickTol && H(k+1)>ptop);
  return ((bot-L(k))/rng>=PinWick && bp<=PinBody) || (bp<=StarBody && top<=pbot+WickTol && bot>=L(k+1)-WickTol && pbot>L(k+1));
}
bool Eng(int k,bool sell){
  if(sell) return C(k)<O(k) && C(k+1)>O(k+1) && O(k)>=C(k+1)-EngTol && C(k)<=O(k+1)+EngTol;
  return C(k)>O(k) && C(k+1)<O(k+1) && O(k)<=C(k+1)+EngTol && C(k)>=O(k+1)-EngTol;
}
bool Sig(int k,bool sell){ // k = confirm bar shift (closed)
  double a[1],b[1]; if(CopyBuffer(h21,0,k,1,a)<1||CopyBuffer(h55,0,k,1,b)<1) return false;
  if(sell? !(a[0]<b[0]) : !(a[0]>b[0])) return false;
  bool col = sell? C(k)<O(k) : C(k)>O(k);
  bool pat=(UseA&&Rej(k,sell))||(UseB&&Eng(k,sell))||(UseC&&col&&Rej(k+1,sell));
  if(!pat) return false;
  double ext = sell? H(iHighest(_Symbol,PERIOD_M5,MODE_HIGH,LegLen,k))-C(k) : C(k)-L(iLowest(_Symbol,PERIOD_M5,MODE_LOW,LegLen,k));
  return ext<=MaxExt && (!UseZone || ext<=ZoneMax);
}
int OnCalculate(const int rates_total,const int prev_calculated,const datetime &time[],const double &open[],const double &high[],const double &low[],const double &close[],const long &tv[],const long &v[],const int &sp[]){
  datetime t=iTime(_Symbol,PERIOD_M5,0); if(t==lastBar) return rates_total; lastBar=t;
  if(Sig(1,true) )  Alert("SIW2 SELL ",_Symbol," entry ~",DoubleToString(iOpen(_Symbol,PERIOD_M5,0),2)," SL+",DoubleToString(V3SL,1)," TP-",DoubleToString(V3TP,1)," then trail $",DoubleToString(V3Trail,1)," after ",V3AfterBars*5,"min",(V3BE?" +BE":""));
  if(Sig(1,false)) Alert("SIW2 BUY ",_Symbol," entry ~",DoubleToString(iOpen(_Symbol,PERIOD_M5,0),2)," SL-",DoubleToString(V3SL,1)," TP+",DoubleToString(V3TP,1)," then trail $",DoubleToString(V3Trail,1)," after ",V3AfterBars*5,"min",(V3BE?" +BE":""));
  return rates_total;
}
