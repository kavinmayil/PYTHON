from sklearn.preprocessing import StandardScaler
import pandas as pd
df=pd.read_excel(r"C:\Users\KAVIN\Downloads\data2.xlsx")

scaler=StandardScaler()
df[['age','marks','attendance']]=scaler.fit_transform(df[['age','marks','attendance']])
print("----------------------------------------------------")
print(df['age'])
print("----------------------------------------------------")
print(df['marks'])
print("----------------------------------------------------")
print(df.head())
print("----------------------------------------------------")
print(df.columns)
print("----------------------------------------------------")
print(df.describe())

