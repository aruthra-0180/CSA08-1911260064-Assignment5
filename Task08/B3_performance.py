
import time
import sqlite3
import pandas as pd
from collections import defaultdict
from datetime import datetime, timedelta

def generate_data(stations):
    start = datetime(2026, 1, 1)
    rows = []

    for s in range(stations):
        for h in range(8760):
            day = (start + timedelta(hours=h)).strftime("%Y-%m-%d")
            pm25 = float(30 + (s * 7 + h) % 120)
            rows.append((f"Station{s+1}", day, pm25))

    return rows

def python_method(rows):
    groups = defaultdict(lambda: [0.0, 0])

    for station, day, pm25 in rows:
        groups[(station, day)][0] += pm25
        groups[(station, day)][1] += 1

    return {
        key: total / count
        for key, (total, count) in groups.items()
    }

def pandas_method(rows):
    df = pd.DataFrame(
        rows, columns=["station", "day", "pm25"]
    )
    return df.groupby(
        ["station", "day"]
    )["pm25"].mean().to_dict()

def sql_method(rows):
    con = sqlite3.connect(":memory:")
    con.execute(
        "CREATE TABLE readings "
        "(station TEXT, day TEXT, pm25 REAL)"
    )
    con.executemany(
        "INSERT INTO readings VALUES (?, ?, ?)", rows
    )
    result = {
        (s, d): avg
        for s, d, avg in con.execute(
            "SELECT station, day, AVG(pm25) "
            "FROM readings GROUP BY station, day"
        )
    }
    con.close()
    return result

print("B3 PERFORMANCE COMPARISON")
print("-------------------------")

for stations in [1, 12, 120]:
    rows = generate_data(stations)
    print(f"\nStations: {stations}, Rows: {len(rows)}")

    results = []

    for name, method in [
        ("Python", python_method),
        ("Pandas", pandas_method),
        ("SQLite", sql_method)
    ]:
        start = time.perf_counter()
        result = method(rows)
        elapsed = time.perf_counter() - start
        results.append(result)

        print(f"{name}: {elapsed:.4f} seconds")

    assert results[0].keys() == results[1].keys() == results[2].keys()
    assert all(
        abs(results[0][key] - results[1][key]) < 1e-9
        and abs(results[0][key] - results[2][key]) < 1e-9
        for key in results[0]
    )
    print("All methods agree!")
