import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df=pd.read_csv('housing_price.csv')
x=df[['size','bedrooms']].values
y=df['price'].values

model=LinearRegression()
kf=KFold(n_splits=5)
mea_scores=[]
for train_index,test_index in kf.split(x):
    x_train,x_test=x[train_index],x[test_index]
    y_train,y_test=y[train_index],y[test_index]
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    mea=mean_absolute_error(y_test,y_pred)
    mea_scores.append(mea)
average_mae=np.mean(mea_scores)
print(f"average mean absolute error:{average_mae}")    












