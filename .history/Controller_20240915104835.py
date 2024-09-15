# Controller.py
class CowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def check_id(self):
        # รับรหัสวัว/แพะจาก View
        cow_id = self.view.get_cow_id()

        # ตรวจสอบรูปแบบรหัส
        if len(cow_id) != 8 or not cow_id.isdigit() or cow_id[0] == '0':
            self.view.show_error("รหัสต้องเป็นตัวเลข 8 หลัก และตัวแรกไม่ใช่ 0")
            return

        # ดึงข้อมูลจาก Model
        cow_data = self.model.get_cow_data(cow_id)
        if cow_data is None:
            self.view.show_error("ไม่พบรหัสนี้ในฐานข้อมูล")
        else:
            if "is_goat" in cow_data and cow_data["is_goat"]:
                self.view.show_goat_view()
            else:
                # อัปเดตจำนวนเต้านม
                self.model.update_udders(cow_data)

                # คำนวณน้ำนมที่ผลิตได้
                milk_produced = self.model.calculate_milk(cow_data)

                # แสดงผลข้อมูลวัวและปริมาณน้ำนมที่ผลิตได้ใน View
                self.view.show_cow_view(cow_data, milk_produced)

                # บันทึกข้อมูลที่อัปเดตกลับไปยังไฟล์
                self.model.save_data()
