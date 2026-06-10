import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="전공 선호도 비교", layout="centered")

st.title("📊 전자공학 vs 반도체학과 나이대별 선호도")

st.write("각 연령대별로 전자공학과와 반도체학과 선호도를 입력하세요.")

# =========================
# 닉네임
# =========================
name = st.text_input("닉네임 입력")

if name:
    st.subheader(f"👤 {name}님의 데이터")

    st.markdown("### 📘 전자공학과 선호도")

    ee_10 = st.slider("전자공학 - 10대", 0, 100, 60)
    ee_20 = st.slider("전자공학 - 20대", 0, 100, 80)
    ee_30 = st.slider("전자공학 - 30대", 0, 100, 70)
    ee_40 = st.slider("전자공학 - 40대", 0, 100, 60)
    ee_50 = st.slider("전자공학 - 50대+", 0, 100, 50)

    st.markdown("### 📙 반도체학과 선호도")

    si_10 = st.slider("반도체 - 10대", 0, 100, 70)
    si_20 = st.slider("반도체 - 20대", 0, 100, 90)
    si_30 = st.slider("반도체 - 30대", 0, 100, 85)
    si_40 = st.slider("반도체 - 40대", 0, 100, 75)
    si_50 = st.slider("반도체 - 50대+", 0, 100, 60)

    labels = ["10대", "20대", "30대", "40대", "50대+"]

    # =========================
    # 그래프 1 (전자공학)
    # =========================
    fig1, ax1 = plt.subplots()
    ax1.bar(labels, [ee_10, ee_20, ee_30, ee_40, ee_50], color="blue")
    ax1.set_title("전자공학과 선호도")
    ax1.set_ylim(0, 100)

    st.pyplot(fig1)

    # =========================
    # 그래프 2 (반도체)
    # =========================
    fig2, ax2 = plt.subplots()
    ax2.bar(labels, [si_10, si_20, si_30, si_40, si_50], color="red")
    ax2.set_title("반도체학과 선호도")
    ax2.set_ylim(0, 100)

    st.pyplot(fig2)

    # =========================
    # 비교 그래프
    # =========================
    st.markdown("### ⚖️ 비교 그래프")

    fig3, ax3 = plt.subplots()

    width = 0.35
    x = range(len(labels))

    ax3.bar([i - width/2 for i in x],
            [ee_10, ee_20, ee_30, ee_40, ee_50],
            width=width,
            label="전자공학",
            color="blue")

    ax3.bar([i + width/2 for i in x],
            [si_10, si_20, si_30, si_40, si_50],
            width=width,
            label="반도체",
            color="red")

    ax3.set_xticks(list(x))
    ax3.set_xticklabels(labels)
    ax3.set_ylim(0, 100)
    ax3.legend()

    st.pyplot(fig3)
