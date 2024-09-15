# Controller.py

from tkinter import messagebox
from Model import CowModel
from View import CowView

class CowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def check_id(self, cow_id):
        # ตรวจสอบรูปแบบรหัส
        if len(cow_id) != 8 or not cow_id.isdigit() or cow_id[0] == '0':
            messagebox.showerror("Error", "รหัสต้องเป็นตัวเลข 8 หลัก และตัวแรกไม่ใช่ 0")
            return

        # ดึงข้อมูลจาก Model
        data = self.model.get_cow_data(cow_id)
        if data is None:
            messagebox.showerror("Error", "ไม่พบรหัสนี้ในฐานข้อมูล")
        else:
            if "is_goat" in data and data["is_goat"]:
                self.view.show_goat_view()
            else:
                milk_produced, udders = self.model.process_cow(data)
                self.view.show_cow_view(data)
                if udders == 4:
                    tk.Label(self.view.frame, text=f"ผลิตน้ำนม: {milk_produced:.2f} ลิตร").pack()



