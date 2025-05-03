# Querying SQLite3 Database with Python and Pandas

## What is SQLite3?

**SQLite3** is an in-process Python library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. It is a popular choice as an embedded database for local/client storage in application software.

---

## 🔗 How to connect to SQLite3?

You can connect to SQLite3 using the `connect()` function by passing the database name as an argument:

```python
import sqlite3
sql_connection = sqlite3.connect('database.db')
```

This makes `sql_connection` an object of the SQL engine which you can use to execute queries.

---

## 🧱 How to create a table using Pandas?

You can directly load a pandas dataframe into SQLite3 using:

```python
df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
```

- `table_name`: Name of the table to be created.
- `sql_connection`: Connection object to the database.
- `if_exists`: Behavior if table already exists:
  - `'fail'`: Do nothing if table exists.
  - `'replace'`: Overwrite existing table.
  - `'append'`: Add to existing table.
- `index`: Keep this `True` only if the index has value.

---

## 🔍 How to query a database table using Pandas?

Use `read_sql()` to run SQL queries and return a pandas dataframe:

```python
import pandas as pd
df = pd.read_sql("SELECT * FROM table_name", sql_connection)
```

- The first argument is a query string.
- The second argument is the SQLite connection.

---

## 💡 Example Queries

| Query Statement                          | Purpose                                         |
|------------------------------------------|-------------------------------------------------|
| `SELECT * FROM table_name`               | Retrieve all entries of the table               |
| `SELECT COUNT(*) FROM table_name`        | Count all entries in the table                  |
| `SELECT Column_name FROM table_name`     | Retrieve one column from the table              |
| `SELECT * FROM table_name WHERE ...`     | Retrieve entries that meet a specific condition |

---

##  Summary

- SQLite3 is perfect for lightweight embedded databases.
- Use pandas to load and query data easily.
- Great for small projects, prototyping, and local apps.

> **Note:** Always close your database connection when done:
```python
sql_connection.close()
```