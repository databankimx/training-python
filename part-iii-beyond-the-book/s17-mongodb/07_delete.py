"""Delete documents from MongoDB collection"""

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

def delete_record(col: Collection, query: dict[str,str]) -> None:
    """Delete a document from MongoDB collection"""
    print(f"Deleting document matching query: {query}")
    result = col.delete_one(query)
    print(f"Deleted {result.deleted_count} document(s)\n")

def delete_multiple(col: Collection, query: dict[str,str]) -> None:
    """Delete multiple documents from MongoDB collection"""
    print(f"Deleting document(s) matching query: {query}")
    result = col.delete_many(query)
    print(f"Deleted {result.deleted_count} document(s)\n")

def delete_all(col: Collection) -> None:
    """Delete all documents from MongoDB collection"""
    print("Deleting all documents from collection...")
    result = col.delete_many({})
    print(f"Deleted {result.deleted_count} document(s)\n")

def view_remaining(col: Collection) -> None:
    """View remaining documents in MongoDB collection"""
    print("Remaining documents in collection:")
    for doc in col.find({}, {"_id": 0}):
        print(doc)
    print()

def main() -> None:
    """Main function"""
    settings = get_settings()
    client, col = connect(settings)
    query = { "address": "Mountain 21" }
    delete_record(col, query)
    view_remaining(col)
    query = { "address": {"$regex": "^S"} }
    delete_multiple(col, query)
    view_remaining(col)
    # delete_all(col)
    # view_remaining(col)
    client.close()

if __name__ == "__main__":
    main()
