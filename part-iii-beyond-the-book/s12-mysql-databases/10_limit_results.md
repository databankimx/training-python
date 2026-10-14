## Limiting Number of Returned Records

There will be times where you only want a certain number of records from
a `SELECT` query.

---

### The `LIMIT` Clause

To limit the number of returned records, we add a `LIMIT` clause like 
this:

```sql
SELECT * FROM table LIMIT ###
-- Where `###` is an integer number of records to return
```

```python
if conn.is_connected():
    sql = "SELECT * FROM customers LIMIT 5"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('John', 'Highway 21', 1)
('Peter', 'Lowstreet 4', 2)
('Amy', 'Apple st 652', 3)
('Michael', 'Valley 345', 5)
('Sandy', 'Ocean blvd 2', 6)
```

---

### Changing the Start of the Limit

We can also add an `OFFSET` clause which identifies the number of records
to skip before starting the limit counter.

```sql
SELECT * FROM table LIMIT ### OFFSET ##
-- Where `###` is an integer number of records to return
-- And `##` is an integer number of records to skip first
```

```python
if conn.is_connected():
    sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('Amy', 'Apple st 652', 3)
('Michael', 'Valley 345', 5)
('Sandy', 'Ocean blvd 2', 6)
('Betty', 'Green Grass 1', 7)
('Richard', 'Sky st 331', 8)
```

---
