import streamlit as st

st.title('Counter')
st.button("오늘 장사 끝! 손님 수 초기화할게요~")

customer_count = 0

if "customer_count" not in st.session_state:
    st.session_state.custmer_count = 0

print(st.state_count)

if st.button('손님 한명 추가요'):
    st.session_state.custmer_count += 1


if st.button('오늘 장사 끝! 손님 수 초기화 할게요~'):
    st.session_state.custmer_count = 0


st.write(f'지금까지 온 손님수 : {st.session_state.custmer_count}')

