import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")

df = pd.read_csv(r"C:\Users\Jabarlal\Downloads\netflix1.csv")
df.head()

df.shape
df.info()
df.isnull().sum()

df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Not Specified')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['year_added'] = df['date_added'].dt.year

type_count = df['type'].value_counts()

type_count.plot(kind='bar', figsize=(6,4))
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.show()

yearly_content = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(8,4))
yearly_content.plot()
plt.title("Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

top_countries = df['country'].value_counts().head(10)

top_countries.plot(kind='bar', figsize=(8,4))
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()

genres = df['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(10)

top_genres.plot(kind='bar', figsize=(8,4))
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

rating_count = df['rating'].value_counts()

rating_count.plot(kind='bar', figsize=(8,4))
plt.title("Content Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

