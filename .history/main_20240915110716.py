import tkinter as tk
from Model import CowModel
from View import CowView
from Controller import CowController

def main():
    root = tk.Tk()
    root.title("Cow Strike: ตรวจสอบวัวและแพะ")

    model = CowModel("Model.json")
    view = CowView(root)
    controller = CowController(model, view)

    root.mainloop()

if __name__ == "__main__":
    main()


