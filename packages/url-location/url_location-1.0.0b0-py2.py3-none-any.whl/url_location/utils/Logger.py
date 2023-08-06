__author__ = "Eduardo Tuteggito Rosero"
__license__ = "MIT License"
__version__ = "1.0.0-beta"
__maintainer__ = "Eduardo Tuteggito Rosero"
__email__ = "zerhiphop@live.com"
__status__ = "Development"
__date__ = "08/December/2022"

import logging


class Logger:
    def __init__(self, LEVEL=logging.INFO):
        self.level = LEVEL
        self.logFormat = '[%(asctime)s.%(msecs)03d] - [%(process)d-%(name)s] - %(levelname)s - %(message)s'
        self.dateFormat = '%d-%b-%y %H:%M:%S'

    def getLogger(self, className):
        logging.basicConfig(format=self.logFormat, datefmt=self.dateFormat)
        logger = logging.getLogger(className)
        logger.setLevel(self.level)
        return logger
