import pandas as pd

# Reading Excel file
df = pd.read_excel(r"C:\Users\KAVIN\Downloads\data2.xlsx")
# Display full data
print(df)
print("-----------------------------------------------------------")
print(df.describe())
print("-----------------------------------------------------------")
print(df.info())
print("-----------------------------------------------------------")
print(df.isnull().sum())
print("-----------------------------------------------------------")
print(df['marks'].value_counts())
print(df['age'].unique())
print("-----------------------------------------------------------")
import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='marks',data=df)
plt.title('count no of Grade')
plt.xlabel("Grade")
plt.ylabel("count")
plt.show()
sns.histplot(df['marks'],bins=10,kde='True')
plt.show()
sns.heatmap(df.corr(),annot=True,cmap='plasma')
plt.show()
print("-----------------------------------------------------------")
