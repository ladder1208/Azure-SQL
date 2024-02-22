import pandas as pd
import datetime

df = pd.read_csv('bfro_reports.csv')

def date():
    while True:
        year = int(input("Year: "))
        current_year = datetime.datetime.now().year
        if year > current_year:
            print(f"El año no puede ser mayor al año actual ({current_year}). Por favor, inténtalo de nuevo.")
        else:
            return year
    
def data():
    season = input("Season: ").capitalize()
    state = input("State: ").capitalize()
    country = input("Country: ").capitalize()
    class_ = input("Class: ").capitalize()
    month = input("Month: ").capitalize()
    latitude = input("Latitude: ")
    longitude = input("Longitude: ")
    return season, state, country, class_, month, latitude, longitude

year = date()
season, state, country, class_, month, latitude, longitude = data()

new_data = {'Year': year, 'Season':season, 'State': state, 'Country': country, 'Class': class_, 'Month': month, 'Latitude': latitude, 'Longitude': longitude, 'Index': df['Index'].max() + 1}
new_df = pd.DataFrame([new_data])

df = pd.concat([df, new_df], ignore_index=True)
df.to_csv('bfro_reports.csv', index=False)
print("Data added successfully!")
