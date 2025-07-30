import pandas as pd

# Reading Excel file
df = pd.read_excel(r"C:\Users\KAVIN\Downloads\data2.xlsx")
# Display full data
print(df)
print("-----------------------------------------------------------")
import seaborn as sns
import matplotlib.pyplot as plt


for i in df['marks']:
    if 'marks' == 90:
        print("yes")
    else:
        print("no")
print("-----------------------------------------------------------")
"""
q1=df['age'].quantile(0.25)
q2=df['age'].quantile(0.75)
iqr=q2-q1
df=df[(df['age']<=q1-1.5*iqr)&(df['age']>=q2+1.5*iqr)]
print(df)
print("-----------------------------------------------------------")
# Boxplot for all numeric columns

df.select_dtypes(include='number').plot(kind='box', subplots=True, layout=(2,3), figsize=(12,8), sharex=False)
plt.tight_layout()
plt.show()
"""
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='Greens')
plt.title("Correlation Matrix")
plt.show()
print(df['age'].value_counts())
sns.countplot(x='age',data=df)
plt.show()
print("-----------------------------------------------------------")
print(df.groupby('age')['marks'].mean())
print("-----------------------------------------------------------")
sns.pairplot(df,hue='age',palette='coolwarm',diag_kind='kde')
plt.show()
print("-----------------------------------------------------------")
df.hist(figsize=(10,8),bins=20)
plt.tight_layout()
plt.show()
