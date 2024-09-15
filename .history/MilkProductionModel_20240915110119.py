class MilkProductionModel:
    def __init__(self, cow_data):
        self.cow_data = cow_data

    def calculate_milk(self):
        age_years = self.cow_data["age_years"]
        age_months = self.cow_data["age_months"]
        
        # ปริมาณน้ำนม = อายุปี + อายุเดือน
        milk = age_years + age_months / 12
        return milk
