import pymssql
import csv
from datetime import datetime, timedelta
import time

try:
    conn = pymssql.connect(server='---',
    user='---',
    password='---',
    database='---')
    print("Connected to the database.")
    print("Creating table...")
    input("Press Enter to continue...")
    create_tables = '''IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[csv_bigfoot]') AND type in (N'U'))
                            BEGIN
                            CREATE TABLE [dbo].[csv_bigfoot](
                                bf_index INT PRIMARY KEY,
                                bf_year INT,
                                bf_season VARCHAR(10),
                                bf_state VARCHAR(50),
                                bf_country VARCHAR(50),
                                bf_class VARCHAR(10),
                                bf_month VARCHAR(11),
                                bf_latitude DECIMAL(9,6),
                                bf_longitude DECIMAL(9,6))
                            END'''
    cursor = conn.cursor()
    cursor.execute(create_tables)
    conn.commit()
    print("Table created successfully.")

    with open('bfro_reports.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        query = "DELETE FROM csv_bigfoot"
        cursor.execute(query)
        for row in reader:
            row = [str(value) for value in row]
            query = "INSERT INTO csv_bigfoot (bf_index, bf_year, bf_season, bf_state, bf_country, bf_class, bf_month, bf_latitude, bf_longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8])
            cursor.execute(query, data)
            print(data)
            #time.sleep()
        conn.commit()

    print("Data inserted successfully.")
    cursor.close()
    conn.close()

except Exception as e:
    print("Error connecting to the database: ", e)
