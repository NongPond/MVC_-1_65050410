import random

class UdderModel:
    def __init__(self, cow_data):
        self.cow_data = cow_data
    
    [{
	"resource": "/c:/MVC/Model.py",
	"owner": "python",
	"severity": 8,
	"message": "Expected indented block",
	"source": "Pylance",
	"startLineNumber": 33,
	"startColumn": 1,
	"endLineNumber": 33,
	"endColumn": 1
}]

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

