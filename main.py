import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="전공 선호도 비교", layout="centered")

st.title("📊 전자공학 vs 반도체학과 선호도 비교")

st.write("기본 설정된 평균 선호도 데이터를 기반으로 비교합니다.")

# =========================
# 기본 데이터 (고정값)
# =========================
labels = ["전자공학", "반도체학과"]
values = [72, 85]  # ← 여기 숫자만 바꾸면 그래프 변경됨

# =========================
# 그래프
# =========================
fig, ax = plt.subplots()

ax.bar(labels, values, color=["blue", "red"])
ax.set_ylim(0, 100)
ax.set_title("전공 선호도 비교")

st.pyplot(fig)

# =========================
# 해석
# =========================
if values[0] > values[1]:
    st.success("👉 전자공학 선호도가 더 높습니다.")
elif values[1] > values[0]:
    st.success("👉 반도체학과 선호도가 더 높습니다.")
else:
    st.info("👉 두 전공 선호도가 같습니다.")
