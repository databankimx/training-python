"""Insert a document into a collection in MongoDB"""

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

def insert_doc(col: Collection, data: dict[str, any]) -> None:
    """Insert a document into the collection"""
    try:
        print(f"Inserting document into collection...\n{data}")
        result = col.insert_one(data)
        doc_id = result.inserted_id
        print(f"Document inserted successfully as ID: `{doc_id}`\n")
    # pylint: disable=broad-except
    except Exception as e:
        print(f"Failed to insert document: {str(e)}\n")

def insert_multiple(col: Collection, data: list[dict[str, any]]) -> None:
    """Insert multiple documents into the collection"""
    try:
        print("Inserting multiple documents into collection...")
        for doc in data:
            print(f"• {doc}")
        _ = col.insert_many(data)
        print("Documents inserted successfully.\n")
    # pylint: disable=broad-except
    except Exception as e:
        print(f"Failed to insert documents: {str(e)}\n")

def main() -> None:
    """Main function"""
    client, col = connect()

    single = { "name": "John", "address": "Highway 37" }
    insert_doc(col, single)

    multiple = [
        { "name": "Amy", "address": "Apple st 652"},
        { "name": "Hannah", "address": "Mountain 21"},
        { "name": "Michael", "address": "Valley 345"},
        { "name": "Sandy", "address": "Ocean blvd 2"},
        { "name": "Betty", "address": "Green Grass 1"},
        { "name": "Richard", "address": "Sky st 331"},
        { "name": "Susan", "address": "One way 98"},
        { "name": "Vicky", "address": "Yellow Garden 2"},
        { "name": "Ben", "address": "Park Lane 38"},
        { "name": "William", "address": "Central st 954"},
        { "name": "Chuck", "address": "Main Road 989"},
        { "name": "Viola", "address": "Sideway 1633"}
    ]
    insert_multiple(col, multiple)

    client.close()

if __name__ == "__main__":
    main()
