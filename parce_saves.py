import argparse
import base64
import json
import sys
import logging
from deserialize_dot_net import Deserializer

HEADERS = {
    "playtime": "totalPlaytime/value/totalseconds",
    "exp": "stats/value/totalExp",
    "boss": "stats/value/highestBoss",
    "cumulative_gold": "stats/value/totalGold",
    "base_power": "adventure/value/attack",
    "base_toughness": "adventure/value/defense",
    "base_energy_cap": "capEnergy",
    "base_energy_power": "energyPower",
    "base_energy_bars": "energyBars",
    "base_magic_cap": "magic/value/capMagic",
    "base_magic_power": "magic/value/magicPower",
    "base_magic_bars": "magic/value/magicPerBar",
    "itopod_maxlvl": "adventure/value/highestItopodLevel",
    "itopod_end": "adventure/value/itopodEnd",
    "cur_energy": "curEnergy",
}


LOG = logging.getLogger()
if sys.version_info < (3, 7):
    # We depend on dicts being ordered which requires python 3.7
    LOG.critical("Python >= 3.7 is required")
    sys.exit(1)


def read_savegame(fname):
    """This is a complete hack"""
    LOG.info(f"Reading: {fname}")
    with open(fname, 'rb') as _fh:
        a = _fh.read()
        data = base64.b64decode(a)
        try:
            offset = data.index(b'checksum') + 34
        except:
            logging.critical("Failed to find checksum")
            sys.exit(1)
        data = base64.b64decode(data[offset:])
        obj = []
        des = Deserializer(data, data.index(b'PlayerData') - 6)
        des.parse()
        obj = des.get('PlayerData')
        return obj
