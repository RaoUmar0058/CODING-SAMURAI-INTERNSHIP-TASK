# 🚀 Data Science Internship Projects — Khadija Rao 

Welcome to my Data Science portfolio!  
This repository showcases **two professional data projects** that combine analytical depth, visualization skills, and forecasting techniques — perfect examples of my practical Data Science abilities.

---

## 📊 Project 1: Advanced Stock Analysis & Forecast 

### 🧠 Overview
A comprehensive **stock market analysis and forecasting project** using **Python, Statsmodels, and Yahoo Finance API**.  
It covers real-time data extraction, technical indicators, ARIMA forecasting, and actionable buy/sell signal generation.

---

### 🔍 Key Features
- 📥 **Automated data download** from Yahoo Finance  
- 📊 Calculation of Moving Averages, Volatility, RSI, MACD, EMA, and Bollinger Bands  
- 🔮 **ARIMA model (5,1,0)** for 30-day price forecasting  
- 💡 **Buy/Sell signal detection** using MACD-Signal crossovers & RSI thresholds  
- 📈 **Comprehensive visualizations** for price, trends, and forecasts  
- 💾 CSV export of both analysis and forecast results  

---

### ⚙️ Tech Stack
`Python` • `Pandas` • `NumPy` • `Matplotlib` • `Statsmodels` • `yfinance`

---

### 🧩 Model Performance
The ARIMA model’s performance was validated using **Root Mean Square Error (RMSE)** and **Mean Absolute Percentage Error (MAPE)** to ensure accurate short-term forecasting.

| Metric | Value (Example) |
|---------|----------------|
| RMSE | 2.31 |
| MAPE | 1.87% |

*(Values vary per run depending on live data.)*

---

### ⚔️ Challenges & Solutions
| Challenge | Solution |
|------------|-----------|
| **Non-stationary time series** | Applied differencing (`d=1`) and visual ACF/PACF checks before fitting ARIMA. |
| **Missing values & noise** | Used forward/backward filling and rolling mean smoothing. |
| **Choosing ARIMA order** | Iteratively tuned `(p,d,q)` via AIC and BIC comparison. |

---

### 📊 Insights
- 7-Day vs 30-Day MA comparison indicates short-term reversals.  
- RSI < 30 often coincides with entry opportunities.  
- Volatility spikes align with sudden price corrections.  
- Forecast trend suggests near-term continuation of momentum.  

---

### 📂 Output Files
- `AAPL_analysis.csv` — Full dataset with computed indicators  
- `AAPL_forecast.csv` — 30-day ARIMA forecast values  

---

### 🖼️ Sample Visuals
- Price with Moving Averages  
- MACD vs Signal  
- RSI Trendlines  
- Bollinger Bands  
- 30-Day Forecast Curve  

---

## 🚢 Project 2: Titanic Dataset — Exploratory Data Analysis (EDA)

### 🧠 Overview
This classic dataset project explores passenger demographics and survival patterns aboard the Titanic.  
The goal was to uncover relationships between variables using **data cleaning, descriptive statistics, and visual analysis** — the foundation of any predictive model.

---

### 🔍 Key Features
- 🧹 Missing values handled via median/mode imputation  
- 👥 Gender-based and Class-based survival analysis  
- 📈 Distribution plots for Age, Fare, and Embarkation Ports  
- 🧮 Correlation heatmap of numerical features  
- 📊 Insight-driven storytelling for survival outcomes  

---

### ⚙️ Tech Stack
`Python` • `Pandas` • `NumPy` • `Seaborn` • `Matplotlib`

---

### 📊 Insights
1. Females had a much higher survival rate than males.  
2. 1st-class passengers were most likely to survive.  
3. Younger age correlated with better survival chances.  
4. Higher fare generally meant better safety and class privileges.  
5. Majority of passengers embarked from port **“S”**.

---

### 💭 Challenges & Solutions
| Challenge | Solution |
|------------|-----------|
| Inconsistent missing values (deck, age, embarked) | Dropped `deck`, imputed `age` with median and `embarked` with mode. |
| Skewed age and fare distributions | Used log scaling and KDE plots for better visualization. |
| Class imbalance in survival | Focused on visual ratio comparisons using grouped countplots. |

---

### 🧠 Beyond EDA — ML Readiness
This analysis sets the stage for building a **classification model (e.g., Logistic Regression or Random Forest)**.  
The key insights extracted here can serve as **feature selection guidance** — such as encoding class, sex, and fare as predictors of survival.

---

### 🖼️ Visualizations
- Survival by Gender  
- Class vs Survival  
- Age Distribution Curve  
- Fare vs Survival (Boxplot)  
- Correlation Heatmap  

---

## 🧰 Skills Demonstrated
- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Statistical Feature Engineering  
- Time Series Forecasting (ARIMA)  
- Model Evaluation (RMSE, MAPE)  
- Data Visualization & Interpretation  
- Automation and CSV Reporting  

---

## 🧾 Author
**👩‍💻 Khadija  Rao**  
📍 Data Science Student | Virtual University of Pakistan  
📧 Email: raoumar0058@gmail.com  
🌐 GitHub: https://github.com/RaoUmar0058 
💼 LinkedIn: linkedin.com/in/rao-umar-904807355
---

⭐ *“Turning raw data into meaningful stories — one dataset at a time.”*  
