import requests
from bs4 import BeautifulSoup

# Step 1: Choose a website to scrape
url = "https://example.com"

# Step 2: Send a GET request to the website
response = requests.get('https://free-proxy-list.net/en/')

# Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify)