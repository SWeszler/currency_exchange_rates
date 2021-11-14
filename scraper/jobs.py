from bs4 import BeautifulSoup
from exchange_rates.celery import app
from rates.models import Rate
import re
import requests
from time import sleep

BASE_URL = 'https://www.ecb.europa.eu'
CRAWL_DELAY = 0.5

@app.task
def scrape_exchange_rates():
    """
    Scraping the exchange rate RSS feed urls from ECB website.
    """

    url = f'{BASE_URL}/home/html/rss.en.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('a', href=re.compile(r'/rss/fxref-[a-z]{3}.html')):
        xml_url = f"{BASE_URL}{link.attrs['href']}"
        print(f"Processing RSS link: {xml_url}")
        get_exchange_rates_from_xml(xml_url)
        sleep(CRAWL_DELAY)



def get_exchange_rates_from_xml(url):
    """
    Parsing the XML file and saving the data to the database.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    for item in items:
        rate = {
            'date': item.find('dc:date').text,
            'rate': item.find('cb:value').text,
            'currency': item.find('cb:targetCurrency').text 
        }
        msg = f"Adding new exchange rate for {rate['currency']}. "
        try:
            rate, crated = Rate.objects.get_or_create(**rate)
            if crated:
                msg += "Success!"
            else:
                msg += "Already exists."
        except Exception as e:
            msg = f'ERROR: Cannot save the rate in the database. Message: {e}'
            
        print(msg)

