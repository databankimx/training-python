## Sorting Retrieved Data

When retrieving data, especially in large amounts, it can be very useful
to sort the records on the basis of one or more columns.

---

## The `ORDER BY` Clause

To sort retrieved records, we add an `ORDER BY` clause to the end of the
query, which can be followed by one or more column names separated by
commas.

```sql
SELECT * FROM customers ORDER BY name
```

```python
if conn.is_connected():
    sql = "SELECT * FROM customers ORDER BY name"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('Amy', 'Apple st 652', 3)
('Ben', 'Park Lane 38', 11)
('Betty', 'Green Grass 1', 7)
('Chuck', 'Main Road 989', 13)
('Hannah', 'Mountain 21', 4)
('John', 'Highway 21', 1)
('Michael', 'Valley 345', 5)
('Michelle', 'Blue Village', 15)
('Peter', 'Lowstreet 4', 2)
('Richard', 'Sky st 331', 8)
('Sandy', 'Ocean blvd 2', 6)
('Susan', 'One way 98', 9)
('Vicky', 'Yellow Garden 2', 10)
('Viola', 'Sideway 1633', 14)
('William', 'Central st 954', 12)
```

---

## Sorting in Descending Order

There are two modifiers available that can be added to the end of an
`ORDER BY` clause:

* `ASC`: Ascending order
    * Note: this is the default, so you can omit it.
* `DESC`: Descending order

```python
if conn.is_connected():
    sql = "SELECT * FROM customers ORDER BY address DESC"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('Vicky', 'Yellow Garden 2', 10)
('Michael', 'Valley 345', 5)
('Richard', 'Sky st 331', 8)
('Viola', 'Sideway 1633', 14)
('Ben', 'Park Lane 38', 11)
('Susan', 'One way 98', 9)
('Sandy', 'Ocean blvd 2', 6)
('Hannah', 'Mountain 21', 4)
('Chuck', 'Main Road 989', 13)
('Peter', 'Lowstreet 4', 2)
('John', 'Highway 21', 1)
('Betty', 'Green Grass 1', 7)
('William', 'Central st 954', 12)
('Michelle', 'Blue Village', 15)
('Amy', 'Apple st 652', 3)
```

---
