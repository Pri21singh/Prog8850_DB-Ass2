import mysql.connector
from mysql.connector import Error

# Database connection details
DB_CONFIG = {
    "host": "priyasin94.mysql.database.azure.com",  # Update with the MySQL server name
    "user": "priyas1994",        # Update with the MySQL admin user name
    "password": "Software@2025",   # Update with the MySQL password
    "database": "companydb"  # Update with the database name
}

def execute_sql_script(sql_file):
    connection = None
    cursor = None
    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Read SQL file
        with open(sql_file, "r") as file:
            sql_commands = file.read().split(";")

        # Execute each SQL command
        for command in sql_commands:
            command = command.strip()  # Remove any leading/trailing whitespace
            if command:  # Skip empty commands
                print(f"Executing command: {command[:50]}...")  # Debugging output
                cursor.execute(command)
                connection.commit()  # Commit after each command

        print("SQL script executed successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        # Ensure cursor and connection are closed properly
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    execute_sql_script("schema_changes.sql")