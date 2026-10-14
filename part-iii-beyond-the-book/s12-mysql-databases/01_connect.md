## Connecting to MySQL

Our first step is to establish a connection to MySQL.

---

### Preparation

To simplify a few things, I have included the following ancillary files:

* [utility_functions.py](./utility_functions.py) - contains:
    * `get_settings()` - read your connection settings from a JSON file
* [relative_paths.py](./relative_paths.py) - contains
    * `get_path()` - obtain a relative path to your JSON file
* [settings.json](./files/settings.json) - connection settings
    * You may need to edit this file if you used different credentials:  
      ```json
      {
          "host": "localhost",
          "username": "python",
          "password": "training",
          "schema": "mydatabase"
      }
      ```

---

### Acquiring Settings

In each of the following lessons, the first instruction in my code will be
to acquire the settings from the above JSON file thus:

```python
from utility_functions import get_settings

settings = get_settings()
```

The `get_settings()` function looks like this:

```python
def get_settings(file: str="settings.json", folder: str="files") -> dict[str, str]:
    """Get settings dictionary from JSON file"""
    return json.loads(Path(get_path(file, folder)).read_text())
```

Since this is not a lesson on reading a file, I will omit this instruction
in all later lessons in this section.

---

### Getting Connected

The `mysql.connector` library exposes a `connect()` method that takes the
following keyword arguments:

* `host`: The host server to connect to (in our case: `localhost`)
* `user`: The username to log in (in my example: `python`)
* `password`: The login password (in my example: `training`)
* `database`: The database to open
    * In later lessons, this will be called `mydatabase`
    * For now, since we haven't yet created a database, we'll omit this

So, here is our code to make a connection:

```python
conn = mysql.connector.connect(
    host=settings["host"],
    user=settings["username"],
    password=settings["password"]
)
print(f"Connected to {conn.server_host}: {conn.server_port}")
```

Output (port may vary):

```
Connected to localhost: 3306
```

---

### Verifying Connection

To verify that we are connected, we'll run a sql query to list the
databases in MySQL:

```sql
SHOW DATABASES
```

To execute this from python, we have to take a couple of steps:

---

#### Create Cursor

A database cursor is an object that is used to traverse the records in a
database.

In some languages, this is returned as the result of executing a command.

For example, in C# ...

```csharp
MySqlCommand cmd = new MySqlCommand("Some SQL Query", connection);
MySqlDataReader reader = cmd.ExecuteReader();
```

... the cursor is the resulting `MySqlDataReader` object

In Python, however, the command object that executes the query and the
resulting data reader are the same object: the connection's cursor.

```python
if conn.is_connected():
    cursor = conn.cursor()
```

---

#### Querying for Databases

To list the databases on the server, we first need a query.

Queries are written in SQL (Structured Query Language). Our query to list
the databases is very simple:

```python
sql = "SHOW DATABASES"
```

We then execute the query using the cursor object, like this:

```python
cursor.execute(sql)
```

---

#### Listing Databases

Now, the cursor contains several rows in which the database list appears.

To display them, we'll just iterate over the results in a loop.

Each result in the cursor is returned as a tuple, so we'll extract index
0 to get just the database name:

```python
print("DATABASES:")
for database in cursor:
    print(f" - {database[0]}")
```

Output:

```
DATABASES:
 - information_schema
 - mysql
 - performance_schema
 - sys
 - world
```

---

### Disconnecting

Although some database architectures will automatically disconnect the
session (in our case the `mysql.connector.connection`), others will not.

It is critical not to leave behind orphaned open sessions on a database
server, as these can result in locking or blocking issues that can affect
performance for all users.

So, the last call in any database interaction should be to disconnect the
session.

It's possible that due to some error, either we failed to create the
connection or it is not connected, so we'll check for these conditions
before disconnecting.

```python
if conn is not None or not conn.is_connected():
    conn.disconnect()
```

---
