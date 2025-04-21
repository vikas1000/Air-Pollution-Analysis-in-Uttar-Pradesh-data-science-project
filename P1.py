import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = r"C:\All subject\INT375DATA SCIENCE TOOLBOX PYTHON PROGRAMMING\Project\Cleaned_AIR_Pollution_UP.csv"
df = pd.read_csv(file_path)

# Convert 'Sampling Date' to datetime format
if 'Sampling Date' in df.columns:
    df['Sampling Date'] = pd.to_datetime(df['Sampling Date'], errors='coerce')
else:
    print("Warning: 'Sampling Date' column not found.")

# Drop 'SPM' column if it exists and has all missing values
if 'SPM' in df.columns and df['SPM'].isna().all():
    df.drop(columns=['SPM'], inplace=True)

# Display dataset structure and first few rows
print("\nDataset Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Check and fill missing values (numerical columns)
print("\nMissing Values:")
print(df.isnull().sum())

numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())


# ---------------- PLOTS ---------------- #

# Set style
sns.set(style="whitegrid")

# 1. Histogram of PM10 (RSPM) levels
plt.figure(figsize=(10, 6))
sns.histplot(df['RSPM/PM10'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribution of PM10 Levels')  
plt.xlabel('PM10 (µg/m³)')
plt.ylabel('Frequency')
plt.grid()
plt.show()

# 2. Correlation heatmap of pollutants
plt.figure(figsize=(10, 6))
corr = df[['SO2', 'NO2', 'RSPM/PM10']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Air Pollutants') 
plt.show()

# 3. PM10 over time (line plot)
plt.figure(figsize=(12, 6))
df_sorted = df.sort_values('Sampling Date')
plt.plot(df_sorted['Sampling Date'], df_sorted['RSPM/PM10'], marker='o', linestyle='-', color='green')
plt.title('PM10 Levels Over Time')  
plt.ylabel('PM10 (µg/m³)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# 4. Top 10 most polluted cities by average PM10
city_pollution = df.groupby('City/Town/Village/Area')['RSPM/PM10'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=city_pollution.values, y=city_pollution.index, palette='Reds_r')
plt.xlabel('Average PM10 Level')
plt.ylabel('City')
plt.title('Top 10 Most Polluted Cities in Uttar Pradesh (by PM10)')  
plt.tight_layout()
plt.show()

# 5. Histogram of SO2
plt.figure(figsize=(8, 5))
sns.histplot(df['SO2'].dropna(), kde=True, color='skyblue')
plt.title('Distribution of SO2')  
plt.show()

# 6. Histogram of NO2
plt.figure(figsize=(8, 5))
sns.histplot(df['NO2'].dropna(), kde=True, color='orange')
plt.title('Distribution of NO2')  
plt.show()

# 7. Boxplot for pollutants
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['SO2', 'NO2', 'RSPM/PM10']])
plt.title('Boxplot of Pollutants')  
plt.show()

# 8. Monthly average pollution levels (SO2, NO2, PM10)
df_time = df.dropna(subset=['Sampling Date'])
df_time['Month'] = df_time['Sampling Date'].dt.to_period('M')
monthly_avg = df_time.groupby('Month')[['SO2', 'NO2', 'RSPM/PM10']].mean()

plt.figure(figsize=(15, 6))
monthly_avg.plot(marker='o')
plt.title('Monthly Average Pollution Levels (SO2, NO2, PM10)')  
plt.xlabel('Month')
plt.ylabel('Pollutant Level')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

















