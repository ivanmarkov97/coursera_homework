import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
X = data[['Pclass', 'Fare', 'Age', 'Sex']]
X = X.replace(to_replace=['male', 'female'], value=[1, 0])
Y = data['Survived']
X = X.dropna(how='any')
Y = Y[X.index]
clf = DecisionTreeClassifier(random_state=241)
clf.fit(X, Y)
importances = clf.feature_importances_
idx = importances.argsort()
print X.columns.values[idx[-1]], X.columns.values[idx[-2]]
