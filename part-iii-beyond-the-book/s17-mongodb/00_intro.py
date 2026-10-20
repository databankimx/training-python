"""Introduction to MongoDB"""

import pymongo
from login import get_settings

def test_mongodb_connection() -> None:
    """Test connection to MongoDB"""
    auth = get_settings()
    local = auth["use_local"]
    url = auth["local_url"] if local else auth["cloud_url"]

    client = pymongo.MongoClient(url)
    ping = client.admin.command("ping")
    print(f"Ping: {ping}")
    if ping["ok"] == 1:
        print("MongoDB server is connected")
    else:
        print("MongoDB server is not connected")
    client.close()

def main() -> None:
    """Main function"""
    test_mongodb_connection()

if __name__ == "__main__":
    main()
