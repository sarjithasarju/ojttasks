import pandas as pd
data=pd.read_csv("air-pollution.csv")
# print(data)

 
# data['Nitrogen oxide (NOx)_mean'] = data['Nitrogen oxide (NOx)'].mean()
# data['Nitrogen oxide (NOx)_median'] = data['Nitrogen oxide (NOx)'].median()
# data['Nitrogen oxide (NOx)_std'] = data['Nitrogen oxide (NOx)'].std()



# data['Carbon monoxide (CO) emissions_mean'] = data['Carbon monoxide (CO) emissions'].mean()
# data['Carbon monoxide (CO) emissions_median'] = data['Carbon monoxide (CO) emissions'].median()
# data['Carbon monoxide (CO) emissions_std'] = data['Carbon monoxide (CO) emissions'].std()

data['Organic carbon (OC) emissions_mean'] = data['Organic carbon (OC) emissions'].mean()
data['Organic carbon (OC) emissions_median'] = data['Organic carbon (OC) emissions'].median()
data['Organic carbon (OC) emissions_std'] = data['Organic carbon (OC) emissions'].std()
print(data)
data.to_csv('Organic carbon (OC) emissions.csv', index=False)