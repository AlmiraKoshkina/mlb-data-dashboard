from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Headless browser settings (run without opening a browser window)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Automatically install and configure ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Create a directory for CSV output if it doesn't exist
os.makedirs("data", exist_ok=True)

# Years to scrape
years = range(1980, 1991)

for year in years:
    print(f"Scraping {year}...")
    url = f"https://www.baseball-almanac.com/yearly/yr{year}.htm"
    driver.get(url)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    content_cell = soup.find("td", class_="content")
    if not content_cell:
        print(f"No content found for {year}")
        continue

    paragraphs = content_cell.find_all("p")
    data = []

    for p in paragraphs:
        text = p.get_text(strip=True)
        if text and not text.startswith("The information"):
            data.append({"year": year, "event": text})

    if data:
        df = pd.DataFrame(data)
        df.to_csv(f"data/events_{year}.csv", index=False)
        print(f"Saved {len(df)} events for {year}")

driver.quit()
print("Scraping completed.")
