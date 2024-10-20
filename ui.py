import tkinter as tk
from tkinter import messagebox

class CallbackSchedulerUI:
  def __init__(self, root, schedule_callback):
    self.root = root
    self.schedule_callback = schedule_callback

    self.root.title("Schedule Callback")
    self.root.configure(bg='#2E2E2E')
    self.root.geometry('400x500')

    self.label_style = {'bg': '#2E2E2E', 'fg': 'white', 'font': ('Arial', 14)}
    self.button_style = {'bg': '#5E5E5E', 'fg': 'white', 'font': ('Arial', 12), 'width': 5, 'height': 2}
    self.entry_style = {'bg': '#3E3E3E', 'fg': 'white', 'font': ('Arial', 18)}

    self.create_widgets()

  def create_widgets(self):
    label = tk.Label(self.root, text="Enter Mobile Number:", **self.label_style)
    label.pack(pady=10)

    self.entry = tk.Entry(self.root, **self.entry_style, width=15)
    self.entry.pack(pady=10)

    buttons_frame = tk.Frame(self.root, bg='#2E2E2E')
    buttons_frame.pack(pady=10)

    numbers = [
      ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
      ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
      ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
      ('0', 4, 1)
    ]

    for (text, row, col) in numbers:
      button = tk.Button(buttons_frame, text=text, command=lambda t=text: self.entry.insert(tk.END, t), **self.button_style)
      button.grid(row=row, column=col, padx=5, pady=5)

    schedule_button = tk.Button(self.root, text="Schedule Callback", command=self.schedule_callback, bg='#4CAF50', fg='white', font=('Arial', 14), width=20, height=2)
    schedule_button.pack(pady=20)