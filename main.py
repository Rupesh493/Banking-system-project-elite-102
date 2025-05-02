import mysql.connector
def connect_database():
     return mysql.connector.connect(
         user='root', database='banking_system', password='Godblessyou@77'
     )
def register_account(name, pin, phone):
    try:
        connection = connect_database() #to connect to the database
        cursor = connection.cursor()  #to execute sql queries
        query = "INSERT INTO accounts (name, pin, phone, balance) VALUES (%s, %s, %s, %s)"  #sql query to add account
        cursor.execute(query, (name, pin, phone, 0.0)) #to execute sql query
        connection.commit()   # to tommit the changes to the database
        print("Account registered successfully!")
    
    except mysql.connector.Error as err:  #to handle sql errors
        print(f"Error: {err}")
    
    except Exception as e:  #error handling
        print(f"An error occurred: {e}")
    
    finally:  #close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
def view_balance(account_id): 
    connection = connect_database() #to connect to the database
    cursor = connection.cursor()  # to execute sql queries 
    query = "insert into accounts (name,pin,phone,balance) values (%s,%s,%s,%s)"  # %s used as place holders
    cursor.execute(query,(name,pin,phone,0.0))  #execute the query with provided values 
    cursor.close()  #used to close a cursor
    connection.commit()   #used to commit the changes 
   
def update_account(account_id,pin,phone):
    connection = connect_database()
    cursor = connection.cursor()
    query = "update accounts set pin = %s, phone = %s where account_id = %s" #Sql query to update the account's id,pin,number
    cursor.execute(query,(pin,phone,account_id)) 
    connection.commit() #to save the changes to the database
    cursor.close()
    connection.close()

def delete_account(account_id):
    connection = connect_database()
    if connection is None:  #if connection fails it returns nothing
        return
    cursor = connection.cursor()
    try:
        query = "delete from accounts where account_id = %s" #to delete the account with the matching account id
        cursor.execute(query,(account_id,))
        connection.commit()
        return f"Account {account_id} deleted"
    finally:
        cursor.close()
        connection.close()

def deposit(account_id,balance):  #function to deposit
    connection = connect_database()
    if connection is None:
        return "connection failed"
    cursor = connection.cursor()
    try:
        query = "Update accounts set balance = balance + %s where account_id = %s" #sql query to add the amount to the balance
        cursor.execute(query,(balance,account_id))  #to execute the query
        connection.commit()
        return(f"deposited {balance} into account {account_id}")
    finally:
        cursor.close()
        connection.close()

def withdraw(account_id,balance):  #function to withdraw
    connection = connect_database()
    if connection is None:
        return "connection failed"
    cursor = connection.cursor()
    try:
        query = "Update accounts set balance = balance - %s where account_id = %s"  #sql query to subtract the amount from the balance 
        cursor.execute(query,(balance,account_id))  #to execute the query
        connection.commit()
        return f"withdrew {balance} from accounts {account_id}" #return message
    finally:
        cursor.close()
        connection.close()

    


