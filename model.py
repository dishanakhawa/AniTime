# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Load dataset
# df = pd.read_csv("anime_cleaned.csv")

# # Fill missing values
# df["Name"] = df["Name"].fillna("")
# df["Genres"] = df["Genres"].fillna("")
# df["Type"] = df["Type"].fillna("")
# df["Rating"] = df["Rating"].fillna(0)

# # Combine text features
# df["combined"] = df["Name"] + " " + df["Genres"]

# # Convert text to vectors
# vectorizer = TfidfVectorizer(stop_words="english")
# tfidf_matrix = vectorizer.fit_transform(df["combined"])

# # Similarity matrix
# similarity = cosine_similarity(tfidf_matrix)

# def search_anime(query):
#     query = query.lower()

#     matches = df[df["Name"].str.lower().str.contains(query)]

#     if matches.empty:
#         return pd.DataFrame()

#     idx = matches.index[0]

#     scores = list(enumerate(similarity[idx]))
#     scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

#     recs = df.iloc[[i[0] for i in scores]]

#     return recs
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("anime_cleaned.csv")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Clean data
df["name"] = df["name"].fillna("")
df["genre"] = df["genre"].fillna("")
df["type"] = df["type"].fillna("")
df["rating"] = df["rating"].fillna(0)

# Combine features (ONLY THIS LINE)
df["combined"] = df["name"] + " " + df["genre"]

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined"])

# Similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# ✅ SEARCH FUNCTION (this is your function)
def search_anime(query):
    query = query.lower()

    # Find matching anime
    matches = df[df["name"].str.lower().str.contains(query)]

    if matches.empty:
        return pd.DataFrame()

    idx = matches.index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    recs = df.iloc[[i[0] for i in scores]]

    return recs