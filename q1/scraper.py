import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

search_term = input("Enter search term: ")

encoded_term = quote_plus(search_term)

url = f"https://mdcomputers.in/?route=product%2Fsearch&search={encoded_term}"


response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.select(".product-grid-item")

print("Products found:", len(products))

print(soup.title.text)
