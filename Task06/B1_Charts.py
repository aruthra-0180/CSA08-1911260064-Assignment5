
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path(__file__).parent

df = pd.read_csv(folder / "air_quality.csv")
df["pm25"] = pd.to_numeric(df["pm25"], errors="coerce")
df = df.dropna(subset=["pm25"])
df = df[df["pm25"].between(0, 999)]
df = df.drop_duplicates(subset=["station", "date", "hour"])

# Chart 1: PM2.5 Trend
daily = df.groupby("date")["pm25"].mean()
daily.plot(kind="line", marker="o")
plt.title("PM2.5 Trend")
plt.xlabel("Date")
plt.ylabel("Average PM2.5 (µg/m³)")
plt.tight_layout()
plt.savefig(folder / "chart1_trend.png")
plt.show()

# Chart 2: Station Comparison
plt.figure()
station = df.groupby("station")["pm25"].mean()
station.plot(kind="bar")
plt.title("Station Comparison")
plt.xlabel("Station")
plt.ylabel("Average PM2.5 (µg/m³)")
plt.tight_layout()
plt.savefig(folder / "chart2_stations.png")
plt.show()

# Chart 3: Temperature vs PM2.5
plt.figure()
plt.scatter(df["temperature"], df["pm25"])
plt.title("Temperature vs PM2.5")
plt.xlabel("Temperature (raw CSV values)")
plt.ylabel("PM2.5 (µg/m³)")
plt.tight_layout()
plt.savefig(folder / "chart3_scatter.png")
plt.show()

# Chart 4: Worst Pollution Hours
plt.figure()
hourly = df.groupby("hour")["pm25"].mean()
hourly.plot(kind="bar")
plt.title("Average PM2.5 by Hour")
plt.xlabel("Hour")
plt.ylabel("Average PM2.5 (µg/m³)")
plt.tight_layout()
plt.savefig(folder / "chart4_hours.png")
plt.show()

print("All 4 charts saved successfully!")
