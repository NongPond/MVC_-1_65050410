# Model.py

import json
from UdderModel import UdderModel
from MilkProductionModel import MilkProductionModel

class CowModel:
    def __init__(self, json_file):
        self.json_file = json_file
        self.cows_and_goats = self.load_data()

    def load_data(self):
        with open(self.json_file, "r") as file:
            data = json.load(file)
        return {item["id"]: item for item in data}

    def get_cow_data(self, cow_id):
        return self.cows_and_goats.get(cow_id)

    def process_cow(self, cow_data):
        # สร้างออบเจ็กต์ UdderModel และตรวจสอบการเปลี่ยนแปลงเต้านม
        udder_model = UdderModel(cow_data)
        udder_model.check_udder_status()

        # สร้างออบเจ็กต์ MilkProductionModel และคำนวณน้ำนม
        milk_model = MilkProductionModel(cow_data)
        milk_produced = milk_model.calculate_milk()

        return milk_produced, cow_data["udders"]

