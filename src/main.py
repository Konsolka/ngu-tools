import base64
import logging
import sys

from PySide6.QtWidgets import QApplication

from logger import logger
from deserialize_dot_net import Deserializer

from main_window import MainWindow

from handler import Handler


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
        des = Deserializer(data, data.index(b'PlayerData') - 6)
        des.parse()
        ret = des.get('PlayerData')
        return ret

if __name__ == "__main__":
    logger.info("Starting the application")
    handler = Handler(read_savefile("test.txt"))

    app = QApplication(sys.argv)

    window = MainWindow(handler)
    window.ratios_draw_all()

    window.show()

    logger.info("Ending the application")
    sys.exit(app.exec())


