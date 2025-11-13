# =============================================
# 📊 ADVANCED STOCK ANALYSIS & FORECAST (v3)
# Author: Khadija Rao
# =============================================

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import statsmodels.api as sm

# -------------------------------------------------
# 1️⃣  DOWNLOAD DATA
# -------------------------------------------------
ticker = "AAPL"  # You can change e.g. "TSLA" or "MSFT"
print(f"\n📥 Downloading {ticker} data for last 1 year...")
data = yf.download(ticker, period="1y", progress=False)

if data.empty:
    print("❌ Data download failed.")
    exit()

# Prepare Data
df = data.reset_index()[["Date", "Close"]].copy()
df.rename(columns={"Close": "y"}, inplace=True)
df["y"] = df["y"].astype(float).fillna(method="ffill").fillna(method="bfill")

# -------------------------------------------------
# 2️⃣  BASIC METRICS
# -------------------------------------------------
df["MA7"] = df["y"].rolling(7).mean()
df["MA30"] = df["y"].rolling(30).mean()
df["Returns"] = df["y"].pct_change() * 100
df["Volatility"] = df["Returns"].rolling(30).std()

# -------------------------------------------------
# 3️⃣  ADVANCED INDICATORS
# -------------------------------------------------
# Exponential Moving Averages
df["EMA12"] = df["y"].ewm(span=12, adjust=False).mean()
df["EMA26"] = df["y"].ewm(span=26, adjust=False).mean()

# MACD and Signal Line
df["MACD"] = df["EMA12"] - df["EMA26"]
df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

# RSI (Relative Strength Index)
delta = df["y"].diff()
gain = delta.clip(lower=0)
loss = -1 * delta.clip(upper=0)
avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()
rs = avg_gain / avg_loss
df["RSI"] = 100 - (100 / (1 + rs))

# Bollinger Bands
df["BB_Mid"] = df["y"].rolling(20).mean()
df["BB_Std"] = df["y"].rolling(20).std()
df["BB_Upper"] = df["BB_Mid"] + 2 * df["BB_Std"]
df["BB_Lower"] = df["BB_Mid"] - 2 * df["BB_Std"]

# -------------------------------------------------
# 4️⃣  FORECAST USING ARIMA
# -------------------------------------------------
print("\n🔮 Building ARIMA forecast model (please wait)...")
model = sm.tsa.ARIMA(df["y"], order=(5, 1, 0))
model_fit = model.fit()
forecast_arima = model_fit.forecast(steps=30)

# Future Dates
future_dates = pd.date_range(df["Date"].iloc[-1], periods=31, freq="D")[1:]
forecast_df = pd.DataFrame({"Date": future_dates, "ARIMA_Forecast": forecast_arima.values})

# -------------------------------------------------
# 5️⃣  BUY / SELL SIGNALS
# -------------------------------------------------
df["Buy_Signal"] = (df["MACD"] > df["Signal"]) & (df["RSI"] < 30)
df["Sell_Signal"] = (df["MACD"] < df["Signal"]) & (df["RSI"] > 70)

# -------------------------------------------------
# 6️⃣  PLOTS
# -------------------------------------------------
plt.style.use("seaborn-v0_8-darkgrid")

# (a) Price + Moving Averages
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["y"], label="Price", linewidth=2)
plt.plot(df["Date"], df["MA7"], label="7-Day MA")
plt.plot(df["Date"], df["MA30"], label="30-Day MA")
plt.title(f"{ticker} — Price with Moving Averages")
plt.xlabel("Date"); plt.ylabel("Price (USD)"); plt.legend(); plt.tight_layout(); plt.show()

# (b) MACD
plt.figure(figsize=(12,4))
plt.plot(df["Date"], df["MACD"], label="MACD", color="blue")
plt.plot(df["Date"], df["Signal"], label="Signal", color="red")
plt.title(f"{ticker} — MACD vs Signal")
plt.xlabel("Date"); plt.legend(); plt.tight_layout(); plt.show()

