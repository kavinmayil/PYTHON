import pandas as pd
data={
    'class_attend':[2,3,4,1,1,5,6,8,9,0],
    'internal_mark':[55,66,89,76,45,78,67,89,90,56],
    'result':[0,1,0,1,1,1,1,1,0,0]
}
df=pd.DataFrame(data)
print(df)
print("------------------------------------------------------------------------------------")
X=df[['class_attend', 'internal_mark']]
Y=df['result']
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.7,random_state=42)
from sklearn.tree import DecisionTreeClassifier 
model=DecisionTreeClassifier()
model.fit(X_train,Y_train)  
y_pred=model.predict(X_test)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
print("Accuracy:", accuracy_score(Y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred))  
print("Classification Report:\n", classification_report(Y_test, y_pred))
from sklearn import tree
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
tree.plot_tree(model,feature_names=['class_attend', 'internal_mark'], class_names=['Fail', 'Pass'], filled=True )
plt.show()
