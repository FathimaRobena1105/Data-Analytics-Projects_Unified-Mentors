#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")
pd.set_option("display.max_columns", None)

#Load Dataset
df = pd.read_csv(
    r"C:\Users\Jabarlal\Downloads\Summer-Olympic-medals-1976-to-2008.csv",
    encoding="latin1"
)
df.head()

#Understand the dataset
df.shape
df.info()
df.isnull().sum()

#Drop unnecessary columns
df = df.drop(columns=['Event_gender', 'Country_Code'], errors='ignore')
df = df.copy()

#Fix data types & missing rows
df = df.dropna(how='all')
df['Year'] = df['Year'].astype(int)
df = df.dropna(subset=['City', 'Sport', 'Athlete', 'Gender', 'Country', 'Medal'])

#Analysis Questions
#Q1 — Which city hosted maximum number of Olympics?
q1 = (
    df[['City', 'Year']]
    .drop_duplicates('Year')
)

q1

#Q2 — Which city hosted most events?
q2 = df['City'].value_counts()

plt.figure(figsize=(10,4))
q2.plot(kind='bar')
plt.title("Number of Olympic Events by City")
plt.xlabel("City")
plt.ylabel("Event Count")
plt.show()

#Q3 — How many unique events & sports?
q3 = df[['Sport', 'Discipline', 'Event']].drop_duplicates()

print("Total unique events:", len(q3))

#Events by sport
q3_sport = q3.groupby('Sport').size().sort_values(ascending=False)

plt.figure(figsize=(10,4))
q3_sport.plot(kind='bar')
plt.title("Number of Events by Sport")
plt.xlabel("Sport")
plt.ylabel("Event Count")
plt.show()

#Q4 — Which athlete won the most medals?
q4 = (
    df.groupby('Athlete')
      .size()
      .reset_index(name='Medal_Count')
      .sort_values(by='Medal_Count', ascending=False)
      .head(10)
)

plt.figure(figsize=(10,4))
sns.barplot(data=q4, x='Athlete', y='Medal_Count')
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Athletes by Medal Count")
plt.show()

#Q5 — Gender distribution of medal winners
q5 = df['Gender'].value_counts()

plt.figure(figsize=(5,4))
q5.plot(kind='bar')
plt.title("Gender Distribution of Medal Winners")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

#Q6 — Medal count by country & year (SAFE VERSION)
q6 = (
    df.groupby(['Year', 'Country', 'Medal'])
      .size()
      .reset_index(name='Count')
)

q6_pivot = (
    q6.pivot_table(
        index=['Year', 'Country'],
        columns='Medal',
        values='Count',
        fill_value=0
    )
    .reset_index()
)

q6_pivot['Total'] = q6_pivot[['Gold', 'Silver', 'Bronze']].sum(axis=1)
q6_pivot.head()

#Q7 — Which country dominated which sport?
q7 = (
    df.groupby(['Sport', 'Country'])
      .size()
      .reset_index(name='Medal_Count')
      .sort_values(['Sport', 'Medal_Count'], ascending=[True, False])
)

# Example: Archery
q7[q7['Sport'] == 'Archery'].head(5)

#Q8 — Athletes who won medals in multiple sports
athlete_sports = (
    df[['Athlete', 'Sport']]
    .drop_duplicates()
    .groupby('Athlete')['Sport']
    .nunique()
)

multi_sport_athletes = athlete_sports[athlete_sports > 1]
multi_sport_athletes.head(10)

#Q9 — Top 5 countries per Olympics (CLEAN VERSION)
top5 = (
    q6_pivot
    .sort_values(['Year', 'Total'], ascending=[True, False])
    .groupby('Year')
    .head(5)
)

trend = (
    top5.pivot_table(
        index='Year',
        columns='Country',
        values='Total',
        fill_value=0
    )
)

plt.figure(figsize=(14,6))
sns.lineplot(data=trend)
plt.title("Top 5 Countries Medal Trend (1976–2008)")
plt.ylabel("Total Medals (Athlete Count)")
plt.show()

