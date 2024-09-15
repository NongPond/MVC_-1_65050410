import random
from tkinter import messagebox

class CowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def check_id(self):
        cow_id = self.view.entry.get()

        if len(cow_id) != 8 or not cow_id.isdigit() or cow_id[0] == '0':
            messagebox.showerror("Error", "รหัสต้องเป็นตัวเลข 8 หลัก และตัวแรกไม่ใช่ 0")
            return

        animal_data = self.model.get_animal(cow_id)
        if animal_data:
            if "is_goat" in animal_data:
                self.view.show_goat_view()
            else:
                self.view.show_cow_view(animal_data)
                self.process_milking(animal_data, cow_id)
        else:
            messagebox.showerror("Error", "ไม่พบรหัสนี้ในฐานข้อมูล")

    def process_milking(self, cow_data, cow_id):
        udders = cow_data["udders"]
        if udders == 4:
            milk_amount = cow_data["age_years"] + (cow_data["age_months"] / 12.0)
            self.view.show_message(f"รีดนมได้ {milk_amount:.2f} ลิตร")

            if random.random() < 0.05:
                udders -= 1
                self.model.update_udder(cow_id, udders)
                self.view.show_message(f"เต้านมหลุดไป 1 เต้า ตอนนี้เหลือ {udders} เต้า")
        elif udders == 3 and random.random() < 0.2:
            udders = 4
            self.model.update_udder(cow_id, udders)
            self.view.show_message("วัวกลับมามี 4 เต้าอีกครั้ง!")
