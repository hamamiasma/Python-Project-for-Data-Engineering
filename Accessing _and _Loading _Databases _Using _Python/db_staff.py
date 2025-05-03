'''
Erstellt eine Verbindung zu einer SQLite-Datenbank.
Lädt Daten aus einer CSV-Datei und Speichert sie als Tabelle in die Datenbank.
Führt mehrere SQL-Abfragen aus.
Fügt einen neuen Datensatz hinzu und Überprüft erneut die Datenbank.
Schließt die Verbindung.
Abschnitt	Funktion
read_csv =>	  Lädt CSV in Pandas
to_sql(... replace) =>	Erstellt Tabelle neu
SELECT Queries =>	Zeigen, zählen, filtern
to_sql(... append) =>	Fügt neuen Datensatz hinzu
close() =>	Verbindungsende
'''

import sqlite3
import pandas as pd

# Connect to the SQLite3 service
conn = sqlite3.connect('STAFF.db')

# Define table parameters
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Read the CSV data
file_path = '/Users/asmaahamami/Downloads/Python Project for Data Engineering/Accessing _and _Loading _Databases _Using _Python/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

# Load the CSV to the database
'''
Speichert die Daten als SQL-Tabelle INSTRUCTOR.
replace: Überschreibt die Tabelle, falls sie existiert.
index=False: Pandas-Index wird nicht gespeichert.
'''
df.to_sql(table_name, conn, if_exists = 'replace', index = False)
print('Table is ready')

# Query 1: Display all rows of the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Query 2: Display only the FNAME column for the full table.
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Query 3: Display the count of the total number of rows.
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Query 4: Display the count of the rows where CITY is Paris.
query_statement = f"SELECT COUNT(*) FROM {table_name} WHERE CITY = 'Illinois' "
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)



# Define data to be appended
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

# Append data to the table
data_append.to_sql(table_name, conn, if_exists = 'append', index = False)
print('Data appended successfully')

# Query 4: Display the count of the total number of rows.
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
# Close the connection
conn.close()