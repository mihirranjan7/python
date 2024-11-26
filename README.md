 JSON to MySQL Importer

 Description

This project is designed to import JSON data into a MySQL database. It reads JSON files from a specified directory, processes them, and inserts the data into a table in a MySQL database. The program handles both single dictionaries and lists of dictionaries within the JSON files, making it flexible for different data structures.

 Features

- Supports importing data from JSON files into MySQL tables.
- Handles both single JSON objects and lists of JSON objects.
- Escapes special characters (e.g., quotes and backslashes) in data.
- Configurable MySQL connection settings.
- Processes all JSON files in a specified directory.

 Requirements

- Python 3.x
- MySQL 5.x or above
- MySQL Connector for Python

 Installation

 1. Clone the repository:
bash
git clone https://github.com/mihirranjan7/python.git
cd json-to-mysql-importer


 2. Install dependencies:
You need to install mysql-connector-python for database interaction.

bash
pip install mysql-connector-python


 3. Configure MySQL Database:
Make sure you have a MySQL database set up and replace the db_config in the script with your MySQL credentials:
python
db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}


 4. Prepare the JSON Files:
Put your JSON files inside the json_files directory. The script will read all the .json files in this directory.

 5. Set Up the MySQL Table:
Make sure the target table (company_data) exists in the MySQL database. You may need to modify the script to match your table's structure or create a new table based on the JSON data.

 6. Run the Script:
bash
python json_to_mysql.py


This will read the JSON files from the json_files directory and insert the data into the MySQL database table.

 Script Overview

 Key Functions:

- escape_sql_value(value): Escapes special characters in the values to avoid SQL injection or syntax errors.
- convert_to_sql(record): Converts a dictionary record into an SQL INSERT statement.
- process_json_file(file_path, table_name, db_config): Processes an individual JSON file, converts the data, and inserts it into the database.
- process_all_json_files(directory, table_name, db_config): Processes all JSON files in the specified directory.

 Handling Errors

If a record is invalid or cannot be processed, it will be skipped, and the error message will be displayed in the console.

 License

This project is open-source and available under the MIT License.
