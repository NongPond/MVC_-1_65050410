import tkinter as tk
from Model import CowModel
from View import CowView
from Controller import CowController

if __name__ == "__main__":
    root = tk.Tk()

    # สร้าง Model, View, Controller
    model = CowModel("cows_and_goats.json")
    view = CowView(root)
    controller = CowController(model, view)

    # ส่ง controller ให้กับ view
    view.controller = controller

    root.mainloop()
