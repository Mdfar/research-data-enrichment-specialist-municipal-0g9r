Municipal Data Enrichment Engine

This tool automates the research task of identifying municipal entity details from a list of URLs.

How it works

Crawler: Uses Playwright to visit the site.

Classifier: Uses OpenAI to identify "Municipal Court", "Utility Billing", and "General Billing" portals.

Validator: Hits the Census Bureau API to verify FIPS codes based on identified City/State.

Output: Generates a standardized Excel file.

Setup

Run pip install -r requirements.txt

Run playwright install

Add your OpenAI API key to scraper/enricher.py

Place your source file as municipal_list.xlsx and run python main.py