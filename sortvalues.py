import pandas as pd
d={'name':['manisha','sairam'],'age':[20,30],'score':[10,99]}
print(d)
df=pd.DataFrame(d)
print(df)
df.sort_values(by='score')
print(df)
s=df['score'].sum()
print(s)
mi=df['score'].min()
print(mi)
ma=df['score'].max()
print(ma)
df.groupby('age').sum()
print(df)

