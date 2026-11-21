
import re

positive = {"good", "clean", "improved", "helpful", "fast"}
negative = {"bad", "dirty", "smoke", "slow", "broken"}

def sentiment(text):
    words = re.findall(r"\b\w+\b", text.lower())
    score = 0

    for i, word in enumerate(words):
        value = 0

        if word in positive:
            value = 1
        elif word in negative:
            value = -1

        if i > 0 and words[i - 1] == "not":
            value = -value

        score += value

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"


complaints = [
    "The air is good and clean",
    "There is smoke and dirty air",
    "The service is not good",
    "The station is helpful",
    "Air quality report is available"
]

print("CITIZEN COMPLAINT SENTIMENT ANALYSIS")
print("------------------------------------")

for complaint in complaints:
    print("Complaint:", complaint)
    print("Sentiment:", sentiment(complaint))
    print()
