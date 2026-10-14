## Read Data from the Database

There's little use in having data stores in a structured database if you
can't read it out and report on it.

Let's review how we read data from tables.

---

### The `SELECT` Query

To retrieve data from the database we use the SQL `SELECT` command.

The simplest form is just to select all the records, like this:

```sql
SELECT * FROM table_name
```

In our code, it'll looks something like this:

```python
if conn.is_connected():
    sql = "SELECT * FROM customers"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Note: We use the `fetchall()` method to retrieve all the records in the
cursor.

Output:

```
('John', 'Highway 21', 1)
('Peter', 'Lowstreet 4', 2)
('Amy', 'Apple st 652', 3)
('Hannah', 'Mountain 21', 4)
('Michael', 'Valley 345', 5)
('Sandy', 'Ocean blvd 2', 6)
('Betty', 'Green Grass 1', 7)
('Richard', 'Sky st 331', 8)
('Susan', 'One way 98', 9)
('Vicky', 'Yellow Garden 2', 10)
('Ben', 'Park Lane 38', 11)
('William', 'Central st 954', 12)
('Chuck', 'Main Road 989', 13)
('Viola', 'Sideway 1633', 14)
('Michelle', 'Blue Village', 15)
```

---

### Limiting Returned Columns

We can specify the specific columns we want to return by adding their
names to the query:

```sql
SELECT col_1, col_2, ... FROM table_name
```

```python
if conn.is_connected():
    sql = "SELECT name, address FROM customers"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('John', 'Highway 21')
('Peter', 'Lowstreet 4')
('Amy', 'Apple st 652')
('Hannah', 'Mountain 21')
('Michael', 'Valley 345')
('Sandy', 'Ocean blvd 2')
('Betty', 'Green Grass 1')
('Richard', 'Sky st 331')
('Susan', 'One way 98')
('Vicky', 'Yellow Garden 2')
('Ben', 'Park Lane 38')
('William', 'Central st 954')
('Chuck', 'Main Road 989')
('Viola', 'Sideway 1633')
('Michelle', 'Blue Village')
```

As you'll note, the rows are returned as tuples.

---

### Retrieving a Single Record

We can retrieve a single record by using `fetchone()` instead of
`fetchall()`

```python
if conn.is_connected():
    sql = "SELECT * FROM customers"
    cursor = conn.cursor()
    cursor.execute(sql)
    print(cursor.fetchone())
```

Output:

```
('John', 'Highway 21', 1)
```

---
