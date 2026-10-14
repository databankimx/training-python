"""Sort documents from MongoDB collection"""

from login import get_settings, get_client, server_connected
# pylint: disable=unused-import
from pymongo import MongoClient, ASCENDING, DESCENDING
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

def sort_results(col: Collection, field: str) -> None:
    """Sort the documents in the collection by a specified field"""
    try:
        print(f"Sorting documents by field: {field}")
        for doc in col.find({}, {"_id": 0}).sort(field):
            print(doc)
    # pylint: disable=broad-except
    except Exception as e:
        print(f"Error sorting documents: {str(e)}")
    print()

def reverse_results(col: Collection, field: str) -> None:
    """Sort the documents in the collection by a specified field"""
    try:
        print(f"Sorting documents by field: {field} (reversed)")
        for doc in col.find({}, {"_id": 0}).sort(field, DESCENDING):
            print(doc)
    # pylint: disable=broad-except
    except Exception as e:
        print(f"Error sorting documents: {str(e)}")
    print()

def main() -> None:
    """Main function"""
    settings = get_settings()
    client, col = connect(settings)
    field = "name"
    sort_results(col, field)
    reverse_results(col, field)
    client.close()

if __name__ == "__main__":
    main()
