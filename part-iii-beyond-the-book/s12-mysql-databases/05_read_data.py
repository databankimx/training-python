"""Read data from MySQL Database Table"""

import mysql.connector
# pylint: disable=no-name-in-module
from mysql.connector.connection import MySQLConnection
from utility_functions import get_settings

def connect(settings: dict[str, str]) -> MySQLConnection:
    """Connect to MySQL Server"""
    conn = mysql.connector.connect(
        host=settings["host"],
        user=settings["username"],
        password=settings["password"],
        database=settings["schema"]
    )
    print(f"Connected to {conn.server_host}: {conn.server_port}\n")
    return conn

def disconnect(conn: MySQLConnection) -> None:
    """Disconnect from MySQL Server"""
    if conn is not None and conn.is_connected():
        conn.disconnect()
        print("\nConnection closed")

def get_all_rows(conn: MySQLConnection) -> None:
    """Retrieve all rows from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print()

def get_two_columns(conn: MySQLConnection) -> None:
    """Retrieve specific columns from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT name, address FROM customers"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print()

def get_one_row(conn: MySQLConnection) -> None:
    """Retrieve one row from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers"
    cursor = conn.cursor()
    cursor.execute(sql)
    print(cursor.fetchone(), "\n")

def main() -> None:
    """Main function"""
    settings = get_settings()
    conn = connect(settings)
    get_all_rows(conn)
    get_two_columns(conn)
    get_one_row(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
