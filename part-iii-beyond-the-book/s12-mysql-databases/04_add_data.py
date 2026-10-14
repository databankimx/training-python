"""Add Data to MySQL Database Table"""

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

def clear_table(conn: mysql.connector.connection) -> None:
    """Clear out all records from the `customers` table"""
    # Performing this task to allow the code to be run more than once
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "TRUNCATE TABLE customers"
    cursor = conn.cursor()
    cursor.execute(sql)

def add_row(conn: mysql.connector.connection, data: tuple[str, str]) -> None:
    """Add a new row to the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    print(f"{cursor.rowcount} row(s) inserted.")
    print(f"Last inserted ID: {cursor.lastrowid}\n")

def add_rows(conn: mysql.connector.connection,
             data: list[tuple[str, str]]):
    """Add a multiple rows to the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    cursor = conn.cursor()
    cursor.executemany(sql, data)
    conn.commit()
    print(f"{cursor.rowcount} row(s) inserted.")
    print(f"Last inserted ID: {cursor.lastrowid}\n")

def main() -> None:
    """Main program"""
    settings = get_settings()
    conn = connect(settings)
    clear_table(conn)
    one_row = ("John", "Highway 21")
    add_row(conn, one_row)
    multiple = [
        ("Peter", "Lowstreet 4"),
        ("Amy", "Apple st 652"),
        ("Hannah", "Mountain 21"),
        ("Michael", "Valley 345"),
        ("Sandy", "Ocean blvd 2"),
        ("Betty", "Green Grass 1"),
        ("Richard", "Sky st 331"),
        ("Susan", "One way 98"),
        ("Vicky", "Yellow Garden 2"),
        ("Ben", "Park Lane 38"),
        ("William", "Central st 954"),
        ("Chuck", "Main Road 989"),
        ("Viola", "Sideway 1633")
    ]
    add_rows(conn, multiple)
    one_row = ("Michelle", "Blue Village")
    add_row(conn, one_row)

    disconnect(conn)

if __name__ == "__main__":
    main()
