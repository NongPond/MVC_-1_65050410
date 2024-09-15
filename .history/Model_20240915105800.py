import random

class UdderModel:
    def __init__(self, cow_data):
        self.cow_data = cow_data

    def check_udder_status(self):
        udders = self.cow_data.get("teats", 0)  # ใช้ 'teats' ตามคำอธิบายของโจทย์

        if udders == 4:
            # โอกาส 5% ที่เต้านมจะลดลง 1 เต้า
            if random.random() < 0.05:
                self.cow_data["teats"] = 3
                print(f"วัว {self.cow_data['id']} เต้านมหลุดไป 1 เต้า ตอนนี้เหลือ {self.cow_data['teats']} เต้า")
        elif udders == 3:
            # โอกาส 20% ที่จะกลับมามี 4 เต้า
            if random.random() < 0.20:
                self.cow_data["teats"] = 4
                print(f"วัว {self.cow_data['id']} กลับมาสมบูรณ์อีกครั้ง ตอนนี้มี {self.cow_data['teats']} เต้า")

# ตัวอย่างการใช้งาน
cow_data_example = {
    "id": "12345678",
    "age_years": 5,
    "age_months": 6,
    "teats": 4
}

# คำนวณน้ำนม
milk_model = MilkProductionModel(cow_data_example)
milk_produced = milk_model.calculate_milk()
print(f"ปริมาณน้ำนมที่ผลิตได้: {milk_produced} ลิตร")

# ตรวจสอบสถานะเต้านม
udder_model = UdderModel(cow_data_example)
udder_model.check_udder_status()


