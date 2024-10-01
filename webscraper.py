import requests
from bs4 import BeautifulSoup

def scrape_tsx_spodumene(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        
        found_results = soup.find_all('div', class_='layoutStyling__BodyContainer-sc-1im3qdr-0 fPrxRm')  
        found_companies = []

        for container in found_results:
            name = container.find('div', class_='companyname')
            description = container.find('div', class_='queryly_item_description')
            title = container.find('div', class_='queryly_item_title')

           
            name_text = name.get_text(strip=True) if name else 'N/A'
            title_text = title.get_text(strip=True) if title else 'N/A'
            description_text = description.get_text(strip=True) if description else 'N/A'
            
            
            if 'spodumene' in title_text.lower() or 'pegmatite' in title_text.lower():
                found_companies.append((name_text, title_text, description_text))

        if found_companies:
            print("Companies related to Spodumene Pegmatite:")
            for name, title, desc in found_companies:
                print(f"Company: {name}, Title: {title}, Description: {desc}")
        else:
            print("No companies found related to Spodumene Pegmatite.")
    else:
        print(f"Failed to retrieve data: {response.status_code}")


tsx_url = 'https://money.tmx.com/search?query=lithium'
scrape_tsx_spodumene(tsx_url)