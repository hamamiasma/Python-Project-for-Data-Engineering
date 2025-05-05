# ETL GDP Project

---

## Code Explanation: Parsing GDP Table Rows

The following code block iterates through HTML table rows and extracts relevant GDP data:

python
for row in rows:
    col = row.find_all('td')
    if len(col) != 0:
        if col[0].find('a') is not None and '—' not in col[2]:
            data_dict = {"Country": col[0].a.contents[0],
                         "GDP_USD_millions": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
return df


### Step-by-Step Breakdown:

- rows: list of <tr> tags from the GDP HTML table.
- col = row.find_all('td'): extract <td> cells from each row.
- if len(col) != 0: skip empty rows.
- col[0].find('a'): ensures the row contains a country link.
- '—' not in col[2]: excludes rows with missing GDP data.
- col[0].a.contents[0]: fetches the country name.
- col[2].contents[0]: fetches the GDP value.
- df1: one-row DataFrame from current row.
- df = pd.concat(...): append row to the full DataFrame.

This logic ensures only valid, complete entries are extracted and appended to the final dataset.

---

## Code Explanation: GDP Transformation

The following code transforms GDP values from text format (with commas) to numeric billions (rounded to 2 decimals):

```python
GDP_list = df["GDP_USD_millions"].tolist()
GDP_list = [float("".join(x.split(','))) for x in GDP_list]
GDP_list = [np.round(x / 1000, 2) for x in GDP_list]
df["GDP_USD_millions"] = GDP_list
df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})
return df
```

### Explanation:

- `df["GDP_USD_millions"].tolist()` – Extracts GDP column as a list of strings (e.g., `"1,234,567"`).
- `"".join(x.split(','))` – Removes all commas from the string:
  - `"1,234,567"` → `"1234567"`
- `float(...)` – Converts to a floating point number.
- `/ 1000` – Converts from millions to billions.
- `np.round(..., 2)` – Rounds to 2 decimal places.
- The DataFrame column is renamed accordingly.

This ensures clean, numerical GDP data in billions for further use.
