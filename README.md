#  Salaries Dataset Analysis Project

This project demonstrates a complete end-to-end data analytics workflow using Python to analyze an employee salaries dataset. It shows how to clean, explore, visualize, and draw insights from real-world data.

---

## Project Overview

**Objectives:**
- Load and inspect raw salary data
- Clean and preprocess the dataset
- Perform descriptive statistical analysis
- Detect and analyze outliers
- Visualize salary distributions and trends
- Provide actionable business recommendations

---

##  Dataset

The dataset contains employee salary records, including:
- Employee identifiers
- Departments
- Gender
- Salary amounts
- [Other relevant columns if applicable]

---

## 🛠 Technologies Used

- Python
- pandas
- matplotlib
- seaborn
- Colab Notebook

---

## Project Workflow

1. **Data Loading**
   - Read raw CSV data into a pandas DataFrame
   - Inspect data structure and types

2. **Data Cleaning**
   - Standardize column names
   - Handle missing values (e.g., imputation)
   - Convert data types
   - Remove duplicates
   - Validate salary ranges

3. **Exploratory Data Analysis**
   - Descriptive statistics (mean, median, min, max)
   - Salary summaries by department and gender
   - Outlier detection using the IQR method

4. **Data Visualization**
   - Histograms of salary distributions
   - Boxplots of salary by department and gender
   - Bar charts of average salaries
   - Correlation heatmaps

5. **Insights & Recommendations**
   - Highlight trends, anomalies, and potential areas for further analysis

---

## Sample Visualizations

<p align="center">
  <img src="images/salary_distribution.png" alt="Salary Distribution" width="600"/>
</p>

<p align="center">
  <img src="images/salary_by_department.png" alt="Salary by Department" width="600"/>
</p>

---
## 📊 Visualizations

### Salary Distribution
![Salary Distribution](outputs/salary_distribution.png)

### Salary by Experience
![Salary by Experience](outputs/salary_by_experience.png)

### Salary by Company Size
![Salary by Company Size](outputs/salary_by_company_size.png)

### Correlation Matrix
![Correlation Matrix](outputs/correlation_matrix.png)

### Simple Regression
![Regression](outputs/simple_regression.png)


## 💡 Key Insights

- The salary distribution is **[right-skewed / normal / other]**
- **[Department X]** has the highest average salaries
- **[N]** salary outliers were detected
- [If applicable] Gender analysis suggests **[potential disparities / no significant difference]**

---

## Recommendations

- Review high outlier salaries to confirm data validity
- Evaluate compensation consistency across departments
- Implement data validation rules to reduce inconsistencies in future entries

---

