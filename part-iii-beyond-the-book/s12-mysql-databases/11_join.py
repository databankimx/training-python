"""Joining Tables"""

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

def inner_join(conn: MySQLConnection) -> None:
    """Join users and products with an inner join"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT users.name, products.name FROM users " + \
          "INNER JOIN products ON users.fav = products.id"
    cursor = conn.cursor()
    cursor.execute(sql)
    print("INNER JOIN")
    for row in cursor.fetchall():
        print(row)
    print()

def left_join(conn: MySQLConnection) -> None:
    """Join users and products with a left outer join"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT users.name, products.name FROM users " + \
          "LEFT OUTER JOIN products ON users.fav = products.id"
    cursor = conn.cursor()
    cursor.execute(sql)
    print("LEFT OUTER JOIN")
    for row in cursor.fetchall():
        print(row)
    print()

def right_join(conn: MySQLConnection) -> None:
    """Join users and products with a right outer join"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "SELECT users.name, products.name FROM users " + \
          "RIGHT OUTER JOIN products ON users.fav = products.id"
    cursor = conn.cursor()
    cursor.execute(sql)
    print("RIGHT OUTER JOIN")
    for row in cursor.fetchall():
        print(row)
    print()

def main() -> None:
    """Main function"""
    settings = get_settings()
    conn = connect(settings)
    inner_join(conn)
    left_join(conn)
    right_join(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
