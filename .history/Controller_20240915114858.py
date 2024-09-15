from tkinter import messagebox

class CowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def check_id(self, cow_id):
        # ตรวจสอบรูปแบบรหัส
        if len(cow_id) != 8 or not cow_id.isdigit() or cow_id[0] == '0':
            messagebox.showerror("Error", "รหัสต้องเป็นตัวเลข 8 หลัก และตัวแรกไม่ใช่ 0", font=("Arial", 16))
            return

        # ดึงข้อมูลจาก Model และทำการประมวลผล
        cow_data, milk_amount = self.model.process_cow(cow_id)
        if cow_data is None:
            messagebox.showerror("Error", "ไม่พบรหัสนี้ในฐานข้อมูล" ,font=("Arial", 16))
        else:
            if "is_goat" in cow_data and cow_data["is_goat"]:
                self.view.show_goat_view()
            else:
                self.view.show_cow_view(cow_data, milk_amount)
