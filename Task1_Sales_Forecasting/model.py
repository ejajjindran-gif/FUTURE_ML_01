import pandas as pd
from prophet import Prophet

# Load dataset
df = pd.read_csv("Sample - Superstore.csv")

# Prepare data for Prophet
df = df.rename(columns={"Order Date": "ds", "Sales": "y"})
df["ds"] = pd.to_datetime(df["ds"])

# Build model
model = Prophet()
model.fit(df)

# Create future dates
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Save forecast
forecast.to_csv("forecast_output.csv", index=False)
