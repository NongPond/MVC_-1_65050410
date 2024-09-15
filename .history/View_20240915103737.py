import tkinter as tk
from tkinter import messagebox

class CowView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cow Strike: ตรวจสอบวัวและแพะ")

        # สร้างหน้าจอ GUI หลัก
        tk.Label(self.root, text="กรอกรหัสวัวหรือแพะ (8 หลัก):").pack(pady=10)
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        # ปุ่มตรวจสอบ
        tk.Button(self.root, text="ตรวจสอบ", command=self.check_id).pack(pady=10)

        # Frame สำหรับแสดงผลวัวหรือแพะ
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

    def get_cow_id(self):
        return self.entry.get()

    def show_cow_view(self, cow_data, milk_produced):
        # เคลียร์ผลลัพธ์ก่อนหน้า
        for widget in self.frame.winfo_children():
            widget.destroy()

        # แสดงผลข้อมูลวัว
        age_years = cow_data["age_years"]
        age_months = cow_data["age_months"]
        udders = cow_data["udders"]

        if udders == 4:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า สามารถรีดนมได้").pack()
        else:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า รีดนมไม่ได้").pack()

        # แสดงปริมาณน้ำนมที่ผลิตได้
        tk.Label(self.frame, text=f"ปริมาณน้ำนมที่ผลิตได้: {milk_produced:.2f} ลิตร").pack()

    def show_goat_view(self):
        # เคลียร์ผลลัพธ์ก่อนหน้า
        for widget in self.frame.winfo_children():
            widget.destroy()

        # แสดงผลข้อมูลแพะ
        tk.Label(self.frame, text="นี่คือแพะ ไม่สามารถรีดนมได้").pack()
        tk.Button(self.frame, text="ไล่แพะออก", command=lambda: messagebox.showinfo("Goat", "แพะถูกไล่ออกแล้ว")).pack()

    def show_error(self, message):
        messagebox.showerror("Error", message)
