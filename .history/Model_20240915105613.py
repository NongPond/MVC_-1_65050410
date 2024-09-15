import json

class CowModel:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_data()

    def load_data(self):
        with open(self.json_file, "r") as file:
            data = json.load(file)
        return {item["id"]: item for item in data}

    def get_cow_data(self, cow_id):
        return self.data.get(cow_id)

