import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


search_term = input("Enter search term: ")

encoded_term = quote_plus(search_term)

url = f"https://mdcomputers.in/?route=product%2Fsearch&search={encoded_term}"

response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

products = soup.select(".product-grid-item")

print("Products found:", len(products))

for product in products:
    name = product.select_one(".product-entities-title a").get_text(strip=True)
    url = product.select_one(".product-image-link")["href"]
    price = product.select_one(".price .ins .amount").get_text(strip=True)

    print("Name:", name)
    print("Price:", price)
    print("URL:", url)
    print()