import tkinter as tk
from tkinter import messagebox
from main import register_account  # Import the function you made
window = tk.Tk()
window.title("Banking App")
window.geometry("300x250")
# Name input
tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

# PIN input
tk.Label(window, text="PIN").pack()
pin_entry = tk.Entry(window, show='*')
pin_entry.pack()

# Phone input
tk.Label(window, text="Phone").pack()
phone_entry = tk.Entry(window)
phone_entry.pack()
def handle_register():
    name = name_entry.get()
    pin = pin_entry.get()
    phone = phone_entry.get()
    
    if name and pin and phone:
        register_account(name, pin, phone)
        messagebox.showinfo("Success", "Account registered successfully!")
    else:
        messagebox.showerror("Error", "All fields must be filled out.")
tk.Button(window, text="Register Account", command=handle_register).pack(pady=10)
window.mainloop()
