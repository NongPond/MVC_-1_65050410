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
