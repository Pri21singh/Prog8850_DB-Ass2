import mysql.connector
from mysql.connector import Error

# Database connection details
DB_CONFIG = {
    "host": "server host name",
    "user": "user name",
    "password": "the password",
    "database": "db name"
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