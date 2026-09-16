# Q3 - Company CSV Processing Script

## Overview

This program accepts a CSV URL, downloads the CSV file, and extracts the company name, headquarters location, and founding year for each company.

The results are sorted by founding year in ascending order.

## Requirements

- Bash
- curl
- awk
- sort

These tools are available in Git Bash on Windows and standard Unix-like systems.

## Usage

Run the script with:

```bash
bash companies.sh "<CSV_URL>"
```

Example:

```bash
bash companies.sh "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/refs/heads/main/data/constituents.csv"
```

The program downloads the CSV and prints the results in the following format:

```text
Company | Location | Founded
```

Example:

```text
BNY Mellon | New York City, New York | 1784
State Street Corporation | Boston, Massachusetts | 1792
Colgate-Palmolive | New York City, New York | 1806
```

## Design Choices

### Dynamic Input

The CSV URL is provided as a command-line argument, so the script can work with different CSV sources without modifying the code.

### CSV Parsing

`awk` with `FPAT` is used to correctly handle fields containing quoted commas, such as company names and locations.

### Sorting

The founding year is temporarily placed first so that `sort -n` can sort the records numerically by founding year. The output is then formatted into the required order.

### Error Handling

The script checks that exactly one CSV URL is provided and verifies that the CSV download is successful.

### Assumptions

The script expects the CSV to contain the required company, location, and founding year fields in the expected column structure.

For founding-year values containing additional information, the first four-digit year is used.

## Output

For each company, the program displays:

- Company name
- Headquarters location
- Founding year
