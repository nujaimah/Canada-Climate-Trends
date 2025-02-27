import pandas as pd
import numpy
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import calendar

data = pd.read_csv('CombinedData.csv')
data.info()
data.isnull().sum()
data['Max Temp (°C)'].fillna(data['Max Temp (°C)'].median(), inplace=True)
data['Min Temp (°C)'].fillna(data['Min Temp (°C)'].median(), inplace=True)
data['Mean Temp (°C)'].fillna(data['Mean Temp (°C)'].median(), inplace=True)
data['Heat Deg Days (°C)'].fillna(data['Heat Deg Days (°C)'].median(), inplace=True)
data['Cool Deg Days (°C)'].fillna(data['Cool Deg Days (°C)'].median(), inplace=True)
data['Total Rain (mm)'].fillna(data['Total Rain (mm)'].median(), inplace=True)
data['Total Snow (cm)'].fillna(data['Total Snow (cm)'].median(), inplace=True)
data['Total Precip (mm)'].fillna(data['Total Precip (mm)'].median(), inplace=True)
data['Snow on Grnd (cm)'].fillna(data['Snow on Grnd (cm)'].median(), inplace=True)
data['Dir of Max Gust (10s deg)'].fillna(data['Dir of Max Gust (10s deg)'].median(), inplace=True)
data['Spd of Max Gust (km/h)'].fillna(data['Spd of Max Gust (km/h)'].median(), inplace=True)

plt.figure()
sns.kdeplot(data['Max Temp (°C)'], fill=True)
plt.figure()
sns.kdeplot(data['Min Temp (°C)'], fill=True)
plt.figure()
sns.kdeplot(data['Mean Temp (°C)'], fill=True)
plt.figure()
sns.kdeplot(data['Heat Deg Days (°C)'], fill=True)
plt.figure()
sns.kdeplot(data['Cool Deg Days (°C)'], fill=True)
plt.figure()
sns.kdeplot(data['Total Rain (mm)'], fill=True)
plt.figure()
sns.kdeplot(data['Total Snow (cm)'], fill=True)
plt.figure()
sns.kdeplot(data['Total Precip (mm)'], fill=True)
plt.figure()
sns.kdeplot(data['Snow on Grnd (cm)'], fill=True)
plt.figure()
sns.kdeplot(data['Dir of Max Gust (10s deg)'], fill=True)
plt.figure()
sns.kdeplot(data['Spd of Max Gust (km/h)'], fill=True)

# IQR Method

def find_outliers_IQR(data):
   outliers_dict = {}

   for column in data.columns:
        q1 = data[column].quantile(0.25)
        q3 = data[column].quantile(0.75)
        IQR = q3 - q1
  
        lower_bound = q1 - 1.5 * IQR
        upper_bound = q3 + 1.5 * IQR

        outliers = data[column][(data[column] < lower_bound) | (data[column] > upper_bound)]
        outliers_dict[column] = outliers

        print(f"{column}:")
        print(f"   IQR: {IQR}")
        print(f"   Lower Bound: {lower_bound}")
        print(f"   Upper Bound: {upper_bound}")
        print(f"   Number of Outliers: {len(outliers)}\n")
  
   return outliers_dict

columns = [
    "Max Temp (°C)", "Min Temp (°C)", "Mean Temp (°C)",
    "Heat Deg Days (°C)", "Cool Deg Days (°C)", "Total Rain (mm)",
    "Total Snow (cm)", "Snow on Grnd (cm)", "Dir of Max Gust (10s deg)",
    "Spd of Max Gust (km/h)"
]
outliers = find_outliers_IQR(data[columns])

