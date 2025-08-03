import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel(r"C:\Users\KAVIN\Downloads\data2.xlsx")

le = LabelEncoder()
df['age']=le.fit_transform(df['age'])
df['attendance']=df['attendance'].fillna(70)
print(df)
print('-----------------------------------------------------')
print(df['age'])
print('-----------------------------------------------------')
df['task']=df['age']+1
df.drop(['age','marks'],axis=1,inplace=True)
print(df)
print('-----------------------------------------------------')
print(df['task'])
