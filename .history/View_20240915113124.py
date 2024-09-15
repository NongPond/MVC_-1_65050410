import tkinter as tk
from tkinter import messagebox

class CowView:
    def __init__(self, root, controller):
        self.controller = controller
        
        # สร้าง GUI
        root.title("Cow Strike: ตรวจสอบวัวและแพะ")
        
        # ช่องรับรหัส
        tk.Label(root, text="กรอกรหัสวัวหรือแพะ (8 หลัก):").pack(pady=10)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # ปุ่มตรวจสอบ
        tk.Button(root, text="ตรวจสอบ", command=self.check_id).pack(pady=10)
        
        # Frame สำหรับแสดงผล
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

    def check_id(self):
        cow_id = self.entry.get()
        self.controller.check_id(cow_id)

    def show_cow_view(self, cow_data, milk_amount):
        self.clear_frame()
        age_years = cow_data.get("age_years", 0)
        age_months = cow_data.get("age_months", 0)
        udders = cow_data.get("udders", 0)
        milk_amount = milk_amount

        if udders == 4:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า สามารถรีดนมได้").pack()
        else:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า รีดนมไม่ได้").pack()

        tk.Label(self.frame, text=f"ปริมาณน้ำนมที่ผลิตได้: {milk_amount} ลิตร").pack()
        tk.Button(self.frame, text="กลับสู่การรับรหัสใหม่", command=self.reset_view).pack(pady=10)

    def show_goat_view(self):
        self.clear_frame()
        tk.Label(self.frame, text="นี่คือแพะ ไม่สามารถรีดนมได้").pack()
        tk.Button(self.frame, text="ไล่แพะออก", command=lambda: messagebox.showinfo("Goat", "แพะถูกไล่ออกแล้ว")).pack()
        tk.Button(self.frame, text="กลับสู่การรับรหัสใหม่", command=self.reset_view).pack(pady=10)

    def reset_view(self):
        self.clear_frame()
        tk.Label(self.frame, text="กรอกรหัสวัวหรือแพะ (8 หลัก):").pack(pady=10)
        self.entry.delete(0, tk.END)
        tk.Button(self.frame, text="ตรวจสอบ", command=self.check_id).pack(pady=10)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
