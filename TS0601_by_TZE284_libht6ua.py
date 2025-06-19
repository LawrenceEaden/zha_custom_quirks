"""Custom quirk for Tuya blind motor _TZE284_libht6ua TS0601."""

from zigpy.profiles import zha
from zigpy.zcl.clusters.general import Basic, Groups, Ota, Scenes, Time
import zigpy.types as t
from zigpy.zcl import foundation

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.tuya import (
    TuyaManufacturerWindowCover,
    TuyaManufCluster,
    TuyaWindowCover,
    TuyaWindowCoverControl,
)


class TuyaBlindMotor_TZE284_libht6ua_Priority(TuyaWindowCover):
    """Tuya blind motor _TZE284_libht6ua with correct command and position mapping."""

    # Command mapping to match motor unit labeling
    # Open button (0x0000) → OPEN command (0x0000)
    # Close button (0x0001) → CLOSE command (0x0002) 
    # Stop button (0x0002) → STOP command (0x0001)
    tuya_cover_command = {0x0000: 0x0000, 0x0001: 0x0002, 0x0002: 0x0001}
    
    # Invert position values to match motor unit (0% = closed, 100% = open)
    tuya_cover_inverted_by_default = True

    signature = {
        MODELS_INFO: [
            ("_TZE284_libht6ua", "TS0601"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: 0x0104,
                DEVICE_TYPE: 0x0051,
                INPUT_CLUSTERS: [0x0000, 0x0004, 0x0005, 0xed00, 0xef00],
                OUTPUT_CLUSTERS: [0x000a, 0x0019],
            }
        },
        "manufacturer": "_TZE284_libht6ua",
        "model": "TS0601",
    }

    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaManufacturerWindowCover,
                    TuyaWindowCoverControl,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            }
        },
    }
