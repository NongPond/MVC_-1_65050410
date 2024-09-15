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

    # ตรวจสอบและอัปเดตจำนวนเต้านม
    def update_udders(self, cow_data):
        udders = cow_data["udders"]

        if udders == 4:
            # มีโอกาส 5% ที่จะเสีย 1 เต้า
            if random.random() < 0.05:
                cow_data["udders"] -= 1
                print(f"วัวรหัส {cow_data['id']} สูญเสีย 1 เต้า เหลือ {cow_data['udders']} เต้า")
        elif udders == 3:
            # มีโอกาส 20% ที่จะกลับมาเป็น 4 เต้า
            if random.random() < 0.20:
                cow_data["udders"] += 1
                print(f"วัวรหัส {cow_data['id']} ฟื้นฟู 1 เต้า กลับมาเป็น {cow_data['udders']} เต้า")

    # คำนวณน้ำนมที่ผลิต
    def calculate_milk(self, cow_data):
        age_years = cow_data["age_years"]
        age_months = cow_data["age_months"]
        milk_produced = age_years + (age_months / 12)  # คำนวณน้ำนมที่ผลิต
        return milk_produced

    # บันทึกข้อมูลที่ถูกแก้ไขกลับไปยังไฟล์ JSON
    def save_data(self):
        with open(self.json_file, "w") as file:
            json.dump(list(self.data.values()), file, indent=4)

