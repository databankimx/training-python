"""Create a new database on the MySQL Server"""

import mysql.connector
# pylint: disable=no-name-in-module
from utility_functions import get_settings

def connect(settings: dict[str, str]) -> mysql.connector.connection:
    """Connect to MySQL Server"""
    conn = mysql.connector.connect(
        host=settings["host"],
        user=settings["username"],
        password=settings["password"]
    )
    print(f"Connected to {conn.server_host}: {conn.server_port}\n")
    return conn

def disconnect(conn: mysql.connector.connection) -> None:
    """Disconnect from MySQL Server"""
    if conn is not None or not conn.is_connected():
        conn.disconnect()

def create_database(conn: mysql.connector.connection, name: str) -> None:
    """Create a new database on the MySQL Server"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    cursor = conn.cursor()
    sql = f"CREATE DATABASE IF NOT EXISTS {name}"
    cursor.execute(sql)
    conn.commit()
    print(f"Database '{name}' created successfully!\n")

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

def main() -> None:
    """Main function"""
    settings = get_settings()
    conn = connect(settings)
    create_database(conn, settings["schema"])
    list_databases(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
