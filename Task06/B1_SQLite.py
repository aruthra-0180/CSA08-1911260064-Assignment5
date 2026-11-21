
import sqlite3
import csv
from pathlib import Path

folder = Path(__file__).parent
con = sqlite3.connect(folder / "air_quality.db")

con.execute("""
CREATE TABLE IF NOT EXISTS readings (
    station TEXT,
    date TEXT,
    hour INTEGER,
    pm25 REAL
)
""")

con.execute("DELETE FROM readings")

with open(folder / "air_quality.csv", newline="") as f:
    data = csv.DictReader(f)
    rows = []

    for r in data:
        try:
            pm25 = float(r["pm25"])
            if 0 <= pm25 <= 999:
                rows.append((
                    r["station"].strip().title(),
                    r["date"],
                    int(r["hour"]),
                    pm25
                ))
        except (ValueError, TypeError):
            continue

con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?, ?)",
    rows
)
con.commit()

print("SQLITE QUERY RESULTS")

queries = [
    ("Average PM2.5 by Station",
     "SELECT station, ROUND(AVG(pm25), 2) "
     "FROM readings GROUP BY station"),

    ("Maximum PM2.5 by Station",
     "SELECT station, MAX(pm25) "
     "FROM readings GROUP BY station"),

    ("Number of Readings by Station",
     "SELECT station, COUNT(*) "
     "FROM readings GROUP BY station")
]

for title, sql in queries:
    print("\n" + title)
    for result in con.execute(sql):
        print(result)

con.close()
