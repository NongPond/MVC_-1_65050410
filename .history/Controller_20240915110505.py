from tkinter import messagebox

class CowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

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
                self.view.show_cow_view(data)
    def show_cow_view(cow_data):
        
    for widget in frame.winfo_children():
        widget.destroy()

    age_years = cow_data["age_years"]
    age_months = cow_data["age_months"]
    udders = cow_data["udders"]

    # สร้างออบเจ็กต์ UdderModel และตรวจสอบการเปลี่ยนแปลงเต้านม
    udder_model = UdderModel(cow_data)
    udder_model.check_udder_status()

    # สร้างออบเจ็กต์ MilkProductionModel และคำนวณน้ำนม
    milk_model = MilkProductionModel(cow_data)
    milk_produced = milk_model.calculate_milk()

    if cow_data["udders"] == 4:
        tk.Label(frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {cow_data['udders']} เต้า รีดนมได้ {milk_produced:.2f} ลิตร").pack()
    else:
        tk.Label(frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {cow_data['udders']} เต้า รีดนมไม่ได้").pack()

