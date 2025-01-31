import mysql.connector
from mysql.connector import Error
import config


# Database connection details
db_config = config.db_config

try:
    # Establish the connection
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Connected to the database")

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a simple query to get the server and database information
        cursor.execute("SELECT DATABASE();")
        database_name = cursor.fetchone()
        print(f"You're connected to database: {database_name[0]}")

        # Execute a query to fetch some data, like the list of tables
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("List of tables in the database:")
        for table in tables:
            print(f"- {table[0]}")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")