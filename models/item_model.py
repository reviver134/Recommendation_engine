from pydantic import BaseModel
from typing import List,Optional
from typing import Union

class BrandModel(BaseModel):
    brand:Optional[str] = None
    model:Optional[str] = None
    model_alias:Optional[str] = None

class Design(BaseModel):
    width: Optional[str] = None
    height: Optional[str] = None  
    thickness: Optional[str] = None
    weight: Optional[str] = None
    Volume: Optional[str] = None
    color: Union[str, List[str]] = None
    body_material: Optional[str] = None
    certification: Union[str, List[str]] = None

class SIMcard(BaseModel):
    SIM_card_type:Optional[str] = None
    Number_of_SIM_cards:Optional[str] = None
    Features:Union[str, List[str]] = None

class Network(BaseModel):
    GSM: Union[str, List[str]] = None
    W_CDMA: Union[str, List[str]] = None
    LTE:Union[str, List[str]]= None
    five_G_NR: Union[str, List[str]]= None

class Mobile_network_technologies_and_bandwidths(BaseModel):
    Mobile_network_technologies: Union[str, List[str]] = None

class OperatingSystem(BaseModel):
    OS: Optional[str] = None
    UI: Optional[str] = None

class System_on_chip(BaseModel):
    SoC: Optional[str] = None
    Process_technology: Optional[str] = None
    CPU: Union[str, List[str]] = None
    CPU_bits: Optional[str] = None
    Instruction_set: Optional[str] = None
    CPU_cores: Optional[str] = None
    CPU_frequency: Optional[str] = None
    GPU: Optional[str] = None
    GPU_cores: Optional[str] = None
    RAM_capacity:Union[str, List[str]]= None
    RAM_type: Optional[str] = None
    RAM_channels: Optional[str] = None
    RAM_frequency: Optional[str] = None

class Storage(BaseModel):
    Storage: Union[str, List[str]] = None

class Display(BaseModel):
    Type_or_Technology: Optional[str] = None
    Diagonal_size: Union[str, List[str]] = None
    Width: Optional[str] = None
    Height: Optional[str] = None
    Aspect_ratio: Optional[str] = None
    Resolution: Optional[str] = None
    Pixel_density: Optional[str] = None
    Color_depth: Optional[List[str]] = None
    Display_area: Optional[str] = None
    other_features:Union[str, List[str]] = None

class Sensors(BaseModel):
    Sensors: Union[str, List[str]] = None

class Rear_camera(BaseModel):
    Sensor_model: Optional[str] = None
    Sensor_type: Optional[str] = None
    Sensor_format: Optional[str] = None
    Aperture: Optional[str] = None
    Focal_length_in_35mm_equivalent: Optional[str] = None
    Field_of_view: Optional[str] = None
    Number_of_lenses: Optional[str] = None
    Flash_type: Optional[str] = None
    image_resolution: Optional[str] = None
    Video_resolution: Optional[str] = None
    Video_FPS: Optional[str] = None
    Features: Union[str, List[str]] = None
class Front_camera(BaseModel):
    Sensor_model: Optional[str] = None
    Sensor_type: Optional[str] = None
    Sensory_format: Optional[str] = None
    Aperture: Optional[str] = None
    Focal_length_in_35mm_equivalent: Optional[str] = None
    Field_of_view: Optional[str] = None
    Number_of_lenses: Optional[str] = None
    Flash_type: Optional[str] = None
    image_resolution: Optional[str] = None
    Video_resolution: Optional[str] = None
    Video_FPS: Optional[str] = None
    Features: Union[str, List[str]] = None

class Audio(BaseModel):
    Speaker: Union[str, List[str]] = None
    Other_features: Union[str, List[str]] = None
class Radio(BaseModel):
    FM_radio: Optional[str] = None
    NFC: Optional[str] = None
    Infrared_port: Optional[str] = None
    Other_features: Union[str, List[str]] = None
class Tracking_or_Positioning(BaseModel):
    GPS: Optional[bool] = None
    GLONASS: Optional[bool] = None
    BeiDou: Optional[bool] = None
    Galileo: Optional[bool] = None
    Other_features: Union[str, List[str]] = None

class Wi_Fi(BaseModel):
    Wi_Fi: Union[str, List[str]] = None

class Bluetooth(BaseModel):
    Version: Optional[str] = None
    Features: Union[str, List[str]] = None

class USB(BaseModel):
    Version: Optional[str] = None
    Features: Union[str, List[str]] = None
    Connector_type: Optional[str] = None

class Headphone_jack(BaseModel):
    Headphone_jack: Optional[str] = None
    Features: Union[str, List[str]] = None

class Connectivity(BaseModel):
    connectivity: Union[str, List[str]]= None

class Browser(BaseModel):
    Browser:Union[str, List[str]] = None

class Audio_file_formats(BaseModel):
    Audio_file_formats: Union[str, List[str]] = None

class Video_file_formats(BaseModel):
    Video_file_formats: Union[str, List[str]] = None

class Battery(BaseModel):
    Battery_capacity: Optional[str] = None
    Battery_type: Optional[str] = None
    Charging_power: Optional[str] = None
    Charging_time: Optional[str] = None
    Features: Union[str, List[str]] = None
    
class PhoneSpecs(BaseModel):
    brand_model: Optional[BrandModel] = None
    design: Optional[Design] = None
    sim_card: Optional[SIMcard] = None
    network: Optional[Network] = None
    bandwidths: Optional[Mobile_network_technologies_and_bandwidths] = None
    os: Optional[OperatingSystem] = None
    soc: Optional[System_on_chip] = None
    storage: Optional[Storage] = None
    display: Optional[Display] = None
    sensors: Optional[Sensors] = None
    rear_camera: Optional[Rear_camera] = None
    front_camera: Optional[Front_camera] = None
    audio: Optional[Audio] = None
    radio: Optional[Radio] = None
    positioning: Optional[Tracking_or_Positioning] = None
    wifi: Optional[Wi_Fi] = None
    bluetooth: Optional[Bluetooth] = None
    usb: Optional[USB] = None
    headphone_jack: Optional[Headphone_jack] = None
    connectivity: Optional[Connectivity] = None
    browser: Optional[Browser] = None
    audio_formats: Optional[Audio_file_formats] = None
    video_formats: Optional[Video_file_formats] = None
    battery: Optional[Battery] = None
