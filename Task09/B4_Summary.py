
import re
from collections import Counter

complaints = [
    "The road is dusty and air pollution is high.",
    "Smoke from vehicles is increasing.",
    "The air quality is poor near the school.",
    "Dust pollution is affecting the area.",
    "The road has heavy traffic and smoke."
]

stop_words = {
    "the", "is", "and", "a", "an", "from",
    "near", "has", "in", "of", "to"
}

def summarise(texts, count=2):
    words = []

    for text in texts:
        for word in re.findall(r"\b[a-z]+\b", text.lower()):
            if word not in stop_words:
                words.append(word)

    frequency = Counter(words)
    scores = []

    for index, sentence in enumerate(texts):
        sentence_words = re.findall(
            r"\b[a-z]+\b", sentence.lower()
        )
        score = sum(
            frequency[word]
            for word in sentence_words
            if word not in stop_words
        )
        scores.append((score, index))

    selected = sorted(
        scores, reverse=True
    )[:count]

    indices = sorted(index for _, index in selected)
    return " ".join(texts[i] for i in indices)


print("CITIZEN COMPLAINT SUMMARY")
print("-------------------------")
print(summarise(complaints))
