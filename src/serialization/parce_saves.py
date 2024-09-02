import base64
import sys
from src.serialization.deserialize_dot_net import Deserializer
from src.logger import logger as LOG

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
            LOG.critical("Failed to find checksum")
            sys.exit(1)
        data = base64.b64decode(data[offset:])
        obj = []
        des = Deserializer(data, data.index(b'PlayerData') - 6)
        des.parse()
        obj = des.get('PlayerData')
        return obj
