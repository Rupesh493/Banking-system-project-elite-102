import mysql.connector
from mysql.connector import Error

# Function to connect to the database
def connect_to_database():
    try:
        return mysql.connector.connect(
            user='root',
            password='Godblessyou@77',
            database='banking_system'
        )
    except Error as e:
        print(f"Error: {e}")
        return None  # Return None if connection fails

# Register a new account
def register_account(name, pin, phone):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Query to insert a new account into the database
        query = """
        INSERT INTO accounts (name, pin, phone, balance)
        VALUES (%s, %s, %s, %s)
        """
        values = (name, pin, phone, 0.00)  # Starting balance is 0.00
        cursor.execute(query, values)
        connection.commit()

        print(f"Account for {name} registered successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Login function (checks if account exists)
def login(name, pin):
    connection = connect_to_database()
    if connection is None:
        return False

    cursor = connection.cursor()

    try:
        # Query to check if account exists with matching name and pin
        query = "SELECT * FROM accounts WHERE name = %s AND pin = %s"
        cursor.execute(query, (name, pin))
        result = cursor.fetchone()

        if result:
            print(f"Login successful for account {name}")
            return True
        else:
            print("Invalid name or PIN")
            return False
    except Error as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connection.close()

# View balance for an account
def view_balance(account_id):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Query to get the balance of the specified account
        query = "SELECT balance FROM accounts WHERE account_id = %s"
        cursor.execute(query, (account_id,))
        result = cursor.fetchone()

        if result:
            balance = result[0]
            print(f"Balance for account {account_id}: {balance}")
        else:
            print("Account not found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Deposit money into an account
def deposit_money(account_id, amount):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Query to update the account balance
        query = "UPDATE accounts SET balance = balance + %s WHERE account_id = %s"
        cursor.execute(query, (amount, account_id))
        connection.commit()

        print(f"Deposited {amount} into account {account_id}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Withdraw money from an account
def withdraw_money(account_id, amount):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Query to get the current balance
        cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
        current_balance = cursor.fetchone()

        if current_balance and current_balance[0] >= amount:
            # Query to update the account balance
            query = "UPDATE accounts SET balance = balance - %s WHERE account_id = %s"
            cursor.execute(query, (amount, account_id))
            connection.commit()
            print(f"Withdrew {amount} from account {account_id}")
        else:
            print("Insufficient funds or account does not exist")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Update account details (for example, name or phone)
def update_account(account_id, new_name, new_phone):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Query to update account details
        query = "UPDATE accounts SET name = %s, phone = %s WHERE account_id = %s"
        cursor.execute(query, (new_name, new_phone, account_id))
        connection.commit()

        print(f"Account {account_id} details updated")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Delete an account
def delete_account(account_id):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Query to delete the account
        query = "DELETE FROM accounts WHERE account_id = %s"
        cursor.execute(query, (account_id,))
        connection.commit()

        print(f"Account {account_id} deleted")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
