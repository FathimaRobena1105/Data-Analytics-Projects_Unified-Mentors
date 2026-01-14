import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")

df = pd.read_csv(r"C:\Users\Jabarlal\Downloads\SGS.csv")
df.head()

df.shape
df.info()
df.isnull().sum()

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df.duplicated().sum()
df = df.drop_duplicates()

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month_Name'] = df['Order Date'].dt.strftime('%B')
df.head()

#Total Sales & Profit#
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

#Sales by Category#
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

category_sales.plot(kind='bar', figsize=(8,5))
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

#Profit by Category#
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

category_profit.plot(kind='bar', figsize=(8,5), color='green')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

#Monthly Sales Trend#
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#Yearly Sales Distribution#
yearly_sales = df.groupby('Year')['Sales'].sum()

yearly_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title("Yearly Sales Distribution")
plt.ylabel("")
plt.show()

#Top 5 Cities by Sales#
top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)

top_cities.plot(kind='bar', figsize=(8,5), color='orange')
plt.title("Top 5 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()

#Discount vs Profit Relationship#
plt.figure(figsize=(7,5))
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title("Discount vs Profit")
plt.show()

