
# B4 – Final Engineering Decision

## 1. Sentiment Analysis

A rule-based sentiment classifier was developed
to classify citizen complaints as:

- Positive
- Negative
- Neutral

Negation words such as "not" were also handled.

## 2. Complaint Summarisation

An extractive summarisation method was used.

The program:
- Counts important words.
- Calculates sentence scores.
- Selects the highest-scoring sentences.
- Produces a short complaint summary.

## 3. Chatbot Implementation

A rule-based chatbot was developed using SQLite.

The chatbot:
- Accepts air-quality questions.
- Identifies station names.
- Retrieves PM2.5 values.
- Returns a message for unsupported questions.

## 4. Limitations

- Sentiment analysis may fail with sarcasm.
- Summaries may miss important information.
- The chatbot supports only predefined questions.

## 5. Final Engineering Decision

SQLite is suitable for storing and querying
air-quality readings.

Pandas is useful for data analysis and reports.

Rule-based sentiment analysis and chatbots
are suitable for a basic prototype.

For production use, the system requires
more testing, monitoring and validation.
