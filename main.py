from bs4 import BeautifulSoup
import requests
from models.item_model import (
    BrandModel, Design, SIMcard, Network,
    Mobile_network_technologies_and_bandwidths, OperatingSystem,
    System_on_chip, Sensors, Storage, Display, Rear_camera, Front_camera,
    Audio, Radio, Tracking_or_Positioning, Wi_Fi, Bluetooth, USB,
    Headphone_jack, Connectivity, Browser, Audio_file_formats,
    Video_file_formats, Battery
)
phone_specs = [BrandModel, Design, SIMcard, Network,
    Mobile_network_technologies_and_bandwidths, OperatingSystem,
    System_on_chip, Sensors, Storage, Display, Rear_camera,
    Front_camera, Audio, Radio, Tracking_or_Positioning, Wi_Fi,
    Bluetooth, USB, Headphone_jack, Connectivity, Browser,
    Audio_file_formats, Video_file_formats, Battery]
url = "https://www.realme.com/global/realme-gt-7-5g/specs"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0; +http://yourdomain.com)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

section = soup.find('section', class_='sec-specs-params')

all_classes = set()
scrapped_data = {}
def parse_raw_text_to_dict(div: str) -> dict:
        lines=[line.strip() for line in div.text.split('\n') if line.strip()]
        for line in lines:
            if ':' in line:
                key,value=line.split(':', 1)
                scrapped_data[key.strip()]=value.strip()
            elif ': ' in line:
                key, value = line.split(': ', 1)
                scrapped_data[key.strip()] = value.strip()
            else:
                scrapped_data.setdefault('Features', []).append(line.strip())
for i in range(12):
    div=section.find('div', class_=f'sec-params-{i}')
    parse_raw_text_to_dict(div)

for val in phone_specs:
    ans=val(**scrapped_data)
    print(ans.model_dump())