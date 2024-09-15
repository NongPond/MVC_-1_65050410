import tkinter as tk
from Model import CowModel
from View import CowView
from Controller import CowController

def main():
    def main():
    root = tk.Tk()
    model = CowModel()  # สร้าง Model
    controller = CowController(model)  # สร้าง Controller พร้อมเชื่อมกับ Model
    view = CowView(root, controller)  # ส่ง Controller ไปยัง View
    root.mainloop()

class CowController:
    def __init__(self, model):
        self.model = model

    def check_id(self, cow_id):
        animal = self.model.get_animal(cow_id)
        if animal:
            if "is_goat" in animal:
                print(f"{cow_id} เป็นแพะ")
                # เพิ่มการแสดงผลหรือฟังก์ชันไล่แพะออกไป
            else:
                print(f"{cow_id} เป็นวัว")
                # เพิ่มการตรวจสอบจำนวนเต้านมและรีดนม
        else:
            print("ไม่พบข้อมูลวัวหรือแพะ")


    # ผูก View กับ Controller
    view.controller = controller

    # เริ่มโปรแกรม
    root.mainloop()

if __name__ == "__main__":
    main()
