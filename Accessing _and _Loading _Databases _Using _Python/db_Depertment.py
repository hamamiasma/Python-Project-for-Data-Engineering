import sqlite3
import pandas as pd
import requests
import os

# Function to download CSV file
def download_csv(url, file_name):
    print(f"Downloading {file_name}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"Download of {file_name} completed successfully.")
        return True
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")
        return False

# Connect to the SQLite3 database
conn = sqlite3.connect('STAFF.db')
print("Connected to STAFF.db database")

# Download the Departments CSV file
csv_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/Departments.csv"
csv_file = "Departments.csv"

if download_csv(csv_url, csv_file):
    # Define table parameters
    table_name = 'Departments'
    attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']
    
    # Read the CSV data
    df = pd.read_csv(csv_file, names=attribute_list)
    
    # Display the data loaded from CSV
    print("\nData loaded from CSV:")
    print(df)
    
    # Load the CSV to the database
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"\nTable {table_name} created successfully")
    
    # Append additional department data
    data_to_append = {
        'DEPT_ID': [9],
        'DEP_NAME': ['Quality Assurance'],
        'MANAGER_ID': [30010],
        'LOC_ID': ['L0010']
    }
    
    df_append = pd.DataFrame(data_to_append)
    df_append.to_sql(table_name, conn, if_exists='append', index=False)
    print("\nAdditional department data appended successfully")
    
    # Run queries
    
    # Query 1: View all entries
    print("\n--- Query 1: View all entries ---")
    query_1 = f"SELECT * FROM {table_name}"
    query_output_1 = pd.read_sql(query_1, conn)
    print(query_1)
    print(query_output_1)
    
    # Query 2: View only the department names
    print("\n--- Query 2: View only the department names ---")
    query_2 = f"SELECT DEP_NAME FROM {table_name}"
    query_output_2 = pd.read_sql(query_2, conn)
    print(query_2)
    print(query_output_2)
    
    # Query 3: Count the total entries
    print("\n--- Query 3: Count the total entries ---")
    query_3 = f"SELECT COUNT(*) FROM {table_name}"
    query_output_3 = pd.read_sql(query_3, conn)
    print(query_3)
    print(query_output_3)
    
    '''# Clean up - remove downloaded CSV file
    if os.path.exists(csv_file):
        os.remove(csv_file)
        print(f"\nRemoved {csv_file}") '''
    
else:
    print("Failed to process the Departments table due to download error.")

# Close the database connection
conn.close()
print("\nDatabase connection closed.")