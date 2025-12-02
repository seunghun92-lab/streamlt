import streamlit as st

st.title('사용자 입력 받는 페이지')

col1, _, col2 = st.columns(3)
# stream에서 영역 안에 UI 요소를 배치하는 레이어드
with col1:
    nickname = st.text_input('닉네임 입력')

    age = st.number_input('나이 입력', min_value = 13, max_value = 100)

    national_option = ['한국', '중국', '일본', '미국', '외계']
    national = st.selectbox('국적', national_option)

    hobby = st.radio('취미' , ['맛집 탐방', '영화 감상', '음악 감상', '뜨개질'])

    private_check = st.checkbox('개인정보 제공 동의')


with col2:
    pass
    if st.button('입력완료'):
        st.write(f'이름이 뭐야? {nickname}')
        st.write(f'몇 살이야? {age}')
        st.write(f'어디서 뭐야? {national}')
        st.write(f'취미가 뭐야? {hobby}')
        st.write(f'개인정보 제공? {private_check}')