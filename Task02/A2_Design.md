
## A2.1 – Cleaning Rules

### 1. Missing Values
Fill missing PM2.5 readings using the previous valid
reading from the same station.
If unavailable, use the station median.

Reason: This preserves records and avoids unnecessary
data loss.

### 2. Impossible Values
Remove negative pollutant readings and values above
the accepted sensor limit, such as PM2.5 > 999.

Reason: These readings may be caused by sensor errors.

### 3. Duplicate Rows
Remove duplicate records with the same station,
date and hour.

Reason: Duplicates can affect average calculations.

### 4. Fahrenheit Temperatures
Convert Fahrenheit to Celsius using:

Celsius = (Fahrenheit - 32) × 5 / 9

Example: 86°F = 30°C

Reason: All temperatures must use the same unit.

## A2.2 – Normalisation (2 Marks)

### 1. Min-Max Normalisation

Formula:
X_normalised = (X - Min) / (Max - Min)

Example:
PM2.5 values = [20, 40, 60]

Normalised values = [0, 0.5, 1]

Use:
Min-max normalisation scales PM2.5 values
between 0 and 1.

It is useful for charts and comparing readings.

### 2. Z-Score Standardisation

Formula:
Z = (X - Mean) / Standard Deviation

Example:
PM2.5 values = [20, 40, 60]

Mean = 40
Standard Deviation = 16.33

Z-scores = [-1.225, 0, 1.225]

Use:
Z-score standardisation shows how far a
PM2.5 reading is from the mean.

It is useful for identifying unusual readings.

### Conclusion

Min-max normalisation is suitable for scaling
PM2.5 values to a fixed range.

Z-score standardisation is suitable for
detecting unusual pollution levels.

If Max = Min or standard deviation = 0,
return 0 for all values to avoid division by zero.

## A2.3 – Formatting (1 Mark)

### 1. Date Format
Use YYYY-MM-DD format.

Example: 2026-10-01

### 2. Station Name Format
Use consistent title case and remove extra spaces.

Example:
"adyar" → "Adyar"
" GUINDY " → "Guindy"

### 3. Number Format
Store pollutant readings as numeric values
and display them with two decimal places.

Example:
PM2.5 = 48.00
PM10 = 75.00
NO2 = 22.00

Store temperature in Celsius.

Example: 30.00°C

### Conclusion
Standard formatting ensures consistency,
accuracy and easy analysis of air-quality data.
