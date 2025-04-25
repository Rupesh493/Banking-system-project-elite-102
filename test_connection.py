import mysql.connector

connection = mysql.connector.connect(
    host='localhost',            # usually 'localhost'
    user='root',                 # your MySQL username
    password='Godblessyou@77',    # your MySQL password
    database='banking_system'    # the name of your database
)

print("Connection successful!")

connection.close()

import mysql.connector

# Establish the connection to MySQL
connection = mysql.connector.connect(
    user='root',       # Replace with your MySQL username
    password='Godblessyou@77',   # Replace with your MySQL password
    database='banking_system'    # Replace with your database name
)

# Check if the connection is successful
if connection.is_connected():
    print("Connection successful!")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# The SQL query to retrieve data from your table
testQuery = "SELECT * FROM accounts;"  # Replace 'accounts' with the name of your table

# Execute the query
cursor.execute(testQuery)

# Fetch and print the results
for item in cursor:
    print(item)

# Close the cursor and connection
cursor.close()
connection.close()

import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='Godblessyou@77',
    database='banking_system'
)

cursor = connection.cursor()

# Replace with your actual column names and values
addData = """
INSERT INTO accounts (name, pin, balance, phone)
VALUES ('George Washington', '4567', 500.00, '555-1234')
"""

cursor.execute(addData)

connection.commit()

cursor.close()
connection.close()
