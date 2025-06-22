MLB INTERACTIVE STATS VISUALIZER

This is an interactive web application built with Streamlit that visualizes historical MLB statistics from 1980 to 1990. It allows users to explore and analyze key player performance metrics by team, year, and statistical category.

FEATURES

Interactive bar charts of top players by statistic

Filter by year (1980–1990)

Filter by team and player

Powered by SQLite database (mlb.db)

Deployed live on Streamlit Cloud

LIVE APP

mlb-stats-visualizer.streamlit.app

TECH STACK

Python

Streamlit

Pandas

Plotly

SQLite

(Optional) Selenium, BeautifulSoup for scraping

DATA SOURCES

Baseball Almanac – statistical data used in the dashboard was extracted via scraping from this site using custom Python scripts.

PROJECT STRUCTURE

mlb-data-dashboard/
├── app.py # Main Streamlit app
├── data/
│ ├── mlb.db # SQLite database with 'events' table
│ └── check_db.py # Utility to inspect DB contents
├── import_to_db.py # Script to populate the database
├── scraper.py # Web scraper (Selenium + BeautifulSoup)
├── requirements.txt # App dependencies
└── README.md # Project info

HOW TO RUN LOCALLY

Clone this repo:

git clone https://github.com/AlmiraKoshkina/mlb-data-dashboard.git
cd mlb-data-dashboard

CREATE AND ACTIVATE A VIRTUAL ENVIROMENT:

python -m venv venv
venv\Scripts\activate # On Windows

INSTALL DEPENDENCIES:

pip install -r requirements.txt

LAUNCH THE APP:

streamlit run app.py

DEPLOYMENT

The app is deployed on Streamlit Cloud, configured to automatically pull from the GitHub repository.

AUTHOR

Almira Koshkina
