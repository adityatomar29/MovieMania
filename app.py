import streamlit as st
import pickle
import pandas as pd 

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title("Welcome To Movie Recommender System")
st.image('https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D')

selected_movie_name = st.selectbox(
    'Select your previous watched movie...',
    (movies['title'].values)
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        movie_id = i[0]
        # Fetching Poster 

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


similarity = pickle.load(open('similarity.pkl', 'rb'))


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write("Here are top 5 movies related to your previously watched movie: ")
    for i in recommendations:
        st.write(i)