import tkinter as tk
from Model import CowModel
from View import CowView
from Controller import CowController

def main():
    root = tk.Tk()

    # สร้าง Model, View, Controller
    model = CowModel("cows_and_goats.json")
    view = CowView(root, None)
    controller = CowController(model, view)

    # ผูก View กับ Controller
    view.controller = controller

    # เริ่มโปรแกรม
    root.mainloop()

if __name__ == "__main__":
    main()
