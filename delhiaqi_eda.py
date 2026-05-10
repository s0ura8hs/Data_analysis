"""# **Exploratory Data Analysis**"""

df.describe().T

for i in df.select_dtypes(include="number").columns:
  sns.histplot(data=df, x=i)
  plt.show()

for i in df.select_dtypes(include="number").columns:
    sns.boxplot(data=df, x=i)
    plt.show()

# scatterplot to understand relationship
df.select_dtypes(include="number").columns

for i in ['year', 'month', 'day', 'hour', 'is_weekend', 'latitude', 'longitude',
       'pm25', 'pm10', 'no2', 'so2', 'co', 'o3', 'temperature', 'humidity',
       'wind_speed', 'visibility']:
       sns.scatterplot(data=df, x=i, y= 'aqi')
       plt.show()

for i in ['year', 'month', 'day', 'hour', 'is_weekend', 'latitude', 'longitude',
       'pm25', 'pm10', 'no2', 'so2', 'co', 'o3', 'temperature', 'humidity',
       'wind_speed']:
       sns.scatterplot(data=df, x=i, y= 'visibility')
       plt.show()

for i in ['year', 'month', 'day', 'hour', 'is_weekend', 'latitude', 'longitude',
       'pm25', 'pm10', 'no2', 'so2', 'co', 'o3', 'temperature', 'humidity']:
       sns.scatterplot(data=df, x=i, y= 'wind_speed')
       plt.show()

for i in ['year', 'month', 'day', 'hour', 'is_weekend', 'latitude', 'longitude',
       'pm25', 'pm10', 'no2', 'so2', 'co', 'o3', 'temperature']:
       sns.scatterplot(data=df, x=i, y= 'humidity')
       plt.show()

for i in ['year', 'month', 'day', 'hour', 'is_weekend', 'latitude', 'longitude',
       'pm25', 'pm10', 'no2', 'so2', 'co', 'o3']:
       sns.scatterplot(data=df, x=i, y= 'temperature')
       plt.show()

# correlation with heatmap
df.select_dtypes(include="number").corr()

s= df.select_dtypes(include="number").corr()
sns.heatmap(s,annot= True)
