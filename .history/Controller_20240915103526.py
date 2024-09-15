from tkinter import messagebox

class CowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # ฟังก์ชันสำหรับตรวจสอบรหัสวัว/แพะ
    def check_id(self, cow_id):
        # ตรวจสอบรูปแบบรหัส
        if len(cow_id) != 8 or not cow_id.isdigit() or cow_id[0] == '0':
            messagebox.showerror("Error", "รหัสต้องเป็นตัวเลข 8 หลัก และตัวแรกไม่ใช่ 0")
            return

        # ดึงข้อมูลจาก Model
        cow_data = self.model.get_cow_data(cow_id)
        if cow_data is None:
            messagebox.showerror("Error", "ไม่พบรหัสนี้ในฐานข้อมูล")
        else:
            if "is_goat" in cow_data and cow_data["is_goat"]:
                self.view.show_goat_view()
            else:
                self.view.show_cow_view(cow_data)

                # อัปเดตจำนวนเต้านมตามข้อกำหนด
                self.model.update_udders(cow_data)

                # คำนวณน้ำนมที่ผลิตได้
                milk_produced = self.model.calculate_milk(cow_data)
                print(f"วัวรหัส {cow_id} ผลิตน้ำนมได้ {milk_produced:.2f} ลิตร")

                # บันทึกข้อมูลที่อัปเดตกลับไปยังไฟล์
                self.model.save_data()




