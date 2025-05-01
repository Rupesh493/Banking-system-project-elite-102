import mysql.connector #import mysql connector
def connect_database():
    return mysql.connector.connect(
        user='root', database='banking system', password='Godblessyou@77'
    )
def register_account(name,pin,phone):
    connection = connect_database() #to connect to the database
    cursor = connection.cursor()  # to execute sql queries 
    query = "insert into accounts (name,pin,phone,balance) values (%s,%s,%s,%s)"  # %s used as place holders
    cursor.execute(query,(name,pin,phone,0.0))  #execute the query with provided values 
    cursor.close()  #used to close a cursor
    connection.commit()   #used to commit the changes 

def view_balance(account_id): 
    connection = connect_database() 
    cursor = connection.cursor()
    query = "select balance from accounts where account_id = (%s)" #sql command to select the balance of the given account id 
    cursor.execute(query, (account_id,))
    account = cursor.fetchone() #to get the a row of the account id
    cursor.close()
    connection.close() 
    if account:
        return f"The balance for account {account_id} is {account[0]}"
    else:
        return "Account not found"

def update_account(account_id,pin,number):
    connection = connect_database()
    cursor = connection.cursor()
    query = "update accounts set account_id = %s, pin = %s, number = %s" #Sql query to update the account's id,pin,number
    cursor.execute(query,(account_id,pin,number)) 
    connection.commit() #to save the changes to the database
    cursor.close()
    connection.close()

def delete_account(account_id,pin,number,balance):
    connection = connect_database()
    if connection is None:  #if connection fails it returns nothing
        return
    cursor = connection.cursor()
    try:
        query = "delete from accounts where account_id = %s"
        cursor.execute(query,(account_id,pin,number,balance))
        connection.commit()
        return f"Account {account_id} deleted"
    finally:
        cursor.close()
        connection.close()

def deposit(account_id,balance):
    connection = connect_database()
    if connection is None:
        return "connection failed"
    cursor = connection.cursor()
    try:
        query = "Update accounts set balance = balance + %s where account_id = %s"
        cursor.execute(query,(account_id,balance))
        connection.commit()
        return(f"deposited {balance} into account {account_id}")
    finally:
        cursor.close()
        connection.commit()

def withdraw(account_id,balance):
    connection = connect_database()
    if connection is None:
        return "connection failed"
    cursor = connection.cursor()
    try:
        query = "Update accounts set balance = balance - %s where account_id = %s"
        cursor.execute(query,(account_id,balance))
        connection.commit()
        return(f"withdrew {balance} into accounts {account_id}")
    finally:
        cursor.close()
        connection.commit()

    


