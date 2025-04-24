🌫️ Air Quality Analysis - India

This project provides an exploratory data analysis of air quality data across various cities and states in India. Using Python and essential data science libraries, it highlights pollution trends, categorizes pollution levels, and visualizes geographical hotspots for different pollutants.

📁 Dataset

The dataset used in this project is assumed to be named:

air_quality_data.csv

It should contain columns such as:
 City,
 State,
 Date,
 Latitude,
 Longitude,
 Pollutant columns (e.g., PM2.5, NO2, SO2, etc.)

📦 Dependencies
Install the following Python libraries before running the script:

pip install pandas numpy matplotlib seaborn plotly folium

📌 Objectives Covered

1.Exploratory Data Analysis (EDA)

  Analyze structure, count of records per city/state, common pollutants, and basic statistics.

2.Pollution Level Categorization

  Add pollution_level column (e.g., Good, Moderate, Unhealthy) based on pollutant averages.
  Visualize category frequencies by city/state.

3.Geographical Pollution Heatmap

  Use latitude/longitude to map pollution intensity across India using a heatmap.

4.Dominant Pollutants by State

  Identify the most frequently recorded pollutant in each state.
  Visualize dominant pollutants using bar charts.

🧼 Data Cleaning

  Handled missing or null pollutant values.

  Standardized pollutant column names.

  Removed duplicate entries and ensured consistent data types.


📃 License
Feel free to modify and use this analysis for educational or personal projects. Attribution is appreciated.
