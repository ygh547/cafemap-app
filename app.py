import streamlit as st
from tkinter import Menu
from PIL import Image
from app_eda import run_eda

from app_home import run_home



def main():

    st.title('카페 위치를 알려주는 앱입니다.')
    menu = ['Home', 'EDA',]
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    img = Image.open('data/coffee.jpg')

    st.sidebar.image(img,use_column_width=True)
    

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
        
if __name__ == '__main__' :
    main()