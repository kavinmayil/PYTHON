import pandas as pd

# Reading Excel file
df = pd.read_excel(r"C:\Users\KAVIN\OneDrive\Desktop\data1.xlsx")
# Display full data
print(df)
print("---------------------------------------------------------")
print(df.head(1))  #5 rows
print("---------------------------------------------------------")
print(df.tail(1))
print("---------------------------------------------------------")
print(df.isnull())
print(df.isnull().sum())
# fill missing value
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Marks']=df['Marks'].fillna(0)
df['Grade']=df['Grade'].fillna("Unknown")
df['Name']=df['Name'].fillna("kavin")
print("---------------------------------------------------------")
print(df)
print("---------------------------------------------------------")
print("Average Mark :",df['Marks'].mean())
print("max mark :",df['Marks'].max())
print("mix mark :",df['Marks'].min())
print("---------------------------------------------------------")
print("Grade count :",df['Grade'].value_counts())
print("---------------------------------------------------------")
print(df.sort_values(by='Marks',ascending=True))
print("---------------------------------------------------------")
