"""Update rows in database table"""

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

def update_rows(conn: MySQLConnection) -> None:
    """Update rows in `customers`"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "UPDATE customers SET address = 'Canyon 123' " + \
          "WHERE address = 'Valley 345'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record(s) affected\n")

def parameterize(conn: MySQLConnection) -> None:
    """Update rows in `customers`"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "UPDATE customers SET address = %s WHERE address = %s"
    params = ("Valley 345", "Canyon 123")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    print(cursor.rowcount, "record(s) affected\n")

def main() -> None:
    """Main program"""
    settings = get_settings()
    conn = connect(settings)
    update_rows(conn)
    parameterize(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
