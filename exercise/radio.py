import streamlit as st

# 라디오 버튼 생성
choice = st.radio("선호하는 색상을 선택하세요:", ["빨강", "파랑", "초록"])

st.write(f"선택된 색상: {choice}")
