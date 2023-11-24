import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, KFold
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

file_path = "./data/09_irisdata.csv"
column_name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pd.read_csv(file_path, names=column_name)

print(dataset.columns)
print(dataset.shape)
print(dataset.describe())
print(dataset.groupby('class').size())

scatter_matrix(dataset, figsize=(10, 10))
plt.savefig("scatter_matrix.png")

X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values

model = DecisionTreeClassifier()

model.fit(X, y)

y_pred = model.predict(X)

kfold = KFold(n_splits=10, random_state=10, shuffle=True)
results = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
print(results.mean())
