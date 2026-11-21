
import sqlite3

con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE readings (
    station TEXT,
    pm25 REAL
)
""")

data = [
    ("Adyar", 48),
    ("Guindy", 95),
    ("T Nagar", 65)
]

con.executemany(
    "INSERT INTO readings VALUES (?, ?)", data
)
con.commit()

def chatbot(question):
    question = question.lower()

    if "pm25" in question or "air quality" in question:
        for station in ["Adyar", "Guindy", "T Nagar"]:
            if station.lower() in question:
                result = con.execute(
                    "SELECT pm25 FROM readings WHERE station = ?",
                    (station,)
                ).fetchone()

                if result:
                    return f"{station} PM2.5: {result[0]} µg/m³"

        return "Please mention a station name."

    return "Sorry, I can answer only air-quality questions."


questions = [
    "What is the PM25 in Adyar?",
    "Tell me the air quality in Guindy",
    "What is the PM25 in T Nagar?",
    "What is the weather today?"
]

print("AIR QUALITY CHATBOT")
print("-------------------")

for question in questions:
    print("User:", question)
    print("Bot:", chatbot(question))
    print()

con.close()
