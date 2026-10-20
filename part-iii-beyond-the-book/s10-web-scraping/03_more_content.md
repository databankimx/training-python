## Parsing More HTML Content

We may also wish to extract content that isn't a tag value from the 
HTML.

You'll recall that the HTML extracted from our first URL looked like 
this:

```html
<html>
<head>
    <title>Profile: Aphrodite</title>
</head>
<body bgcolor="yellow">
    <center>
        <br><br>
        <img src="/static/aphrodite.gif" />
        <h2>Name: Aphrodite</h2>
        <br><br>
        Favorite animal: Dove
        <br><br>
        Favorite color: Red
        <br><br>
        Hometown: Mount Olympus
    </center>
</body>
</html>
```

We can see in here that there are several data that we could extract:

* Name
* Favorite animal
* Favorite color
* Hometown

Reviewing HTML this way and making assumptions about what is part of a
template and will be common across many pages versus what is specific to
the page being interrogated can sometimes take longer than writing the
scraping code.

That's just the way it is sometimes.

---

### Extracting the Additional Content

Keeping the code we have already developed, let's add a function that
extracts the individual elements.

```python
def parse_html_content(html: str, search: str) -> str:
    """Read data from the HTML contents"""
    start = html.lower().find(search.lower()) + len(search)
    end = html[start:].find("<") + start
    return html[start:end].strip(" \r\n\t")
```

This function allows us to pass in a search term and then capture the
remaining information on the line on which the term appears (ignoring
any trailing HTML tags).

Let's test this:

```python
html = scrape_page("http://olympus.realpython.org/profiles/aphrodite")
animal = parse_html_content(html, "Favorite Animal:")
print(animal)
```

Output:

```
Dove
```

---

### Meaningful Reporting

Finally, to test our web scrape, let's take everything we've done so far
and extract a report across a set of URLs.

```python
pages = [
    "http://olympus.realpython.org/profiles/aphrodite",
    "http://olympus.realpython.org/profiles/poseidon",
    "http://olympus.realpython.org/profiles/dionysus"
]

for page in pages:
    html = scrape_page(page)
    title = parse_html_tag(html, "title")
    print(title)
    data = [
        "Name",
        "Hometown",
        "Favorite Animal",
        "Favorite Color"
    ]
    for datum in data:
        item = parse_html_content(html, f"{datum}:")
        print(f" - {datum}: {item}")
    print()
```

Output:

```
Profile: Aphrodite
 - Name: Aphrodite
 - Hometown: Mount Olympus
 - Favorite Animal: Dove
 - Favorite Color: Red

Profile: Poseidon
 - Name: Poseidon
 - Hometown: Sea
 - Favorite Animal: Dolphin
 - Favorite Color: Blue

Profile: Dionysus
 - Name: Dionysus
 - Hometown: Mount Olympus
 - Favorite Animal: Leopard
 - Favorite Color: Wine
```

Obviously this is a very simplified example, but we have effectively
scraped and reported on all meaningful data available on these web 
pages.

---
