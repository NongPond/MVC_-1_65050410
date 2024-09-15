import tkinter as tk
from tkinter import messagebox
import json

# โหลดข้อมูลจากไฟล์ JSON
def load_data():
    with open("cows_and_goats.json", "r") as file:
        data = json.load(file)
    # เปลี่ยนรูปแบบข้อมูลจาก list ให้เป็น dictionary เพื่อการเข้าถึงที่ง่ายขึ้น
    data_dict = {item["id"]: item for item in data}
    return data_dict

# ฟังก์ชันตรวจสอบรหัส
def check_id():
    cow_id = entry.get()

    if len(cow_id) != 8 or not cow_id.isdigit() or cow_id[0] == '0':
        messagebox.showerror("Error", "รหัสต้องเป็นตัวเลข 8 หลัก และตัวแรกไม่ใช่ 0")
        return

    if cow_id in Model:
        data = cows_and_goats[cow_id]
        if "is_goat" in data and data["is_goat"]:
            show_goat_view()
        else:
            show_cow_view(data)
    else:
        messagebox.showerror("Error", "ไม่พบรหัสนี้ในฐานข้อมูล")

# แสดงหน้าจอวัว
def show_cow_view(cow_data):
    for widget in frame.winfo_children():
        widget.destroy()

    age_years = cow_data["age_years"]
    age_months = cow_data["age_months"]
    udders = cow_data["udders"]

    if udders == 4:
        tk.Label(frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า สามารถรีดนมได้").pack()
    else:
        tk.Label(frame, text=f"วัวอายุ {age_years} ปี {age_months} เดือน มีเต้านม {udders} เต้า รีดนมไม่ได้").pack()

# แสดงหน้าจอแพะ
def show_goat_view():
    for widget in frame.winfo_children():
        widget.destroy()
    
    tk.Label(frame, text="นี่คือแพะ ไม่สามารถรีดนมได้").pack()
    tk.Button(frame, text="ไล่แพะออก", command=lambda: messagebox.showinfo("Goat", "แพะถูกไล่ออกแล้ว")).pack()

# สร้างหน้าจอ GUI หลัก
root = tk.Tk()
root.title("Cow Strike: ตรวจสอบวัวและแพะ")

# ช่องรับรหัส
tk.Label(root, text="กรอกรหัสวัวหรือแพะ (8 หลัก):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# ปุ่มตรวจสอบ
tk.Button(root, text="ตรวจสอบ", command=check_id).pack(pady=10)

# Frame สำหรับแสดงผลวัวหรือแพะ
frame = tk.Frame(root)
frame.pack(pady=20)

# โหลดข้อมูลวัวและแพะจากไฟล์ JSON
with open("C:/MVC/Model.Json", "r") as file:
    data = json.load(file)


root.mainloop()
