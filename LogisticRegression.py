import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
data ={
    'age':[22,25,24,23,22],
    'salary':[1000,2000,3000,4000,1000],
    'purchase':[1,0,0,1,1]
}
df=pd.DataFrame(data)
X=df[['age','salary']]
Y=df['purchase']


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(X_train, Y_train)
y_pred=model.predict(X_test)  
print("prediction\n",y_pred)
print("Accuracy\n",accuracy_score(Y_test,y_pred))
print("Confusion Matrix\n",confusion_matrix(Y_test,y_pred))
print("classification report\n",classification_report(Y_test,y_pred))
