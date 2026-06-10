import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="전공 선호도 비교", layout="centered")

st.title("📊 전자공학 vs 반도체학과 선호도 비교")

st.write("연령대별 선호도를 입력하면 두 전공을 비교합니다.")

labels = ["10대", "20대", "30대", "40대", "50대+"]

# =========================
# 전자공학 입력
# =========================
st.subheader("📘 전자공학과 선호도")

ee_values = [
    st.slider("10대 (전자공학)", 0, 100, 60),
    st.slider("20대 (전자공학)", 0, 100, 80),
    st.slider("30대 (전자공학)", 0, 100, 70),
    st.slider("40대 (전자공학)", 0, 100, 60),
    st.slider("50대+ (전자공학)", 0, 100, 50),
]

# =========================
# 반도체 입력
# =========================
st.subheader("📙 반도체학과 선호도")

si_values = [
    st.slider("10대 (반도체)", 0, 100, 70),
    st.slider("20대 (반도체)", 0, 100, 90),
    st.slider("30대 (반도체)", 0, 100, 85),
    st.slider("40대 (반도체)", 0, 100, 75),
    st.slider("50대+ (반도체)", 0, 100, 60),
]

# =========================
# 비교 그래프
# =========================
st.subheader("⚖️ 비교 결과")

fig, ax = plt.subplots()

x = range(len(labels))
width = 0.35

ax.bar([i - width/2 for i in x], ee_values, width=width, label="전자공학", color="blue")
ax.bar([i + width/2 for i in x], si_values, width=width, label="반도체", color="red")

ax.set_xticks(list(x))
ax.set_xticklabels(labels)
ax.set_ylim(0, 100)
ax.legend()
ax.set_title("연령대별 전공 선호도 비교")

st.pyplot(fig)
