## Problem Statement
The objective of this project is to analyze Netflix content data to understand
content distribution, genre trends, country-wise production, and release-year
patterns using Python-based exploratory data analysis.
  
##Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")

##Load Dataset
df = pd.read_csv("../data/netflix_titles.csv")
df.head()

##Data Understanding
df.shape
df.info()
df.isnull().sum()

##Data Cleaning
**Handle missing values**
df['country'].fillna('Unknown', inplace=True)
df['director'].fillna('Not Specified', inplace=True)

**Convert date column (if present)**
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

##Feature Engineering
df['year_added'] = df['date_added'].dt.year

##Exploratory Data Analysis (EDA)

**1. Movies vs TV Shows**
type_count = df['type'].value_counts()

type_count.plot(kind='bar', figsize=(6,4))
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.show()

**2. Content Added Over the Years**
yearly_content = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(8,4))
yearly_content.plot()
plt.title("Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

**3. Top 10 Countries Producing Content**
top_countries = df['country'].value_counts().head(10)

top_countries.plot(kind='bar', figsize=(8,4))
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()

**4. Most Common Genres**
genres = df['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(10)

top_genres.plot(kind='bar', figsize=(8,4))
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

**5. Content Rating Distribution**
rating_count = df['rating'].value_counts()

rating_count.plot(kind='bar', figsize=(8,4))
plt.title("Content Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

## Key Insights
- Netflix hosts more Movies than TV Shows.
- Content production increased significantly after 2015.
- United States produces the highest number of titles.
- Drama and International Movies are the most common genres.
- TV-MA is the most frequent content rating.

## Business Recommendations
- Continue investing in movie production as it dominates the platform.
- Increase content creation in fast-growing genres like Drama.
- Expand content production in emerging markets.
- Maintain balanced content ratings to reach diverse audiences.

## Conclusion
This analysis provided insights into Netflix’s content distribution,
growth trends, and genre popularity. Python-based EDA helped identify
key patterns that can support content strategy decisions.
