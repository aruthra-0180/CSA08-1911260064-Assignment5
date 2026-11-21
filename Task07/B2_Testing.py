
import sqlite3

con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE readings (
    station TEXT,
    date TEXT,
    pm25 REAL
)
""")

test_data = [
    ("Adyar", "2026-10-01", 48),
    ("Guindy", "2026-10-01", 95),
    ("Adyar", "2026-10-02", -10),
    ("Guindy", "2026-10-02", 1500),
    ("Adyar", "2026-10-01", 48),
    ("T Nagar", "2026-10-03", None)
]

valid = []
rejected = []

for row in test_data:
    station, date, pm25 = row

    if pm25 is None or not 0 <= pm25 <= 999:
        rejected.append(row)
    elif row in valid:
        rejected.append(row)
    else:
        valid.append(row)

con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)",
    valid
)
con.commit()

print("ADVERSARIAL TEST RESULTS")
print("------------------------")

print("Total records:", len(test_data))
print("Valid records:", len(valid))
print("Rejected records:", len(rejected))

print("\nRejected Data:")
for row in rejected:
    print(row)

con.close()
