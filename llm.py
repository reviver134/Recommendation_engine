import ollama

def extract_design_specifications(raw_specs):

    
    response = ollama.chat(
        model='llama2',
        messages = [
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone design specifications. '
                    'give nothing but whats mentioned in the formate provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "width": "...",\n'
                    '  "height": "...",\n'
                    '  "thickness": "...",\n'
                    '  "weight": "...",\n'
                    '  "Volume": "...",\n'
                    '  "color": ["..."],\n'
                    '  "body_material": "...",\n'
                    '  "certification": ["..."]\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "width": "76.13mm",\n'
                    '  "height": "162.42mm",\n'
                    '  "thickness": "8.73mm",\n'
                    '  "weight": "211g",\n'
                    '  "Volume": null,\n'
                    '  "color": ["Dream White", "Astro Black"],\n'
                    '  "body_material": "Glass front, metal frame",\n'
                    '  "certification": ["IP68"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': (raw_specs),
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip()  # Return the extracted design specifications as a string

def extract_sim_card_specifications(raw_specs):

    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone SIM card specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "SIM_card_type": "...",\n'
                    '  "Number_of_SIM_cards": "...",\n'
                    '  "Features": ["..."]\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "SIM_card_type": "Nano-SIM/eSIM",\n'
                    '  "Number_of_SIM_cards": "Dual SIM",\n'
                    '  "Features": ["Dual Standby", "5G supported"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_brand_model_info(raw_specs):
    
        response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone branding details. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "brand": "...",\n'
                    '  "model": "...",\n'
                    '  "model_alias": "..."\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "brand": "realme",\n'
                    '  "model": "GT 7 Pro",\n'
                    '  "model_alias": "RMX3880"\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
        llm_output = response['message']['content']
        return llm_output.strip() 


def extract_network_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone network specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If a field contains multiple values, return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "GSM": "... or [ ... ]",\n'
                    '  "W_CDMA": "... or [ ... ]",\n'
                    '  "LTE": "... or [ ... ]",\n'
                    '  "five_G_NR": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "GSM": ["850", "900", "1800", "1900"],\n'
                    '  "W_CDMA": "2100",\n'
                    '  "LTE": ["1", "3", "5", "8", "20"],\n'
                    '  "five_G_NR": ["n1", "n78", "n41"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_mobile_network_technologies(raw_specs):
   
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone mobile network technologies and bandwidths. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple values are present, return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Mobile_network_technologies": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Mobile_network_technologies": ["GSM", "WCDMA", "LTE", "5G"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_operating_system_info(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone software details. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "OS": "...",\n'
                    '  "UI": "..."\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "OS": "Android 15",\n'
                    '  "UI": "realme UI 6.0"\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_soc_specifications(raw_specs):
    import ollama

    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone SoC (System on Chip) and memory specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple values are present, return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "SoC": "...",\n'
                    '  "Process_technology": "...",\n'
                    '  "CPU": "... or [ ... ]",\n'
                    '  "CPU_bits": "...",\n'
                    '  "Instruction_set": "...",\n'
                    '  "CPU_cores": "...",\n'
                    '  "CPU_frequency": "...",\n'
                    '  "GPU": "...",\n'
                    '  "GPU_cores": "...",\n'
                    '  "RAM_capacity": "... or [ ... ]",\n'
                    '  "RAM_type": "...",\n'
                    '  "RAM_channels": "...",\n'
                    '  "RAM_frequency": "..."\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "SoC": "MediaTek Dimensity 9400e",\n'
                    '  "Process_technology": "4nm",\n'
                    '  "CPU": ["1x Cortex-X4 @ 3.4GHz", "3x Cortex-A720 @ 3.1GHz", "4x Cortex-A520 @ 2.0GHz"],\n'
                    '  "CPU_bits": "64-bit",\n'
                    '  "Instruction_set": "ARMv9",\n'
                    '  "CPU_cores": "8",\n'
                    '  "CPU_frequency": "3.4GHz",\n'
                    '  "GPU": "Immortalis-G720",\n'
                    '  "GPU_cores": "10",\n'
                    '  "RAM_capacity": ["8GB", "12GB", "16GB"],\n'
                    '  "RAM_type": "LPDDR5X",\n'
                    '  "RAM_channels": "4",\n'
                    '  "RAM_frequency": "8533MHz"\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs
            }
        ]
    )
    
    return response['message']['content'].strip()


def extract_storage_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone internal storage specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple values are present, return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Storage": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Storage": ["128GB", "256GB", "512GB"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_display_specifications(raw_specs):
   
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone display specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple values are present, return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Type_or_Technology": "...",\n'
                    '  "Diagonal_size": "... or [ ... ]",\n'
                    '  "Width": "...",\n'
                    '  "Height": "...",\n'
                    '  "Aspect_ratio": "...",\n'
                    '  "Resolution": "...",\n'
                    '  "Pixel_density": "...",\n'
                    '  "Color_depth": [ ... ],\n'
                    '  "Display_area": "...",\n'
                    '  "other_features": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Type_or_Technology": "AMOLED",\n'
                    '  "Diagonal_size": "6.78 inches",\n'
                    '  "Width": "69.9 mm",\n'
                    '  "Height": "150.9 mm",\n'
                    '  "Aspect_ratio": "20:9",\n'
                    '  "Resolution": "2780 x 1264 pixels",\n'
                    '  "Pixel_density": "450 ppi",\n'
                    '  "Color_depth": ["10-bit", "1.07B colors"],\n'
                    '  "Display_area": "90.8%",\n'
                    '  "other_features": ["HDR10+", "144Hz refresh rate", "6000 nits peak brightness"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_sensor_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone sensor specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple sensors are present, return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Sensors": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Sensors": ["Accelerometer", "Gyroscope", "Proximity sensor", "Compass", "In-display fingerprint sensor"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_rear_camera_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting rear camera specifications from smartphone spec sheets. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple features are present, return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Sensor_model": "...",\n'
                    '  "Sensor_type": "...",\n'
                    '  "Sensor_format": "...",\n'
                    '  "Aperture": "...",\n'
                    '  "Focal_length_in_35mm_equivalent": "...",\n'
                    '  "Field_of_view": "...",\n'
                    '  "Number_of_lenses": "...",\n'
                    '  "Flash_type": "...",\n'
                    '  "image_resolution": "...",\n'
                    '  "Video_resolution": "...",\n'
                    '  "Video_FPS": "...",\n'
                    '  "Features": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Sensor_model": "Sony IMX906",\n'
                    '  "Sensor_type": "Exmor-RS CMOS",\n'
                    '  "Sensor_format": "1/1.56\"",\n'
                    '  "Aperture": "f/1.69",\n'
                    '  "Focal_length_in_35mm_equivalent": "26mm",\n'
                    '  "Field_of_view": "84°",\n'
                    '  "Number_of_lenses": "6-element lens",\n'
                    '  "Flash_type": "Dual-LED flash",\n'
                    '  "image_resolution": "50 MP",\n'
                    '  "Video_resolution": "4K (3840x2160)",\n'
                    '  "Video_FPS": "60 fps",\n'
                    '  "Features": ["OIS", "EIS", "HDR", "Night mode", "AI Scene Detection"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_front_camera_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting front (selfie) camera specifications from smartphone spec sheets. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple values are present in "Features", return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Sensor_model": "...",\n'
                    '  "Sensor_type": "...",\n'
                    '  "Sensory_format": "...",\n'
                    '  "Aperture": "...",\n'
                    '  "Focal_length_in_35mm_equivalent": "...",\n'
                    '  "Field_of_view": "...",\n'
                    '  "Number_of_lenses": "...",\n'
                    '  "Flash_type": "...",\n'
                    '  "image_resolution": "...",\n'
                    '  "Video_resolution": "...",\n'
                    '  "Video_FPS": "...",\n'
                    '  "Features": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Sensor_model": "Sony IMX615",\n'
                    '  "Sensor_type": "CMOS",\n'
                    '  "Sensory_format": "1/2.74\"",\n'
                    '  "Aperture": "f/2.4",\n'
                    '  "Focal_length_in_35mm_equivalent": "24mm",\n'
                    '  "Field_of_view": "80°",\n'
                    '  "Number_of_lenses": "5-element lens",\n'
                    '  "Flash_type": "Screen flash",\n'
                    '  "image_resolution": "32 MP",\n'
                    '  "Video_resolution": "1080p (1920x1080)",\n'
                    '  "Video_FPS": "30 fps",\n'
                    '  "Features": ["HDR", "Portrait mode", "Face unlock"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_audio_specifications(raw_specs):
   
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone audio specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple values are present in any field, return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Speaker": "... or [ ... ]",\n'
                    '  "Other_features": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Speaker": ["Stereo speakers", "Bottom-firing speaker"],\n'
                    '  "Other_features": ["Hi-Res Audio", "Dolby Atmos", "3.5mm audio jack"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_radio_specifications(raw_specs):
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone specifications related to radio features. '
                    'Provide only a valid JSON output in the following format:\n\n'
                    '{\n'
                    '  "FM_radio": "Yes" or "No" or null\n'
                    '}\n\n'
                    'Return only this JSON. If FM radio info is missing, set the value to null. No explanation or extra text.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip()
 

def extract_tracking_positioning_specifications(raw_specs):
   
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone tracking and positioning features. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'Use `true` if a satellite system is supported, `false` if it is clearly not supported, and `null` if not mentioned. '
                    'If multiple features are present in "Other_features", return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "GPS": true/false/null,\n'
                    '  "GLONASS": true/false/null,\n'
                    '  "BeiDou": true/false/null,\n'
                    '  "Galileo": true/false/null,\n'
                    '  "Other_features": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "GPS": true,\n'
                    '  "GLONASS": true,\n'
                    '  "BeiDou": true,\n'
                    '  "Galileo": null,\n'
                    '  "Other_features": ["QZSS", "NavIC", "A-GPS"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_wifi_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting Wi-Fi specifications from smartphone spec sheets. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If multiple versions or features are present, return them as a list of strings. If no value is found, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Wi_Fi": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Wi_Fi": ["Wi-Fi 802.11 a/b/g/n/ac/ax", "Dual-band", "Wi-Fi 6E", "Wi-Fi Direct", "Hotspot"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_bluetooth_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting Bluetooth specifications from smartphone spec sheets. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple features are present in "Features", return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Version": "...",\n'
                    '  "Features": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Version": "5.3",\n'
                    '  "Features": ["A2DP", "LE", "aptX HD"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_usb_specifications(raw_specs):
   
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone USB specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple features are present in "Features", return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Version": "...",\n'
                    '  "Features": "... or [ ... ]",\n'
                    '  "Connector_type": "..." \n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Version": "USB Type-C 3.2",\n'
                    '  "Features": ["OTG", "Charging", "Data transfer", "DisplayPort"],\n'
                    '  "Connector_type": "USB Type-C"\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_headphone_jack_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone headphone jack specifications. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If a value is missing, return null. If multiple features are present in "Features", return them as a list of strings.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Headphone_jack": "...",\n'
                    '  "Features": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Headphone_jack": "3.5mm",\n'
                    '  "Features": ["Hi-Res Audio", "Dedicated DAC"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_connectivity_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone connectivity and synchronization features. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If multiple connectivity options are present, return them as a list of strings. '
                    'If none are found, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "connectivity": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "connectivity": ["computer sync", "OTA sync", "infrared", "tethering", "NFC", "voLTE"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_browser_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone browser support details. '
                    'Give nothing but what is mentioned in the format provided below.\n\n'
                    'The user will provide raw specifications. Extract only the data relevant to the following JSON format. '
                    'If multiple browsers are listed, return them as a list of strings. If nothing is found, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Browser": "... or [ ... ]"\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Browser": ["HTML5", "Chrome", "WebKit", "Opera"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_audio_file_formats(raw_specs):
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting supported audio file formats from smartphone specifications. '
                    'Return only what is mentioned in the format below.\n\n'
                    'The user will provide raw specifications. Extract only the audio file formats mentioned and output them as a list of strings. '
                    'Preserve the exact casing and naming if provided. If nothing relevant is found, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Audio_file_formats": [ ... ]\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Audio_file_formats": [\n'
                    '    "AMR", "AMR-NB", "AMR-WB", "aptX", "aptX HD", "aptX Lossless",\n'
                    '    "eAAC+", "HE-AAC v2", "FLAC", "MIDI", "MP3", "OGG",\n'
                    '    "WMA", "WAV", "LDAC"\n'
                    '  ]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 


def extract_video_file_formats(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting supported video file formats from smartphone specifications. '
                    'Return only what is mentioned in the format below.\n\n'
                    'The user will provide raw specifications. Extract only the supported video file formats and return them as a list of strings. '
                    'Preserve the exact casing and naming if provided. If nothing relevant is found, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Video_file_formats": [ ... ]\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Video_file_formats": [\n'
                    '    "3GPP", "AVI", "DivX", "Flash Video", "H.263", "H.264", "MKV", "MP4",\n'
                    '    "WebM", "WMV", "Xvid"\n'
                    '  ]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 

def extract_battery_specifications(raw_specs):
    
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'system',
                'content': (
                    'You are an expert at extracting smartphone battery specifications. '
                    'Return only what is mentioned in the format below.\n\n'
                    'The user will provide raw specifications. Extract only the relevant values and return them in the following JSON format. '
                    'If a field is not mentioned, return null.\n\n'

                    'Format:\n'
                    '{\n'
                    '  "Battery_capacity": "...",\n'
                    '  "Battery_type": "...",\n'
                    '  "Charging_power": "...",\n'
                    '  "Charging_time": "...",\n'
                    '  "Features": ["..."]\n'
                    '}\n\n'

                    'Example:\n'
                    '{\n'
                    '  "Battery_capacity": "7200 mAh",\n'
                    '  "Battery_type": "Li-Polymer",\n'
                    '  "Charging_power": "10V / 10A",\n'
                    '  "Charging_time": null,\n'
                    '  "Features": ["Fast charging", "Non-removable", "Silicon/Carbon (Si/C) anode", "841 Wh/L"]\n'
                    '}\n\n'

                    'Only respond with the final JSON, no explanation and no notes also.'
                )
            },
            {
                'role': 'user',
                'content': raw_specs,
            }
        ]
    )
    llm_output = response['message']['content']
    return llm_output.strip() 
