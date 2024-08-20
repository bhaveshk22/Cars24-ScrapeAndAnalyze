import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re


# Step 1: Prompt the user for input
brand = input("Enter the brand name (e.g., Toyota): ").strip()
city = input("Enter the city or location (e.g., Mumbai): ").strip()

# Step 2: Update the URL based on the user input
base_url = f'https://www.cars24.com/buy-used-{brand.lower()}-cars-'
city_slug = city.lower().replace(' ', '-')  # Convert city to a URL-friendly slug
cars24_url = f'{base_url}{city_slug}/'

# Step 3: Set up Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode for efficiency
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the page
driver.get(cars24_url)

# Scroll to load dynamic content
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollBy(0, 10000);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get page source after scrolling
page_source = driver.page_source
driver.quit()

# Parse the page with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Step 4: Extract car data
cars_data = []

# Locate the car elements
car_elements = soup.find_all('div', class_='_2YB7p')

for car_element in car_elements:
    # Extract car model and clean it
    car_model_tag = car_element.find('h3', class_='_11dVb')
    if car_model_tag:
        car_model = car_model_tag.text
        year = car_model.split()[0]
        model = ' '.join(car_model.split()[1:]).replace(f'{brand} ', '')
    else:
        year = model = 'Unknown'

    # Extract car details (km run, fuel type, transmission type)
    details_tag = car_element.find('ul', class_='_3J2G-')
    if details_tag:
        details = details_tag.find_all('li')
        km_run = details[0].text.strip() 
        fuel_type = details[2].text.strip() 
        transmission = details[4].text.strip() 
    else:
        km_run = fuel_type = transmission = 'Unknown'

    # Extract car price
    price_tag = car_element.find('strong', class_='_3RL-I')
    price = price_tag.text if price_tag else 'Unknown'

    # Set location based on user input
    location = city

    cars_data.append({
        'Brand': brand,
        'Manufacturing Year': year,
        'Model': model,
        'Kilometers Driven': km_run,
        'Fuel Type': fuel_type,
        'Transmission Type': transmission,
        'Price': price,
        'Location': location
    })

# Create DataFrame
cars24_df = pd.DataFrame(cars_data)

# Function to clean the 'Kilometers Driven' column
def clean_kilometers(km_str):
    str = km_str.replace(' km', '').strip()
    return int(str.replace(',', ''))

# Function to convert 'Price'  to integer format
def convert_price(price_str):
    price_str = price_str.replace('₹', '').replace(' Lakh', '').strip()
    return int(float(price_str.replace(',', '')) * 100)*1000

# Apply cleaning functions to the DataFrame
cars24_df['Kilometers Driven'] = cars24_df['Kilometers Driven'].apply(clean_kilometers)
cars24_df['Price'] = cars24_df['Price'].apply(convert_price)

# Step 5: Save the DataFrame to a CSV file
file_name = f'{brand.lower()}-{city.lower()}.csv'
cars24_df.to_csv(file_name, index=False)

# Display the DataFrame
print(cars24_df)
print(f'Data saved to {file_name}')
