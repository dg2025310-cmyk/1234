import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="전공 선호도 비교", layout="centered")

st.title("📊 전자공학 vs 반도체학과 선호도 비교")

st.write("두 전공의 선호도를 비교합니다 (전체 평균 기준)")

# =========================
# 전자공학
# =========================
st.subheader("📘 전자공학과 선호도")

ee_value = st.slider("전자공학 선호도", 0, 100, 70)

# =========================
# 반도체
# =========================
st.subheader("📙 반도체학과 선호도")

si_value = st.slider("반도체학과 선호도", 0, 100, 80)

# =========================
# 비교 그래프
# =========================
st.subheader("⚖️ 비교 결과")

labels = ["전자공학", "반도체학과"]
values = [ee_value, si_value]

fig, ax = plt.subplots()
ax.bar(labels, values, color=["blue", "red"])
ax.set_ylim(0, 100)
ax.set_title("전공 선호도 비교")

st.pyplot(fig)

# =========================
# 결과 해석
# =========================
if ee_value > si_value:
    st.success("👉 전자공학 선호도가 더 높습니다.")
elif si_value > ee_value:
    st.success("👉 반도체학과 선호도가 더 높습니다.")
else:
    st.info("👉 두 전공 선호도가 같습니다.")
