import tkinter as tk

class CowView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cow Strike")
        
        self.label = tk.Label(root, text="Enter Cow ID:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)
        
        self.check_button = tk.Button(root, text="ตรวจสอบ", command=self.check_id)
        self.check_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
    def get_cow_id(self):
        return self.entry.get()
    
    def check_id(self):
        if hasattr(self, 'controller'):
            self.controller.check_id()

    def show_error(self, message):
        self.result_label.config(text=message, fg="red")
    
    def show_goat_view(self):
        self.result_label.config(text="เป็นแพะ ไม่สามารถรีดนมได้", fg="blue")
    
    def show_cow_view(self, cow_data, milk_produced):
        self.result_label.config(
            text=f"วัวรหัส: {cow_data['id']}\nอายุ: {cow_data['age_years']} ปี {cow_data['age_months']} เดือน\n"
                 f"จำนวนเต้านม: {cow_data['teats']}\nปริมาณน้ำนมที่ผลิตได้: {milk_produced} ลิตร", 
            fg="green"
        )
