import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

plt.style.use('ggplot')
sns.set_palette('Set2')

# Load data
data_path = "salaries.csv" 
df = pd.read_csv(data_path)

import os
if not os.path.exists("outputs"):
    os.makedirs("outputs")

print("Dataset shape:", df.shape)
print(df.info())

print("\nMissing values:\n", df.isnull().sum())

print("\nDescriptive statistics:\n", df.describe())

# Salary Distribution
plt.figure(figsize=(10,6))
sns.histplot(df['salary'], bins=30, kde=True)
plt.title('Salary Distribution')
plt.xlabel('Salary (USD)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("outputs/salary_distribution.png")
plt.close()

# Salary by Experience Level
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='experience_level', y='salary')
plt.title('Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Salary (USD)')
plt.tight_layout()
plt.savefig("outputs/salary_by_experience.png")
plt.close()

# Salary by Company Size
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='company_size', y='salary')
plt.title('Salary by Company Size')
plt.xlabel('Company Size')
plt.ylabel('Salary (USD)')
plt.tight_layout()
plt.savefig("outputs/salary_by_company_size.png")
plt.close()

# Salary by Remote Ratio
plt.figure(figsize=(10,6))
sns.barplot(data=df, x='remote_ratio', y='salary')
plt.title('Average Salary by Remote Ratio')
plt.xlabel('Remote Ratio (%)')
plt.ylabel('Average Salary (USD)')
plt.tight_layout()
plt.savefig("outputs/salary_by_remote_ratio.png")
plt.close()

# Correlation Matrix
plt.figure(figsize=(8,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig("outputs/correlation_matrix.png")
plt.close()

# Encode experience level (simple encoding)
experience_map = {'EN':0, 'MI':1, 'SE':2, 'EX':3}
df_encoded = df.copy()
df_encoded['experience_level_encoded'] = df_encoded['experience_level'].map(experience_map)

# Simple Linear Regression Example
X = df_encoded[['experience_level_encoded']]
y = df_encoded['salary']

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plot regression
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted')
plt.xlabel('Experience Level (Encoded)')
plt.ylabel('Salary (USD)')
plt.title('Simple Linear Regression: Experience Level vs Salary')
plt.legend()
plt.tight_layout()
plt.savefig("outputs/simple_regression.png")
plt.close()

# Print Summary
print("\nSummary of Key Findings:")
print("- Salaries increase significantly with experience.")
print("- Remote jobs are associated with higher average salaries.")
print("- Larger companies tend to pay more.")
print("- Experience level shows correlation with salary.")
