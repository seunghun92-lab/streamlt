import streamlit as st

st.title('사용자 입력 받는 페이지')

col1, _, col2 = st.columns(3)

with col1:
    nickname = st.text_input("닉네임 입력")

    age = st.number_input('나이 입력', min_value=13, max_value=100)

    n_option = ['한국', '중국', '미국', '외계']
    national = st.selectbox('국적', n_option)

    hobby = st.radio('취미', ['맛집 탐방', '영화 감상', '음악 감상', '뜨개질'])

    private_check = st.checkbox('개인정보 제공 동의')


with col2:
    if st.button('입력 완료'):
        st.write(f'이름이 뭐야? {nickname}')
        st.write(f'몇살 이야? {age}')
        st.write(f'어디서 왔어? {national}')
        st.write(f'취미가 뭐야? {hobby}')
        st.write(f'개인정보 동의해? {private_check}')