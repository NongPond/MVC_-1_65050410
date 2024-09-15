import tkinter as tk
from tkinter import messagebox

# ตัวอย่างข้อมูลวัวและแพะ (ฐานข้อมูลจำลอง)
cows_and_goats = {
    "12345678": {"age_years": 5, "age_months": 8, "udders": 4},
    "23456789": {"age_years": 3, "age_months": 4, "udders": 3},
    "34567890": {"age_years": 7, "age_months": 11, "udders": 4},
    "45678901": {"age_years": 1, "age_months": 6, "udders": 3},
    "56789012": {"age_years": 9, "age_months": 2, "udders": 4},
    "67890123": {"age_years": 6, "age_months": 9, "udders": 4},
    "78901234": {"age_years": 2, "age_months": 3, "udders": 3},
    "89012345": {"age_years": 4, "age_months": 7, "udders": 4},
    "90123456": {"age_years": 3, "age_months": 10, "udders": 3},
    "67890125": {"is_goat": True},
    "78901236": {"is_goat": True}
}

# ฟังก์ชันตรวจสอบรหัส
def check_id():
    cow_id = entry.get()

    if len(cow_id) != 8 or not cow_id.isdigit() or cow_id[0] == '0':
        messagebox.showerror("Error", "รหัสต้องเป็นตัวเลข 8 หลัก และตัวแรกไม่ใช่ 0")
        return

    if cow_id in cows_and_goats:
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

root.mainloop()
