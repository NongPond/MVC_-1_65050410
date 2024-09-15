import tkinter as tk
from Model import CowModel
from View import CowView
from Controller import CowController

if __name__ == "__main__":
    root = tk.Tk()

    # สร้าง Model, View, Controller
    root = tk.Tk()
view = CowView(root)  # ลบ None ออก
controller = CowController(model, view)


    # ส่ง controller ให้กับ view
    view.controller = controller

    root.mainloop()
