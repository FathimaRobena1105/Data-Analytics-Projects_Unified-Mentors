import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")

#Load dataset
df = pd.read_csv(r"C:\Users\Jabarlal\Downloads/Data Science Job Salaries.csv")
df.head()

#Understand dataset
df.shape
df.info()
df.isnull().sum()

#Data cleaning
df = df.drop_duplicates()

df = df.rename(columns={'salary_in_usd': 'salary'})

#Make Data Human_Readable
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

#4. Job type (remote/hybrid/onsite)
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