# (c) RSI
plt.figure(figsize=(12,4))
plt.plot(df["Date"], df["RSI"], color="purple")
plt.axhline(70, color="red", linestyle="--")
plt.axhline(30, color="green", linestyle="--")
plt.title(f"{ticker} — RSI (Overbought/ Oversold)")
plt.xlabel("Date"); plt.tight_layout(); plt.show()

# (d) Bollinger Bands
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["y"], label="Price", color="blue")
plt.plot(df["Date"], df["BB_Upper"], label="Upper Band", linestyle="--", color="red")
plt.plot(df["Date"], df["BB_Lower"], label="Lower Band", linestyle="--", color="green")
plt.title(f"{ticker} — Bollinger Bands")
plt.xlabel("Date"); plt.ylabel("Price (USD)"); plt.legend(); plt.tight_layout(); plt.show()

# (e) Forecast Plot
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["y"], label="History", linewidth=2)
plt.plot(forecast_df["Date"], forecast_df["ARIMA_Forecast"], label="30-Day ARIMA Forecast", color="orange", linewidth=2)
plt.title(f"{ticker} — ARIMA Forecast (Next 30 Days)")
plt.xlabel("Date"); plt.ylabel("Price (USD)"); plt.legend(); plt.tight_layout(); plt.show()

# -------------------------------------------------
# 7️⃣  SUMMARY (FIXED)
# -------------------------------------------------
last_price = float(df["y"].iloc[-1])
forecast_start = float(forecast_df["ARIMA_Forecast"].iloc[0])
last_rsi = float(df["RSI"].iloc[-1])

print("\n✅ Analysis Completed Successfully!")
print(f"📊 Total Buy Signals: {int(df['Buy_Signal'].sum())}")
print(f"📉 Total Sell Signals: {int(df['Sell_Signal'].sum())}")
print(f"💰 Last Closing Price: {last_price:.2f}")
print(f"🔮 Forecast Start Price: {forecast_start:.2f}")
print(f"📊 Last RSI Value: {last_rsi:.2f}")

# Save CSVs
df.to_csv(f"{ticker}_analysis.csv", index=False)
forecast_df.to_csv(f"{ticker}_forecast.csv", index=False)
print(f"\n💾 Files saved: {ticker}_analysis.csv & {ticker}_forecast.csv")

print("\n============================================================")
print(f"📈 {ticker} — Advanced Stock Insights")
print("============================================================")

# Progress simulation (simple dots instead of tqdm)
import time
for _ in range(3):
    print("⏳ Analyzing Advanced Metrics" + "." * (_ + 1))
    time.sleep(0.5)

print("\n------------------------------------------------------------")

# Compute insights safely
avg_return = df['Returns'].mean()
volatility = df['Volatility'].iloc[-1]
rsi_value = df['RSI'].iloc[-1]
trend = "UPTREND" if df['EMA12'].iloc[-1] > df['EMA26'].iloc[-1] else "DOWNTREND"

# RSI interpretation (text only)
if rsi_value < 30:
    rsi_status = "🟢 Oversold (Buy Zone)"
elif rsi_value > 70:
    rsi_status = "🔴 Overbought (Sell Zone)"
else:
    rsi_status = "🟡 Neutral (Wait/Observe)"

# Display clean summary
start_date = pd.to_datetime(df["Date"].iloc[0]).date()
end_date = pd.to_datetime(df["Date"].iloc[-1]).date()
print(f"📅 Period Analyzed: {start_date} → {end_date}")
print(f"💹 Avg Daily Return: {avg_return:.2f} %")
print(f"📊 30-Day Volatility: {volatility:.2f} %")
print(f"💱 Market Trend: {trend}")
print(f"🎯 RSI Status: {rsi_status}")

print("------------------------------------------------------------")
print("✅ All analytics completed successfully!")
print("============================================================\n")