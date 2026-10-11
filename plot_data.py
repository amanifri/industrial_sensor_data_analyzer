

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sensor_data.csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

axes[0].plot(data["timestamp"], data["temperature"])
axes[0].set_title("Motor Temperature Over Time")
axes[0].set_ylabel("Temperature (°C)")

axes[1].plot(data["timestamp"], data["vibration"])
axes[1].set_title("Motor Vibration Over Time")
axes[1].set_ylabel("Vibration")
axes[1].set_xlabel("Time")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

correlation = data["temperature"].corr(data["vibration"])
print("Temperature-vibration correlation:", correlation)