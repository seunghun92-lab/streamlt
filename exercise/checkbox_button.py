import streamlit as st

# 체크박스 생성
agree = st.checkbox("동의합니다")

if agree:
    st.write("동의해주셔서 감사합니다!")