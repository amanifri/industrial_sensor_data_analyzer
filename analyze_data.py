
import pandas as pd

# Load the sensor dataset
data = pd.read_csv("sensor_data.csv")

# Convert timestamp to datetime
data["timestamp"] = pd.to_datetime(data["timestamp"])

# Display basic information
print("=== DATASET INFORMATION ===")
print(data.info())

print("\n=== FIRST 5 READINGS ===")
print(data.head())

print("\n=== STATISTICAL SUMMARY ===")
print(data[["temperature", "vibration", "rpm"]].describe())

print("\n=== SENSOR AVERAGES ===")
print(data[["temperature", "vibration", "rpm"]].mean())


# Define experimental warning thresholds
temperature_limit = 68
vibration_limit = 3.5

# Find readings that exceed the thresholds
data["high_temperature"] = (
    data["temperature"] > temperature_limit
)

data["high_vibration"] = (
    data["vibration"] > vibration_limit
)

# Select readings that need review
alerts = data[
    data["high_temperature"] | data["high_vibration"]
]

print("\n=== SENSOR ALERTS ===")
print(alerts[
    ["timestamp", "temperature", "vibration",
     "high_temperature", "high_vibration"]
])

print("\nTotal readings requiring review:", len(alerts))
