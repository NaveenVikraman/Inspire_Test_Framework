import logging
import datetime
import os
from utilities.readData import ReadData


class LogGen:
    @staticmethod
    def logGen():
        time_stamp = datetime.datetime.now().timestamp()
        base_log_dir = ReadData().read_file_location_data()["logging_dir"] + str(time_stamp)
        if not os.path.exists(base_log_dir):
            os.makedirs(base_log_dir)
        logging.basicConfig(
            level="WARNING",
            format="%(asctime)s - %(name)s - [ %(message)s ]",
            datefmt='%d-%b-%y %H:%M:%S',
            force=True,
            handlers=[
                logging.FileHandler(base_log_dir + "/automation.log"),
                logging.StreamHandler()
            ])
        logger = logging.getLogger()
        logger.root.setLevel(logging.INFO)
        return logger,base_log_dir
    @staticmethod
    def screenshotGen(base_log_dir):
        screenshots_dir = base_log_dir +"/Screenshots/"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        return screenshots_dir
