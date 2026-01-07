from sklearn import datasets
import numpy as np
cancer=datasets.load_breast_cancer()
print("Features: ",cancer.feature_names)
#print labels
print("Labels: ",cancer.target_names)
#shape of vector
print(cancer.data.shape)
#print(first five record)
print(cancer.data[0:5])
print(cancer.target)

#import train_test_split function
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)
print(x_train)
#import SVM model
from sklearn import svm
#create classifier
clf=svm.SVC(kernel='rbf')
#Train the model
clf.fit(x_train,y_train)

#predict the response for test datasets
y_pred=clf.predict(x_test)
print(y_pred)

#import skitlearn
from sklearn import metrics

print('Accuracy :',metrics.accuracy_score(y_test,y_pred))

#plotting test data
import matplotlib.pyplot as plt
plt.scatter(x_test[:,0],x_test[:,1],c="pink",alpha=0.4)
plt.Xlabel("Features")
plt.Ylabel("Target")
plt.title("Test Data")
plt.show()

#plotting trained data
import matplotlib.pyplot as plt
plt.scatter(x_train[:,0],x_train[:,1],c=y_train)
plt.Xlabel("Features")
plt.Ylabel("Target")
plt.title("Train Data")
plt.show()
