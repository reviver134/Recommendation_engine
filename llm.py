from models.item_model import (
    BrandModel, Design, SIMcard, Network,
    Mobile_network_technologies_and_bandwidths, OperatingSystem,
    System_on_chip, Sensors, Storage, Display, Rear_camera, Front_camera,
    Audio, Radio, Tracking_or_Positioning, Wi_Fi, Bluetooth, USB,
    Headphone_jack, Connectivity, Browser, Audio_file_formats,
    Video_file_formats, Battery
)
from main import scrapped_data 

# Instantiate each submodel and dump to flat dict
models = [
    BrandModel(), Design(), SIMcard(), Network(),
    Mobile_network_technologies_and_bandwidths(), OperatingSystem(),
    System_on_chip(), Sensors(), Storage(), Display(), Rear_camera(),
    Front_camera(), Audio(), Radio(), Tracking_or_Positioning(), Wi_Fi(),
    Bluetooth(), USB(), Headphone_jack(), Connectivity(), Browser(),
    Audio_file_formats(), Video_file_formats(), Battery()
]
from pymongo import MongoClient
# Merge all dumped dicts into a single flat schema
flattened_schema = {}
for model in models:
    flattened_schema.update(model.model_dump())


llm_prompt = f"""
You are a mobile phone spec parser.

The following JSON structure represents the expected format for phone specs.
Fill this structure with appropriate values based on the raw text provided below.

JSON structure (keys with None mean missing value):
{flattened_schema}

Raw phone spec text:
\"\"\"
{scrapped_data}
\"\"\"

Respond only with the updated JSON object.
Only return a clean, structured JSON object. Do not explain anything.
"""

import json
import subprocess


# Convert the PhoneSpecs object to a JSON dict

json_data =scrapped_data

# Create a detailed prompt
prompt = f"""
You are a JSON assistant.

Given the JSON schema below and raw phone spec text, fill the schema values accurately from the spec.

Respond ONLY with valid JSON. No explanations, no extra text.

JSON schema:
{json.dumps(flattened_schema, indent=2)}

Raw phone spec text:
\"\"\"
{scrapped_data}
\"\"\"
"""

# Run the prompt with Ollama + LLaMA 2
# Run the prompt with Ollama + LLaMA 2
process = subprocess.run(
    ["ollama", "run", "llama2"],
    input=llm_prompt.encode("utf-8"),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

raw_output = process.stdout.decode("utf-8")
print("LLM RAW OUTPUT:\n", raw_output)

# --- Step 3: Extract only valid JSON ---
def extract_json(text):
    brace_count = 0
    start = None
    for i, char in enumerate(text):
        if char == '{':
            if brace_count == 0:
                start = i
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0 and start is not None:
                try:
                    return json.loads(text[start:i+1])
                except json.JSONDecodeError:
                    continue
    raise ValueError("No valid JSON object found in text.")


# ✅ FIXED: Assign cleaned_data from LLM output
cleaned_data = extract_json(raw_output)

# --- Step 4: Insert into MongoDB ---
client = MongoClient("mongodb://localhost:27017")
db = client["mobiledb"]
collection = db["phones"]

insert_result = collection.insert_one(cleaned_data)
print(f"✅ Inserted into MongoDB with ID: {insert_result.inserted_id}")
