import pandas as pd
raw_data={'first_name':['manisha'],'last_name':['venagandula'],'age':[2]}
print(raw_data)
df=pd.DataFrame(raw_data,columns=['first_name','last_name','age'])
print(df)

