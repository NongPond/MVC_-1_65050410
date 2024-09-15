mport json
import random

class CowModel:
    def __init__(self, json_file="cows_and_goats.json"):  
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
           
i