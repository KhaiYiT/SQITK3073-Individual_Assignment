import yfinance as yf
import matplotlib.pyplot as plt

stocks = {
    "Maybank": "1155.KL",
    "Tenaga": "5347.KL",
    "TM": "4863.KL",
    "Nestle": "4707.KL",
    "IJM": "3336.KL"
}

plt.figure(figsize=(12,6))

start_date = "2026-04-01"
end_date = "2026-05-01"

for company, ticker in stocks.items():
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    plt.plot(data.index, data["Close"], label=company)

plt.title("Bursa Malaysia Stocks - April 2026 Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price (RM)")
plt.legend()
plt.grid()

plt.show()
