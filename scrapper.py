from bs4 import BeautifulSoup
import requests


def scrape_phone_specs()-> str:
    url = "https://www.vivo.com/in/products/y18"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0; +http://yourdomain.com)"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # return soup.get_text()

    section = soup.find('section', class_='sec-specs-params')

    scrapped_data = ""

    for i in range(12):
        div=section.find('div', class_=f'sec-params-{i}').get_text()
        scrapped_data += div + "\n"
    return scrapped_data

