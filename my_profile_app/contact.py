import streamlit as st
import base64
import os

# --- 페이지 설정 ---
st.set_page_config(page_title= "자기소개", page_icon="🐰")

# --- 배경 이미지 적용 함수 ---
def set_bg_local(image_file):
    if not os.path.exists(image_file):
        st.warning(f"⚠ 이미지 파일을 찾을 수 없습니다: {image_file}")
        return
    with open(image_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Google Fonts + 글씨색 ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap" rel="stylesheet">
<style>
body, h1, h2, h3, h4, h5, h6, p, div {
    font-family: 'Nanum Gothic', sans-serif;
    color: #FFA500;  /* 글자 색: 주황색 */
}
</style>
""", unsafe_allow_html=True)

# --- 이미지 적용 ---
set_bg_local(r"C:\Users\신승훈\Desktop\IMG_8918.jpeg")

# --- 본문 내용 ---
st.markdown('<h1>나를 소개합니다</h1>', unsafe_allow_html=True)
st.markdown('<h3>Streamlit으로 만드는 나의 프로필페이지</h3>', unsafe_allow_html=True)

st.markdown("""
<p>
<strong>이름:</strong> 신승훈  <br>
<strong>직업:</strong> AI 개발자 지망생  <br>
<strong>관심 분야:</strong> 파이썬  <br>
<strong>취미:</strong> 영어회화, 음악감상
<strong>MBTI : ISFP
</p>
""", unsafe_allow_html=True)

st.divider()

# --- 기술 스택 ---
st.markdown("### 💻 기술 스택")
st.markdown("""
<div style="
    padding:15px;
    border-radius:15px;
    background-color:#FFF0F5CC;
    border:1px solid #FFC0CB;">
- Python 🐍  
- Machine Learning 🤖  
- Streamlit 📊
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 좋아하는 음악 ---
st.markdown("### 🎧 좋아하는 음악")
st.markdown("""
<div style="
    padding:15px; 
    border-radius:15px; 
    background-color:#FFF0F5CC;
    border:1px solid #FFC0CB;">
- ✨ 잔잔한 인디 음악  
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 좋아하는 아티스트 ---
st.markdown("### 🎶 좋아하는 아티스트")
st.markdown("""
<div style="
    padding:15px;
    border-radius:15px;
    background-color:#FFF0F5CC;
    border:1px solid #FFC0CB;">
- 🎸 **wave to earth**  
- 🌊 따뜻하고 감성적인 밴드 음악을 좋아해요!
</div>
""", unsafe_allow_html=True)

# --- YouTube 영상 embed (안정적 재생) ---
video_id = "SXdapBpFC9I"
st.markdown(f"""
<iframe width="560" height="315"
src="https://www.youtube.com/embed/{video_id}" 
title="YouTube video player" frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen>
</iframe>
""", unsafe_allow_html=True)

st.divider()

# --- 하루 루틴 ---
st.markdown("### 🕒 하루 루틴")
with st.expander("루틴 보기"):
    st.markdown("""
<div>
- ☀ 아침: 수업  
- 🌤 점심: 수업  
- 🌙 밤: 수업 복습  
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 가치관 ---
st.markdown("### 가치관")
st.markdown("""
<div style="
    padding:15px; 
    border-radius:15px; 
    background-color:#FFF8DC99;  
    border:1px solid #FFD700;">
- "꾸준함이 가장 큰 재능이다."    
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 연락 ---
st.markdown("### 💌 연락")
st.markdown("""
<p>
📧 이메일: seunghunsin92@gmail.com  <br>
📞 010-2307-5942
</p>
""", unsafe_allow_html=True)

# --- 인터랙티브 버튼 ---
if st.button("💌 인사하기"):
    st.success("안녕하세요! 만나서 반가워요 😊")
