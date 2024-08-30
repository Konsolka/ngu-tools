import base64
import logging
import sys

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow

from deserialize_dot_net import Deserializer

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

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file_name = "untitled.ui.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open():
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        window = loader.load(ui_file)


if __name__ == "__main__":
    logger.debug("Starting the application")
    obj = read_savefile("test.txt")
    print(obj.get("curEnergy/value"))

    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    logger.debug("Ending the application")
    sys.exit(app.exit())


