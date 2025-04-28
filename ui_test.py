import tkinter as tk
from tkinter import messagebox
from main import register_account, login, view_balance, deposit_money, withdraw_money, update_account, delete_account  # Import necessary functions

# Initialize window
window = tk.Tk()
window.title("Banking App")
window.geometry("300x350")

# Function to show the registration form
def show_registration_form():
    # Clear the window
    for widget in window.winfo_children():
        widget.pack_forget()

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

    # Function to handle registering a new account
    def handle_register():
        name = name_entry.get()
        pin = pin_entry.get()
        phone = phone_entry.get()

        if name and pin and phone:
            register_account(name, pin, phone)  # Call the register_account function from main.py
            messagebox.showinfo("Success", "Account registered successfully!")
            show_login_form()  # After successful registration, show the login form again
        else:
            messagebox.showerror("Error", "All fields must be filled out.")
    
    # Register button
    tk.Button(window, text="Register Account", command=handle_register).pack(pady=10)

# Function to show the login form
def show_login_form():
    # Clear the window
    for widget in window.winfo_children():
        widget.pack_forget()

    # Login form
    tk.Label(window, text="Login").pack()

    # Name input (or any other login details you want)
    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    # PIN input
    tk.Label(window, text="PIN").pack()
    pin_entry = tk.Entry(window, show='*')
    pin_entry.pack()

    # Function to handle login
    def handle_login():
        name = name_entry.get()
        pin = pin_entry.get()

        if name and pin:
            # Here you would handle the actual login logic (authentication)
            messagebox.showinfo("Success", "Login successful!")
            show_dashboard()  # After successful login, show the dashboard (next screen)
        else:
            messagebox.showerror("Error", "Please enter both name and PIN.")

    # Login button
    tk.Button(window, text="Login", command=handle_login).pack(pady=10)

    # Register account button
    tk.Button(window, text="Register Account", command=show_registration_form).pack(pady=10)

# Function to show the dashboard (view balance, deposit, etc.)
def show_dashboard():
    # Clear the window
    for widget in window.winfo_children():
        widget.pack_forget()

    # Dashboard form (buttons for balance, deposit, etc.)
    tk.Label(window, text="Dashboard").pack()

    # View balance input (Account ID)
    tk.Label(window, text="Account ID").pack()
    account_id_entry = tk.Entry(window)
    account_id_entry.pack()

    # Function to handle viewing balance
    def handle_view_balance():
        account_id = account_id_entry.get()  # Get the account ID from the user input field
        if account_id:
            try:
                account_id = int(account_id)  # Ensure account_id is an integer
                view_balance(account_id)  # Call the view_balance function from main.py
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid account ID.")
        else:
            messagebox.showerror("Error", "Please enter an account ID.")

    # View balance button
    tk.Button(window, text="View Balance", command=handle_view_balance).pack(pady=10)

    # Deposit money input
    tk.Label(window, text="Amount to Deposit").pack()
    deposit_entry = tk.Entry(window)
    deposit_entry.pack()

    def handle_deposit():
        amount = deposit_entry.get()
        if amount:
            try:
                amount = float(amount)  # Ensure amount is a float
                account_id = int(account_id_entry.get())
                deposit_money(account_id, amount)  # Call the deposit_money function from main.py
                messagebox.showinfo("Success", f"Deposited {amount}")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            messagebox.showerror("Error", "Please enter an amount.")

    tk.Button(window, text="Deposit Money", command=handle_deposit).pack(pady=10)

    # Withdraw money input
    tk.Label(window, text="Amount to Withdraw").pack()
    withdraw_entry = tk.Entry(window)
    withdraw_entry.pack()

    def handle_withdraw():
        amount = withdraw_entry.get()
        if amount:
            try:
                amount = float(amount)  # Ensure amount is a float
                account_id = int(account_id_entry.get())
                withdraw_money(account_id, amount)  # Call the withdraw_money function from main.py
                messagebox.showinfo("Success", f"Withdrew {amount}")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            messagebox.showerror("Error", "Please enter an amount.")

    tk.Button(window, text="Withdraw Money", command=handle_withdraw).pack(pady=10)

    # Update account input
    tk.Label(window, text="New Name").pack()
    new_name_entry = tk.Entry(window)
    new_name_entry.pack()

    tk.Label(window, text="New Phone").pack()
    new_phone_entry = tk.Entry(window)
    new_phone_entry.pack()

    def handle_update_account():
        new_name = new_name_entry.get()
        new_phone = new_phone_entry.get()
        account_id = int(account_id_entry.get())
        if new_name and new_phone:
            update_account(account_id, new_name, new_phone)  # Call the update_account function from main.py
            messagebox.showinfo("Success", "Account details updated!")
        else:
            messagebox.showerror("Error", "Please enter both new name and phone.")

    tk.Button(window, text="Update Account", command=handle_update_account).pack(pady=10)

    # Delete account button
    def handle_delete_account():
        account_id = int(account_id_entry.get())
        delete_account(account_id)  # Call the delete_account function from main.py
        messagebox.showinfo("Success", "Account deleted!")
        show_login_form()  # Show login form after account deletion

    tk.Button(window, text="Delete Account", command=handle_delete_account).pack(pady=10)

# Show the login form first when the app starts
show_login_form()

# Run the main loop to keep the app running
window.mainloop()
