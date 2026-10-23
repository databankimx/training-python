"""Sort Data"""

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
        print("Connection closed")

def sort_data(conn: MySQLConnection) -> None:
    """Retrieve rows from `customers` sorted by name"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers ORDER BY name"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print()

def sort_desc(conn: MySQLConnection) -> None:
    """Retrieve rows from `customers` reverse sorted by address"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers ORDER BY address DESC"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print()

def main() -> None:
    """Main Function"""
    settings = get_settings()
    conn = connect(settings)
    sort_data(conn)
    sort_desc(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
