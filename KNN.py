import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
data = {
    'hours_studied':[1,2,3,4,5,6,7,8,9,10],
    'attendance':[40,45,50,55,60,65,70,75,80,85],
    'result':[0,0,0,0,1,1,1,1,1,1]
}
df = pd.DataFrame(data)
print(df)
print("-------------------------------------------------------------------------")
x=df[['hours_studied', 'attendance']]
y=df['result']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = KNeighborsClassifier(n_neighbors=3) 
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("prediction:",y_pred)
print("Actual:", y_test.values)
print("Accuracy:",accuracy_score(y_test, y_pred))

a=int(input("Enter new student studie hours:"))
b=int(input("Enter new student attendance:"))
new_student=[[a,b]]
result=model.predict(new_student)
print("will student pass?",'Yes' if result[0]== 1 else 'No')
