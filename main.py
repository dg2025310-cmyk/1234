import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("반도체 선호도 분석 앱")

        # =========================
        # 1. 닉네임 입력 (첫 창)
        # =========================
        self.nickname = simpledialog.askstring("닉네임", "닉네임을 입력하세요:")
        if not self.nickname:
            self.nickname = "사용자"

        # =========================
        # 2. UI 프레임
        # =========================
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        tk.Label(
            self.frame,
            text=f"{self.nickname}님의 반도체 선호도 설문",
            font=("Arial", 14, "bold")
        ).pack()

        # =========================
        # 3. 데이터 (연령대)
        # =========================
        self.values = {
            "10대": tk.IntVar(value=50),
            "20대": tk.IntVar(value=80),
            "30대": tk.IntVar(value=70),
            "40대": tk.IntVar(value=60),
            "50대+": tk.IntVar(value=40),
        }

        # =========================
        # 4. 슬라이더 UI
        # =========================
        for age, var in self.values.items():
            row = tk.Frame(root)
            row.pack()

            tk.Label(row, text=age, width=8).pack(side="left")

            tk.Scale(
                row,
                from_=0,
                to=100,
                orient="horizontal",
                variable=var,
                command=self.update_chart
            ).pack(side="left")

        # =========================
        # 5. 그래프 영역
        # =========================
        self.fig, self.ax = plt.subplots(figsize=(5, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(pady=10)

        # 버튼
        tk.Button(
            root,
            text="결과 보기",
            command=self.update_chart,
            bg="skyblue"
        ).pack(pady=5)

        self.draw_chart()

    # =========================
    # 그래프 그리기
    # =========================
    def draw_chart(self):
        self.ax.clear()

        labels = list(self.values.keys())
        data = [v.get() for v in self.values.values()]

        self.ax.bar(labels, data, color=["green", "blue", "orange", "purple", "red"])
        self.ax.set_ylim(0, 100)
        self.ax.set_title("전자공학·반도체 선호도")

        self.canvas.draw()

    # =========================
    # 업데이트
    # =========================
    def update_chart(self, event=None):
        self.draw_chart()


# =========================
# 실행
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
