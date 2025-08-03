
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
data={
    'hour_studied':[2,4,6,8,10,12],
    'attendance':[0,0,1,1,1,1]
}
df=pd.DataFrame(data)
print(df)
#from sklearn.preprocessing import LabelEncoder
#df['attendance']=LabelEncoder().fit_transform(df['attendance'])
x=df[['hour_studied']]
y=df['attendance']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42,stratify=y)
model=SVC(kernel='linear')
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))  
