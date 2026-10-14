"""Drop a collection from MongoDB"""

from login import get_settings, get_client, server_connected
from pymongo import MongoClient
from pymongo.synchronous.database import Database

def connect(settings: dict[str, any]=None) -> tuple[MongoClient, Database]|None:
    """Connect to MongoDB database"""
    if not settings:
        settings = get_settings()
    client = get_client(settings)
    if not client:
        print("Failed to obtain MongoClient")
        return None
    if not server_connected(client):
        print("MongoDB Server not connected")
        return None
    print("MongoDB server is connected\n")
    db = client[settings["db_name"]]
    print(f"Connected to database: `{db.name}`\n")
    col = db[settings["col_name"]]
    print(f"Connected to collection: `{col.name}`\n")
    return (client, db)

def view_databases(client: MongoClient) -> None:
    """View all databases in the MongoDB server"""
    if not client:
        return
    databases = client.list_database_names()
    print("Available databases:")
    for db_name in databases:
        print(f"• {db_name}")
    print()

def view_collections(db: Database) -> None:
    """View all collections in the specified database"""
    collections = db.list_collection_names()
    print(f"Collections in database `{db.name}`:")
    for col_name in collections:
        print(f"• {col_name}")
    print()

def remove_collection(db: Database, col_name: str) -> None:
    """Remove a collection from the specified database"""
    view_collections(db)
    print(f"Removing collections: `{col_name}`...")
    if col_name in db.list_collection_names():
        db.drop_collection(col_name)
        print(f"Collection '{col_name}' removed successfully.")
    else:
        print(f"Collection '{col_name}' does not exist.")
    print()
    view_collections(db)

def remove_database(client: MongoClient, db_name: str) -> None:
    """Remove a database from the MongoDB server"""
    view_databases(client)
    print(f"Removing database: `{db_name}`...")
    client.drop_database(db_name)
    print(f"Database '{db_name}' removed.\n")
    view_databases(client)

def main() -> None:
    """Main function"""
    settings = get_settings()
    client, db = connect(settings)

    remove_collection(db, settings["col_name"])
    print("-----\n")
    remove_database(client, settings["db_name"])

    client.close()

if __name__ == "__main__":
    main()
