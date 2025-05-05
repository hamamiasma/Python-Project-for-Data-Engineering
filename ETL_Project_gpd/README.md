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
- Column renamed to `GDP_USD_billions`

### 3. **Load**
- Data saved into a CSV: `Countries_by_GDP.csv`
- Data loaded into SQLite3 DB: `World_Economies.db`, table `Countries_by_GDP`

---

## Query Example

After loading, a SQL query is run to extract all countries with GDP >= 100 billion USD:

```sql
SELECT * FROM Countries_by_GDP WHERE GDP_USD_billions >= 100;
```

The output is printed to terminal.

---

## Output Files

| File                     | Description                                |
|--------------------------|--------------------------------------------|
| `Countries_by_GDP.csv`   | Cleaned GDP data in CSV format             |
| `World_Economies.db`     | SQLite3 database with loaded GDP table     |
| `etl_project_log.txt`    | Timestamped log of each ETL step           |
| `etl_project_gdp.py`     | Python script for the entire ETL process   |

---

## Log Tracking

Each step of the ETL process is logged into `etl_project_log.txt` using timestamped entries.

Example:

```
2025-Apr-28-13:15:22 : Data extraction complete. Initiating Transformation process
```

---

## Code Explanation: Parsing GDP Table Rows

The following code block iterates through HTML table rows and extracts relevant GDP data:

```python
for row in rows:
    col = row.find_all('td')
    if len(col) != 0:
        if col[0].find('a') is not None and '—' not in col[2]:
            data_dict = {"Country": col[0].a.contents[0],
                         "GDP_USD_millions": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
return df
```

### Step-by-Step Breakdown:

- `rows`: list of `<tr>` tags from the GDP HTML table.
- `col = row.find_all('td')`: extract `<td>` cells from each row.
- `if len(col) != 0`: skip empty rows.
- `col[0].find('a')`: ensures the row contains a country link.
- `'—' not in col[2]`: excludes rows with missing GDP data.
- `col[0].a.contents[0]`: fetches the country name.
- `col[2].contents[0]`: fetches the GDP value.
- `df1`: one-row DataFrame from current row.
- `df = pd.concat(...)`: append row to the full DataFrame.

This logic ensures only valid, complete entries are extracted and appended to the final dataset.


## 🔄 Code Explanation: GDP Transformation

The following code transforms GDP values from text format (with commas) to numeric billions (rounded to 2 decimals):

```python
GDP_list = df["GDP_USD_millions"].tolist()
GDP_list = [float("".join(x.split(','))) for x in GDP_list]
GDP_list = [np.round(x / 1000, 2) for x in GDP_list]
df["GDP_USD_millions"] = GDP_list
df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})
return df
```

### 💡 Explanation:

- `df["GDP_USD_millions"].tolist()` – Extracts GDP column as a list of strings (e.g., `"1,234,567"`).
- `"".join(x.split(','))` – Removes all commas from the string:
  - `"1,234,567"` → `"1234567"`
- `float(...)` – Converts to a floating point number.
- `/ 1000` – Converts from millions to billions.
- `np.round(..., 2)` – Rounds to 2 decimal places.
- The DataFrame column is renamed accordingly.

This ensures clean, numerical GDP data in billions for further use.

---

## 👤 Author

**Asmaa Hamami** 

---

##  Note

This project uses archived data for reproducibility. Update the URL in `etl_project_gdp.py` if newer GDP lists are available.

