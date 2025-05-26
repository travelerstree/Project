# app.py
import streamlit as st

st.title("🧮 제곱 계산기")

# 숫자 입력 받기
number = st.number_input("숫자를 입력하세요", value=1)

# 제곱 계산
square = number**2

# 결과 출력
st.write(f"{number}의 제곱은 {square}입니다.")
