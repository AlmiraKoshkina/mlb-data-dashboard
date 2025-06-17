import os
import requests

# List of years to scrape
years = list(range(1980, 1991))

# Make sure the data directory exists
os.makedirs("data", exist_ok=True)

for year in years:
    print(f"Scraping year: {year}")
    url = f"https://www.baseball-almanac.com/yearly/yr{year}a.shtml"

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve {year}: {e}")
        continue

    filepath = f"data/page_{year}.html"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Saved {filepath}")

print("Scraping complete.")
