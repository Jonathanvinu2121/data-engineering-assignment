import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def build_search_url(search_term):
    encoded_term = quote_plus(search_term)
    return f"https://mdcomputers.in/?route=product%2Fsearch&search={encoded_term}"


def fetch_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def extract_products(html):
    soup = BeautifulSoup(html, "html.parser")

    products = soup.select(".product-grid-item")

    results = []

    for product in products:
        name_element = product.select_one(".product-entities-title a")
        price_element = product.select_one(".price .ins .amount")
        url_element = product.select_one(".product-image-link")

        if not name_element or not price_element or not url_element:
            continue

        name = name_element.get_text(strip=True)
        price = price_element.get_text(strip=True)
        url = url_element["href"]

        results.append({
            "name": name,
            "price": price,
            "url": url
        })

    return results


def main():
    search_term = input("Enter search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    url = build_search_url(search_term)

    try:
        html = fetch_page(url)
    except requests.RequestException as exc:
        print(f"Failed to fetch search results: {exc}")
        return

    products = extract_products(html)

    if not products:
        print("No products found.")
        return

    print("Products found:", len(products))

    for product in products:
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("URL:", product["url"])
        print()


if __name__ == "__main__":
    main()