import pandas as pd
import numpy as np
data={
    'hour_studied':[2,3,4,1,1,5,6,8,9,0],
    'sleep_hours':[6,7,4,5,3,1,1,2,4,7],
    'attendance_rate':[60,72,68,90,88,76,79,82,45,99],
    'previous_grade':[55,66,89,76,45,78,67,89,90,56],
    'present_today':[0,1,0,1,1,1,1,1,0,0]
}
df=pd.DataFrame(data)
print(df)
print(df.describe())
print(df.isnull().sum())
from sklearn.model_selection import train_test_split
X=df.drop('present_today',axis=1)
Y=df['present_today']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.7,random_state=42)

from sklearn.tree import DecisionTreeClassifier

model=DecisionTreeClassifier()
model.fit(X_train,Y_train)

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
Y_pred=model.predict(X_test)
print("Accuracy:",accuracy_score(Y_test,Y_pred))
print("Confusion_Matrics:",confusion_matrix(Y_test,Y_pred))
print("Classification_report:\n",classification_report(Y_test,Y_pred))
import joblib
joblib.dump(model,'student_attendance_prediction.pkl')
