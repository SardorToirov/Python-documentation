import requests
from bs4 import BeautifulSoup

# Fetch the page content
try:
    r = requests.get("https://kun.uz/news/main")
    r.raise_for_status()  # Raises an error if the request was unsuccessful
except requests.exceptions.RequestException as e:
    print(f"Error occurred while fetching the webpage: {e}")
    exit()

# Parse the HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Find all news titles
news = soup.find_all(class_="news-title")

# Ensure there are enough news items
if len(news) < 10:
    print("Not enough news items found.")
    exit()

# Print the news titles
print("\n\tushbu ma'lumotlar: https://kun.uz/news/main web saytadan olinmoqda:) \n")
j = 1
while j < 10:
    # Clean up the news text and remove any leading/trailing whitespace
    print(f"{j}. {news[j].text.strip()}")
    j += 1

