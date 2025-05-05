# coding: utf-8
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import numpy as np


DATA_URL = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
EXCHANGE_RATE_CSV_URL = './exchange_rate.csv'
EXTRACT_TABLE_ATTRIBS = ["Name", "MC_USD_Billion"]
FINAL_TABLE_ATTRIBS = ["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
OUTPUT_CSV_PATH = './Largest_banks_data.csv'
DB_NAME = 'Banks.db'
TABLE_NAME = 'Largest_banks'
LOG_FILE = 'code_log.txt'


def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
     code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Month-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("code_log.txt","a") as f:
        f.write(timestamp + ' : ' + message + '\n')


# Task 2: Extract
def extract(url, table_attribs):
    ''' Extracts the required table (by market capitalization) from the webpage
    and returns a DataFrame containing the columns defined in table_attribs.
    '''
    log_progress("Starting data extraction from URL")
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    df = pd.DataFrame(columns=table_attribs)
    tables = soup.find_all("table", {"class": "wikitable"})
    rows = tables[0].find_all("tr")
    
    for row in rows:
        if row.find('td') is not None:
            col = row.find_all("td")
            bank_name = col[1].find_all('a')[1].get('title', 'Unknown')
            market_cap = float(col[2].get_text(strip=True).replace(',', ''))
            data_dict = {"Name": bank_name, 
                        "MC_USD_Billion": float(market_cap)}
            df1 = pd.DataFrame(data_dict , index= [0])
            df = pd.concat([df, df1] , ignore_index=True)
    log_progress(f"Extraction complete. {len(df)} rows extracted.")
    return df

# Task 3: Transform
def transform(df, csv_path):
    """
    Transforms the DataFrame by converting the market capitalization from USD (Billion)
    to GBP, EUR and INR using the exchange rate information provided in the CSV.
    The final DataFrame will contain columns for each currency, rounded to 2 decimals.
    """
    log_progress("Starting data transformation process")
   
    exchange_rate = pd.read_csv(csv_path)
    exchange_rate = exchange_rate.set_index('Currency'). to_dict()['Rate']
    df[ 'MC_GBP_Billion'] = [np. round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion' ]]
    df[ 'MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion' ]]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion' ]]
    
    log_progress("Data transformation complete")
    return df

# Task 4: Load_to_csv
def load_to_csv(df, output_path):
    """
    Saves the final DataFrame to a CSV file at the provided output path.
    """
    df.to_csv(output_path, index=False)
    log_progress("Data saved to CSV file at " + output_path)


# Task 5:load_to_db
def load_to_db(df, sql_connection, table_name):
    """
    Loads the final DataFrame as a table in the provided SQL connection.
    """
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    log_progress("Data loaded to Database table: " + table_name)

# Task 6: run_query
def run_query(query_statement, sql_connection):
    """
    Runs the given SQL query on the database and prints the result.
    """
    log_progress("Running query: " + query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_statement)
    print(query_output)

# Task 7: MAIN_ETL_PROCESS
if __name__ == "__main__":
    log_progress("Preliminaries complete. Initiating ETL process")
    
    # Extraction phase
    banks_df = extract(DATA_URL, EXTRACT_TABLE_ATTRIBS)
    print(banks_df)
    print("\n")
    
    # Transformation phase
    transformed_df = transform(banks_df, EXCHANGE_RATE_CSV_URL)
    print(transformed_df)
    print("\n")
    
    # Loading phase to CSV
    load_to_csv(transformed_df, OUTPUT_CSV_PATH)
    
    # Loading phase to Database
    sql_conn = sqlite3.connect(DB_NAME)
    load_to_db(transformed_df, sql_conn, TABLE_NAME)
    print("\n")
    
    # Run queries
    log_progress("Calling run_query function for query 1")
    query1 = f"SELECT * FROM {TABLE_NAME}"
    run_query(query1, sql_conn)
    print("\n")
    
    log_progress("Calling run_query function for query 2")
    query2 = f"SELECT AVG(MC_GBP_Billion) FROM {TABLE_NAME}"
    run_query(query2, sql_conn)
    print("\n")
    
    log_progress("Calling run_query function for query 3")
    query3 = f"SELECT Name from {TABLE_NAME} WHERE MC_EUR_Billion > 100"
    run_query(query3, sql_conn)
    print("\n")
    
    log_progress("Calling run_query function for query 4")
    query4 = f"SELECT Name, MC_USD_Billion from {TABLE_NAME} ORDER BY MC_USD_Billion DESC LIMIT 5"
    run_query(query4, sql_conn)
    print("\n")
    
    log_progress("ETL process complete.")
    sql_conn.close()
