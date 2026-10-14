"""Filter data from MySQL Server"""

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

def filter_equal(conn: mysql.connector.connection) -> None:
    """Retrieve matching rows from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print()

def filter_like(conn: mysql.connector.connection) -> None:
    """Retrieve matching rows from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
    print()

def parameterize(conn: mysql.connector.connection) -> None:
    """Retrieve matching rows from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT * FROM customers WHERE address =%s"
    params = ("Yellow Garden 2",)
    cursor = conn.cursor()
    cursor.execute(sql, params)
    for row in cursor.fetchall():
        print(row)
    print()

def main() -> None:
    """Main function"""
    settings = get_settings()
    conn = connect(settings)
    filter_equal(conn)
    filter_like(conn)
    parameterize(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
