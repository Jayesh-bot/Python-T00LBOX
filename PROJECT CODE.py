import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load dataset
df = pd.read_csv(r"C:\Users\Jayesh\OneDrive\Desktop\python ca\PYTHON DATASET  AIR QUALITY.csv")
print(df)
print("\nShape of the Data set: ",df.shape)
print("\nInformation of Data Set :",df.info())
print(df.isnull())
print("total null in columns", df.isnull().sum())
print("Total null elements in whole dataset", df.isnull().sum().sum())

df['last_update'] = pd.to_datetime(df['last_update'])
df = df.dropna(subset=['pollutant_avg'])

# Obj 1: Exploratory Data Analysis
print("\n Objective 1: Exploratory Data Analysis")

print("\n--- Record Count Per State ---")
print(df['state'].value_counts().head())
print("\n   ---------- Common Pollutants ---------- ")
print(df['pollutant_id'].value_counts().head())
print("\n   ---------- Basic Statistics -----------")
print(df[['pollutant_min','pollutant_max','pollutant_avg']].describe())

# Objth-wise PM2.5 Trend for Top 5 Polluted Cities in 2025

print("\nObjective 2: Month-wise PM2.5 Trend for Top 5 Polluted Cities in 2025")
df['year'] = df['last_update'].dt.year
df['month'] = df['last_update'].dt.month
selected_year = 2025
df_year = df[df['year'] == selected_year]
df_pm25 = df_year[df_year['pollutant_id'] == 'PM2.5']
city_avg_pm25 = df_pm25.groupby('city')['pollutant_avg'].mean()
top_5_cities = city_avg_pm25.sort_values(ascending=False).head(5).index
df_top5 = df_pm25[df_pm25['city'].isin(top_5_cities)]

fig,ax =plt.subplots(figsize=(14, 6))
first_half= df_top5[df_top5['month'] <= 6].groupby(['city', 'month'])['pollutant_avg'].mean().unstack()

first_half.T.plot(kind='bar', ax=ax)
ax.set_title(f"PM2.5 Monthly Trend (Jan–Jun {selected_year}) - Top 5 Cities")
ax.set_xlabel("Month")
ax.set_ylabel("Average PM2.5")
ax.set_xticks(range(6))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], rotation=0)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.legend(title='City')
plt.tight_layout()
plt.show()


#Obj 3:Categorize Pollution Levels
print("\nObjective 3:Categorize Pollution Levels")

bins=[0,50,100,150,200,300,np.inf]
labels=['Good','Moderate','Unhealthy for Sensitive','Unhealthy','Very Unhealthy','Hazardous']
df['pollution_level'] = pd.cut(df['pollutant_avg'],bins=bins,labels=labels)
plt.figure(figsize=(10,6))

sns.countplot(data=df,y='pollution_level',hue='pollution_level',palette="Oranges",legend=False)
plt.title("Pollution Level Categories")
plt.xlabel("Count")
plt.ylabel("Pollution Level")
plt.tight_layout()
plt.show()


# Obj 4:State-wise Average Pollutant Heatmap
print("\nObjective 4:State-wise Average Pollutant Heatmap")

state_pollution= df.pivot_table(values='pollutant_avg', index='state', columns='pollutant_id')
plt.figure(figsize=(14, 8))
sns.heatmap(state_pollution,cmap='YlOrRd',linewidths=0.5,annot=True,fmt=".1f")
plt.title("State-wise Average Pollutant")
plt.tight_layout()
plt.show()

# Obj 5:most Common Pollutant Per State
print("\nObjective 5:most Common Pollutant Per State")
common_p=df.groupby(['state', 'pollutant_id']).size().reset_index(name='count')
idx=common_p.groupby('state')['count'].idxmax()
dominant_p = common_p.loc[idx]
plt.figure(figsize=(12,6))
sns.barplot(data=dominant_p,x='state',y='count',hue='pollutant_id')
plt.xticks(rotation=90)
plt.title("Most Common Pollutant per State")
plt.tight_layout()
plt.show()


#Obj 6:Top 5 Most Polluted Cities

city_p=df.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,6))
sns.heatmap(city_p.to_frame(),annot=True,cmap="coolwarm",linewidths=0.5)
plt.title("Top Polluted Cities")
plt.xlabel("Average Pollution")
plt.ylabel("City")
plt.tight_layout()
plt.show()

#States with Highest Max Pollution
print("\nStates with Highest Max Pollution")
max_p= df.groupby('state')['pollutant_max'].max().sort_values(ascending=False).to_frame()
plt.figure(figsize=(8,10))
sns.heatmap(max_p.head(20),annot=True,cmap="Reds",fmt=".1f",linewidths=.5)
plt.title("Max Pollution by State -(Top 20)")
plt.tight_layout()
plt.show()
