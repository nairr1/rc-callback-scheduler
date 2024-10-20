import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
from auth import fetch_access_token
from api import queue_callback
from ui import CallbackSchedulerUI
from utils import validate_phone_number

load_dotenv()

NICE_AUTH_BASE_URL = os.getenv('NICE_AUTH_BASE_URL')
NICE_API_BASE_URL = os.getenv('NICE_API_BASE_URL')
NICE_ACCESS_KEY_ID = os.getenv('NICE_ACCESS_KEY_ID')
NICE_ACCESS_KEY_SECRET = os.getenv('NICE_ACCESS_KEY_SECRET')

# Skill ID for the callback to be logged under
skill_id =  

def schedule_callback():
  mobile_number = ui.entry.get()
  if not validate_phone_number(mobile_number):
    messagebox.showerror("Invalid input", "Please enter a valid phone number")
    return

  try:
    access_token, refresh_token = fetch_access_token(NICE_AUTH_BASE_URL, NICE_ACCESS_KEY_ID, NICE_ACCESS_KEY_SECRET)
    response = queue_callback(NICE_API_BASE_URL, access_token, skill_id, mobile_number)
    messagebox.showinfo("Success", f"Callback scheduled: {response}")
  except Exception as e:
    messagebox.showerror("Error", str(e))

root = tk.Tk()
ui = CallbackSchedulerUI(root, schedule_callback)
root.mainloop()
