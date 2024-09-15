import random

class UdderModel:
    def __init__(self, cow_data):
        self.cow_data = cow_data

    def calculate_milk(self):
        age_years = self.cow_data["age_years"]
        age_months = self.cow_data["age_months"]
        
        # ปริมาณน้ำนม = อายุปี + อายุเดือน
        milk = age_years + age_months / 12
        return milk

    def check_udder_status(self):
        udders = self.cow_data["udders"]

        if udders == 4:
            # โอกาส 5% ที่เต้านมจะลดลง 1 เต้า
            if random.random() < 0.05:
                self.cow_data["udders"] = 3
                print(f"วัว {self.cow_data['id']} เต้านมหลุดไป 1 เต้า ตอนนี้เหลือ {self.cow_data['udders']} เต้า")
        elif udders == 3:
            # โอกาส 20% ที่จะกลับมามี 4 เต้า
            if random.random() < 0.2:
                self.cow_data["udders"] = 4
                print(f"วัว {self.cow_data['id']} กลับมาสมบูรณ์อีกครั้ง ตอนนี้มี {self.cow_data['udders']} เต้า")

                class MilkProductionModel:

 

