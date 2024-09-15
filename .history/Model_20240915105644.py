import json

class CowModel:
    def __init__(self, json_file):
        self.json_file = json_file  # กำหนดไฟล์ JSON ที่จะโหลดข้อมูลวัวและแพะ
        self.data = self.load_data()  # โหลดข้อมูลจากไฟล์เมื่อสร้างออบเจ็กต์ CowModel

    def load_data(self):
        with open(self.json_file, "r") as file:  # เปิดไฟล์ JSON
            data = json.load(file)  # โหลดข้อมูลจากไฟล์เป็นรูปแบบ dictionary หรือ list
        return {item["id"]: item for item in data}  # เปลี่ยนข้อมูลให้เป็น dictionary โดยใช้ "id" เป็น key

    def get_cow_data(self, cow_id):
        return self.data.get(cow_id)  # ค้นหาข้อมูลวัวหรือแพะตาม cow_id ที่ผู้ใช้กรอก


