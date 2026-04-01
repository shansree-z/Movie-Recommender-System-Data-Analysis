# 🎬 Shan~Movie Recommender   

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

A high-performance Content-Based Movie Recommendation System. This project transforms raw movie data into an interactive web experience, providing instant suggestions based on cinematic metadata.

---

## 🔗 Live Project
Access the deployed application here: 
👉 [**Shan~Movie Recommender Web App**](https://movie-recommender-system-data-analysis-msottamh57qqw8vppzihaq.streamlit.app/)

---

## 📖 Project Overview
This system analyzes the TMDB 5000 Movies dataset to find similarities between films. It uses **Natural Language Processing (NLP)** to process genres, cast, and keywords into searchable tags.


### Key Features
* **Custom Branding**: Fully personalized as "Shan~Movie Recommender".
* **Optimized Performance**: Uses a truncated similarity matrix (`similarity_tiny.pkl`) for fast mobile loading.
* **Clean Interface**: Custom CSS hides the Streamlit toolbar and GitHub "Fork" buttons for a standalone app feel.
* **Autocomplete Search**: Integrated dropdown for easy movie selection.

---

## 📂 Repository Contents
* `app.py`: The Streamlit frontend script with embedded custom styling.
* `movie_dict.pkl`: Serialized movie data dictionary.
* `similarity_tiny.pkl`: Optimized similarity scores (Top 10 matches per movie).
* `requirements.txt`: Necessary libraries: `streamlit`, `pandas`, `scikit-learn`.
* `movie_recommendations_system.ipynb`: The original development notebook from Google Colab.

---

## 🛠️ Installation & Local Usage
1. **Clone the repo:** `git clone https://github.com/shansree-z/Movie-Recommender-System-Data-Analysis.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the app:** `streamlit run app.py`

---

## 🧬 Algorithm Logic
* **Data Preprocessing**: Merging movie metadata (genres, keywords, overview, cast, and crew) into a single "tags" column.
* **Text Vectorization**: Converting movie tags into 5000-dimensional vectors using `CountVectorizer` (Bag of Words).
* **Similarity Calculation**: Applying **Cosine Similarity** to measure the angular distance between movie vectors.
* **Truncation Optimization**: Keeping only the Top 10 highest-scoring matches per movie to ensure the final data remains under the 25MB GitHub limit.

---

## 👤 Author
Shansree K 
*Data Analysis & Machine Learning Enthusiast*
