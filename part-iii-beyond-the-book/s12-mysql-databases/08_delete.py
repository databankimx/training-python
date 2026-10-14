"""Delete rows from database table"""

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

def delete_rows(conn: mysql.connector.connection) -> None:
    """Delete rows from `customers`"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record(s) deleted\n")

def parameterize(conn: mysql.connector.connection) -> None:
    """Delete rows from `customers`"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    sql = "DELETE FROM customers WHERE address = %s"
    params = ("Yellow Garden 2", )
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    print(cursor.rowcount, "record(s) deleted\n")

def main() -> None:
    """Main program"""
    settings = get_settings()
    conn = connect(settings)
    delete_rows(conn)
    parameterize(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
