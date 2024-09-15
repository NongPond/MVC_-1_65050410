import tkinter as tk
from tkinter import messagebox

class CowView:
    def __init__(self, root, controller):
        self.controller = controller

        # ตั้งค่าขนาดของหน้าต่างหลัก
        root.geometry("600x400")  # ตั้งค่าขนาดหน้าต่างที่ต้องการ (กว้าง x สูง)
        
        # สร้าง GUI
        root.title("Cow Strike: ตรวจสอบวัวและแพะ")
        
        # ช่องรับรหัส
        tk.Label(root, text="กรอกรหัสวัวหรือแพะ (8 หลัก):").pack(pady=10)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # ปุ่มตรวจสอบ
        tk.Button(root, text="ตรวจสอบ", font=("Arial", 16), command=self.check_id).pack(pady=20)
        
        # Frame สำหรับแสดงผล
        self.frame = tk.Frame(root)
        self.frame.pack(pady=30, fill=tk.BOTH, expand=True)

    def check_id(self):
        cow_id = self.entry.get()
        self.controller.check_id(cow_id)

    def show_cow_view(self, cow_data, milk_amount):
        self.clear_frame()
        age_years = cow_data["age_years"]
        age_months = cow_data["age_months"]
        udders = cow_data["udders"]

        if udders == 4:
                tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า สามารถรีดนมได้",font=("Arial", 16)).pack()).pack()
        else:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า รีดนมไม่ได้").pack()
        
        tk.Label(self.frame, text=f"ปริมาณน้ำนมที่ผลิตได้: {milk_amount} ลิตร").pack()
        tk.Button(self.frame, text="กลับไปหน้าหลัก", font=("Arial", 16), command=self.reset_view).pack(pady=20)

    def show_goat_view(self):
        self.clear_frame()
        tk.Label(self.frame, text="ฉันคือแพะ ฉันสามารถรีดนมได้").pack()
        tk.Button(self.frame, text="ไล่แพะออก กลับไปภูเขา ปายๆ", command=lambda: messagebox.showinfo("Goat", "แพะถูกไล่ออกแล้ว")).pack()
        tk.Button(self.frame, text="กลับไปหน้าหลัก", font=("Arial", 16), command=self.reset_view).pack(pady=20)

    def reset_view(self):
        self.entry.delete(0, tk.END)
        self.clear_frame()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

