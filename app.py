import streamlit as st
import pandas as pd
import pickle


def recommend(songs):
    songs_index = df_songs[df_songs['track_name'] == songs].index[0]
    distances = similarity[songs_index]
    songs_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


    recommend_songs =[]
    for i in songs_list:
        recommend_songs.append(df_songs.iloc[i[0]].track_name)
    return recommend_songs
songs_dict = pickle.load(open('songs_dict.pkl','rb'))
df_songs = pd.DataFrame(songs_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Top 5 Songs')


selected_songs_name = st.selectbox(
'Songs that you like',
df_songs['track_name'].values)

if st.button('SEARCH'):
    recommendations = recommend(selected_songs_name)
    for i in recommendations:
        st.write(i)




