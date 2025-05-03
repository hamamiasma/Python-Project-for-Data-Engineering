'''
This Python project automatically extracts the 50 highest-rated films from an archived website and 
saves them locally as a CSV file(top_50_films.csv) and in a SQLite database(Movies.db).
'''

import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')
'''
You now need to write the loop to extract the appropriate information from the web page. 
The rows of the table needed can be accessed using the find_all() function with the BeautifulSoup object using the statements below.
Here, the variable tables gets the body of all the tables in the web page and the variable rows gets all the rows of the first table.
'''
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

'''
You can now iterate over the rows to find the required data. 
Use the code shown below to extract the information.
'''
for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

'''
the code functions as follows.

Iterate over the contents of the variable rows.
Check for the loop counter to restrict to 50 entries.
Extract all the td data objects in the row and save them to col.
Check if the length of col is 0, that is, if there is no data in a current row. This is important since, many timesm there are merged rows that are not apparent in the web page appearance.
Create a dictionary data_dict with the keys same as the columns of the dataframe created for recording the output earlier and corresponding values from the first three headers of data.
Convert the dictionary to a dataframe and concatenate it with the existing one. This way, the data keeps getting appended to the dataframe with every iteration of the loop.
Increment the loop counter.
Once the counter hits 50, stop iterating over rows and break the loop.
'''

print(df)
df.to_csv(csv_path)

'''
To store the required data in a database, you first need to initialize a connection to the database, save the dataframe as a table, and then close the connection. This can be done using the following code:
'''
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()