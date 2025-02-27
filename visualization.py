import pandas as pd
import numpy
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import calendar

data = pd.read_csv('CombinedData.csv')

toronto_2024_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2024)]
toronto_avgtemp_2024 = toronto_2024_data.groupby('Month')['Mean Temp (°C)'].mean()
toronto2024_df = pd.DataFrame(toronto_avgtemp_2024)
toronto2024_df_reset = toronto2024_df.reset_index()
toronto2024_df_reset['Month'] = toronto2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(12,6))
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title('Average Monthly Temperature in Toronto in 2024')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.plot(toronto2024_df_reset['Month'], toronto2024_df_reset['Mean Temp (°C)'],  marker='o')
plt.xticks(rotation=45)
plt.tight_layout()
for i, value in enumerate(toronto2024_df_reset['Mean Temp (°C)']):
    plt.text(i, value, round(value, 2), ha='center', va='bottom', fontsize=12, color='black', fontweight='bold')

toronto_2023_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2023)]
toronto_avgtemp_2023 = toronto_2023_data.groupby('Month')['Mean Temp (°C)'].mean()
toronto2023_df = pd.DataFrame(toronto_avgtemp_2023)
toronto2023_df_reset = toronto2023_df.reset_index()
toronto2023_df_reset['Month'] = toronto2023_df_reset['Month'].apply(lambda x: calendar.month_name[x])

toronto_2024_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2024)]
toronto_avgtemp_2024 = toronto_2024_data.groupby('Month')['Mean Temp (°C)'].mean()
toronto2024_df = pd.DataFrame(toronto_avgtemp_2024)
toronto2024_df_reset = toronto2024_df.reset_index()
toronto2024_df_reset['Month'] = toronto2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(12,6))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.title('Average Monthly Temperature in Toronto in 2023 and 2024')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

plt.plot(toronto2023_df_reset['Month'], toronto2023_df_reset['Mean Temp (°C)'], marker='o', label='2023', color='blue')

plt.plot(toronto2024_df_reset['Month'], toronto2024_df_reset['Mean Temp (°C)'], marker='s', label='2024', color='red')

plt.xticks(rotation=45)

for i, value in enumerate(toronto2023_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1.5, round(value, 2), ha='right', va='top', fontsize=10, color='blue', fontweight='bold')

for i, value in enumerate(toronto2024_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1, round(value, 2), ha='right', va='top', fontsize=10, color='red', fontweight='bold')

plt.tight_layout()
plt.legend()
plt.show()

toronto_2023_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2023)]
toronto_avgtemp_2023 = toronto_2023_data.groupby('Month')['Mean Temp (°C)'].mean()
toronto2023_df = pd.DataFrame(toronto_avgtemp_2023)
toronto2023_df_reset = toronto2023_df.reset_index()
toronto2023_df_reset['Month'] = toronto2023_df_reset['Month'].apply(lambda x: calendar.month_name[x])

toronto_2013_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2013)]
toronto_avgtemp_2013 = toronto_2013_data.groupby('Month')['Mean Temp (°C)'].mean()
toronto2013_df = pd.DataFrame(toronto_avgtemp_2013)
toronto2013_df_reset = toronto2013_df.reset_index()
toronto2013_df_reset['Month'] = toronto2013_df_reset['Month'].apply(lambda x: calendar.month_name[x])

toronto_2003_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2003)]
toronto_avgtemp_2003= toronto_2003_data.groupby('Month')['Mean Temp (°C)'].mean()
toronto2003_df = pd.DataFrame(toronto_avgtemp_2003)
toronto2003_df_reset = toronto2003_df.reset_index()
toronto2003_df_reset['Month'] = toronto2003_df_reset['Month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(12,6))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.title('Average Monthly Temperature in Toronto in 2023, 2013, and 2003')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

plt.plot(toronto2023_df_reset['Month'], toronto2023_df_reset['Mean Temp (°C)'], marker='o', label='2023', color='blue')

plt.plot(toronto2013_df_reset['Month'], toronto2013_df_reset['Mean Temp (°C)'], marker='s', label='2013', color='red')

plt.plot(toronto2003_df_reset['Month'], toronto2003_df_reset['Mean Temp (°C)'], marker='s', label='2003', color='green')

plt.xticks(rotation=45)

for i, value in enumerate(toronto2023_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1.5, round(value, 2), ha='right', va='top', fontsize=10, color='blue', fontweight='bold')

for i, value in enumerate(toronto2013_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1, round(value, 2), ha='right', va='top', fontsize=10, color='red', fontweight='bold')

for i, value in enumerate(toronto2003_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1, round(value, 2), ha='right', va='top', fontsize=10, color='green', fontweight='bold')

plt.tight_layout()
plt.legend()
plt.show()

jasper_2023_data = data[(data['Station Name'] == 'JASPER WARDEN') & (data['Year'] == 2023)]
jasper_avgtemp_2023 = jasper_2023_data.groupby('Month')['Mean Temp (°C)'].mean()
jasper2023_df = pd.DataFrame(jasper_avgtemp_2023)
jasper2023_df_reset = jasper2023_df.reset_index()
jasper2023_df_reset['Month'] = jasper2023_df_reset['Month'].apply(lambda x: calendar.month_name[x])

jasper_2024_data = data[(data['Station Name'] == 'JASPER WARDEN') & (data['Year'] == 2024)]
jasper_avgtemp_2024 = jasper_2024_data.groupby('Month')['Mean Temp (°C)'].mean()
jasper2024_df = pd.DataFrame(jasper_avgtemp_2024)
jasper2024_df_reset = jasper2024_df.reset_index()
jasper2024_df_reset['Month'] = jasper2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(12,6))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.title('Average Monthly Temperature in Jasper in 2023 and 2024')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

