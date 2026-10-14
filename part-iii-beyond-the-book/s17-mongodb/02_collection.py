"""Create a new collection in MongoDB"""

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
    return (client, db)

def make_collection(db: Database, settings: dict[str, any]=None) -> None:
    """Create a new collection in MongoDB"""
    if not settings:
        settings = get_settings()
    collection = db[settings["col_name"]]
    print(f"Created collection: `{collection.name}`\n")

def get_collections(db: Database, settings: dict[str, any]=None) -> None:
    """List collections in MongoDB"""
    if not settings:
        settings = get_settings()
    collections = db.list_collection_names()
    print(f"Collections in database `{db.name}`:")
    for collection in collections:
        print(f"• {collection}")
    print()
    col_name = settings["col_name"]
    print(f"Collection `{col_name}`", end=" ")
    if col_name in collections:
        print("exists\n")
    else:
        print("does not exist\n")

def main() -> None:
    """Main function"""
    settings = get_settings()
    client, db = connect(settings)
    make_collection(db, settings)
    get_collections(db, settings)

    client.close()

if __name__ == "__main__":
    main()
