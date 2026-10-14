## Width, Fill, and Alignment

Format specifiers allow very granular control over the width and alignment (as
well as padding/fill) for strings.

There are an abundance of options here, so this functionality deserves a
separate topic unto itself.

---

### Width

We can specify the minimum width of the output string by indicating the 
number of characters wise the string must be:

```python
s = "abc"
print(f"'{s:5}'")
```

Output:

```
'abc  '
```

---

#### Overflow is Permitted

This setting, by itself is only a minimum width, so if a value is longer than
the set number of characters, it will print more than specified:

```python
s = "abcdef"
print(f"'{s:5}'")
```

Output:

```
'abcdef'
```

---

#### Truncating Overflow

We can repurpose the decimal precision syntax to set a maximum width for
string data.

```python
s = "abcdef"
print(f"'{s:5.5}'")
```

Output:

```
'abcde'
```

Be carful using this option, as it truncates the string to the set character
limit.

---

### Alignment

Within the width prescribed, we can set the alignment with these characters:

|Character|Effect|
|:-:|-|
|`<`|Left justify (within the width size)|
|`>`|Right justify (within the width size)|
|`^`|Center (within the width size)|

---

#### Left-Justification

To left-justify the string, include a `<` character before the width number.

```python
s = "abc"
print(f"left justify: '{s:<9}'")
```

Output:

```
left justify: 'abc      '
```

---

#### Right-Justification

To right-justify the string, include a `>` character before the width number.

```python
s = "abc"
print(f"right justify: '{s:<9}'")
```

Output:

```
right justify: '      abc'
```

---

### Centering

To center the string, include a `^` character before the width number.

```python
s = "abc"
print(f"center: '{s:^9}'")
```

Output:

```
center: '   abc   '
```

---

### Filling Padded Space

You can specify a *fill* character before the alignment and width to fill the
blank space in the width with the character specified:

```python
s = "abc"
print(f"{s:.>9}")
print(f"{s:*<9}")
print(f"{s:~^9}")
```

Output:

```
......abc
abc******
~~~abc~~~
```

---
