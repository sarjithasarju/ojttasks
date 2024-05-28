import pandas as pd
df =pd.read_csv('online.csv',
                dtype={'age':int,'salary':float},
                usecols=['Name','Age','Place'])
# print(df)

# df_clean_row=df.dropna(how="all")
# # print(df_clean_row)

# df_clean_col=df_clean_row.dropna(axis=1,how="all")
# print(df_clean_col)

df_filled_data=df.fillna(0)
print(df_filled_data)