import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import KBinsDiscretizer

# Load the dataset
df = pd.read_csv('housing_price.csv')

# Define features and target variable
x = df[['size', 'bedrooms']].values
y = df['price'].values

# Discretize the target variable into bins
num_bins = 5
est = KBinsDiscretizer(n_bins=num_bins, encode='ordinal', strategy='uniform')
y_binned = est.fit_transform(y.reshape(-1, 1)).astype(int).flatten()

# Check the distribution of bins
unique, counts = np.unique(y_binned, return_counts=True)
bin_distribution = dict(zip(unique, counts))
print(f"Bin distribution: {bin_distribution}")

# Ensure each bin has enough members for StratifiedKFold
min_count_per_bin = min(counts)
if min_count_per_bin < 5:
    num_bins = max(2, num_bins - 1)
    est = KBinsDiscretizer(n_bins=num_bins, encode='ordinal', strategy='uniform')
    y_binned = est.fit_transform(y.reshape(-1, 1)).astype(int).flatten()

# Initialize the model and StratifiedKFold
model = LinearRegression()
skf = StratifiedKFold(n_splits=5)
mea_scores = []

# Perform Stratified K-Fold cross-validation
for train_index, test_index in skf.split(x, y_binned):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Fit the model and predict
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    
    # Calculate mean absolute error and store it
    mea = mean_absolute_error(y_test, y_pred)
    mea_scores.append(mea)

# Calculate and print the average mean absolute error
average_mae = np.mean(mea_scores)
print(f"Average Mean Absolute Error: {average_mae}")
