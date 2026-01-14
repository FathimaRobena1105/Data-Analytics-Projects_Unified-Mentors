```python
#1. Problem Statement
    #The objective of this project is to analyze Supermart grocery sales data to identify sales trends, top-performing categories, 
    #regional performance, and profit behavior, and provide actionable business insights.

#2. Import Libraries#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
    
plt.style.use("default")

#3. Load Dataset#
   
df = pd.read_csv(r"C:\Users\Jabarlal\Downloads\SGS.csv")
df.head()

#4. Data Understanding#

df.shape
df.info()
df.isnull().sum()

#5. Data Cleaning#

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df.duplicated().sum()
df = df.drop_duplicates()

#6. Feature Engineering#

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month_Name'] = df['Order Date'].dt.strftime('%B')
    
df.head()

#7. Exploratory Data Analysis (EDA)#

    #1. Total Sales & Profit#

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

    #2. Sales by Category#

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

category_sales.plot(kind='bar', figsize=(8,5))
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

    #3. Profit by Category#

category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

category_profit.plot(kind='bar', figsize=(8,5), color='green')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

    #4. Monthly Sales Trend#

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

    #5. Yearly Sales Distribution#

yearly_sales = df.groupby('Year')['Sales'].sum()

yearly_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title("Yearly Sales Distribution")
plt.ylabel("")
plt.show()

    #6. Top 5 Cities by Sales#

top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)

top_cities.plot(kind='bar', figsize=(8,5), color='orange')
plt.title("Top 5 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()

    #7. Discount vs Profit Relationship#

plt.figure(figsize=(7,5))
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title("Discount vs Profit")
plt.show()

#8. Key Insights#
   # - Egg, Meat & Fish is the highest revenue-generating category.
   # - Sales peak during the later months of the year.
   # - Certain high-discount products result in negative profits.
   # - A small number of cities contribute a large portion of sales.

#9. Business Recommendations#

   # - Increase inventory and promotions for high-performing categories.
   # - Optimize discount strategies to avoid loss-making products.
   # - Focus marketing efforts on top-performing cities.
   # - Plan inventory in advance for seasonal demand.

#10. Conclusion#

     #This analysis provided insights into sales performance, category trends, regional demand, and profitability. 
     #The findings can help Supermart improve sales strategies, reduce losses, and optimize operations.
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 9994 entries, 0 to 9993
    Data columns (total 11 columns):
     #   Column         Non-Null Count  Dtype  
    ---  ------         --------------  -----  
     0   Order ID       9994 non-null   object 
     1   Customer Name  9994 non-null   object 
     2   Category       9994 non-null   object 
     3   Sub Category   9994 non-null   object 
     4   City           9994 non-null   object 
     5   Order Date     9994 non-null   object 
     6   Region         9994 non-null   object 
     7   Sales          9994 non-null   int64  
     8   Discount       9994 non-null   float64
     9   Profit         9994 non-null   float64
     10  State          9994 non-null   object 
    dtypes: float64(2), int64(1), object(8)
    memory usage: 859.0+ KB
    Total Sales: 14956982
    Total Profit: 3747121.1999999997
    


    
![png](output_0_1.png)
    



    
![png](output_0_2.png)
    



    
![png](output_0_3.png)
    



    
![png](output_0_4.png)
    



    
![png](output_0_5.png)
    



    
![png](output_0_6.png)
    



```python

```
