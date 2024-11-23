#########################################################################################
################################## This is a file #######################################
#########################################################################################


import sqlite3


def create_random_string(length: int) -> str:
    '''
    This function will create a random string 
    by using the parameter length for the number
    of characters will be used.

    :param length: An integer number for the length
    of the string which will be created.
    :param type: int
    :return: str
    '''
    import random
    import string
    # Define the character set to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def create_database(database_name: str) -> None:
    '''
    This function will create a database in your
    current directory with a table for users.
    
    :param database_name: Name of the database file.
    :type: str
    :return: None
    '''
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')
        
        print(f"Database '{database_name}' created successfully.")
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


def add_data_to_database(database_name: str, data: list) -> None:
    """
    Add data to the users table in a SQLite database.

    :param database_name: Name of the SQLite database file
    :param data: List of tuples containing the data to be inserted
    :return: None
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Prepare the INSERT statement
        insert_query = "INSERT INTO users (name, age) VALUES (?, ?)"

        # Execute the INSERT statement for each data tuple
        cursor.executemany(insert_query, data)

        # Commit the changes
        conn.commit()
        print(f"Successfully added {len(data)} rows to 'users' table.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


def retrieve_and_print_data(database_name: str) -> None:
    """
    Retrieves all data from the users table in a SQLite database and prints it.

    :param database_name: Name of the SQLite database file
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Execute a SELECT query to retrieve all data from the table
        cursor.execute("SELECT * FROM users")

        # Fetch all rows
        rows = cursor.fetchall()

        # Get column names
        column_names = [description[0] for description in cursor.description]

        # Print column names
        print("| " + " | ".join(column_names) + " |")
        print("-" * (sum(len(name) for name in column_names) + 3 * len(column_names) + 1))

        # Print each row
        for row in rows:
            print("| " + " | ".join(str(item) for item in row) + " |")

        print(f"\nTotal rows: {len(rows)}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


