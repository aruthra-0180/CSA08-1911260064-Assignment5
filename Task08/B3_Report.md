
# B3 – Loops vs Libraries vs SQL

## B3.1 – Correctness on Small Data

The daily average PM2.5 was calculated using
three methods: Python loops, pandas groupby,
and SQLite GROUP BY.

All three methods produced the same results.

Adyar: 54.0
Guindy: 108.0

Result: PASS

## B3.2 – Performance Comparison

The three methods were tested with:

1. 1 station – 8,760 readings
2. 12 stations – 105,120 readings
3. 120 stations – 1,051,200 readings

The execution time was measured using
time.perf_counter().

The actual execution times are recorded
in B3_Performance_Output.png.

## B3.3 – Profiling

The Python implementation was analysed
using cProfile.

The profiler measured the execution time
and function calls to help identify
performance bottlenecks.

The function with the highest cumulative
time should be identified from the output.

## B3.4 – Engineering Trade-Off

### Plain Python Loops

Advantages:
- Simple to understand and implement.
- No external libraries required.
- Suitable for small datasets.
- Supports memory-efficient streaming.

Disadvantages:
- May be slower for complex data analysis.
- Requires more manual programming.

### Pandas GroupBy

Advantages:
- Easy to perform data analysis.
- Requires fewer lines of code.
- Supports large datasets efficiently.

Disadvantages:
- Requires additional memory.
- The dataset is usually loaded into RAM.

### SQLite GROUP BY

Advantages:
- Suitable for stored data.
- Supports SQL queries and indexing.
- Avoids loading the entire database
  into Python memory.

Disadvantages:
- Database setup is required.
- Inserting data adds processing time.

## Alternative Concept and Complexity Analysis

A running sum and count can calculate
daily averages in one pass.

Time Complexity: O(n)
Space Complexity: O(g)

Here, n is the number of readings and
g is the number of station-day groups.

Storing all readings before calculating
the mean requires O(n) memory.

## Final Decision

For a quick one-time analysis of CSV data,
pandas groupby is a practical choice
when sufficient RAM is available.

For daily automated reports using data
already stored in a database, SQLite
GROUP BY is preferred.

The final performance decision should
be supported by the measured timings.
