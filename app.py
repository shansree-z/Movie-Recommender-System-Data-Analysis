import streamlit as st
import pickle
import pandas as pd

# This hides the 'Fork' button and the Streamlit menu for a cleaner look
st.set_page_config(page_title="Shan~Movie Recommender", page_icon="🎬", layout="centered")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title('Shan~Movie Recommender')

# Load the data - using the tiny file you already uploaded
movies = pd.DataFrame(pickle.load(open('movie_dict.pkl','rb')))
similarity_tiny = pickle.load(open('similarity_tiny.pkl','rb'))

selected_movie = st.selectbox('Type or select a movie:', movies['title'].values)

if st.button('Recommend'):
    idx = movies[movies['title'] == selected_movie].index[0]
    recommendations = similarity_tiny[idx]
    
    st.subheader("Recommended for you:")
    for i in recommendations:
        st.info(movies.iloc[i[0]].title)
        
