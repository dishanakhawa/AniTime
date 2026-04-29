import streamlit as st
from model import search_anime

# Page settings
st.set_page_config(
    page_title="AniTime",
    page_icon="⛩️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# FULL DARK THEME CSS
st.markdown("""
<style>
/* Whole app background */
.stApp {
    background-color: #0b0b0b;
    color: white;
}

/* Main block */
.main .block-container {
    padding-top: 2rem;
    max-width: 1000px;
}

/* Title */
.title {
    text-align: center;
    font-size: 4rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 0.3rem;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #b3b3b3;
    margin-bottom: 2rem;
}

/* Input box */
.stTextInput input {
    background-color: #1a1a1a !important;
    color: white !important;
    border: 1px solid #333 !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

/* Button */
.stButton button {
    width: 100%;
    background-color: #e50914;
    color: white;
    border-radius: 12px;
    padding: 12px;
    font-weight: bold;
    border: none;
}

/* Cards */
.card {
    background: #141414;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    border: 1px solid #222;
}

/* Rating */
.rating {
    color: #ffd700;
    font-weight: bold;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">⛩️ AniTime ⛩️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI anime recommendations based on your mood🍜</div>',
    unsafe_allow_html=True
)

# # Input
query = st.text_input(
    "",
    placeholder="Try: horror, romance, action fantasy..."
)

# Center button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    clicked = st.button("✨ Get Recommendations", use_container_width=True)

if clicked:
    if query:
        results = search_anime(query)

        st.markdown("## 🌟 Top Picks For You")

        for row in results.itertuples():
            st.markdown(f"""
            <div class="card">
                <h2>🎥 {row.name}</h2>
                <p><b>🎭 Genre:</b> {row.genre}</p>
                <p><b>📺 Type:</b> {row.type}</p>
                <p class="rating">⭐ Rating: {row.rating}</p>
            </div>
            """, unsafe_allow_html=True)
