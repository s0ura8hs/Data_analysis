import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#data loading
df = pd.read_csv("zomato.csv")
#removing duplicates
df.drop_duplicates(inplace=True)

df['name'] = df['name'].str.replace('[^A-Za-z0-9 ]', '', regex=True)

#NLP

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# ML
from sklearn.feature_extraction.text import TfidfVectorizer


import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# TEXT PREPROCESSING FUNCTION
def preprocess_text(text):
    if pd.isna(text):
        return ""
    
    text = text.lower()
    
    # Tokenization
    words = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w.isalnum() and w not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words]
    
    return " ".join(words)


#APPLY TEXT CLEANING 

df['dish_liked'] = df['dish_liked'].fillna('not available')

df['cleaned_text'] = df['dish_liked'].apply(preprocess_text)

df['cuisines'] = df['cuisines'].fillna('unknown')
df['cuisines'] = df['cuisines'].str.lower().str.strip()
df['cuisines'] = df['cuisines'].apply(preprocess_text)

# TF-IDF 
tfidf = TfidfVectorizer(max_features=1000)
X_text = tfidf.fit_transform(df['cleaned_text'])

df['online_order'] = df['online_order'].astype(str).str.strip().str.lower()
df['online_order'] = df['online_order'].map({'yes': 1, 'no': 0})
df['online_order'] = df['online_order'].fillna(df['online_order'].mode()[0])


df['book_table'] = df['book_table'].astype(str).str.strip().str.lower()
df['book_table'] = df['book_table'].map({'yes': 1, 'no': 0})
df['book_table'] = df['book_table'].fillna(df['book_table'].mode()[0])

#rate column cleaning
def clean_rate(x):
    if isinstance(x, str):
        x = x.strip()
        if x == 'NEW' or x == '-':
            return np.nan
        else:
            return float(x.split('/')[0])
    return np.nan

df['rate'] = df['rate'].apply(clean_rate)


df['votes'] = df['votes'].astype(str).str.extract(r'(\d+)')
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')


df = df.drop(['phone','listed_in(city)','menu_item','url'], axis=1, errors='ignore')

df['location'] = df['location'].astype(str)  

# Keep short values (likely real locations)
df = df[df['location'].str.split().str.len() <= 2]

# Remove sentences and special characters
df = df[df['location'].str.contains(r'^[A-Za-z ]+$', na=False)]

# Clean text
df['location'] = df['location'].str.lower().str.strip()

df['location'] = df['location'].astype(str)



df['rest_type'] = df['rest_type'].astype(str)
df['rest_type'] = df['rest_type'].str.split(',').str[0]
df['rest_type'] = df['rest_type'].str.lower().str.strip()

df['rest_type'] = df['rest_type'].fillna(df['rest_type'].mode()[0])


df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str).str.extract(r'(\d+)')
df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')
  
  
Q1 = df['approx_cost(for two people)'].quantile(0.25)
Q3 = df['approx_cost(for two people)'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].clip(lower, upper)

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(
    lambda x: np.nan if x < 50 else x
)

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].fillna(
    df['approx_cost(for two people)'].median()
)

from sklearn.impute import KNNImputer

# Select numeric columns
num_cols = ['rate', 'votes', 'approx_cost(for two people)']

# Apply KNN Imputer
imputer = KNNImputer(n_neighbors=5)

df[num_cols] = imputer.fit_transform(df[num_cols])



df['reviews_list'] = df['reviews_list'].astype(str)
df['reviews_list'] = df['reviews_list'].str.replace(r'Rated \d\.\d', '', regex=True)
df['reviews_list'] = df['reviews_list'].str.replace(r'[^A-Za-z ]', ' ', regex=True)
df['reviews_list'] = df['reviews_list'].str.lower()
df['reviews_list'] = df['reviews_list'].str.replace(r'\s+', ' ', regex=True).str.strip()
df['reviews_list'] = df['reviews_list'].str.replace('rated n', '', regex=False)
df['reviews_list'] = df['reviews_list'].str.replace(r'\s+', ' ', regex=True).str.strip()

# Global average rating
C = df['rate'].mean()

# Minimum votes required (you can adjust)
m = df['votes'].quantile(0.75)


# Weighted score function
def weighted_rating(x, m=m, C=C):
    v = x['votes']
    R = x['rate']
    return (v/(v+m) * R) + (m/(v+m) * C)

# Apply score
df['score'] = df.apply(weighted_rating, axis=1)

print(df.select_dtypes(include="number").columns)

"""# **Exploratory Data Analysis**"""

"""# **Exploratory Data Analysis**"""

df.describe().T

for i in df.select_dtypes(include="number").columns:
  sns.histplot(data=df, x=i)
  plt.show()

for i in df.select_dtypes(include="number").columns:
    sns.boxplot(data=df, x=i)
    plt.show()

# scatterplot to understand relationship

for i in ['online_order', 'book_table', 'rate', 'votes', 'approx_cost(for two people)']:
       sns.scatterplot(data=df, x=i, y= 'score')
       plt.show()

for i in ['online_order', 'book_table', 'rate', 'votes']:
       sns.scatterplot(data=df, x=i, y=  'approx_cost(for two people)')
       plt.show()

for i in ['online_order', 'book_table', 'rate']:
       sns.scatterplot(data=df, x=i, y= 'votes')
       plt.show()

for i in ['online_order', 'book_table']:
       sns.scatterplot(data=df, x=i, y= 'rate')
       plt.show()


# correlation with heatmap
df.select_dtypes(include="number").corr()

s= df.select_dtypes(include="number").corr()
sns.heatmap(s,annot= True)
plt.show()
