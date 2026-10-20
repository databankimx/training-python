"""Update documents in MongoDB collection"""

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

def update_single(col: Collection, query: dict[str,str],
                  update: dict[str,dict[str,str]]) -> None:
    """Update a single document in the collection"""
    print(f"Updating single document matching: `{query}`")
    print(f"  with new values: `{update['$set']}`")
    res = col.update_one(query, update)
    print(f"Updated {res.modified_count} document(s)\n")
    view_all(col)

def update_multiple(col: Collection, query: dict[str,str],
                  update: dict[str,dict[str,str]]) -> None:
    """Update multiple documents in the collection"""
    print(f"Updating multiple documents matching: `{query}`")
    print(f"  with new values: `{update['$set']}`")
    res = col.update_many(query, update)
    print(f"Updated {res.modified_count} document(s)\n")
    view_all(col)

def view_all(col: Collection) -> None:
    """View all documents in MongoDB collection"""
    print("Documents in collection:")
    for doc in col.find({}, {"_id": 0}):
        print(doc)
    print()

def main() -> None:
    """Main program"""
    settings = get_settings()
    client, col = connect(settings)
    view_all(col)
    query = { "address": "Valley 345" }
    update = { "$set": { "address": "Canyon 123" } }
    update_single(col, query, update)
    query = { "address": { "$regex": "^O" } }
    update = { "$set": { "name": "Minnie" } }
    update_multiple(col, query, update)
    client.close()

if __name__ == "__main__":
    main()
