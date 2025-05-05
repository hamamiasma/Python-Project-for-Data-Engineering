# ETL Project: Countries by GDP (Nominal)

## Project Description

This ETL project extracts, transforms, and loads data regarding countries and their GDP (in billions USD) as published by the International Monetary Fund (IMF). The goal is to make this data accessible for future business expansion analysis.

The IMF publishes GDP data twice yearly, and this script is built to automatically handle such updates.

---

## Technologies Used

- Python 3
- BeautifulSoup (for web scraping)
- Requests
- Pandas & NumPy
- SQLite3 (for database handling)
- Logging with datetime

---

## ETL Workflow

### 1. **Extract**
- Data is scraped from the [Wikipedia IMF GDP List (Archived)](https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29)
- Table rows are parsed and filtered
- Country names and their GDP in **millions USD** are extracted

### 2. **Transform**
- GDP values are cleaned (commas removed)
- Converted from millions to **billions USD**
- Rounded to 2 decimal places
- Column renamed to GDP_USD_billions

### 3. **Load**
- Data saved into a CSV: Countries_by_GDP.csv
- Data loaded into SQLite3 DB: World_Economies.db, table Countries_by_GDP

---

## Query Example

After loading, a SQL query is run to extract all countries with GDP >= 100 billion USD:

sql
SELECT * FROM Countries_by_GDP WHERE GDP_USD_billions >= 100;


The output is printed to terminal.

---

## Output Files

| File                     | Description                                |
|--------------------------|--------------------------------------------|
| Countries_by_GDP.csv   | Cleaned GDP data in CSV format             |
| World_Economies.db     | SQLite3 database with loaded GDP table     |
| etl_project_log.txt    | Timestamped log of each ETL step           |
| etl_project_gdp.py     | Python script for the entire ETL process   |

---

## Log Tracking

Each step of the ETL process is logged into etl_project_log.txt using timestamped entries.

Example:

2025-Apr-28-13:15:22 : Data extraction complete. Initiating Transformation process

---

## 👤 Author

**Asmaa Hamami**  
> Junior Data Engineer

---

##  Note

This project uses archived data for reproducibility. Update the URL in etl_project_gdp.py if newer GDP lists are available.