# Task 1 — Sales Forecasting

This task focuses on analyzing historical Superstore sales data and forecasting the next 30 days using time series modeling.

---

## 📌 Objective
To prepare daily sales data, visualize sales trends, and generate a 30-day forecast using a machine-learning time series model.

---

## 📂 Files in This Folder

| File Name | Description |
|----------|-------------|
| `Sample - Superstore.csv` | Raw sales dataset provided for analysis |
| `EDA.ipynb` | Jupyter Notebook containing data cleaning, preparation, visualization, and forecasting steps |
| `daily_sales_trend.png` | Visualization of daily historical sales |
| `forecast_plot.png` | 30-day sales forecast visualization |
| `30_day_forecast.csv` | Final predicted values for the next 30 days |
| `model.py` | Model script used for time-series forecasting |
| `TASK1_README.md` | Documentation for Task 1 |

---

## 🧹 Step 1 — Data Preparation (EDA)
- Read the Superstore dataset  
- Convert `Order Date` to datetime  
- Aggregate data to daily level  
- Handle missing values  
- Prepare cleaned daily sales series  

---

## 📊 Step 2 — Visualizations
### **1. Daily Sales Trend**
File: `daily_sales_trend.png`  
Shows the overall daily fluctuation and seasonality in sales.

### **2. 30-Day Forecast Plot**
File: `forecast_plot.png`  
Displays predicted sales with upper–lower confidence intervals.

---

## 🔮 Step 3 — Forecasting Model
- Used Facebook Prophet time series model  
- Trained on daily aggregated sales  
- Generated future dataframe for 30 days  
- Predicted sales stored in `30_day_forecast.csv`

---

## ✅ Final Output Delivered
- **30-day sales forecast (CSV)**  
- **Trend & Forecast plots (PNG)**  
- **Well-structured EDA notebook**  
- **Model script**  
- **This README documentation**

---

## 📌 Conclusion
The forecasting model successfully identifies sales patterns and predicts upcoming demand. These insights can help in **inventory planning, staffing, and strategic decision-making.**
