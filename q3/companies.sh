#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <CSV_URL>"
    exit 1
fi

CSV_URL="$1"
CSV_FILE="companies.csv"

if ! curl -L --fail --silent --show-error "$CSV_URL" -o "$CSV_FILE"; then
    echo "Error: Failed to download CSV."
    exit 1
fi

echo "Company | Location | Founded"

awk '
BEGIN {
    FPAT = "([^,]+)|(\"([^\"]|\"\")*\")"
}

NR > 1 {
    company = $2
    location = $5
    founded = $8

    gsub(/^"|"$/, "", company)
    gsub(/^"|"$/, "", location)

    match(founded, /[0-9]{4}/, year)

    if (year[0] != "") {
        print year[0] "\t" company "\t" location
    }
}
' "$CSV_FILE" |
sort -n -k1,1 |
awk -F'\t' '{print $2 " | " $3 " | " $1}'