# ai_semiconductor_analysis.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 분석 대상 기업
companies = {
    "NVIDIA": "NVDA",
    "AMD": "AMD",
    "TSMC": "TSM",
    "Intel": "INTC"
}

# 최근 3년 주가 데이터
end_date = datetime.today()
start_date = end_date - timedelta(days=365 * 3)

price_data = pd.DataFrame()

for name, ticker in companies.items():
    stock = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False
    )

    price_data[name] = stock["Close"]

# 수익률 계산
returns = (price_data / price_data.iloc[0] - 1) * 100

plt.figure(figsize=(12, 6))
for company in returns.columns:
    plt.plot(
        returns.index,
        returns[company],
        label=company
    )

plt.title("AI Semiconductor Companies Stock Performance")
plt.ylabel("Return (%)")
plt.xlabel("Date")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 기업 가치 지표 수집
valuation_data = []

for name, ticker in companies.items():
    info = yf.Ticker(ticker).info

    valuation_data.append({
        "Company": name,
        "Market Cap ($B)": round(
            info.get("marketCap", 0) / 1e9, 2
        ),
        "Forward PE": info.get("forwardPE"),
        "Price/Sales": info.get("priceToSalesTrailing12Months"),
        "Revenue Growth": info.get("revenueGrowth")
    })

valuation_df = pd.DataFrame(valuation_data)

print("\n=== Valuation Metrics ===")
print(valuation_df)

# 성장성 점수 계산
valuation_df["Growth Score"] = (
    valuation_df["Revenue Growth"].fillna(0) * 100
)

valuation_df = valuation_df.sort_values(
    by="Growth Score",
    ascending=False
)

print("\n=== Growth Ranking ===")
print(
    valuation_df[
        ["Company", "Growth Score"]
    ]
)

# 시각화
plt.figure(figsize=(10, 5))
plt.bar(
    valuation_df["Company"],
    valuation_df["Growth Score"]
)

plt.title("Revenue Growth Comparison")
plt.ylabel("Growth Score")
plt.tight_layout()
plt.show()
