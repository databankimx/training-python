"""Cleanup MySQL Database"""

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

def drop_tables(conn: mysql.connector.connection) -> None:
    """Retrieve all rows from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    tables = ["customers", "users", "products"]
    for table in tables:
        sql = f"DROP TABLE IF EXISTS {table}"
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print(f"Table {table} dropped")
    print()

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
    print()

def drop_database(conn: mysql.connector.connection) -> None:
    """Retrieve all rows from the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    db = "mydatabase"
    sql = f"DROP DATABASE IF EXISTS {db}"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(f"Database {db} dropped")
    print()

def list_databases(conn: mysql.connector.connection) -> None:
    """List the available databases on the MySQL Server"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    cursor = conn.cursor()
    sql = "SHOW DATABASES"
    cursor.execute(sql)
    print("DATABASES:")
    for database in cursor:
        print(f" - {database[0]}")
    print()

def main() -> None:
    """Main function"""
    settings = get_settings()
    conn = connect(settings)
    print("Before dropping tables:")
    list_tables(conn)
    drop_tables(conn)
    print("After dropping tables:")
    list_tables(conn)
    print("Before dropping database:")
    list_databases(conn)
    drop_database(conn)
    print("After dropping database:")
    list_databases(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
