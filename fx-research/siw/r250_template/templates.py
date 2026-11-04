import pandas as pd
T=pd.read_csv('nov3_signals.csv').head(3);T.to_csv('templates.csv',index=False);print(T.T)
