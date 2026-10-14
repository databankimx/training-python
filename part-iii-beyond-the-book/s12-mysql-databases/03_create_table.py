"""Create a table in MySQL database"""

import mysql.connector
# pylint: disable=no-name-in-module
from utility_functions import get_settings

def connect(settings: dict[str, str]) -> mysql.connector.connection:
    """Connect to MySQL Server"""
    conn = mysql.connector.connect(
        host=settings["host"],
        user=settings["username"],
        password=settings["password"],
        database = settings["schema"]
    )
    print(f"Connected to {conn.server_host}: {conn.server_port}\n")
    return conn

def disconnect(conn: mysql.connector.connection) -> None:
    """Disconnect from MySQL Server"""
    if conn is not None or not conn.is_connected():
        conn.disconnect()
    print("\nConnection closed")

def create_table(conn: mysql.connector.connection) -> None:
    """Create a new table in the MySQL database"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS customers " + \
          "(name VARCHAR(255), address VARCHAR(255))"
    cursor.execute(sql)
    conn.commit()
    print("Table `customers` created successfully!\n")

def add_primary_key(conn: mysql.connector.connection) -> None:
    """Add a primary key to the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "ALTER TABLE customers " + \
          "ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("Column `id` added successfully!\n")

def list_columns(conn: mysql.connector.connection) -> None:
    """List the columns in the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SHOW COLUMNS in customers"
    cursor = conn.cursor()
    cursor.execute(sql)
    print("COLUMNS in `customers`:")
    for column in cursor:
        print(f"- {column[0]} {column[1]}")

def list_tables(conn: mysql.connector.connection) -> None:
    """List the available tables in the MySQL database"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    cursor = conn.cursor()
    sql = "SHOW TABLES"
    cursor.execute(sql)
    print("TABLES:")
    for table in cursor:
        print(f" - {table[0]}")

def main() -> None:
    """Main function"""
    settings = get_settings()
    conn = connect(settings)
    create_table(conn)
    list_tables(conn)
    add_primary_key(conn)
    list_columns(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
