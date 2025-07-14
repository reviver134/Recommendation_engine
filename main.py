import json
import re
from scrapper import scrape_phone_specs
from llm import extract_design_specifications,extract_sim_card_specifications, extract_brand_model_info, extract_network_specifications, extract_mobile_network_technologies,extract_operating_system_info,extract_soc_specifications, extract_storage_specifications, extract_display_specifications,extract_sensor_specifications
from llm import extract_rear_camera_specifications, extract_front_camera_specifications, extract_audio_specifications, extract_radio_specifications,extract_wifi_specifications, extract_bluetooth_specifications, extract_usb_specifications, extract_headphone_jack_specifications,extract_connectivity_specifications
from llm import extract_browser_specifications, extract_audio_file_formats, extract_video_file_formats, extract_battery_specifications, extract_tracking_positioning_specifications
from models.item_model import Design,SIMcard, BrandModel, Network, Mobile_network_technologies_and_bandwidths, OperatingSystem, System_on_chip, Sensors, Storage, Display, Rear_camera, Front_camera, Audio, Radio, Tracking_or_Positioning, Wi_Fi, Bluetooth, USB, Headphone_jack, Connectivity, Browser, Audio_file_formats, Video_file_formats, Battery
import asyncio
'''returns a string contained inside {} brackets'''

import regex  # instead of re
import json

def extract_json_block(text: str) -> str:
    match = regex.search(r'\{(?:[^{}]|(?R))*\}', text, regex.DOTALL)
    if not match:
        return None
    return match.group(0)

import re
import json

def clean_trailing_commas(json_string: str) -> str:
    # Remove trailing commas in objects
    json_string = re.sub(r',\s*([\]}])', r'\1', json_string)
    return json_string

async def extract_json_block_async(raw_str):
    try:
        clean_json_str = extract_json_block(raw_str)
        if clean_json_str is None:
            return None
        clean_json_str = clean_trailing_commas(clean_json_str)
        parsed = json.loads(clean_json_str)
        return parsed
    except Exception as e:
        print(f"Error parsing JSON block: {e}")
        return None


async def main():
    scrapped_data = scrape_phone_specs() # This function return the text data extracted from the website

    raw_str=extract_brand_model_info(scrapped_data)
    extractor=(await extract_json_block_async(raw_str))
    brand_model = BrandModel(**extractor) if extractor else None

    raw_str1 = extract_design_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str1)
    design_obj = Design(**extractor) if extractor else None

    raw_str2=extract_sim_card_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str2)
    sim_model= SIMcard(**extractor) if extractor else None

    raw_str3=extract_network_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str3)
    network_model = Network(**extractor) if extractor else None

    raw_str4=extract_mobile_network_technologies(scrapped_data)
    extractor = await extract_json_block_async(raw_str4)
    bandwidths_model = Mobile_network_technologies_and_bandwidths(**extractor) if extractor else None

    raw_str5 = extract_operating_system_info(scrapped_data)
    extractor = await extract_json_block_async(raw_str5)
    os_model = OperatingSystem(**extractor) if extractor else None

    raw_str6=extract_soc_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str6)
    soc_model = System_on_chip(**extractor) if extractor else None

    raw_str7 = extract_storage_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str7)
    storage_model = Storage(**extractor) if extractor else None

    raw_str8 = extract_display_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str8)
    display_model = Display(**extractor) if extractor else None

    raw_str9=extract_sensor_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str9)
    sensors_model = Sensors(**extractor) if extractor else None

    raw_str10 = extract_rear_camera_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str10)
    rear_camera_model = Rear_camera(**extractor) if extractor else None

    raw_str11 = extract_front_camera_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str11)
    front_camera_model = Front_camera(**extractor) if extractor else None

    raw_str12 = extract_audio_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str12)
    audio_model = Audio(**extractor) if extractor else None

    raw_str13=extract_radio_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str13)
    radio_model = Radio(**extractor) if extractor else None

    raw_str14 = extract_tracking_positioning_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str14)
    tracking_model = Tracking_or_Positioning(**extractor) if extractor else None

    raw_str15 = extract_wifi_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str15)
    wifi_model = Wi_Fi(**extractor) if extractor else None

    raw_str16 = extract_bluetooth_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str16)
    bluetooth_model = Bluetooth(**extractor) if extractor else None

    raw_str17 = extract_usb_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str17)
    usb_model = USB(**extractor) if extractor else None

    raw_str18 = extract_headphone_jack_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str18)
    headphone_jack_model = Headphone_jack(**extractor) if extractor else None

    raw_str19 = extract_connectivity_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str19)
    connectivity_model = Connectivity(**extractor) if extractor else None

    raw_str20 = extract_browser_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str20)
    browser_model = Browser(**extractor) if extractor else None

    raw_str21 = extract_audio_file_formats(scrapped_data)
    extractor = await extract_json_block_async(raw_str21)
    audio_formats_model = Audio_file_formats(**extractor) if extractor else None


    raw_str22 = extract_video_file_formats(scrapped_data)
    extractor = await extract_json_block_async(raw_str22)
    video_formats_model = Video_file_formats(**extractor) if extractor else None

    raw_str23 = extract_battery_specifications(scrapped_data)
    extractor = await extract_json_block_async(raw_str23)
    battery_model = Battery(**extractor) if extractor else None

    return {"brand_model": brand_model,"design": design_obj,
        "sim_card": sim_model,
        "network": network_model,
        "mobile_network_technologies_and_bandwidths": bandwidths_model,
        "operating_system": os_model,
        "system_on_chip": soc_model,
        "storage": storage_model,
        "display": display_model,
        "sensors": sensors_model,
        "rear_camera": rear_camera_model,
        "front_camera": front_camera_model,
        "audio": audio_model,
        "radio": radio_model,
        "tracking_or_positioning": tracking_model,
        "wi_fi": wifi_model,
        "bluetooth": bluetooth_model,
        "usb": usb_model,
        "headphone_jack": headphone_jack_model,
        "connectivity": connectivity_model,
        "browser": browser_model,
        "audio_file_formats": audio_formats_model,
        "video_file_formats": video_formats_model,
        "battery": battery_model
    }



design_data = asyncio.run(main())
for key, value in design_data.items():
    print(f"{key}:\n{value}\n")
