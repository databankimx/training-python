## Modifying Data

Of course, there are times when it's necessary to modify the data in a
record. Perhaps a table contains an inventory, or a person moves or 
changes their name. Any number of things can necessitate data changes.

To modify a record, we use the `UPDATE` command.

```sql
UPDATE table_name SET col_1 = val_1, ... WHERE column = value
```

---

### Updating a Record

Let's modify a record in our database.

```python
if conn.is_connected():
    sql = "UPDATE customers SET address = 'Canyon 123'" + \
          "WHERE address = 'Valley 345'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record(s) affected")
```

Output:

```
1 record(s) affected
```

---

### Parameterizing an Update

As always, you should parameterize values in the `SET` and `WHERE` 
clauses.

```python
if conn.is_connected():
    sql = "UPDATE customers SET address = %s WHERE address = %s"
    params = ("Valley 345", "Canyon 123")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    print(cursor.rowcount, "record(s) affected")
```

Output:

```
1 record(s) affected
```

---
