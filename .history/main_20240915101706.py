import tkinter as tk
from Model import CowModel
from View import CowView
from Controller import CowController

def main():
    def main():
    root = tk.Tk()
    model = CowModel()  # สร้าง Model
    controller = CowController(model)  # สร้าง Controller พร้อมเชื่อมกับ Model
    view = CowView(root, controller)  # ส่ง Controller ไปยัง View
    root.mainloop()


    # ผูก View กับ Controller
    view.controller = controller

    # เริ่มโปรแกรม
    root.mainloop()

if __name__ == "__main__":
    main()
