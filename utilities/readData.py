import json


class ReadData:
    def read_file_location_data(self):
        self.json_path = "/Users/Naveen/PycharmProjects/Inspire_Test_Framework/utilities/file_location.json"
        with open(self.json_path, 'r') as j:
            self.data = json.loads(j.read())
        return self.data

    def read_input_json_data(self):
        self.json_path = self.read_file_location_data()['input_json']
        with open(self.json_path, 'r') as j:
            self.data = json.loads(j.read())
        return self.data



