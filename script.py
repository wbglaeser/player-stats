import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the Samsonite stores page
url = 'https://www.samsonite.de/samsonite-stores/'

# Send a GET request to the URL and store the response in a variable
response = requests.get(url)

# Parse the HTML content of the response using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the store elements on the page
store_elements = soup.find_all('div', {'class': 'store-item'})

# Create a CSV file to store the store details
with open('samsonite_stores.csv', 'w', newline='', encoding='utf-8') as file:

    # Define the column headers for the CSV file
    headers = ['Name', 'Address', 'Phone', 'Email', 'Latitude', 'Longitude']

    # Create a CSV writer object and write the headers to the file
    writer = csv.writer(file)
    writer.writerow(headers)

    # Loop through each store element and extract its details
    for store in store_elements:
        name = store.find('h3').text.strip()
        address = store.find('p', {'class': 'address'}).text.strip()
        phone = store.find('a', {'class': 'phone'}).text.strip()
        email = store.find('a', {'class': 'email'}).text.strip()
        latitude = store['data-lat']
        longitude = store['data-lng']

        # Write the store details to the CSV file
        writer.writerow([name, address, phone, email, latitude, longitude])

print('Store details saved to samsonite_stores.csv')
