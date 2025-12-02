import streamlit as st
import pandas as pd
import numpy as np

# 가상 데이터 생성: 2025년 1월부터 12월까지 월별 매출 데이터
months = pd.date_range(start="2025-01-01", periods=12, freq="M")
sales = np.random.randint(20000, 50000, size=12)

data = pd.DataFrame({
    '월': months.strftime("%Y-%m"),
    '매출': sales
})

# 차트를 사용해 매출 데이터 시각화
st.write("2025년 월별 매출 추이")
st.line_chart(data.set_index('월'))