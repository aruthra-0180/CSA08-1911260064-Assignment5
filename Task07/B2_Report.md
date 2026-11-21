## B2 – Adversarial Testing Report

### Test Cases

1. Negative PM2.5 (-10)
   Expected: Rejected
   Actual: Rejected
   Result: PASS

2. Very High PM2.5 (1500)
   Expected: Rejected
   Actual: Rejected
   Result: PASS

3. Duplicate Reading
   Expected: Rejected
   Actual: Rejected
   Result: PASS

4. Missing PM2.5 (None)
   Expected: Rejected
   Actual: Rejected
   Result: PASS

### Test Summary

Total Records: 6
Valid Records: 2
Rejected Records: 4

### Observation

The testing program correctly identifies
negative values, impossible values,
duplicate records and missing readings.

### Limitation

The tests use a small sample dataset.
Additional tests are needed for invalid dates,
hours, station names and non-numeric values.

### Conclusion

All four implemented adversarial test cases
passed successfully.
## B2 – Final Testing Summary

### Problems Identified

1. Negative PM2.5 readings.
2. Extremely high PM2.5 readings.
3. Duplicate air-quality records.
4. Missing PM2.5 values.

### Improvements Suggested

1. Validate pollutant readings before insertion.
2. Use unique station, date and hour combinations.
3. Handle missing values consistently.
4. Record rejected data for future inspection.
5. Use parameterised SQLite queries for safety.

### Final Result

The adversarial testing program detected
four invalid records out of six test records.

The valid records were successfully inserted
into the SQLite database.

The test demonstrates basic data validation
and safe database insertion.