# ETL Project: Top 10 Largest Banks by Market Capitalization

## Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline to retrieve, convert, and store data on the top 10 largest banks in the world, ranked by market capitalization (in billion USD).

The extracted data is transformed into multiple currencies using official exchange rates and made available in CSV and SQL formats for reporting from different global offices.

---

## Technologies Used

- **Python 3**
- **BeautifulSoup** – Web scraping
- **Pandas & NumPy** – Data manipulation and math
- **SQLite3** – Embedded database
- **Requests** – Data fetching
- **datetime** – Logging with timestamps

---

## ETL Steps

### 1. Extract

- Source: [Wikipedia - Largest Banks by Market Capitalization (Archived)](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks)
- Table extracted: "By market capitalization"
- Columns: `Name`, `MC_USD_Billion`

### 2. Transform

- Load exchange rates from CSV:
  - Source: `exchange_rate.csv`
- Convert market capitalization to:
  - GBP (`MC_GBP_Billion`)
  - EUR (`MC_EUR_Billion`)
  - INR (`MC_INR_Billion`)
- Rounded to 2 decimal places

### 3. Load

- Save to CSV: `Largest_banks_data.csv`
- Save to SQLite database:
  - File: `Banks.db`
  - Table: `Largest_banks`

---

## SQL Queries

These queries were executed on the final database:

1. **Show full table**  
   `SELECT * FROM Largest_banks;`

2. **Average market cap in GBP**  
   `SELECT AVG(MC_GBP_Billion) FROM Largest_banks;`

3. **Top 5 banks**  
   `SELECT Name FROM Largest_banks LIMIT 5;`

---

## 🧾 Log Tracking

Each step is recorded in `code_log.txt`, including:

- Extraction completed
- Transformation started
- Data loaded into CSV and DB
- SQL queries executed

Log format:  
`<timestamp> : <message>`

---

## Output Files

| File                      | Description                                 |
|---------------------------|---------------------------------------------|
| `Largest_banks_data.csv`  | Final processed data in CSV format          |
| `Banks.db`                | SQLite3 database with the table             |
| `code_log.txt`            | ETL execution log with timestamps           |
| `exchange_rate.csv`       | Currency exchange rates used in conversion  |

---

### Explanation: `exchange_rate = exchange_rate.set_index('Currency').to_dict()['Rate']`

This line converts a CSV file containing exchange rates into a Python dictionary.

1. **`set_index('Currency')`**  
   ➤ Sets the Currency column as the DataFrame index. Example::

   ```csv
   Currency,Rate
   GBP,0.74
   EUR,0.85
   INR,74.3
   ```

   → becomes:

   ```
           Rate
   Currency      
   GBP       0.74
   EUR       0.85
   INR      74.30
   ```

2. **`.to_dict()`**  
   ➤ Converts the DataFrame into a nested dictionary::

   ```python
   {
     'Rate': {
       'GBP': 0.74,
       'EUR': 0.85,
       'INR': 74.3
     }
   }
   ```

3. **`['Rate']`**  
   ➤ Extracts the inner dictionary for the Rate column::

   ```python
   {
     'GBP': 0.74,
     'EUR': 0.85,
     'INR': 74.3
   }
   ```

The result: A handy dictionary exchange_rate, which you can use to convert values from USD to other currencies – for example:

```python
df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]
```
---

## 👤 Author

**Asmaa Hamami**  
> Junior Data Engineer  

---

##  Notes

- Make sure you have internet access to fetch data and exchange rates.
- You can rerun this pipeline bi-annually when IMF updates the data.
"""
