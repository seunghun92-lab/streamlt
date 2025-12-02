import streamlit as st

# 멀티 셀렉트 박스 생성
selected = st.multiselect("구매할 품목을 선택하세요:", ["사과", "바나나", "딸기"])

st.write(f"선택된 품목: {selected}")