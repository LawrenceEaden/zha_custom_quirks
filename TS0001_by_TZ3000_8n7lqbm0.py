"""Quirk for Tuya USB Power Switch."""
import logging
from zhaquirks.tuya import TuyaSwitch

LOG = logging.getLogger(__name__)


class USBPowerSwitch(TuyaSwitch):
    """Custom quirk for Tuya USB Power Switch (_TZ3000_8n7lqbm0 TS0001)."""
    
    signature = {
        "models_info": [("_TZ3000_8n7lqbm0", "TS0001")],
        "endpoints": {
            1: {
                "profile_id": 0x0104,
                "device_type": 0x0009,
                "input_clusters": [
                    0x0000,  # Basic
                    0x0006,  # On/Off
                ],
                "output_clusters": [],
            },
        },
    }
    
    replacement = {
        "endpoints": {
            1: {
                "device_type": 0x0009,
                "input_clusters": [
                    0x0000,  # Basic
                    0x0006,  # On/Off
                ],
                "output_clusters": [],
            },
        },
    }
