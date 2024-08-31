import base64
import logging
import sys

from PySide6.QtWidgets import QApplication

from deserialize_dot_net import Deserializer

from main_window import MainWindow

from handler import Handler
from ratioz import Ratios

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def read_savefile(file):
    logger.info(f"Reading file {file}")
    with open(file, "rb") as savefile:
        a = savefile.read()
        data = base64.b64decode(a)
        try:
            offset = data.index(b'checksum') + 34
        except:
            logging.critical("Failed to find checksum")
            sys.exit(1)
        data = base64.b64decode(data[offset:])
        ret = []
        des = Deserializer(data, data.index(b'PlayerData') - 6)
        des.parse()
        ret = des.get('PlayerData')
        return ret





if __name__ == "__main__":
    logger.debug("Starting the application")
    handler = Handler(read_savefile("test.txt"))

    app = QApplication(sys.argv)

    window = MainWindow(handler)
    window.init_ratios()


    window.show()

    logger.debug("Ending the application")
    sys.exit(app.exec())


