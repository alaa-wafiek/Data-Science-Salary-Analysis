
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load Data
df = pd.read_csv("salaries.csv")
print("Initial Data Preview:")
print(df.head())

# Clean Column Names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
print("\nCleaned Columns:", df.columns)

# Convert Data Types
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Handle Missing Values
salary_median = df["salary"].median()
df["salary"].fillna(salary_median, inplace=True)

if "department" in df.columns:
    df.dropna(subset=["department"], inplace=True)

# Standardize Categories
if "department" in df.columns:
    df["department"] = df["department"].str.strip().str.title()

if "gender" in df.columns:
    df["gender"] = (
        df["gender"]
        .str.strip()
        .str.lower()
        .replace({"m": "male", "f": "female", "male": "male", "female": "female"})
    )

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Validate Salary
df = df[df["salary"] >= 0]

# Outlier Detection
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df["is_outlier"] = df["salary"].apply(lambda x: x < lower or x > upper)

print("\nDescriptive Statistics:")
print(df["salary"].describe())

# Visualization (Salary Histogram)
sns.histplot(df["salary"], bins=30, kde=True, color="steelblue")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.close()

# Boxplot by Department
if "department" in df.columns:
    plt.figure(figsize=(12,6))
    sns.boxplot(x="department", y="salary", data=df, palette="viridis")
    plt.title("Salary by Department")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("salary_by_department.png")
    plt.close()

# Boxplot by Gender
if "gender" in df.columns:
    sns.boxplot(x="gender", y="salary", data=df, palette="Set2")
    plt.title("Salary by Gender")
    plt.tight_layout()
    plt.savefig("salary_by_gender.png")
    plt.close()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.close()

# Save Cleaned Data
df.to_csv("salaries_cleaned.csv", index=False)
print("\n Cleaned data saved as 'salaries_cleaned.csv'")
