import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, KFold
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

file_path = "./data/09_irisdata.csv"

column_name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

data= pd.read_csv(file_path, names=column_name)

print(data.columns)
print(data.shape)
print(data.describe())
print(data.groupby('class').size())

scatter_matrix(data, figsize=(10, 10))
plt.savefig("scatter_matrix.png")

X = data.iloc[:, 0:4].values
y = data.iloc[:, 4].values

kfold = KFold(n_splits=10, random_state=10, shuffle=True)
model = DecisionTreeClassifier()
results = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
print(results.mean())
