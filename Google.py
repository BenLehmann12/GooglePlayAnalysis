import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder


google = pd.read_csv('googleplay.csv')
google = google.drop(['Last Updated','Current Ver','Android Ver'], axis=1)
google = google.drop_duplicates(subset=['App'], keep='first')

#Type Count plot
plt.figure(figsize=(5,3))
fig = sns.countplot(x=google['Type'])
fig.set_xticklabels(fig.get_xticklabels(),rotation=90)
#plt.show(fig)

#Plot Content Ratings
plt.figure(figsize=(6,3))
cont = sns.countplot(x=google['Content Rating'])
cont.set_xticklabels(cont.get_xticklabels(),rotation=90)
#plt.show(cont)

#Plot Category
plt.figure(figsize=(20,5))
cat = sns.countplot(x=google['Category'])
cat.set_xticklabels(cat.get_xticklabels(), rotation=90)
#plt.show(cat)

#Plot Ratings
plt.figure(figsize=(6,3))
review = sns.countplot(x=google['Rating'])
review.set_xticklabels(review.get_xticklabels())
#plt.show(review)

#Plot Genres
plt.figure(figsize=(10,3))
genre = sns.countplot(x=google['Genres'])
genre.set_xticklabels(genre.get_xticklabels(), rotation=90)
#plt.show()


#Find the top 10 Genres
x = google['Genres'].value_counts().reset_index()[:10]['index']
y = google['Genres'].value_counts().reset_index()[:10]['Genres']
plt.figure(figsize=(10,3))
top_genre = sns.barplot(y=google['Genres'].value_counts().reset_index()[:10]['Genres'], x=google['Genres'].value_counts().reset_index()[:10]['index'])
top_genre.set_xticklabels(top_genre.get_xticklabels(), rotation=90)
#plt.show()

#Top 10 APPS
sorted_val = google.sort_values(by=['Reviews'], ascending=False)

plt.figure(figsize=(6,4))
ratings = sns.barplot(y=sorted_val['Reviews'][:10], x=sorted_val['App'][:10])
ratings.set_xticklabels(ratings.get_xticklabels(), rotation=90)
#plt.show()

#Installs Plot
plt.figure(figsize=(20,5))
install = sns.countplot(x=google['Installs'])
install.set_xticklabels(install.get_xticklabels(),rotation=90)
plt.show()


google = google.drop(google.index[10472])
google = google.drop(google.index[7314])    #Get rid of the Unrated
google = google.drop(google.index[8268])
google = google[pd.notnull(google['Content Rating'])]

google['Size'] = google['Size'].str.replace('M', "00000")
google['Size'] = google['Size'].str.replace('K','000')
google['Size'] = google['Size'].replace('Varies with device',0)


google['Installs'] = google['Installs'].apply(lambda x: x.strip('+').replace(',',''))
google['Price'] = google['Price'].map(lambda x: x.strip('$'))
google['Price'] = google.to_numeric(google['Price'], errors='coerce')



label = LabelEncoder()

#All the encoding of string values

google['App'] = label.fit_transform(google['App'])
google['Rating'] = google['Rating'].fillna(google['Rating'].median())
google['Genres'] = label.fit_transform(google['Genres'])
google['Type'] = pd.get_dummies(google['Type'])
google['Content Rating'] = label.fit_transform(google['Content Rating'])

