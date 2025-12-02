import streamlit as st

# 토글 스위치 생성
activated = st.toggle("기능 활성화")

if activated:
    st.write("기능이 활성화되었습니다.")
else:
    st.write("기능이 비활성화되었습니다.")