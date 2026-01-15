import streamlit as st
import pickle
import pandas as pd

# 1. Page Configuration and Hiding the Fork/Toolbar
st.set_page_config(page_title="Shan~Movie Recommender", page_icon="🎬", layout="centered")

hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp [data-testid="stToolbar"] {display:none;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

# 2. Title
st.title('Shan~Movie Recommender')

# 3. Load the data 
# Make sure these filenames match exactly what you uploaded to GitHub
movies = pd.DataFrame(pickle.load(open('movie_dict.pkl','rb')))
similarity_tiny = pickle.load(open('similarity_tiny.pkl','rb'))

# 4. Search UI
selected_movie = st.selectbox('Type or select a movie:', movies['title'].values)

if st.button('Recommend'):
    # Get the index of the selected movie
    idx = movies[movies['title'] == selected_movie].index[0]
    
    # Get pre-saved recommendations from your tiny file
    recommendations = similarity_tiny[idx]
    
    st.subheader("Recommended for you:")
    for i in recommendations:
        # i[0] is the index of the recommended movie
        st.info(movies.iloc[i[0]].title)
        
