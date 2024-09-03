import logging

IS_ON_DEBUG = False

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("../app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

if not IS_ON_DEBUG:
    logger.setLevel(logging.INFO)
