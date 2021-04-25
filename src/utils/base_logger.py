
from src.configs.config import LOG_DIR, ROOT_DIR

import logging

log_format = "%(asctime)s:%(levelname)s:%(name)s:"\
             "%(filename)s:%(lineno)d - %(message)s"

logging.basicConfig(filename=f'{LOG_DIR}/example.log',
                    filemode='a',
                    level='DEBUG',
                    format=log_format)
logger = logging