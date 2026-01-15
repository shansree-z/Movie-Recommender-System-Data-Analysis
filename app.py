import streamlit as st
import pickle
import pandas as pd

# Load the data
movies = pd.DataFrame(pickle.load(open('movie_dict.pkl', 'rb')))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Colorful Page Styling
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { background-color: #ff4b4b; color: white; width: 100%; border-radius: 8px; font-weight: bold; }
    .stSelectbox div[data-baseweb="select"] { color: black; }
    </style>
    """, unsafe_allow_html=True)

st.title('📽️Shan~ Movie Recommender')

# Autocomplete Search Box
selected_movie = st.selectbox('Type to search for a movie:', movies['title'].values)

if st.button('Recommend'):
    idx = movies[movies['title'] == selected_movie].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
    st.subheader(f"Recommended for {selected_movie}:")
    # Display top 5 movies in colorful boxes
    for i in distances[1:6]:
        st.info(movies.iloc[i[0]].title)
