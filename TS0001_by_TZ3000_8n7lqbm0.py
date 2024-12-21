# USB Zigbee USB Switch (Tuya) - TS0001 by _TZ3000_8n7lqbm0
# https://www.aliexpress.com/item/1005007514103570.html?spm=a2g0o.order_list.order_list_main.89.5a7c1802k2AZ0K

import logging
from zhaquirks.tuya import TuyaSwitch

LOG = logging.getLogger(__name__)

class USBPowerSwitch(TuyaSwitch):
    """Custom quirk for Tuya USB Power Switch (_TZ3000_8n7lqbm0 TS0001)."""

    signature = {
        "models_info": [("_TZ3000_8n7lqbm0", "TS0001")],
        "endpoints": {
            1: {
                "profile_id": 0x0104,  # Zigbee Home Automation profile
                "device_type": 0x0100,  # On/Off Light (default type for switches)
                "input_clusters": [
                    0x0000,  # Basic
                    0x0003,  # Identify
                    0x0004,  # Groups
                    0x0005,  # Scenes
                    0x0006,  # On/Off
                    0x0702,  # Metering
                    0x0b04,  # Electrical Measurement
                    0xe000,  # Tuya-specific
                    0xe001,  # Tuya-specific
                ],
                "output_clusters": [
                    0x000a,  # Time
                    0x0019,  # OTA
                ],
            },
            242: {
                "profile_id": 0xa1e0,  # Green Power Proxy profile
                "device_type": 0x0061,  # Proxy Basic
                "input_clusters": [],
                "output_clusters": [0x0021],  # Green Power
            },
        },
    }

    replacement = {
        "endpoints": {
            1: {
                "device_type": 0x0009,  # Switch device type (maps to HA switch)
                "input_clusters": [
                    0x0000,  # Basic
                    0x0006,  # On/Off
                ],
                "output_clusters": [],
            },
        },
    }

    LOG.debug("Custom quirk USBPowerSwitch for TS0001 applied with switch behavior")
