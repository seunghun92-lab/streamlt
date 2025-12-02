import streamlit as st
import pandas as pd
import numpy as np

# 가상 데이터 생성: 도시별 인구와 경제 성장률
cities = ['서울', '부산', '대구', '광주', '인천', '대전', '울산']
population = np.random.randint(100, 1000, size=len(cities))  # 인구 (단위: 만 명)
growth_rate = np.random.uniform(0, 10, size=len(cities))  # 경제 성장률 (단위: %)
income = np.random.randint(10000, 50000, size=len(cities))  # 1인당 평균 소득 (단위: 천 원)

# 데이터프레임 생성
data = pd.DataFrame({
    '도시': cities,
    '인구': population,
    '경제 성장률': growth_rate,
    '1인당 소득': income
})

# 도시별 인구와 경제 성장률을 산포도로 시각화
st.write("도시별 인구와 경제 성장률")
st.scatter_chart(data.rename(columns={'도시': 'index'}).set_index('index'))
