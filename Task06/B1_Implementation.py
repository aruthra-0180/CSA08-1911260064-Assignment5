
import csv
from pathlib import Path

file = Path(__file__).with_name("air_quality.csv")

print("BEFORE CLEANING")
print("-" * 40)

with open(file, "r", encoding="utf-8") as f:
    data = list(csv.DictReader(f))

for row in data:
    print(row)

print("\nAFTER CLEANING")
print("-" * 40)

cleaned = []
seen = set()
previous = {}

for row in data:
    station = row["station"].strip().title()
    date = row["date"].strip()
    hour = int(row["hour"])
    key = (station, date, hour)

    if key in seen:
        continue
    seen.add(key)

    value = row["pm25"].strip()

    if value == "" or value.upper() == "NA":
        pm25 = previous.get(station)
        if pm25 is None:
            continue
    else:
        try:
            pm25 = float(value)
        except ValueError:
            continue

    if not 0 <= pm25 <= 999:
        continue

    previous[station] = pm25

    temperature = float(row["temperature"])

    if temperature > 60:
        temperature = (temperature - 32) * 5 / 9

    cleaned.append((
        station, date, hour,
        pm25, round(temperature, 2)
    ))

for row in cleaned:
    print(row)

print("\nValid readings:", len(cleaned))
