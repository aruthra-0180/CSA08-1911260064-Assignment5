## A1.1 – Inspect the Source

A station CSV file contains columns:
station, date, hour, pm25, pm10, no2, temperature.

Example:
station,date,hour,pm25,pm10,no2,temperature
Adyar,2026-10-01,08,48,75,22,30
Guindy,2026-10-01,09,NA,90,25,86

### Expected Data-Quality Problems

1. Missing values – PM2.5 = NA or blank.
2. Negative readings – PM2.5 = -5.
3. Impossible values – PM2.5 = 1500.
4. Duplicate rows – Same station, date and hour repeated.
5. Mixed temperature units – 86°F instead of 30°C.
6. Inconsistent station names – Adyar, adyar, ADYAR.
7. Incorrect date formats – 01/10/2026 instead of 2026-10-01.
8. Invalid data types – PM10 = abc instead of a number.
9. Missing columns – NO2 column absent.
10. Incorrect hour values – Hour = 25.
## A1.2 – Design the Storage (3 Marks)

SQLite Database Design

Two tables are used to store station information
and air-quality readings.

### Table 1: Stations

CREATE TABLE stations (
    station_id INTEGER PRIMARY KEY,
    station_name TEXT UNIQUE NOT NULL
);

### Table 2: Readings

CREATE TABLE readings (
    reading_id INTEGER PRIMARY KEY,
    station_id INTEGER,
    date TEXT,
    hour INTEGER,
    pm25 REAL,
    pm10 REAL,
    no2 REAL,
    temperature REAL,
    FOREIGN KEY (station_id)
        REFERENCES stations(station_id),
    UNIQUE(station_id, date, hour)
);

### CSV to SQLite Mapping

1. station → stations.station_name
2. date → readings.date
3. hour → readings.hour
4. pm25 → readings.pm25
5. pm10 → readings.pm10
6. no2 → readings.no2
7. temperature → readings.temperature

The station_id connects the two tables.

The station_id and reading_id are primary keys.

This database design reduces duplicate station
information and makes searching and analysing
air-quality data easier.
## A1.3 – CSV or SQL? (2 Marks)

### CSV
1. CSV is simple and easy to create.
2. It is suitable for storing raw sensor data.
3. It does not support complex queries efficiently.
4. Duplicate data is difficult to control.

### SQL (SQLite)
1. SQLite stores data in structured tables.
2. It supports filtering, sorting and aggregation.
3. It reduces duplication using primary and unique keys.
4. It is suitable for analysing large datasets.

### Final Decision

CSV is used for collecting and importing raw
air-quality readings.

SQLite is used for storing cleaned data and
performing efficient queries.

Therefore, using both CSV and SQLite is the
best choice for this project.
## A1.4 – Data Validation

The following validation rules are used to
check the air-quality readings.

1. Station name must not be empty.
2. Date must follow YYYY-MM-DD format.
3. Hour must be between 0 and 23.
4. PM2.5, PM10 and NO2 must be numeric.
5. Negative pollutant readings are invalid.
6. Missing values must be identified.
7. Duplicate station, date and hour records
   must be detected.
8. Temperature units must be consistent.

### Validation Process

1. Read the CSV file.
2. Check the required columns.
3. Identify missing and invalid values.
4. Detect duplicate records.
5. Separate valid and rejected records.
6. Store valid records in SQLite.
7. Generate a data-quality report.

### Result

This validation process improves the accuracy,
consistency and reliability of air-quality data.
## A1.5 – Data Processing Workflow

### Workflow

1. Start
2. Read air-quality CSV files.
3. Check required columns.
4. Validate station, date and hour.
5. Check pollutant readings.
6. Identify missing and duplicate records.
7. Separate valid and invalid records.
8. Store valid records in SQLite.
9. Generate a data-quality report.
10. End.

### Pseudocode

START

READ CSV file

FOR each record:

    CHECK required fields

    IF record is valid:
        STORE record in SQLite
    ELSE:
        ADD record to rejected list

GENERATE validation report

END