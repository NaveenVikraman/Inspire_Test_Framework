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
        return logger
