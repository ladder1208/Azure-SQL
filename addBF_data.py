import pymssql
import datetime
from datetime import datetime, timedelta
import time



def date():
    while True:
        year = int(input("Year: "))
        current_year = datetime.now().year
        if year > current_year:
            print(f"El año no puede ser mayor al año actual ({current_year}). Por favor, inténtalo de nuevo.")
        else:
            return year
    
def get_next_index():
    try:
        conn = pymssql.connect(server='---',
        user='---',
        password='---',
        database='---')
        cursor = conn.cursor()

        query = "SELECT MAX(bf_index) FROM csv_SQL"
        cursor.execute(query)
        result = cursor.fetchone()
        next_index = 1 if result[0] is None else result[0] + 1

        cursor.close()
        conn.close()

        return next_index

    except Exception as e:
        print("Error connecting to the database: ", e)

def add_data_to_db(data):
    try:
        conn = pymssql.connect(server='---',
        user='---',
        password='---',
        database='---')
        cursor = conn.cursor()

        query = "INSERT INTO csv_bigfoot (bf_index, bf_year, bf_season, bf_state, bf_country, bf_class, bf_month, bf_latitude, bf_longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        conn.commit()

        print("Data inserted successfully.")
        cursor.close()
        conn.close()

    except Exception as e:
        print("Error connecting to the database: ", e)

def main():
    # Example of getting new data from user, you can customize this part as needed
    new_index = get_next_index()
    new_data = (
        new_index,
        date(),
        input("Enter season: ").capitalize(),
        input("Enter state: ").capitalize(),
        input("Enter country: ").capitalize(),
        input("Enter class: ").capitalize(),
        input("Enter month: ").capitalize(),
        float(input("Enter latitude: ")),
        float(input("Enter  longitude: "))
    )

    # Convert latitude and longitude to Decimal if needed
    new_data = (
        new_data[0],
        new_data[1],
        new_data[2],
        new_data[3],
        new_data[4],
        new_data[5],
        new_data[6],
        new_data[7],
        new_data[8]
    )

    add_data_to_db(new_data)

if __name__ == "__main__":
    main()

