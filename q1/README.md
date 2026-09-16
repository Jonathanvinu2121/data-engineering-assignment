# Q1 - MD Computers Product Scraper

## Overview

This program accepts a search term from the user, fetches the corresponding search results from MD Computers, and extracts the listed product name, price, and product URL.

## Requirements

- Python 3
- requests
- beautifulsoup4

## Installation

From the project root, install the dependencies with:

```bash
pip install -r q1/requirements.txt
```

## Usage

Run the scraper with:

```bash
python q1/scraper.py
```

Enter a product search term when prompted.

Example:

```text
Enter search term: external hard drive
```

The program displays the number of products found and the name, price, and URL of each product.

## Design Choices

### Search URL construction

The search term is URL-encoded using `quote_plus()` so that spaces and special characters can be handled correctly.

### HTML parsing

BeautifulSoup is used to parse the returned HTML. CSS selectors are used to locate product cards and their corresponding product information.

### Modular structure

The program separates its responsibilities into functions for:

- Building the search URL
- Fetching the search results page
- Extracting product information
- Handling user interaction and output

### Error handling

The HTTP request uses a 10-second timeout and `raise_for_status()` to detect HTTP errors.

The program also handles:

- Empty search terms
- Failed HTTP requests
- Missing product fields
- Searches with no products

## Assumptions

The scraper relies on the current HTML structure of the MD Computers search results page, including the CSS selectors used to identify product cards, names, prices, and URLs.

If the website changes its HTML structure, the selectors may need to be updated.

## Output

For each product, the program displays:

- Product name
- Price
- Product URL
