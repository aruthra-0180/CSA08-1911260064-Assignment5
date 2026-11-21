
import csv
import io
import sqlite3
import pandas as pd
from collections import defaultdict

data = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-01,60
Guindy,2026-10-01,95
Guindy,2026-10-01,121
"""

rows = list(csv.DictReader(io.StringIO(data)))

# Method 1: Plain Python
groups = defaultdict(list)

for row in rows:
    key = (row["station"], row["date"])
    groups[key].append(float(row["pm25"]))

python_result = {
    key: sum(values) / len(values)
    for key, values in groups.items()
}

# Method 2: Pandas
df = pd.DataFrame(rows)
df["pm25"] = df["pm25"].astype(float)

pandas_result = df.groupby(
    ["station", "date"]
)["pm25"].mean().to_dict()

# Method 3: SQLite
con = sqlite3.connect(":memory:")
con.execute(
    "CREATE TABLE readings "
    "(station TEXT, date TEXT, pm25 REAL)"
)

con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)",
    [(r["station"], r["date"], float(r["pm25"]))
     for r in rows]
)

sql_result = {
    (station, date): avg
    for station, date, avg in con.execute(
        "SELECT station, date, AVG(pm25) "
        "FROM readings GROUP BY station, date"
    )
}

print("Python:", python_result)
print("Pandas:", pandas_result)
print("SQLite:", sql_result)

assert python_result == pandas_result == sql_result
print("All three methods agree!")

con.close()