plt.plot(jasper2023_df_reset['Month'], jasper2023_df_reset['Mean Temp (°C)'], marker='o', label='2023', color='blue')

plt.plot(jasper2024_df_reset['Month'], jasper2024_df_reset['Mean Temp (°C)'], marker='s', label='2024', color='red')

plt.xticks(rotation=45)

for i, value in enumerate(jasper2023_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1.5, round(value, 2), ha='right', va='top', fontsize=10, color='blue', fontweight='bold')

for i, value in enumerate(jasper2024_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1, round(value, 2), ha='right', va='top', fontsize=10, color='red', fontweight='bold')

plt.tight_layout()
plt.legend()
plt.show()

jasper_2023_data = data[(data['Station Name'] == 'JASPER WARDEN') & (data['Year'] == 2023)]
jasper_avgtemp_2023 = jasper_2023_data.groupby('Month')['Mean Temp (°C)'].mean()
jasper2023_df = pd.DataFrame(jasper_avgtemp_2023)
jasper2023_df_reset = jasper2023_df.reset_index()
jasper2023_df_reset['Month'] = jasper2023_df_reset['Month'].apply(lambda x: calendar.month_name[x])

toronto_2023_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2023)]
toronto_avgtemp_2023 = toronto_2023_data.groupby('Month')['Mean Temp (°C)'].mean()
toronto2023_df = pd.DataFrame(toronto_avgtemp_2023)
toronto2023_df_reset = toronto2023_df.reset_index()
toronto2023_df_reset['Month'] = toronto2023_df_reset['Month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(12,6))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.title('Average Monthly Temperature in Jasper vs Toronto in 2023')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

plt.plot(jasper2023_df_reset['Month'], jasper2023_df_reset['Mean Temp (°C)'], marker='o', label='Jasper 2023', color='blue')

plt.plot(toronto2023_df_reset['Month'], toronto2023_df_reset['Mean Temp (°C)'], marker='o', label='Toronto 2023', color='red')

plt.xticks(rotation=45)

for i, value in enumerate(jasper2023_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1.5, round(value, 2), ha='right', va='top', fontsize=10, color='blue', fontweight='bold')

for i, value in enumerate(toronto2023_df_reset['Mean Temp (°C)']):
    plt.text(i, value + 1, round(value, 2), ha='right', va='top', fontsize=10, color='red', fontweight='bold')

plt.tight_layout()
plt.legend()
plt.show()

toronto_2024_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2024)]
toronto_avgprecip_2024 = toronto_2024_data.groupby('Month')['Total Precip (mm)'].mean()
toronto2024_df = pd.DataFrame(toronto_avgprecip_2024)
toronto2024_df_reset = toronto2024_df.reset_index()
toronto2024_df_reset['Month'] = toronto2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

jasper_2024_data = data[(data['Station Name'] == 'JASPER WARDEN') & (data['Year'] == 2024)]
jasper_avgprecip_2024 = jasper_2024_data.groupby('Month')['Total Precip (mm)'].mean()
jasper2024_df = pd.DataFrame(jasper_avgprecip_2024)
jasper2024_df_reset = jasper2024_df.reset_index()
jasper2024_df_reset['Month'] = jasper2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(12,6))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.title('Average Precipitation in Jasper vs Toronto in 2024')
plt.xlabel('Month')
plt.ylabel('Average Precipitation (mm)')

plt.plot(toronto2024_df_reset['Month'], toronto2024_df_reset['Total Precip (mm)'], marker='o', label='Toronto 2024', color='blue')

plt.plot(jasper2024_df_reset['Month'], jasper2024_df_reset['Total Precip (mm)'], marker='o', label='Jasper 2024', color='red')

plt.xticks(rotation=45)

for i, value in enumerate(toronto2024_df_reset['Total Precip (mm)']):
    plt.text(i, value + 0.2, round(value, 2), ha='right', va='top', fontsize=10, color='blue', fontweight='bold')

