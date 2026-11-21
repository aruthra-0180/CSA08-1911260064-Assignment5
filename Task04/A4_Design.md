
## A4.1 – Debugging Plan (2 Marks)

### 1. Print Statements
Use print() to display values during data cleaning.

Example:
print("PM2.5 value:", pm25)

This helps identify incorrect or missing values.

### 2. Assert Statements
Use assert to check expected conditions.

Example:
assert pm25 >= 0, "Invalid PM2.5 reading"

This helps detect invalid data during testing.

### 3. Logging
Use the logging module to record errors and warnings.

Example:
logging.warning("Missing PM2.5 value")

This helps track errors without displaying
every message on the screen.

### 4. PDB Debugger
Use pdb or the VS Code debugger to pause
execution and inspect variables.

Example:
breakpoint()

This helps identify the exact line causing
an error in the cleaning program.

### Conclusion
Print, assert, logging and debugging tools
help identify and correct errors in the
air-quality data cleaning process.

## A4.2 – Profiling Plan (2 Marks)

### 1. time.perf_counter()
Measures the execution time of a code section.

Example:
import time
start = time.perf_counter()
# Data cleaning code
end = time.perf_counter()
print("Time:", end - start)

### 2. timeit
Runs a function multiple times to measure
its execution speed accurately.

Example:
import timeit
print(timeit.timeit("sum(range(100))", number=1000))

### 3. cProfile
Identifies functions that take the most
execution time.

Example:
import cProfile
cProfile.run("sum(range(100))")

### Profiling Process
1. Measure CSV loading time.
2. Measure data cleaning time.
3. Measure SQLite insertion time.
4. Measure chart generation time.
5. Use cProfile to identify slow functions.
6. Optimise the slowest part and measure again.

### Alternative Concept and Complexity Analysis

Using thousands of print statements slows
execution because writing to the console
adds extra time.

For n records, printing once per record
requires O(n) output operations.

Logging also has overhead when messages are
enabled, but it supports configurable levels.

Print statements must be removed or disabled
manually after debugging.

Logging can be switched off by increasing
the logging level, such as to ERROR.

A debugger can be disabled by removing
breakpoints or running without debug mode.

### Conclusion
time.perf_counter(), timeit and cProfile
help identify performance bottlenecks
and improve program efficiency.
