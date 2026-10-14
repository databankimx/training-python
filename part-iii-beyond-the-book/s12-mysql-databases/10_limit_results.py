"""Limit Results"""

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
    print("Connection closed")

def get_five_rows(conn: mysql.connector.connection) -> None:
    """Retrieve five rows from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers LIMIT 5"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print()

def offset_five_rows(conn: mysql.connector.connection) -> None:
    """Retrieve five rows from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print()

def main() -> None:
    """Main function"""
    settings = get_settings()
    conn = connect(settings)
    get_five_rows(conn)
    offset_five_rows(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
