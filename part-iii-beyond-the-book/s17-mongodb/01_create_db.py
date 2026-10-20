"""Create a new database in MongoDB"""

from login import get_settings, get_client, server_connected
from pymongo import MongoClient

def connect() -> MongoClient|None:
    """Connect to MongoDB"""
    client = get_client()
    if not client:
        print("Failed to obtain MongoClient")
        return None
    if not server_connected(client):
        print("MongoDB Server not connected")
        return None
    print("MongoDB server is connected")
    print()
    return client

def make_db(client: MongoClient, db_name: str):
    """Create a new database in MongoDB"""
    db = client[db_name]
    print(f"Created database: `{db.name}`")
    print()

def list_databases(client: MongoClient) -> list[str]:
    """List the available databases in MongoDB"""
    databases = client.list_database_names()
    if databases:
        print("Available databases:")
        for db in databases:
            print(f"• {db}")
    else:
        print("No databases found")
    print()
    return databases

def db_exists(db_names: list[str], db_name: str) -> bool:
    """Check if a database exists in MongoDB"""
    return db_name in db_names

def main() -> None:
    """Main function"""
    client = connect()
    if not client:
        return
    settings = get_settings()
    db_name = settings["db_name"]
    make_db(client, db_name)
    db_names = list_databases(client)
    print(f"`{db_name}` ", end="")
    if db_exists(db_names, db_name):
        print("exists\n")
    else:
        print("does not exist\n")
    client.close()

if __name__ == "__main__":
    main()
