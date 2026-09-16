import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def build_search_url(search_term):
    encoded_term = quote_plus(search_term)
    return f"https://mdcomputers.in/?route=product%2Fsearch&search={encoded_term}"


def fetch_page(url):
    response = requests.get(url)
    return response.text


def extract_products(html):
    soup = BeautifulSoup(html, "html.parser")

    products = soup.select(".product-grid-item")

    results = []

    for product in products:
        name = product.select_one(
            ".product-entities-title a"
        ).get_text(strip=True)

        url = product.select_one(
            ".product-image-link"
        )["href"]

        price = product.select_one(
            ".price .ins .amount"
        ).get_text(strip=True)

        results.append({
            "name": name,
            "price": price,
            "url": url
        })

    return results


def main():
    search_term = input("Enter search term: ")

    url = build_search_url(search_term)

    html = fetch_page(url)

    products = extract_products(html)

    print("Products found:", len(products))

    for product in products:
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("URL:", product["url"])
        print()


if __name__ == "__main__":
    main()