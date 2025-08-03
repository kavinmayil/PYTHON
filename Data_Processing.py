import pandas as pd
import numpy as np
data={
    'Name': ['kavin','salvin','bala','subash',np.nan],
    'Age': [20,21,23,np.nan,40],
    'Gender': ['male','female','male','female','male'],
    'Salary': [5000,4000,np.nan,2000,1000],
    'Purchase': ['no','yes','no','yes','no']
}
df=pd.DataFrame(data)
print(df)
print("---------------------------------------------------------------------------------")
print(df.isnull().sum())
print("---------------------------------------------------------------------------------")
#df=df.dropna(subset=data)
#print(df)
print("---------------------------------------------------------------------------------")
df['Age']=df['Age'].fillna(df['Age'].mean()) 
df['Name']=df['Name'].fillna('Divyan')
df['Salary']=df['Salary'].fillna(df['Salary'].mean())
print(df)
print("---------------------------------------------------------------------------------")
#convert gender and purchase into number
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

#df['Gender']=le.fit_transform(df['Gender'])
df['Gender']=df['Gender'].map({'male':0,'female':1})
df['Purchase']=le.fit_transform(df['Purchase'])
print(df)
print("---------------------------------------------------------------------------------")
#standardization
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
df[['Age','Salary']]=sc.fit_transform(df[['Age','Salary']])
df['work']=df['Salary']-1000
print(df)
print("---------------------------------------------------------------------------------")
#train and Test(spliting)
from sklearn.model_selection import train_test_split
X=df[['Age','Gender','Salary']]
Y=df['work']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print(df)
print("--------------------------------------------------------------------------------------")
print(Y_test)
