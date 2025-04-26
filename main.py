import mysql.connector
def connect_to_database():
    return mysql.connector.connect(
         user='root',
         password='Godblessyou@77',
         database='banking_system'
    )
import mysql.connector

def register_account(name, pin, phone):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = """
    INSERT INTO accounts (name, pin, phone, balance)
    VALUES (%s, %s, %s, %s)
    """
    values = (name, pin, phone, 0.00)  # Starting balance is 0.00

    cursor.execute(query, values)
    connection.commit()

    print("Account registered successfully!")

    cursor.close()
    connection.close()
