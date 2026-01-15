```python
## Problem Statement
#The objective of this project is to analyze data analyst and data science job
#salaries to understand how experience level, employment type, company size,
#job type (remote/onsite), and location impact salaries.

#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")

#Load Dataset
df = pd.read_csv(r"C:\Users\Jabarlal\Downloads/Data Science Job Salaries.csv")
df.head()

#Understand the Data
df.shape
df.info()
df.isnull().sum()

#Data Cleaning
#1. Data Cleaning
df = df.drop_duplicates()

#2. Rename salary column (simplify)
df = df.rename(columns={'salary_in_usd': 'salary'})

#Make Data Human-Readable
#1. Experience level
df['experience_level'] = df['experience_level'].map({
    'EN': 'Entry',
    'MI': 'Mid',
    'SE': 'Senior',
    'EX': 'Executive'
})

#2. Employment type
df['employment_type'] = df['employment_type'].map({
    'FT': 'Full-time',
    'PT': 'Part-time',
    'CT': 'Contract',
    'FL': 'Freelance'
})

#3. Company size
df['company_size'] = df['company_size'].map({
    'S': 'Small',
    'M': 'Medium',
    'L': 'Large'
})

#4. Job type (remote / hybrid / onsite)
df['job_type'] = df['remote_ratio'].map({
    0: 'Onsite',
    50: 'Hybrid',
    100: 'Remote'
})

#Exploratory Data Analysis (EDA)
#1. Salary Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['salary'], bins=30, kde=True)
plt.title("Salary Distribution (USD)")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

#2. Salary vs Experience Level
df = df.loc[:, ~df.columns.duplicated()]
salary_cols = [col for col in df.columns if 'salary' in col.lower()]
salary_cols

df = df.copy()
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df = df.dropna(subset=['salary', 'experience_level'])

exp_salary = (
    df.groupby('experience_level', as_index=False)['salary']
      .mean()
      .rename(columns={'salary': 'avg_salary'})
)
exp_salary.plot(kind='bar', figsize=(7,4))
plt.title("Average Salary by Experience Level")
plt.ylabel("Salary (USD)")
plt.show()

#3. Salary vs Employment Type
emp_salary = df.groupby('employment_type')['salary'].mean().sort_values()

emp_salary.plot(kind='bar', figsize=(7,4))
plt.title("Average Salary by Employment Type")
plt.ylabel("Salary (USD)")
plt.show()

#4. Salary vs Company Size
company_salary = df.groupby('company_size')['salary'].mean().sort_values()

company_salary.plot(kind='bar', figsize=(7,4))
plt.title("Average Salary by Company Size")
plt.ylabel("Salary (USD)")
plt.show()

#5. Salary vs Job Type (Remote / Onsite)
jobtype_salary = df.groupby('job_type')['salary'].mean().sort_values()

jobtype_salary.plot(kind='bar', figsize=(7,4))
plt.title("Average Salary by Job Type")
plt.ylabel("Salary (USD)")
plt.show()

#6. Top 10 Highest-Paid Job Titles
top_jobs = df.groupby('job_title')['salary'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_jobs.values, y=top_jobs.index)
plt.title("Top 10 Highest Paid Job Roles")
plt.xlabel("Average Salary (USD)")
plt.show()

## Key Insights
#- Executive and senior roles earn significantly higher salaries.
#- Contract-based roles offer the highest average pay.
#- Large companies pay more than small and medium companies.
#- Remote jobs have higher average salaries than onsite roles.
#- Specialized roles such as Principal Data Engineer and Data Architect
#  are among the highest paid.

## Recommendations
#- Professionals aiming for higher salaries should target senior or executive roles.
#- Remote opportunities can provide better compensation.
#- Large organizations generally offer higher pay scales.
#- Specializing in high-demand roles can significantly increase salary potential.

## Conclusion
#This project analyzed job salary data to identify key salary drivers across
#experience, employment type, company size, and job type. Python-based EDA
#helped extract actionable insights useful for both job seekers and employers.





```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 607 entries, 0 to 606
    Data columns (total 12 columns):
     #   Column              Non-Null Count  Dtype 
    ---  ------              --------------  ----- 
     0   Unnamed: 0          607 non-null    int64 
     1   work_year           607 non-null    int64 
     2   experience_level    607 non-null    object
     3   employment_type     607 non-null    object
     4   job_title           607 non-null    object
     5   salary              607 non-null    int64 
     6   salary_currency     607 non-null    object
     7   salary_in_usd       607 non-null    int64 
     8   employee_residence  607 non-null    object
     9   remote_ratio        607 non-null    int64 
     10  company_location    607 non-null    object
     11  company_size        607 non-null    object
    dtypes: int64(5), object(7)
    memory usage: 57.0+ KB
    


    
![png](output_0_1.png)
    



    
![png](output_0_2.png)
    



    
![png](output_0_3.png)
    



    
![png](output_0_4.png)
    



    
![png](output_0_5.png)
    



    
![png](output_0_6.png)
    



```python

```
