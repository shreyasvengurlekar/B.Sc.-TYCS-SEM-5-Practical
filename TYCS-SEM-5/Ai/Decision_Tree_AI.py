

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

#Load the Dataset
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df
df['target']

#Split the Data into Training and Test Sets
X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], df['target'], random_state=0)
X_train, X_test, y_train, y_test

#Build the Decision Tree Model
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)

#Predictions and Evaluate the Model
y_pred = clf.predict(X_test)
y_pred

#evaluate the accuracy of our model:
print("Accuracy:", accuracy_score(y_test, y_pred))
#Visualize the Decision Tree
#The filled=True argument colors the nodes by their majority class. This can be helpful in visualizing the decision paths.
fig = plt.figure(figsize=(15,10))
_ = tree.plot_tree(clf,
                   feature_names=iris.feature_names,
                   class_names=iris.target_names,
                   filled=True)


