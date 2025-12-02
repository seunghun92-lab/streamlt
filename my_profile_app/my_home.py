import streamlit as st
import base64
import os

st.set_page_config(page_title="자기소개", page_icon="🐰")

# 폰트 적용
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap" rel="stylesheet">
<style>
body, h1, h2, h3, p, div {
    font-family: 'Nanum Gothic', sans-serif;
    color: #FFF700;  /* 레몬옐로우 글자 */
}
</style>
""", unsafe_allow_html=True)

# 배경 이미지
def set_bg(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: #FFF700;
        }}
        </style>
        """, unsafe_allow_html=True)

set_bg(r"C:\Users\신승훈\Desktop\IMG_4015.JPG")

# 내용
st.markdown("<h1>나를 소개합니다</h1>", unsafe_allow_html=True)
st.markdown("<h3>Streamlit으로 만드는 나의 프로필페이지</h3>", unsafe_allow_html=True)

st.markdown("""
<p>
<strong>이름:</strong> 신승훈  <br>
<strong>직업:</strong> AI 개발자 지망생  <br>
<strong>관심 분야:</strong> 파이썬  <br>
<strong>취미:</strong> 영어회화, 음악감상
</p>
""", unsafe_allow_html=True)
