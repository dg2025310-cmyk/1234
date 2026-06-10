import streamlit as st
import matplotlib.pyplot as plt

st.title("전자공학·반도체 선호도 분석")

# 닉네임
name = st.text_input("닉네임 입력")

if name:
    st.subheader(f"{name}님의 설문")

    age10 = st.slider("10대", 0, 100, 60)
    age20 = st.slider("20대", 0, 100, 80)
    age30 = st.slider("30대", 0, 100, 70)
    age40 = st.slider("40대", 0, 100, 60)
    age50 = st.slider("50대+", 0, 100, 50)

    values = [age10, age20, age30, age40, age50]
    labels = ["10대", "20대", "30대", "40대", "50대+"]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylim(0, 100)
    ax.set_title("반도체 선호도")

    st.pyplot(fig)
