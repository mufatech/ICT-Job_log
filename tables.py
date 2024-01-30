import mysql.connector


# Establish connection
connection = mysql.connector.connect(
    host= 'localhost',
    user= 'mufatech',
    passwd = 'mufatech',
    database= 'ict_log'
    
)

# Create cursor
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SHOW TABLES")

# Fetch and display results
tables = cursor.fetchall()
for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
connection.close()




