
#.Load the dataset from a CSV file named 
# sample_dataset.csv into a Pandas DataFrame. Display the first few rows of the dataset
import pandas as pd
df = pd.read_csv('sample_dataset.csv')
print(df.head())
#Generate summary statistics for this dataset. What are the mean and standard deviation 
# of the Sepal Length
print(df.describe())
#What are the unique values in the Species column?
print(df['Species'].unique())
#What is the count of each unique value in the Species column?
print(df['Species'].value_counts())
#Check for any missing values in the dataset. How would you handle them if there were any
print(df.isnull().sum())
#Filter the dataset to only include rows where the Sepal Length is greater than 5.5
df_filtered = df[df['Sepal Length'] > 5.5]
print(df_filtered)
#Convert the species labels to numerical values using a mapping dictionary. 
# For example, map 'FlowerA' to 0, 'FlowerB' to 1, and 'FlowerC' to 2
species_mapping = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC': 2}
df['Species'] = df['Species'].map(species_mapping)
print(df.head())
#.Split the dataset into training and testing sets with 70% training data and 30% testing data. 
# Ensure that the split is stratified based on the species
from sklearn.model_selection import train_test_split
X = df.drop('Species', axis=1)
y = df['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
#Train a simple decision tree classifier on the training data and evaluate its performance on the testing data
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
#Evaluate the model on the testing data
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
#Save the trained model to a file named 'model.pkl' using joblib
import joblib
joblib.dump(clf, 'model.pkl')
