"""Retrieve records from MongoDB collection"""

from login import get_settings, get_client, server_connected
from pymongo import MongoClient
from pymongo.synchronous.collection import Collection

def connect(settings: dict[str, any]=None) -> tuple[MongoClient, Collection]|None:
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
    return (client, col)

def get_record(col: Collection) -> None:
    """Retrieve a single record from MongoDB collection"""
    if col is None:
        print("No active MongoDB collection")
        return None
    res = col.find_one()
    print("Find One Record:")
    if res:
        print(res)
    else:
        print("No records found")
    print()

def get_all_records(col: Collection) -> None:
    """Retrieve all records from MongoDB collection"""
    if col is None:
        print("No active MongoDB collection")
        return None
    print("Find All Records:")
    for res in col.find():
        print(res)
    print()

def get_filtered_records(col: Collection, doc_filter: dict[str, any]) -> None:
    """Retrieve records from MongoDB collection based on filter"""
    if col is None:
        print("No active MongoDB collection")
        return None
    print(f"Find Records with Filter {doc_filter}:")
    for res in col.find(doc_filter):
        print(res)
    print()

def get_all_no_id(col: Collection) -> None:
    """Retrieve all records from MongoDB collection, excluding '_id' field"""
    if col is None:
        print("No active MongoDB collection")
        return None
    print("Find All Records (excluding `_id`):")
    proj = {"_id": 0}
    for res in col.find({}, proj):
        print(res)
    print()

def main() -> None:
    """Main function"""
    settings = get_settings()
    client, col = connect(settings)
    get_record(col)
    get_all_records(col)
    doc_filter = {"name": "John"}
    get_filtered_records(col, doc_filter)
    get_all_no_id(col)
    client.close()

if __name__ == "__main__":
    main()
