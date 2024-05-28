import pandas as pd
data={
    'name':['meenu','unni','subi'],
    'age':[20,21,22],
     'place':['vjmd','nellandu','vamanpuram,']
    }
df=pd.DataFrame(data)
# print (df)
# print (df[['name','place']])
# print (df.iloc[2])
# print(df[df['age']>20])
df['stiphend']=[15000,5000,5000]
# print(df)

df=df.drop(columns=['age'])
# print(df)
print(df.describe())