"""Prepare the MySQL database tables"""

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
    print("\nConnection closed")

def create_tables(conn: mysql.connector.connection) -> None:
    """Create a new table in the MySQL database"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    cursor = conn.cursor()
    table_sql = {
        "users": "CREATE TABLE IF NOT EXISTS users " + \
        "(id INT PRIMARY KEY, name VARCHAR(255), fav INT)",
        "products": "CREATE TABLE IF NOT EXISTS products " + \
        "(id INT PRIMARY KEY, name VARCHAR(255))"
    }
    for name, sql in table_sql.items():
        cursor.execute(sql)
        conn.commit()
        print(f"Table `{name}` created successfully!")
    print()

def add_data(conn: mysql.connector.connection) -> None:
    """Add a primary key to the `customers` table"""
    if not conn.is_connected():
        print("No active connection to MySQL Server!")
        return
    columns = {
        "users": "id, name, fav",
        "products": "id, name"
    }
    data = {
        "users": [
            (1, "John", 154),
            (2, "Peter", 154),
            (3, "Amy", 155),
            (4, "Hannah", None),
            (5, "Michael", None)
        ],
        "products": [
            (154, "Chocolate Heaven"),
            (155, "Tasty Lemons"),
            (156, "Vanilla Dreams")
        ]
    }
    cursor = conn.cursor()
    for name, cols in columns.items():
        placeholder = "%s" + (", %s" * (len(data[name][0]) - 1))
        sql = f"INSERT INTO {name} ({cols}) VALUES ({placeholder})"
        print(sql)
        cursor.executemany(sql, data[name])
        conn.commit()
        print(f"{cursor.rowcount} record(s) added\n")

def main() -> None:
    """Main function"""
    settings = get_settings()
    conn = connect(settings)
    create_tables(conn)
    add_data(conn)
    disconnect(conn)

if __name__ == "__main__":
    main()
