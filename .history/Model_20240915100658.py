import json
import random

class CowModel:
    def __init__(self, json_file):
        self.json_file = json_file
        self.cows_and_goats = self.load_data()

    def load_data(self):
        with open(self.json_file, "r") as file:
            return json.load(file)

    def save_data(self):
        with open(self.json_file, "w") as file:
            json.dump(self.cows_and_goats, file, indent=4)

    def get_animal(self, cow_id):
        return self.cows_and_goats.get(cow_id, None)

    def update_udder(self, cow_id, udders):
        if cow_id in self.cows_and_goats:
            self.cows_and_goats[cow_id]['udders'] = udders
            self.save_data()

    def add_random_cows_and_goats(self):
        for i in range(15):
            cow_id = self.generate_cow_id()
            self.cows_and_goats[cow_id] = {
                "age_years": random.randint(0, 10),
                "age_months": random.randint(0, 11),
                "udders": random.choice([3, 4])
            }
        
        # Adding 2 goats
        for i in range(2):
            goat_id = self.generate_cow_id()
            self.cows_and_goats[goat_id] = {"is_goat": True}
        
        self.save_data()

    def generate_cow_id(self):
        return str(random.randint(1, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(7)])
