import requests
from bs4 import BeautifulSoup


url = "https://mdcomputers.in/?route=product%2Fsearch&search=external+hard+drive"

response = requests.get(url)

print(response.status_code)
print(response.text[:500])