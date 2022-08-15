import logging
import datetime
import os
from utilities.readData import ReadData


class LogGen:
    @staticmethod
    def generate_log_handle():
        """
                generate_log_handle(): To setup the logger
                :return: data - log handler and base_log_dir
        """
        time_stamp = datetime.datetime.now().timestamp()
        base_log_dir = os.getcwd() + ReadData().read_file_location_data()["logging_dir"] + str(time_stamp)
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
        return logger, base_log_dir

    @staticmethod
    def generate_screenshot_dir(base_log_dir):
        """
                generate_screenshot_dir(): To setup the screenshot directory under base log directory
                :return: data - screenshot directory
        """
        screenshots_dir = base_log_dir + "/Screenshots/"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        return screenshots_dir
