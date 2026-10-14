"""Connect to MongoDB"""

import json
from sm_utils import file_path
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_settings() -> dict[str,any]:
    """Retrieve MongoDB connection details from secrets.json"""
    with open(file_path("secrets.json"), encoding="utf-8") as f:
        return json.load(f)

def get_client(settings: dict[str,any]=None) -> MongoClient|None:
    """Obtain connection to MongoDB"""
    if not settings:
        settings = get_settings()
    local = settings["use_local"]
    url = settings["local_url"] if local else settings["cloud_url"]
    try:
        return MongoClient(url)
    except ConnectionFailure:
        print("Failed to connect to MongoDB")
        return None

def server_connected(client: MongoClient=None) -> bool:
    """Check if MongoDB server is connected"""
    if not client:
        client = get_client()
    return client.admin.command("ping")["ok"] == 1

def main() -> None:
    """Test connection to MongoDB"""
    if server_connected():
        print("MongoDB server is connected")
    else:
        print("MongoDB server is not connected")

if __name__ == "__main__":
    main()
