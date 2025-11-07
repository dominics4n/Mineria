import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')
df = pd.read_csv("../muestra4s.csv")
df.drop('id', inplace=True, axis=1)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe().T)
print(df.isnull().sum())
print(df.nunique())
sns.set_style("darkgrid")

numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

plt.figure(figsize=(14, len(numerical_columns) * 3))
for idx, feature in enumerate(numerical_columns, 1):
    plt.subplot(len(numerical_columns), 2, idx)
    sns.histplot(df[feature], kde=True)
    plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")

plt.tight_layout(h_pad=5)
plt.show()

sen = 1
for x in range(4):
    plt.figure(figsize=(10, 8))
    sns.swarmplot(y="sensor"+str(sen), data=df, palette='viridis')
    plt.title('Swarm Plot')
    plt.ylabel('sensor'+str(sen))
    plt.show()
    sen=sen + 1

sns.set_palette("Pastel1")
plt.figure(figsize=(10, 6))
sns.pairplot(df)
plt.suptitle('Pair Plot for DataFrame')
plt.show()

sen = 1
for x in range(4):
    sns.boxplot(y='sensor'+str(sen), data=df)
    plt.suptitle('Sensor '+str(sen))
    plt.show()
    sen=sen + 1

plt.figure(figsize=(15, 10))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='Pastel2', linewidths=2)
plt.title('Correlation Heatmap')
plt.show()