from typing import Dict, TypedDict, List


class Vector(TypedDict):
    x: float
    y: float
    z: float


class LocationDict(TypedDict, total=False):
    name: str
    can_slip_through: bool
    need_laser_cutter: bool
    position: Vector
    need_propulsion_cannon: bool


events: List[str] = ["Neptune Launch", "Disable Quarantine", "Full Infection", "Repair Aurora Drive"]

location_table: Dict[int, LocationDict] = {
    33000: {'can_slip_through': False,
            'name': 'Blood Kelp Trench Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': -1234.3, 'y': -349.7, 'z': -396.0}},
    33001: {'can_slip_through': False,
            'name': 'Blood Kelp Trench Wreck - Inside Databox',
            'need_laser_cutter': False,
            'position': {'x': -1208.0, 'y': -349.6, 'z': -383.0}},
    33002: {'can_slip_through': False,
            'name': 'Blood Kelp Trench Wreck - PDA',
            'need_laser_cutter': False,
            'position': {'x': -1210.6, 'y': -340.7, 'z': -393.4}},
    33003: {'can_slip_through': False,
            'name': 'Bulb Zone West Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': 903.8, 'y': -220.3, 'z': 590.9}},
    33004: {'can_slip_through': False,
            'name': 'Bulb Zone West Wreck - Under Databox',
            'need_laser_cutter': False,
            'position': {'x': 910.9, 'y': -201.8, 'z': 623.5}},
    33005: {'can_slip_through': False,
            'name': 'Bulb Zone West Wreck - Inside Databox',
            'need_laser_cutter': True,
            'position': {'x': 914.9, 'y': -202.1, 'z': 611.8}},
    33006: {'can_slip_through': False,
            'name': 'Bulb Zone West Wreck - PDA',
            'need_laser_cutter': True,
            'position': {'x': 912.6, 'y': -202.0, 'z': 609.5}},
    33007: {'can_slip_through': False,
            'name': 'Bulb Zone East Wreck - Databox',
            'need_laser_cutter': False,
            'position': {'x': 1327.1, 'y': -234.9, 'z': 575.8}},
    33008: {'can_slip_through': False,
            'name': 'Dunes North Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': -1407.7, 'y': -344.2, 'z': 721.5}},
    33009: {'can_slip_through': False,
            'name': 'Dunes North Wreck - Office Databox',
            'need_laser_cutter': False,
            'position': {'x': -1393.9, 'y': -329.7, 'z': 733.5}},
    33010: {'can_slip_through': False,
            'name': 'Dunes North Wreck - PDA',
            'need_laser_cutter': False,
            'position': {'x': -1396.3, 'y': -330.8, 'z': 730.0}},
    33011: {'can_slip_through': False,
            'name': 'Dunes North Wreck - Cargo Databox',
            'need_laser_cutter': True,
            'position': {'x': -1409.8, 'y': -332.4, 'z': 706.9}},
    33012: {'can_slip_through': False,
            'name': 'Dunes West Wreck - Databox',
            'need_laser_cutter': False,
            'position': {'x': -1626.2, 'y': -357.5, 'z': 99.5}},
    33013: {'can_slip_through': False,
            'name': 'Dunes East Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': -1196.3, 'y': -223.0, 'z': 12.5}},
    33014: {'can_slip_through': False,
            'name': 'Dunes East Wreck - Inside Databox',
            'need_laser_cutter': False,
            'position': {'x': -1206.4, 'y': -225.6, 'z': 4.0}},
    33015: {'can_slip_through': False,
            'name': 'Grand Reef North Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': -269.7, 'y': -262.8, 'z': -764.3}},
    33016: {'can_slip_through': False,
            'name': 'Grand Reef North Wreck - Elevator Databox',
            'need_laser_cutter': True,
            'position': {'x': -285.8, 'y': -240.2, 'z': -786.5}},
    33017: {'can_slip_through': False,
            'name': 'Grand Reef North Wreck - Bottom Databox',
            'need_laser_cutter': False,
            'position': {'x': -285.2, 'y': -262.4, 'z': -788.4}},
    33018: {'can_slip_through': False,
            'name': 'Grand Reef North Wreck - Hangar PDA',
            'need_laser_cutter': False,
            'position': {'x': -272.5, 'y': -254.7, 'z': -788.5}},
    33019: {'can_slip_through': False,
            'name': 'Grand Reef South Wreck - Trench Databox',
            'need_laser_cutter': False,
            'position': {'x': -850.9, 'y': -473.2, 'z': -1414.6}},
    33020: {'can_slip_through': False,
            'name': 'Grand Reef South Wreck - Comms Databox',
            'need_laser_cutter': True,
            'position': {'x': -889.4, 'y': -433.8, 'z': -1424.8}},
    33021: {'can_slip_through': False,
            'name': 'Grand Reef South Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': -862.4, 'y': -437.5, 'z': -1444.1}},
    33022: {'can_slip_through': False,
            'name': 'Grand Reef South Wreck - PDA',
            'need_laser_cutter': False,
            'position': {'x': -887.9, 'y': -446.0, 'z': -1422.7}},
    33023: {'can_slip_through': False,
            'name': 'Grassy Plateaus South Wreck - Databox',
            'need_laser_cutter': False,
            'position': {'x': -23.3, 'y': -105.8, 'z': -604.2}},
    33024: {'can_slip_through': False,
            'name': 'Grassy Plateaus South Wreck - PDA',
            'need_laser_cutter': False,
            'position': {'x': -27.3, 'y': -106.8, 'z': -607.2}},
    33025: {'can_slip_through': True,
            'name': 'Grassy Plateaus East Wreck - Breach Databox',
            'need_laser_cutter': True,
            'position': {'x': 313.9, 'y': -91.8, 'z': 432.6}},
    33026: {'can_slip_through': True,
            'name': 'Grassy Plateaus East Wreck - Hangar Databox',
            'need_laser_cutter': True,
            'position': {'x': 319.4, 'y': -104.3, 'z': 441.5}},
    33027: {'can_slip_through': False,
            'name': 'Grassy Plateaus West Wreck - Locker PDA',
            'need_laser_cutter': False,
            'position': {'x': -632.3, 'y': -75.0, 'z': -8.9}},
    33028: {'can_slip_through': False,
            'name': 'Grassy Plateaus West Wreck - Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -664.4, 'y': -97.8, 'z': -8.0}},
    33029: {'can_slip_through': False,
            'name': 'Grassy Plateaus West Wreck - Databox',
            'need_laser_cutter': True,
            'position': {'x': -421.4, 'y': -107.8, 'z': -266.5}},
    33030: {'can_slip_through': False,
            'name': 'Safe Shallows Wreck - PDA',
            'need_laser_cutter': False,
            'position': {'x': -44.0, 'y': -29.1, 'z': -403.6}},
    33031: {'can_slip_through': False,
            'name': 'Kelp Forest Wreck - Databox',
            'need_laser_cutter': False,
            'position': {'x': -317.6, 'y': -78.8, 'z': 247.4}},
    33032: {'can_slip_through': False,
            'name': 'Kelp Forest Wreck - PDA',
            'need_laser_cutter': False,
            'position': {'x': 63.2, 'y': -38.5, 'z': 382.9}},
    33033: {'can_slip_through': False,
            'name': 'Mountains West Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': 740.3, 'y': -389.2, 'z': 1179.8}},
    33034: {'can_slip_through': False,
            'name': 'Mountains West Wreck - Data Terminal',
            'need_laser_cutter': True,
            'position': {'x': 703.7, 'y': -365.9, 'z': 1199.3}},
    33035: {'can_slip_through': False,
            'name': 'Mountains West Wreck - Hangar Databox',
            'need_laser_cutter': True,
            'position': {'x': 698.2, 'y': -350.8, 'z': 1186.9}},
    33036: {'can_slip_through': False,
            'name': 'Mountains West Wreck - Office Databox',
            'need_laser_cutter': False,
            'position': {'x': 676.3, 'y': -343.6, 'z': 1204.6}},
    33037: {'can_slip_through': False,
            'name': 'Mountains East Wreck - Comms Databox',
            'need_laser_cutter': False,
            'position': {'x': 1068.5, 'y': -283.4, 'z': 1345.3}},
    33038: {'can_slip_through': False,
            'name': 'Mountains East Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': 1075.7, 'y': -288.9, 'z': 1321.8}},
    33039: {'can_slip_through': False,
            'name': 'Northwestern Mushroom Forest Wreck - Cargo Databox',
            'need_laser_cutter': True,
            'position': {'x': -655.1, 'y': -109.6, 'z': 791.0}},
    33040: {'can_slip_through': False,
            'name': 'Northwestern Mushroom Forest Wreck - Office Databox',
            'need_laser_cutter': False,
            'position': {'x': -663.4, 'y': -111.9, 'z': 777.9}},
    33041: {'can_slip_through': False,
            'name': 'Northwestern Mushroom Forest Wreck - PDA',
            'need_laser_cutter': False,
            'position': {'x': -662.2, 'y': -113.4, 'z': 777.7}},
    33042: {'can_slip_through': False,
            'name': "Sea Treader's Path Wreck - Outside Databox",
            'need_laser_cutter': False,
            'position': {'x': -1161.1, 'y': -191.7, 'z': -758.3}},
    33043: {'can_slip_through': False,
            'name': "Sea Treader's Path Wreck - Hangar Databox",
            'need_laser_cutter': True,
            'position': {'x': -1129.5, 'y': -155.2, 'z': -729.3}},
    33044: {'can_slip_through': False,
            'name': "Sea Treader's Path Wreck - Lobby Databox",
            'need_laser_cutter': False,
            'position': {'x': -1115.9, 'y': -175.3, 'z': -724.5}},
    33045: {'can_slip_through': False,
            'name': "Sea Treader's Path Wreck - PDA",
            'need_laser_cutter': False,
            'position': {'x': -1136.8, 'y': -157.0, 'z': -734.6}},
    33046: {'can_slip_through': False,
            'name': 'Sparse Reef Wreck - Locker Databox',
            'need_laser_cutter': True,
            'position': {'x': -789.8, 'y': -216.1, 'z': -711.0}},
    33047: {'can_slip_through': False,
            'name': 'Sparse Reef Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': -810.7, 'y': -209.3, 'z': -685.5}},
    33048: {'can_slip_through': False,
            'name': 'Sparse Reef Wreck - Lab Databox',
            'need_laser_cutter': True,
            'position': {'x': -795.5, 'y': -204.1, 'z': -774.7}},
    33049: {'can_slip_through': False,
            'name': 'Underwater Islands Wreck - Outside Databox',
            'need_laser_cutter': False,
            'position': {'x': -170.8, 'y': -187.6, 'z': 880.7}},
    33050: {'can_slip_through': False,
            'name': 'Underwater Islands Wreck - Hangar Databox',
            'need_laser_cutter': True,
            'position': {'x': -138.4, 'y': -193.6, 'z': 888.7}},
    33051: {'can_slip_through': False,
            'name': 'Underwater Islands Wreck - Data Terminal',
            'need_laser_cutter': True,
            'position': {'x': -130.7, 'y': -193.2, 'z': 883.3}},
    33052: {'can_slip_through': False,
            'name': 'Underwater Islands Wreck - Cable Databox',
            'need_laser_cutter': False,
            'position': {'x': -137.8, 'y': -193.4, 'z': 879.4}},
    33053: {'can_slip_through': False,
            'name': 'Underwater Islands Wreck - Pipes Databox 1',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': -124.4, 'y': -200.7, 'z': 853.0}},
    33054: {'can_slip_through': False,
            'name': 'Underwater Islands Wreck - Pipes Databox 2',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': -126.8, 'y': -201.1, 'z': 852.1}},
    33055: {'can_slip_through': False,
            'name': 'Degasi Seabase - Deep Grand Reef - Bedroom Databox',
            'need_laser_cutter': False,
            'position': {'x': -643.8, 'y': -509.9, 'z': -941.9}},
    33056: {'can_slip_through': False,
            'name': 'Degasi Seabase - Deep Grand Reef - Observatory Databox',
            'need_laser_cutter': False,
            'position': {'x': -635.1, 'y': -502.7, 'z': -951.4}},
    33057: {'can_slip_through': False,
            'name': 'Degasi Seabase - Deep Grand Reef - Bedroom PDA',
            'need_laser_cutter': False,
            'position': {'x': -645.8, 'y': -508.7, 'z': -943.0}},
    33058: {'can_slip_through': False,
            'name': 'Degasi Seabase - Deep Grand Reef - Outside PDA',
            'need_laser_cutter': False,
            'position': {'x': -630.5, 'y': -511.1, 'z': -936.1}},
    33059: {'can_slip_through': False,
            'name': 'Degasi Seabase - Deep Grand Reef - Observatory PDA',
            'need_laser_cutter': False,
            'position': {'x': -647.7, 'y': -502.6, 'z': -935.8}},
    33060: {'can_slip_through': False,
            'name': 'Degasi Seabase - Deep Grand Reef - Lab PDA',
            'need_laser_cutter': False,
            'position': {'x': -639.6, 'y': -505.9, 'z': -946.6}},
    33061: {'can_slip_through': False,
            'name': 'Floating Island - Lake PDA',
            'need_laser_cutter': False,
            'position': {'x': -707.2, 'y': 0.5, 'z': -1096.7}},
    33062: {'can_slip_through': False,
            'name': 'Degasi Seabase - Floating Island - Databox',
            'need_laser_cutter': False,
            'position': {'x': -765.7, 'y': 17.6, 'z': -1116.4}},
    33063: {'can_slip_through': False,
            'name': 'Degasi Seabase - Floating Island - Room PDA',
            'need_laser_cutter': False,
            'position': {'x': -754.9, 'y': 14.6, 'z': -1108.9}},
    33064: {'can_slip_through': False,
            'name': 'Degasi Seabase - Floating Island - Green Wall PDA',
            'need_laser_cutter': False,
            'position': {'x': -765.3, 'y': 14.1, 'z': -1115.0}},
    33065: {'can_slip_through': False,
            'name': 'Degasi Seabase - Floating Island - Corridor PDA',
            'need_laser_cutter': False,
            'position': {'x': -758.6, 'y': 14.1, 'z': -1111.3}},
    33066: {'can_slip_through': False,
            'name': 'Degasi Seabase - Floating Island - North Observatory PDA',
            'need_laser_cutter': False,
            'position': {'x': -805.4, 'y': 76.9, 'z': -1055.7}},
    33067: {'can_slip_through': False,
            'name': 'Degasi Seabase - Floating Island - South Observatory PDA',
            'need_laser_cutter': False,
            'position': {'x': -715.9, 'y': 75.4, 'z': -1168.8}},
    33068: {'can_slip_through': False,
            'name': 'Jellyshroom Cave - PDA',
            'need_laser_cutter': False,
            'position': {'x': -540.5, 'y': -250.8, 'z': -83.4}},
    33069: {'can_slip_through': False,
            'name': 'Degasi Seabase - Jellyshroom Cave - Bedroom Databox',
            'need_laser_cutter': False,
            'position': {'x': 110.6, 'y': -264.9, 'z': -369.0}},
    33070: {'can_slip_through': False,
            'name': 'Degasi Seabase - Jellyshroom Cave - Detached PDA',
            'need_laser_cutter': False,
            'position': {'x': 80.6, 'y': -268.6, 'z': -358.3}},
    33071: {'can_slip_through': False,
            'name': 'Degasi Seabase - Jellyshroom Cave - Office PDA',
            'need_laser_cutter': False,
            'position': {'x': 78.2, 'y': -265.0, 'z': -373.4}},
    33072: {'can_slip_through': False,
            'name': 'Degasi Seabase - Jellyshroom Cave - Locker PDA',
            'need_laser_cutter': False,
            'position': {'x': 85.1, 'y': -264.1, 'z': -372.8}},
    33073: {'can_slip_through': False,
            'name': 'Degasi Seabase - Jellyshroom Cave - Bedroom PDA',
            'need_laser_cutter': False,
            'position': {'x': 112.3, 'y': -264.9, 'z': -369.3}},
    33074: {'can_slip_through': False,
            'name': 'Degasi Seabase - Jellyshroom Cave - Observatory PDA',
            'need_laser_cutter': False,
            'position': {'x': 95.5, 'y': -258.9, 'z': -366.5}},
    33075: {'can_slip_through': False,
            'name': 'Lifepod 2 - Databox',
            'need_laser_cutter': False,
            'position': {'x': -483.6, 'y': -504.7, 'z': 1326.6}},
    33076: {'can_slip_through': False,
            'name': 'Lifepod 2 - PDA',
            'need_laser_cutter': False,
            'position': {'x': -481.4, 'y': -503.6, 'z': 1324.1}},
    33077: {'can_slip_through': False,
            'name': 'Lifepod 3 - Databox',
            'need_laser_cutter': False,
            'position': {'x': -34.2, 'y': -22.4, 'z': 410.5}},
    33078: {'can_slip_through': False,
            'name': 'Lifepod 3 - PDA',
            'need_laser_cutter': False,
            'position': {'x': -33.8, 'y': -22.5, 'z': 408.8}},
    33079: {'can_slip_through': False,
            'name': 'Lifepod 4 - Databox',
            'need_laser_cutter': False,
            'position': {'x': 712.4, 'y': -3.4, 'z': 160.8}},
    33080: {'can_slip_through': False,
            'name': 'Lifepod 4 - PDA',
            'need_laser_cutter': False,
            'position': {'x': 712.0, 'y': -3.5, 'z': 161.5}},
    33081: {'can_slip_through': False,
            'name': 'Lifepod 6 - Databox',
            'need_laser_cutter': False,
            'position': {'x': 358.7, 'y': -117.1, 'z': 306.8}},
    33082: {'can_slip_through': False,
            'name': 'Lifepod 6 - Inside PDA',
            'need_laser_cutter': False,
            'position': {'x': 361.8, 'y': -116.2, 'z': 309.5}},
    33083: {'can_slip_through': False,
            'name': 'Lifepod 6 - Outside PDA',
            'need_laser_cutter': False,
            'position': {'x': 359.9, 'y': -117.0, 'z': 312.1}},
    33084: {'can_slip_through': False,
            'name': 'Lifepod 7 - PDA',
            'need_laser_cutter': False,
            'position': {'x': -56.0, 'y': -182.0, 'z': -1039.0}},
    33085: {'can_slip_through': False,
            'name': 'Lifepod 12 - Databox',
            'need_laser_cutter': False,
            'position': {'x': 1119.5, 'y': -271.7, 'z': 561.7}},
    33086: {'can_slip_through': False,
            'name': 'Lifepod 12 - PDA',
            'need_laser_cutter': False,
            'position': {'x': 1116.1, 'y': -271.3, 'z': 566.9}},
    33087: {'can_slip_through': False,
            'name': 'Lifepod 13 - Databox',
            'need_laser_cutter': False,
            'position': {'x': -926.4, 'y': -185.2, 'z': 501.8}},
    33088: {'can_slip_through': False,
            'name': 'Lifepod 13 - PDA',
            'need_laser_cutter': False,
            'position': {'x': -926.8, 'y': -184.4, 'z': 506.6}},
    33089: {'can_slip_through': False,
            'name': 'Lifepod 17 - PDA',
            'need_laser_cutter': False,
            'position': {'x': -514.5, 'y': -98.1, 'z': -56.5}},
    33090: {'can_slip_through': False,
            'name': 'Lifepod 19 - Databox',
            'need_laser_cutter': False,
            'position': {'x': -809.8, 'y': -302.2, 'z': -876.9}},
    33091: {'can_slip_through': False,
            'name': 'Lifepod 19 - Outside PDA',
            'need_laser_cutter': False,
            'position': {'x': -806.1, 'y': -294.1, 'z': -866.0}},
    33092: {'can_slip_through': False,
            'name': 'Lifepod 19 - Inside PDA',
            'need_laser_cutter': False,
            'position': {'x': -810.5, 'y': -299.4, 'z': -873.1}},
    33093: {'can_slip_through': False,
            'name': 'Aurora Seamoth Bay - Upgrade Console',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': 903.5, 'y': -0.2, 'z': 16.1}},
    33094: {'can_slip_through': False,
            'name': 'Aurora Drive Room - Upgrade Console',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': 872.5, 'y': 2.7, 'z': -0.7}},
    33095: {'can_slip_through': False,
            'name': 'Aurora Prawn Suit Bay - Upgrade Console',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 991.6, 'y': 3.2, 'z': -31.0}},
    33096: {'can_slip_through': False,
            'name': 'Aurora - Office PDA',
            'need_laser_cutter': False,
            'position': {'x': 952.1, 'y': 41.2, 'z': 113.9}},
    33097: {'can_slip_through': False,
            'name': 'Aurora - Corridor PDA',
            'need_laser_cutter': False,
            'position': {'x': 977.2, 'y': 39.1, 'z': 83.0}},
    33098: {'can_slip_through': False,
            'name': 'Aurora - Cargo Bay PDA',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': 954.9, 'y': 11.2, 'z': 3.4}},
    33099: {'can_slip_through': False,
            'name': 'Aurora - Seamoth Bay PDA',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': 907.1, 'y': -1.5, 'z': 15.3}},
    33100: {'can_slip_through': False,
            'name': 'Aurora - Medkit Locker PDA',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 951.8, 'y': -2.3, 'z': -34.7}},
    33101: {'can_slip_through': False,
            'name': 'Aurora - Locker PDA',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 952.0, 'y': -3.7, 'z': -23.4}},
    33102: {'can_slip_through': False,
            'name': 'Aurora - Canteen PDA',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 986.5, 'y': 9.6, 'z': -48.6}},
    33103: {'can_slip_through': False,
            'name': 'Aurora - Cabin 4 PDA',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 951.3, 'y': 11.2, 'z': -51.0}},
    33104: {'can_slip_through': False,
            'name': 'Aurora - Cabin 7 PDA',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 967.1, 'y': 10.4, 'z': -47.4}},
    33105: {'can_slip_through': False,
            'name': 'Aurora - Cabin 1 PDA',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 964.1, 'y': 11.1, 'z': -61.9}},
    33106: {'can_slip_through': False,
            'name': 'Aurora - Captain PDA',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 971.2, 'y': 10.8, 'z': -70.4}},
    33107: {'can_slip_through': False,
            'name': 'Aurora - Ring PDA',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': 1033.6, 'y': -8.5, 'z': 16.2}},
    33108: {'can_slip_through': False,
            'name': 'Aurora - Lab PDA',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': 1032.5, 'y': -7.8, 'z': 32.4}},
    33109: {'can_slip_through': False,
            'name': 'Aurora - Office Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': 945.8, 'y': 40.8, 'z': 115.1}},
    33110: {'can_slip_through': False,
            'name': 'Aurora - Captain Data Terminal',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 974.8, 'y': 10.0, 'z': -77.0}},
    33111: {'can_slip_through': False,
            'name': 'Aurora - Battery Room Data Terminal',
            'need_laser_cutter': True,
            'need_propulsion_cannon': True,
            'position': {'x': 1040.8, 'y': -11.4, 'z': -3.4}},
    33112: {'can_slip_through': False,
            'name': 'Aurora - Lab Data Terminal',
            'need_laser_cutter': False,
            'need_propulsion_cannon': True,
            'position': {'x': 1029.5, 'y': -8.7, 'z': 35.9}},
    33113: {'can_slip_through': False,
            'name': "Quarantine Enforcement Platform's - Upper Alien Data "
                    'Terminal',
            'need_laser_cutter': False,
            'position': {'x': 432.2, 'y': 3.0, 'z': 1193.2}},
    33114: {'can_slip_through': False,
            'name': "Quarantine Enforcement Platform's - Mid Alien Data Terminal",
            'need_laser_cutter': False,
            'position': {'x': 474.4, 'y': -4.5, 'z': 1224.4}},
    33115: {'can_slip_through': False,
            'name': 'Dunes Sanctuary - Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -1224.2, 'y': -400.4, 'z': 1057.9}},
    33116: {'can_slip_through': False,
            'name': 'Deep Sparse Reef Sanctuary - Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -895.5, 'y': -311.6, 'z': -838.1}},
    33117: {'can_slip_through': False,
            'name': 'Northern Blood Kelp Zone Sanctuary - Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -642.9, 'y': -563.5, 'z': 1485.5}},
    33118: {'can_slip_through': False,
            'name': 'Lost River Laboratory Cache - Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -1112.3, 'y': -687.3, 'z': -695.5}},
    33119: {'can_slip_through': False,
            'name': 'Disease Research Facility - Upper Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -280.2, 'y': -804.3, 'z': 305.1}},
    33120: {'can_slip_through': False,
            'name': 'Disease Research Facility - Mid Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -267.9, 'y': -806.6, 'z': 250.0}},
    33121: {'can_slip_through': False,
            'name': 'Disease Research Facility - Lower Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -286.2, 'y': -815.6, 'z': 297.8}},
    33122: {'can_slip_through': False,
            'name': 'Alien Thermal Plant - Entrance Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -71.3, 'y': -1227.2, 'z': 104.8}},
    33123: {'can_slip_through': False,
            'name': 'Alien Thermal Plant - Green Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -38.7, 'y': -1226.6, 'z': 111.8}},
    33124: {'can_slip_through': False,
            'name': 'Alien Thermal Plant - Yellow Alien Data Terminal',
            'need_laser_cutter': False,
            'position': {'x': -30.4, 'y': -1220.3, 'z': 111.8}},
    33125: {'can_slip_through': False,
            'name': "Primary Containment Facility's Antechamber - Alien Data "
                    'Terminal',
            'need_laser_cutter': False,
            'position': {'x': 245.8, 'y': -1430.6, 'z': -311.5}},
    33126: {'can_slip_through': False,
            'name': "Primary Containment Facility's Egg Laboratory - Alien Data "
                    'Terminal',
            'need_laser_cutter': False,
            'position': {'x': 165.5, 'y': -1442.4, 'z': -385.8}},
    33127: {'can_slip_through': False,
            'name': "Primary Containment Facility's Pipe Room - Alien Data "
                    'Terminal',
            'need_laser_cutter': False,
            'position': {'x': 348.7, 'y': -1443.5, 'z': -291.9}},
    33128: {'can_slip_through': False,
            'name': 'Grassy Plateaus West Wreck - Beam PDA',
            'need_laser_cutter': True,
            'position': {'x': -641.8, 'y': -111.3, 'z': -19.7}},
    33129: {'can_slip_through': False,
            'name': 'Floating Island - Cave Entrance PDA',
            'need_laser_cutter': False,
            'position': {'x': -748.9, 'y': 14.4, 'z': -1179.5}}}

if False:  # turn to True to export for Subnautica mod
    payload = {location_id: location_data["position"] for location_id, location_data in location_table.items()}
    import json

    with open("locations.json", "w") as f:
        json.dump(payload, f)
