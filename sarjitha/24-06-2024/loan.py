#Importing packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
# load the dataset
data = pd.read_csv('loan_data.csv')
# features used
x = data[['loan_amount', 'interest_rate', 'term', 'income', 'credit_score', 'age', 'employment_length']]
y = data['loan_repaid']
#split train_tests
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2, random_state=42)
#initiate model
model = DecisionTreeClassifier(random_state=42)
#train model
model.fit(x_train,y_train)
#make prediction
y_predict = model.predict(x_test)
accuracy = accuracy_score(y_test, y_predict)
print(f"accuracy: (accuracy:.2f")
print("classification_report: ")
print(classification_report(y_test,y_predict))
#print("confusion Matrix: ")
#print(confusion_matrix(y_test,y_pred))