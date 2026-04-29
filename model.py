import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os

# File path
file_path = os.path.join(os.path.dirname(__file__), "anime_cleaned.csv")

# Load dataset
df = pd.read_csv(file_path)

# Remove missing values
df = df.dropna()

# Create description
df["description"] = (
    df["name"].astype(str) + " " +
    df["genre"].astype(str) + " " +
    df["type"].astype(str)
)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Save embeddings for faster reload
embedding_path = "anime_embeddings.npy"

if os.path.exists(embedding_path):
    embeddings = np.load(embedding_path)
else:
    embeddings = model.encode(df["description"].tolist())
    np.save(embedding_path, embeddings)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

def search_anime(query, top_n=5):
    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"), top_n
    )

    return df.iloc[indices[0]]

