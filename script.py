import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Fetch the webpage content
url = "https://www.nikusteakhouse.com/menu"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status()  # Ensure the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Identify and extract menu sections
menu_sections = soup.find_all('p')
menu_text = " ".join(section.get_text(separator=" ", strip=True) for section in menu_sections)

# Regex pattern to match dish names followed by one or more prices
pattern = re.compile(r'(.+?)\s+(\d+(?:/\d+)?)')
matches = pattern.findall(menu_text)

menu_items = []
for match in matches:
    dish_name = match[0].strip()
    price = match[1].strip()
    menu_items.append({"Dish": dish_name, "Price": price})

# Display the extracted menu items
for item in menu_items:
    print(f"Dish: {item['Dish']}, Price: {item['Price']}")

# Save to CSV
df = pd.DataFrame(menu_items)
df.to_csv("nyc_restaurant_menu.csv", index=False)
