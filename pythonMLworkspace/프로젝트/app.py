import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

movies_path = os.path.join(script_dir, 'movies.pickle')
cosine_sim_path = os.path.join(script_dir, 'cosine_sim.pickle')

movie = Movie()
tmdb = TMDb()

tmdb.api_key = 'e6b42b7fa12cd2f85571480f688fa48b'


def get_recommendations(title):
    
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값 얻기
    idx = movies[movies['title']==title].index[0]
    # 코사인 유사도 매트릭스 에서 인덱스에 해당하는 데이터를 (idx,유사도)형태로 얻기
    cosine_sim[idx]
    # 코사인 유사도 기준으로 내림차순 정렬
 
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    
    
    # 추천 영화 목록 10개의 인덱스 정보 추출
  
    
    # 인덱스 정보를 통해 영화 제목 추출 
  
    


movies = pickle.load(open(movies_path, 'rb'))
cosine_sim = pickle.load(open(cosine_sim_path, 'rb'))

st.set_page_config(layout='wide')
st.header('JongGuflix')

movie_list = movies['title'].values

title = st.selectbox('Choose a movie you like', movie_list)

if st.button('Recommend'):
    images, titles = get_recommendations(title)
