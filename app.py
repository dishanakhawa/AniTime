import streamlit as st
from model import search_anime

# Page settings
st.set_page_config(
    page_title="AniTime",
    page_icon="⛩️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS styling
st.markdown("""
<style>
.stApp {
    background-color: #0b0b0b;
    color: white;
}

.main .block-container {
    padding-top: 2rem;
    max-width: 1000px;
}

.title {
    text-align: center;
    font-size: 4rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 0.3rem;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #b3b3b3;
    margin-bottom: 2rem;
}

.stTextInput input {
    background-color: #1a1a1a !important;
    color: white !important;
    border: 1px solid #333 !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

.stButton button {
    width: 100%;
    background-color: #e50914;
    color: white;
    border-radius: 12px;
    padding: 12px;
    font-weight: bold;
    border: none;
}

.card {
    background: #141414;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    border: 1px solid #222;
}

.rating {
    color: #ffd700;
    font-weight: bold;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">⛩️ AniTime ⛩️</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI anime recommendations based on your mood 🍜</div>', unsafe_allow_html=True)

# Input
query = st.text_input("", placeholder="Try: Naruto, romance, action fantasy...")

# Button (centered)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    clicked = st.button("✨ Get Recommendations", use_container_width=True)

# Logic
if clicked:
    if query.strip():
        results = search_anime(query)

        if results.empty:
            st.warning("No anime found. Try another name.")
        else:
            st.markdown("## 🌟 Top Picks For You")

            for row in results.itertuples():
                name = row.name if row.name else "N/A"
                genre = row.genre if row.genre else "N/A"
                typ = row.type if row.type else "N/A"
                rating = row.rating if row.rating else "N/A"

                st.markdown(f"""
                <div class="card">
                    <h2>🎥 {name}</h2>
                    <p><b>🎭 Genre:</b> {genre}</p>
                    <p><b>📺 Type:</b> {typ}</p>
                    <p class="rating">⭐ Rating: {rating}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("Please enter something")