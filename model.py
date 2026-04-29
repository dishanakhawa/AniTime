import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("anime.csv")

# Combine text features (adjust column names if needed)
df["combined"] = df["Name"] + " " + df["Genres"].fillna("")

# Convert text → vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined"])

# Similarity matrix
similarity = cosine_similarity(tfidf_matrix)

def search_anime(query):
    idx = df[df["Name"].str.lower() == query.lower()].index

    if len(idx) == 0:
        return ["Anime not found"]

    idx = idx[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    return [df.iloc[i[0]]["Name"] for i in scores]
