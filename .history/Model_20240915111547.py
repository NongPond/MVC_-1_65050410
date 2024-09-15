import json
import random

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

    def update_cow_data(self, cow_id, updated_data):
        if cow_id in self.data:
            self.data[cow_id].update(updated_data)
            self.save_data()

    def save_data(self):
        with open(self.json_file, "w") as file:
            json.dump(list(self.data.values()), file, indent=4)

    def calculate_milk(self, cow_data):
        age_years = cow_data.get("age_years", 0)
        age_months = cow_data.get("age_months", 0)
        return age_years + age_months

    def process_cow(self, cow_id):
        cow_data = self.get_cow_data(cow_id)
        if not cow_data:
            return None, None

        udders = cow_data.get("udders", 0)  # Default to 0 if key does not exist
        if udders == 4:
            # มีโอกาส 5% ลดลง 1 เต้า
            if random.random() < 0.05:
                udders -= 1
                self.update_cow_data(cow_id, {"udders": udders})

        elif udders == 3:
            # มีโอกาส 20% เพิ่มขึ้นเป็น 4 เต้า
            if random.random() < 0.20:
                udders = 4
                self.update_cow_data(cow_id, {"udders": udders})

        milk_amount = self.calculate_milk(cow_data)
        return cow_data, milk_amount
