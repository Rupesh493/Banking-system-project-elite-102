import mysql.connector
def connect_database():
    return mysql.connector.connect(
        user='root', database='banking system', password='Godblessyou@77'
    )
def register_account(name,pin,phone):
    connection = connect_database
    cursor = connection.cursor()
    query = "insert into accounts (name,pin,phone,balance) values (%s,%s,%s,%s)"
    cursor.execute(query,(name,pin,phone,0.0))
    cursor.close()
    connection.commit()

def view_balance(account_id):
    connection = connect_database
    cursor = connection.cursor()
    query = "select balance from accounts where account_id = (%s)"
    cursor.execute(query, (account_id,))
    cursor.close()
    account = cursor.fetchone()
    connection.close() 
    if account:
        return f"The balance for account {account_id} is {account[0]}"
    else:
        return "Account not found"
    
