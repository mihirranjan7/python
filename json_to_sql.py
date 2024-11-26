import json
import mysql.connector
import os

# Configuration for MySQL Database Connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'company'
}

# Directory containing JSON files
json_directory = 'json_files'

# Target Table Name
table_name = 'company_data'

def escape_sql_value(value):
    """Escape and format SQL values."""
    if value is None or value == "":
        return "NULL"  # Handle NULL values
    if isinstance(value, str):
        escaped_value = value.replace("'", "''").replace("\\", "\\\\")  # Escape single quotes and backslashes
        return f"'{escaped_value}'"
    return f"'{value}'"

def convert_to_sql(record):
    """Generate an SQL INSERT statement dynamically based on the record."""
    if isinstance(record, dict):
        columns = ', '.join(f"`{key}`" for key in record.keys())  # Escape column names
        values = ', '.join(escape_sql_value(value) for value in record.values())
        return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    else:
        raise ValueError("Record is not a dictionary")

def process_json_file(file_path, table_name, db_config):
    """Process a single JSON file and insert data into the database."""
    # Load JSON data with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Debug: print the loaded data to see its structure
    print(f"Loaded data from {file_path}: {data}")

    # Handle both single dictionary and list of dictionaries
    if isinstance(data, dict):  # If it's a single dictionary
        data = [data]  # Convert it to a list of one dictionary for processing
        print(f"Converted single dictionary to list: {data}")

    elif not isinstance(data, list):  # If it's neither a dictionary nor a list
        print(f"Unexpected data format in {file_path}. Skipping file.")
        return

    # Process data if it's a list (or converted to a list)
    sql_statements = []
    for record in data:
        try:
            sql_statements.append(convert_to_sql(record))
        except ValueError as e:
            print(f"Skipping invalid record: {e}")

    # Execute SQL statements in the database
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        for sql in sql_statements:
            cursor.execute(sql)
        connection.commit()
        print(f"Data from {file_path} successfully inserted into the database.")
    except mysql.connector.Error as err:
        print(f"Error with file {file_path}: {err}")
    finally:
        if 'connection' in locals():
            connection.close()

def process_all_json_files(directory, table_name, db_config):
    """Process all JSON files in a directory."""
    for filename in os.listdir(directory):
        if filename.endswith('.json'):  # Only process JSON files
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")
            process_json_file(file_path, table_name, db_config)

# Run the script
if __name__ == '__main__':
    process_all_json_files(json_directory, table_name, db_config)
