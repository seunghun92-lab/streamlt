import streamlit as st

st.set_page_config(page_title="기술 & 루틴", page_icon="💻")

st.markdown("<h2>💻 기술 스택</h2>", unsafe_allow_html=True)
st.markdown("""
<div style="
    padding:15px;
    border-radius:15px;
    background-color:#1E90FFAA;
    border:1px solid #00BFFF;
    color:#FFF700;">
- Python 🐍  
- Machine Learning 🤖  
- Streamlit 📊
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("<h2>🎧 좋아하는 음악</h2>", unsafe_allow_html=True)
st.markdown("""
<div style="
    padding:15px; 
    border-radius:15px; 
    background-color:#1E90FFAA;
    border:1px solid #00BFFF;
    color:#FFF700;">
- 🎵 lofi 음악    
- 🎤 인디 음악  
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("<h2>🕒 하루 루틴</h2>", unsafe_allow_html=True)
with st.expander("루틴 보기"):
    st.markdown("""
<div style="color:#FFF700;">
- ☀ 아침: 수업  
- 🌤 점심: 수업  
- 🌙 밤: 수업 복습  
</div>
""", unsafe_allow_html=True)
