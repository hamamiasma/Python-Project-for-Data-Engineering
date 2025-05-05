# ETL GDP Project


---

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
