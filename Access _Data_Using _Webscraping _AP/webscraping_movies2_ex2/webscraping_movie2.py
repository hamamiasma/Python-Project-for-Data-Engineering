'''
Extracting only films released between 2000 and 2009, and storing the first 25 of them.
'''

import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

'''
requests: لتحميل صفحة الويب.
sqlite3: لإنشاء وربط قاعدة بيانات SQLite.
pandas: لمعالجة البيانات في جداول.
BeautifulSoup: لتحليل ملفات HTML واستخراج العناصر منها.
'''

# Define URLs and file paths
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies2.db'
table_name = 'Top_25_2000s'
csv_path = 'top_25_2000s_films.csv'

# Initialize DataFrame to store the data
df = pd.DataFrame(columns=["Film", "Year", "Rotten Tomatoes' Top 100"])

# Fetch and parse the web page
'''
requests.get(url).text: تحميل كود HTML للصفحة.
BeautifulSoup(...): تحليل صفحة HTML لتصبح قابلة للمعالجة.
'''
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Find all tables and rows from the first table
'''
find_all('tbody'): يبحث عن كل الجداول في الصفحة.
tables[0]: نأخذ أول جدول فقط.
find_all('tr'): نحصل على كل الصفوف داخل الجدول.
'''
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# Extract data from the table
count = 0
for row in rows:
    col = row.find_all('td')
    if len(col) != 0:
        # Extract year and convert to integer for filtering
        try:
            year = int(col[2].contents[0])
            # Check if the film was released in the 2000s (2000-2009)
            if 2000 <= year <= 2009:
                # Find the index of the "Rotten Tomatoes' Top 100" column
                # The column headers are in a different row, so we need to find which index it is
                # Based on the website, it's the 6th column (index 5)
                rt_rank = col[5].contents[0] if len(col) > 5 else "N/A"
                
                data_dict = {
                    "Film": col[1].contents[0],
                    "Year": year,
                    "Rotten Tomatoes' Top 100": rt_rank
                }
                
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
                count += 1
                
                # Stop after collecting 25 films from the 2000s
                if count >= 25:
                    break
        except (ValueError, IndexError):
            # Skip rows where year can't be converted to integer
            continue

# Display the results
print(f"Total films from 2000s found: {len(df)}")
print(df)

# Save to CSV
df.to_csv(csv_path)

# Save to SQLite database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

print(f"Data has been saved to {csv_path} and {db_name} (table: {table_name})")