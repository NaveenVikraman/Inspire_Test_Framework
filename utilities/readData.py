import json
import os


class ReadData:
    def __init__(self):
        self.data = None
        self.json_path = None

    def read_file_location_data(self):
        """
            read_file_location_data(): To get all the file location data
            :return: data - file location data
        """
        self.json_path = os.getcwd() + "/utilities/file_location.json"
        with open(self.json_path, 'r') as j:
            self.data = json.loads(j.read())
        return self.data

    def read_input_json_data(self):
        """
               read_input_json_data(): To get all the input json data
               :return: data - input json data
        """
        self.json_path =  os.getcwd() + self.read_file_location_data()['input_json']
        with open(self.json_path, 'r') as j:
            self.data = json.loads(j.read())
        return self.data

    def read_locator_json_data(self):
        """
               read_locator_json_data(): To get all the locator  data
               :return: data - locator data
        """
        self.json_path = os.getcwd() + self.read_file_location_data()['locator_data_json']
        with open(self.json_path, 'r') as j:
            self.data = json.loads(j.read())
        return self.data
