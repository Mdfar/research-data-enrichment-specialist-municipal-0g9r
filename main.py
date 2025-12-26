import pandas as pd from playwright.sync_api import sync_playwright from scraper.enricher import DataEnricher

def main(): # Load source URLs df = pd.read_excel("municipal_list.xlsx") enricher = DataEnricher()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    for index, row in df.iterrows():
        url = row['URL']
        print(f"Processing: {url}")
        
        # Extract data using AI-assisted scraping
        enriched_data = enricher.process_site(browser, url)
        
        # Update DataFrame
        for key, value in enriched_data.items():
            df.at[index, key] = value
            
    df.to_excel("municipal_enriched_final.xlsx", index=False)
    browser.close()


if name == "main": main()