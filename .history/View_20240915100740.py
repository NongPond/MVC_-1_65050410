import tkinter as tk
from tkinter import messagebox

class CowView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Cow Strike: ตรวจสอบวัวและแพะ")
        
        self.entry_label = tk.Label(self.root, text="กรอกรหัสวัวหรือแพะ (8 หลัก):")
        self.entry_label.pack(pady=10)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)
        
        self.check_button = tk.Button(self.root, text="ตรวจสอบ", command=self.controller.check_id)
        self.check_button.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

    def show_message(self, message):
        messagebox.showinfo("ผลลัพธ์", message)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show_cow_view(self, cow_data):
        self.clear_frame()
        age_years = cow_data["age_years"]
        age_months = cow_data["age_months"]
        udders = cow_data["udders"]

        if udders == 4:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า สามารถรีดนมได้").pack()
        else:
            tk.Label(self.frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า รีดนมไม่ได้").pack()

    def show_goat_view(self):
        self.clear_frame()
        tk.Label(self.frame, text="นี่คือแพะ ไม่สามารถรีดนมได้").pack()
        tk.Button(self.frame, text="ไล่แพะออก", command=lambda: messagebox.showinfo("Goat", "แพะถูกไล่ออกแล้ว")).pack()
