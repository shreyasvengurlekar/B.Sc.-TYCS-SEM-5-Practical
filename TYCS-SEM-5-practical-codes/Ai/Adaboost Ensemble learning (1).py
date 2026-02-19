
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv("E:\Backup 24\D Backup 24\College stuff\T.Y.C.S\heart.csv")
df
rows=df.shape[0]
columns=df.shape[1]
print(rows,columns)   #input variable x and y
y=df['target']
print(y)
x=df.drop('target',axis=1)
print(x)
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=.25,random_state=42323232)
X_train, X_test, y_train, y_test 
log_clf=LogisticRegression()
rnd_clf=RandomForestClassifier()
svm_clf=SVC()
nbg_clf=GaussianNB()
for clf in(log_clf,rnd_clf,svm_clf,nbg_clf):
    clf.fit(X_train,y_train)
    
    y_pred=clf.predict(X_test)
    print(clf.__class__.__name__,accuracy_score(y_test,y_pred))
  
from sklearn.svm import SVC
svc_clf=SVC(probability=True,kernel='linear')
# AdaboostClassifier with SVM
boost=AdaBoostClassifier(base_estimator=svc_clf,n_estimators=500,algorithm='SAMME',learning_rate=0.5)
boost.fit(X_train,y_train)
y_pred=boost.predict(X_test)
print("Boosting with SVM classifire",accuracy_score(y_test,y_pred))    
#training score
boost.score(X_train,y_train)
#testing score
boost.score(X_test,y_test)