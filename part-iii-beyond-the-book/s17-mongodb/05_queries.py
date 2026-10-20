"""Perform queries on MongoDB collections"""

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

def simple_query(col: Collection, query: dict[str, any]) -> None:
    """Perform a simple query on the collection"""
    print(f"Performing simple query: {query}")
    proj = {"_id": 0}
    for doc in col.find(query, proj):
        print(doc)
    print()

def advanced_query(col: Collection, query: dict[str, any]) -> None:
    """Perform an advanced query on the collection"""
    print(f"Performing advanced query: {query}")
    proj = {"_id": 0}
    for doc in col.find(query, proj):
        print(doc)
    print()

def regex_query(col: Collection, query: dict[str, any]) -> None:
    """Perform a regex query on the collection"""
    print(f"Performing regex query: {query}")
    proj = {"_id": 0}
    for doc in col.find(query, proj):
        print(doc)
    print()

def main() -> None:
    """Main function"""
    settings = get_settings()
    client, col = connect(settings)
    query = {"name": "John"}
    simple_query(col, query)
    query = {"address": {"$gt": "S"}}
    advanced_query(col, query)
    query = { "address": { "$regex": "^S" } }
    regex_query(col, query)
    client.close()

if __name__ == "__main__":
    main()
