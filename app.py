import streamlit as st
import pandas as pd
import joblib

# Load dataset
movies = pd.read_csv("movies.csv")

# Load saved model
cosine_sim = joblib.load("similarity_model.pkl")
indices = joblib.load("movie_indices.pkl")

def recommend_movies(title):

    idx = indices[title]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:6]
    
    movie_indices = [i[0] for i in sim_scores]

    result = movies.iloc[movie_indices][['title']]
    
    result['Similarity Score'] = [i[1] for i in sim_scores]

    return result


st.title("Movie Recommendation System")

movie_name = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    try:
        result = recommend_movies(movie_name)
        st.write(result)
    except:
        st.write("Movie not found in dataset")