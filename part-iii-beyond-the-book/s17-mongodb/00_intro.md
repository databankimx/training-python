## MongoDB

MongoDB is part of the new generation of database architectures known as
*NoSQL* (not only SQL) that use non-tabular data instead of relational 
tables to provide improved ease of use, performance, and scalability. 

---

### Install the MongoDB software:

We'll need to install the MongoDB software. The instructions below assume
that you're setting up a local instance, but you can ignore these 
instructions and set up a cloud account if you prefer.

If you want to set up MongoDB the way I have for these lessons, follow the
steps below:

---

#### Install Required Components

To perform the tasks in the lesson, you'll need to install these items:

* MongoDB Server
    ```
    winget install MongoDB.Server
    ```
* MongoDB Compass UI
    ```
    winget install MongoDB.Compass.Community
    ```

---

#### Install Optional Components

These components are recommended but not required for these lessons:

* MongoDB Database Toolkit
    ```
    winget install MongoDB.DatabaseTools
    ```
* MongoDB Shell
    ```
    winget install MongoDB.Shell
    ```
* MongoDB CLI
    ```
    winget install MongoDB.MongoDBCLI
    ```

---

#### Install the MongoDB Python Library

Of course, we'll also need a python library to connect to our MongoDB instance.

```
python -m pip install pymongo
```

---

### Test Your Connection

We'll need to perform a few steps to test the connection to MongoDB

---

#### Create a Login Secrets File

In [/config](./config/), you'll find a file called `credentials.json`

Save a copy of or rename this file as `secrets.json` in the same location.

```json
{
    "use_local": true,
    "cloud_url": "mongodb+srv://your_cloud_connection_address",
    "local_url": "mongodb://localhost:27017/",
    "db_name": "mydatabase",
    "col_name": "customers"
}
```

If you're using an Atlas cloud instance instead of a local MongoDB instance,
update the following fields:

* `use_local`: `false`
* `cloud_url`: The full URL to your Atlas cluster
    * Note: This URL will include your credentials, but `secrets.json` is 
      excluded in the `.gitignore` file, so it will not be shared in source
      control.

---

#### Install `sm_utils`

I use the `sm_utils` library to support a relative path to load the user
credentials.

```
python -m pip install sm_utils
```

After installing, make sure that you have a file `sm_utils.json` that points
to the directory where your `secrets.json` file is stored.

```json
{
    "default_path": "config"
}
```

---

#### Test Login

Use the following code to log in:

```python
import json
from sm_utils import file_path
import pymongo

def login():
    with open(file_path("secrets.json")) as f:
        return json.load(f)

def test_mongodb_connection() -> None:
    """Test connection to MongoDB"""
    auth = login()
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

test_mongodb_connection()
```

> Note: You should always call `client.close()` after database work is done

Output:

```
Ping: {'ok': 1.0}
MongoDB server is connected
```

If the result includes the key `ok` with a value of `1.0`, you're good to 
proceed.

---

### Utility Functions

Since the initial connection is trivial, I have included a separate file:
[login.py](./login.py) that contains the code for getting connected.

<details>
<summary>login.py</summary>
<br>

```python
import json
from sm_utils import file_path
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_login() -> dict[str,any]:
    """Retrieve MongoDB connection details from secrets.json"""
    with open(file_path("secrets.json")) as f:
        return json.load(f)

def get_client(auth: dict[str,any]=None) -> MongoClient|None:
    """Obtain connection to MongoDB"""
    if not auth:
        auth = get_login()
    local = auth["use_local"]
    url = auth["local_url"] if local else auth["cloud_url"]
    try:
        return MongoClient(url)
    except ConnectionFailure:
        print("Failed to connect to MongoDB")

def server_connected(client: MongoClient=None) -> bool:
    """Check if MongoDB server is connected"""
    if not client:
        client = get_client()
    return client.admin.command("ping")["ok"] == 1
```

</details>
<br>

In the remaining lesson examples, I will just use this code for connecting:

```python
from login.py import get_client, server_connected

client = get_client()
connected = server_connected(client)
```

---
