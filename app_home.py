from PIL import Image
import streamlit as st

def run_home():
    st.subheader('이 앱은 카페 위치에 대한 내용입니다.')
    st.text('왼쪽 사이드바에서 원하는 항목을 선택하세요.')
    

    img = Image.open('data/지도.jpg')

    st.image(img,use_column_width=True)