import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL command to create the database (only if it doesn't exist)
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            # Execute the query
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"except mysql.connector.Error")

    finally:
        # Close the cursor and connection
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
