
import cProfile
import pstats
from collections import defaultdict

def generate_data():
    rows = []

    for station in range(12):
        for hour in range(8760):
            day = hour // 24
            pm25 = 30 + (station * 7 + hour) % 120
            rows.append((station, day, pm25))

    return rows

def python_method(rows):
    groups = defaultdict(lambda: [0, 0])

    for station, day, pm25 in rows:
        groups[(station, day)][0] += pm25
        groups[(station, day)][1] += 1

    return {
        key: total / count
        for key, (total, count) in groups.items()
    }

rows = generate_data()

profiler = cProfile.Profile()
profiler.enable()

result = python_method(rows)

profiler.disable()

print("B3.3 – cProfile Results")
print("Total rows:", len(rows))
print("Daily groups:", len(result))

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats(10)
