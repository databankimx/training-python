## Removing Values from a Dictionary

Like lists, items can be removed from a dictionary using the `del` keyword.

Syntax:  
`del my_dictionary[my_key]`

```python
alien = {"color" : "green", "points" : 5}
print(alien)
del alien["points"]
print(alien)
```

Output:

```
{'color': 'green', 'points': 5}
{'color': 'green'}
```

---
