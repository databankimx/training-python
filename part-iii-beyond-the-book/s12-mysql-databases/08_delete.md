## Deleting Records from a Table

Sometimes it is necessary to remove records from a database table.

Let's talk about the ***highly risky*** process of deleting records.

The syntax takes this form:

```sql
DELETE FROM table_name WHERE column_name = value
```

The `WHERE` clause is critical! It identifies which rows to delete. If 
you omit the `WHERE` clause, you will delete ***ALL ROWS*** from the 
table.

> Note: If you actually want to delete all rows from a table, the 
> preferred SQL Query is the following:
>
> ```sql
> TRUNCATE TABLE table_name
> ```

---

### Deleting a Record

Let's delete a record from our table.

```python
if conn.is_connected():
    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record(s) deleted")
```

Output:

```
1 record(s) deleted
```

---

### Parameterizing the Query

As always, you should parameterize values in the `WHERE` clause

```python
if conn.is_connected():
    sql = "DELETE FROM customers WHERE address = %s"
    params = ("Yellow Garden 2", )
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    print(cursor.rowcount, "record(s) deleted")
```

Output:

```
1 record(s) deleted
```

---
