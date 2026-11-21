
## B1.2 – Compare with Your Design (1 Mark)

### Comparison

The Python implementation follows the cleaning
rules designed in Part A.

1. Missing PM2.5 values are filled using the
   previous valid reading from the same station.

2. Negative and impossible PM2.5 values are removed.

3. Duplicate station, date and hour records
   are removed.

4. Station names are standardised using title case.

5. Temperatures above 60 are assumed to be
   Fahrenheit and converted to Celsius.

### Changes from Original Design

The original design proposed using the station
median when no previous valid reading exists.

The current implementation skips such records
instead of calculating the median.

The implementation also needs additional
validation for other pollutant columns and
explicit temperature units.

### Conclusion

The implementation follows the main cleaning
rules, with some simplifications that should
be improved before production use.

## B1.4 – Chart Interpretation

### Chart 1 – PM2.5 Trend
The line chart displays the average PM2.5
readings by date. The sample contains only
one date, so a monthly trend cannot yet
be determined.

### Chart 2 – Station Comparison
The bar chart compares average PM2.5
readings across stations. It helps identify
which station has higher pollution levels.

### Chart 3 – Temperature vs PM2.5
The scatter plot displays the relationship
between temperature and PM2.5 readings.
The small sample is insufficient to establish
a reliable relationship.

### Chart 4 – Worst Pollution Hours
The bar chart compares average PM2.5
readings at different hours. It helps identify
hours with higher pollution levels.

### Conclusion
The four charts provide a visual overview
of air-quality readings. More dates and
cleaned temperature values are needed
for a reliable final analysis.
