import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
wine=datasets.load_wine()
print(wine)
print(wine.feature_names)
print(wine.target_names)
x=pd.DataFrame(wine['data'])
print(x.head())
y=print(wine.target)
X_train, X_test, y_train, y_test = train_test_split(wine.data,wine.target,test_size=0.30, random_state=100)
X_train, X_test, y_train, y_test 
#import naive bayes classifire
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(X_train,y_train)
y_pred=gnb.predict(X_test)
print(y_pred)
#accuracy
from sklearn import metrics
print(metrics.accuracy_score(y_test,y_pred))
from sklearn.metrics import confusion_matrix
cm=np.array(confusion_matrix(y_test,y_pred))
cm



