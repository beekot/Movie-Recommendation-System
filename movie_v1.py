import pickle
import streamlit as st

hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
# Import Pandas
import pandas as pd
# Load Movies Metadata
metadata = pd.read_csv("movie data_new2.csv", low_memory=False)
metadata.rename(columns={'Unnamed: 0': 'movie_id'}, inplace=True)
metadata.rename(columns={'Movie Name': 'Title'}, inplace=True)
metadata.rename(columns={'Year of Release':'year'}, inplace=True)
metadata.rename(columns={'Movie Rating':'Rating'}, inplace=True)



top10 = metadata.sort_values('Rating', ascending=False)
top10=top10[['Title','Rating']].head(10)


st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
if st.sidebar.button('Top 10 Movies '):
     st.sidebar.table(top10.style.format({"Rating": "{:.2f}"}))




top10R = metadata[(metadata.year) == 2022 ]
top10R=top10R[['Title','Rating']].head(10)

st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
if st.sidebar.button('Recent Releases '):
     st.sidebar.table(top10R.style.format({"Rating": "{:.2f}"}))




metadata.rename(columns={'Year of Release':'year'}, inplace=True)
top10New = metadata[(metadata.year) == 2023 ]
top10New=top10New[['Title','year']].head(10)
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
if st.sidebar.button('Future Releases '):
     st.sidebar.table(top10New.style.format({"year": "{:.0f}"}))



def recommend(movie,type):
    if type==1:
        index = movies[movies['Title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True,key=lambda x: x[1])
        recommended_movie_names = []
        for i in distances[1:6]:
            recommended_movie_names.append(movies.iloc[i[0]].Title)

        return recommended_movie_names

page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://images.unsplash.com/photo-1542204165-65bf26472b9b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80");
  background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown('# Movie Recommendation System ' )
movies = pickle.load(open('movie_list_new.pkl','rb'))
similarity = pickle.load(open('similarity_new.pkl','rb'))
movie_list = movies['Title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,key="1"
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie,1)
    for i in recommended_movie_names:
        st.subheader(i)

#################

def recommendg(movie,type):
    if type==2:
        index = movies[movies['Title'] == movie].index[0]
        distances = sorted(list(enumerate(similarityg[index])), reverse=True,key=lambda y: y[1])
        recommended_movie_namesg = []
        for i in distances[1:6]:
            recommended_movie_namesg.append(movies.iloc[i[0]].Title)

        return recommended_movie_namesg

st.markdown('# Movie Recommendation System By Genre')
moviesg = pickle.load(open('movie_listgenre_new.pkl','rb'))
similarityg = pickle.load(open('similaritygenre_new.pkl','rb'))


movie_listg = moviesg['Title'].values
selected_movieg = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_listg,key="2")

if st.button('Show Recommendation by genre'):
    recommended_movie_namesg = recommendg(selected_movieg,2)
    for i in recommended_movie_namesg:
        st.subheader(i)
