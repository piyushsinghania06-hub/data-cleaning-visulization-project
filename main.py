import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data/sales_data.csv')

# Display basic info
print(df.info())

# -------------------
# Data Cleaning
# -------------------

# Handle missing values
df['Sales'].fillna(df['Sales'].mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# -------------------
# Outlier Removal (IQR)
# -------------------

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Sales'] >= Q1 - 1.5 * IQR) & 
        (df['Sales'] <= Q3 + 1.5 * IQR)]

# Save cleaned data
df.to_csv('outputs/cleaned_data.csv', index=False)

# -------------------
# Visualization
# -------------------

# Sales Trend
plt.figure()
df.groupby('Date')['Sales'].sum().plot()
plt.title('Sales Trend')
plt.savefig('outputs/sales_trend.png')

# Heatmap
plt.figure()
sns.heatmap(df[['Sales', 'Profit']].corr(), annot=True)
plt.savefig('outputs/heatmap.png')

print("Project Completed Successfully!")
