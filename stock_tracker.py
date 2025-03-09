import yfinance as yf
import matplotlib.pyplot as plt

def get_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data["Close"].iloc[-1]

def plot_history(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1mo")
    plt.plot(data.index, data["Close"], label=symbol)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{symbol} - Last Month")
    plt.legend()
    plt.show()

while True:
    s = input("\nEnter stock symbol (or 'exit' to quit): ").upper()
    if s == "EXIT":
        break
    try:
        print(f"{s} price: ${get_price(s):.2f}")
        plot_history(s)
    except:
        print("Invalid stock symbol.")
