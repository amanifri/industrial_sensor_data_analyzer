
import pandas as pd
import numpy as np

# Make the results reproducible
np.random.seed(42)

# Number of sensor readings
n = 100

# Generate timestamps
timestamps = pd.date_range(
    start="2026-01-01 08:00:00",
    periods=n,
    freq="min"
)

# Generate sensor measurements
temperature = np.random.normal(60, 5, n)
vibration = np.random.normal(2.5, 0.5, n)
rpm = np.random.normal(1500, 100, n)

# Create a DataFrame
data = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": temperature,
    "vibration": vibration,
    "rpm": rpm
})

# Save the data to a CSV file
data.to_csv("sensor_data.csv", index=False)

print("Sensor dataset created successfully!")
print(data.head())