for i, value in enumerate(jasper2024_df_reset['Total Precip (mm)']):
    plt.text(i, value + 1, round(value, 2), ha='right', va='top', fontsize=10, color='red', fontweight='bold')

plt.tight_layout()
plt.legend()
plt.show()

toronto_2023_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2023)]
toronto_avgprecip_2023 = toronto_2023_data.groupby('Month')['Total Precip (mm)'].mean()
toronto2023_df = pd.DataFrame(toronto_avgprecip_2023)
toronto2023_df_reset = toronto2023_df.reset_index()
toronto2023_df_reset['Month'] = toronto2023_df_reset['Month'].apply(lambda x: calendar.month_name[x])

berry_2023_data = data[(data['Station Name'] == 'BERRY HILL') & (data['Year'] == 2023)]
berry_avgprecip_2023 = berry_2023_data.groupby('Month')['Total Precip (mm)'].mean()
berry2023_df = pd.DataFrame(berry_avgprecip_2023)
berry2023_df_reset = berry2023_df.reset_index()
berry2023_df_reset['Month'] = berry2023_df_reset['Month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(12,6))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.title('Average Precipitation in Newfoundland vs Toronto in 2023')
plt.xlabel('Month')
plt.ylabel('Average Precipitation (mm)')

plt.plot(toronto2023_df_reset['Month'], toronto2023_df_reset['Total Precip (mm)'], marker='o', label='Toronto 2023', color='blue')

plt.plot(berry2023_df_reset['Month'], berry2023_df_reset['Total Precip (mm)'], marker='o', label='Newfoundland 2023', color='red')

plt.xticks(rotation=45)

for i, value in enumerate(toronto2023_df_reset['Total Precip (mm)']):
    plt.text(i, value + 1.5, round(value, 2), ha='right', va='top', fontsize=10, color='blue', fontweight='bold')

for i, value in enumerate(berry2023_df_reset['Total Precip (mm)']):
    plt.text(i, value + 1, round(value, 2), ha='right', va='top', fontsize=10, color='red', fontweight='bold')

plt.tight_layout()
plt.legend()
plt.show()

toronto_2024_data = data[(data['Station Name'] == 'TORONTO CITY') & (data['Year'] == 2024)]
toronto_avgprecip_2024 = toronto_2024_data.groupby('Month')['Mean Temp (°C)'].mean()
toronto2024_df = pd.DataFrame(toronto_avgprecip_2024)
toronto2024_df_reset = toronto2024_df.reset_index()
toronto2024_df_reset['Month'] = toronto2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

winnipeg_2024_data = data[(data['Station Name'] == 'WINNIPEG A CS') & (data['Year'] == 2024)]
winnipeg_avgprecip_2024 = winnipeg_2024_data.groupby('Month')['Mean Temp (°C)'].mean()
winnipeg2024_df = pd.DataFrame(winnipeg_avgprecip_2024)
winnipeg2024_df_reset = winnipeg2024_df.reset_index()
winnipeg2024_df_reset['Month'] = winnipeg2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

montreal_2024_data = data[(data['Station Name'] == 'MONTREAL/ST-HUBERT') & (data['Year'] == 2024)]
montreal_avgprecip_2024 = montreal_2024_data.groupby('Month')['Mean Temp (°C)'].mean()
montreal2024_df = pd.DataFrame(montreal_avgprecip_2024)
montreal2024_df_reset = montreal2024_df.reset_index()
montreal2024_df_reset['Month'] = montreal2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

ottawa_2024_data = data[(data['Station Name'] == 'OTTAWA CDA') & (data['Year'] == 2024)]
ottawa_avgprecip_2024 = ottawa_2024_data.groupby('Month')['Mean Temp (°C)'].mean()
ottawa2024_df = pd.DataFrame(ottawa_avgprecip_2024)
ottawa2024_df_reset = ottawa2024_df.reset_index()
ottawa2024_df_reset['Month'] = ottawa2024_df_reset['Month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(12,6))

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.title('Average Monthly Temperature in Toronto, Montreal, Winnipeg, and Ottawa in 2024')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

plt.plot(toronto2024_df_reset['Month'], toronto2024_df_reset['Mean Temp (°C)'], marker='o', label='Toronto 2024', color='blue')

plt.plot(winnipeg2024_df_reset['Month'], winnipeg2024_df_reset['Mean Temp (°C)'], marker='s', label='Winnipeg 2024', color='red')

plt.plot(montreal2024_df_reset['Month'], montreal2024_df_reset['Mean Temp (°C)'], marker='x', label='Montreal 2024', color='green')

plt.plot(ottawa2024_df_reset['Month'], ottawa2024_df_reset['Mean Temp (°C)'], marker='o', label='Ottawa 2024', color='orange')

plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()


