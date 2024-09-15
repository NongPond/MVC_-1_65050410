# View.py

import tkinter as tk
from tkinter import messagebox

class CowView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # ช่องรับรหัส
        tk.Label(root, text="กรอกรหัสวัวหรือแพะ (8 หลัก):").pack(pady=10)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # ปุ่มตรวจสอบ
        tk.Button(root, text="ตรวจสอบ", command=self.on_check_id).pack(pady=10)

    def on_check_id(self):
        cow_id = self.entry.get()
        if self.controller:
            self.controller.check_id(cow_id)

    def show_cow_view(self, cow_data):
        for widget in self.frame.winfo_children():
            widget.destroy()

        age_years = cow_data["age_years"]
        age_months = cow_data["age_months"]
        udders = cow_data["udders"]

        if udders == 4:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า รีดนมได้").pack()
        else:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า รีดนมไม่ได้").pack()

    def show_goat_view(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        tk.Label(self.frame, text="นี่คือแพะ ไม่สามารถรีดนมได้").pack()
        tk.Button(self.frame, text="ไล่แพะออก", command=lambda: messagebox.showinfo("Goat", "แพะถูกไล่ออกแล้ว")).pack()

    def set_controller(self, controller):
        self.controller = controller
