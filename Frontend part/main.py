import pandas as pd
import streamlit as st
import pickle
import requests
def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8b5bf56d501238047b5bbb1c3ce36e11&language=en-US'.format(movie_id))
    data=response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = simiarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_posters.append(poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_posters,recommended_movies
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
simiarity=pickle.load(open('simiarity.pkl','rb'))
st.title('Movie Recommender system')
st.header('List of Movies', divider='rainbow')

option = st.selectbox(
 'Please select the Movie',
 movies['title'].values)
if st.button('Recommend'):
    names, posters = recommend(option)
    col1, col2, col3 ,col4,col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
