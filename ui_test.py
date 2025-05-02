import tkinter as tk
from tkinter import messagebox
import mysql.connector  # Connect to the database
def connect_database():
    return mysql.connector.connect(user='root', database='banking_system', password='Godblessyou@77')
from main import register_account, view_balance, update_account, delete_account, deposit, withdraw

def gui_register_account():
    name = entry_name.get()  # To get the name
    pin = entry_pin.get()    # To get the pin
    phone = entry_phone.get()  # To get the number
    if name and pin and phone:
        register_account(name, pin, phone)  # Call the function from main.py
        messagebox.showinfo("Success", "Account registered successfully!")
    else:
        messagebox.showwarning("Error", "Please fill in all fields!")

def gui_view_balance():
    account_id = entry_id.get()  # To get the account id in the entered field
    if account_id:
        balance = view_balance(account_id)  # Call the function from main.py
        if balance is not None:  # Ensure the account was found and balance returned
            messagebox.showinfo("Balance", f"The balance for account {account_id} is {balance}")
        else:
            messagebox.showwarning("Error", "Account not found")
    else:
        messagebox.showwarning("Error", "Please enter account ID")

def gui_deposit():
    account_id = entry_id.get()  # To get account ID
    amount = entry_amount.get()  # To get the deposit amount
    if account_id and amount:
        try:
            amount = float(amount)  # Ensure it's a valid amount
            deposit(account_id, amount)  # Call the deposit function from main.py
            messagebox.showinfo("Success", f"Deposited {amount} into account {account_id}")
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid amount")
    else:
        messagebox.showwarning("Error", "Please enter account ID and amount")

def gui_withdraw():
    account_id = entry_id.get()  # To get account ID
    amount = entry_amount.get()  # To get the withdraw amount
    if account_id and amount:
        try:
            amount = float(amount)  # Ensure it's a valid amount
            withdraw(account_id, amount)  # Call the withdraw function from main.py
            messagebox.showinfo("Success", f"Withdrew {amount} from account {account_id}")
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid amount")
    else:
        messagebox.showwarning("Error", "Please enter account ID and amount")

# Setting up the GUI
root = tk.Tk()
root.title("Banking System")
root.geometry("400x400")
root.configure(bg="green")  # Background color

label_title = tk.Label(root, text="Banking App", font=("Arial", 24))  # Create a title
label_title.pack(pady=10)

# Create an input field for the user's name
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_pin = tk.Label(root, text="PIN:")  # Create a label for the PIN field
label_pin.pack(pady=5)
entry_pin = tk.Entry(root, show="*")
entry_pin.pack(pady=5)

label_phone = tk.Label(root, text="Phone:")  # For the phone field
label_phone.pack(pady=5)
entry_phone = tk.Entry(root)
entry_phone.pack(pady=5)

label_account_id = tk.Label(root, text="Account ID:")  # For the account ID
label_account_id.pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack(pady=5)

label_amount = tk.Label(root, text="Amount:")  # Label for the amount
label_amount.pack(pady=5)
entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

button_register = tk.Button(root, text="Register", command=gui_register_account)  # Register button
button_register.pack(pady=5)

button_view_balance = tk.Button(root, text="View Balance", command=gui_view_balance)  # View balance button
button_view_balance.pack(pady=5)

button_deposit = tk.Button(root, text="Deposit", command=gui_deposit)  # Deposit button
button_deposit.pack(pady=5)

button_withdraw = tk.Button(root, text="Withdraw", command=gui_withdraw)  # Withdraw button
button_withdraw.pack(pady=5)

# To run the GUI
root.mainloop()
