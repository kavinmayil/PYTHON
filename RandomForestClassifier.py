import pandas as pd
data={
    'studietime':[2,3,4,1,1,5,6,8,9,0],
    'attendance':[55,66,89,76,45,78,67,89,90,56],
    'pass':[0,1,0,1,1,1,1,1,0,0]
}
df=pd.DataFrame(data)
print(df)
print("------------------------------------------------------------------------------------")

x=df[['studietime','attendance']]
y=df['pass']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y,train_size=0.7,random_state=42)
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(X_train,Y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(y_pred,Y_test))
print(classification_report(y_pred,Y_test))
