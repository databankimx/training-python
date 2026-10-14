## Basic Web Scraping with `urllib`

The Python Standard Library includes a module `urllib` that can be used
to access and read a URL as though it was a file.

---

### Obtaining Page HTML Content

Using the `urlopen()` function, you can obtain an object representing
the HTML page at a given URL and read its content.

Let's access the page content for one of the pages on the Real Python
example site.

First we'll make a function that reads and returns the HTML content from the URL.

```python
from urllib.request import urlopen

def scrape_page(url: str) -> str:
    """Returns the HTML content of a web page"""
    page = urlopen(url)
    page_bytes = page.read()
    return page_bytes.decode("utf-8")
```

Then we can test it like so:

```python
url = "http://olympus.realpython.org/profiles/aphrodite"
print(scrape_page(url))
```

Output:

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

As you can see, we obtained the entire page content, but we still need
to parse the data into some meaningful form.

---

### Manually Parsing HTML

Let's say what we're after is the page title. If we know a little HTML,
then we're aware that that will typically appear in the `<title>` tag.

So, we might create a *somewhat naive* HTML parsing function to locate 
and print the title from the retrieved HTML like this:

```python
def parse_html(html: str, tag_to_find: str) -> str:
    """Locate specified HTML tag and returns its content"""
    tag_to_find = tag_to_find.lower()
    start_index = html.lower().find(f"<{tag_to_find}>") \
        + len(tag_to_find) + 2
    end_index = html.lower().find(f"</{tag_to_find}>")
    return html[start_index:end_index]
```

#### URL with Good HTML

Testing that on the same page we looked at before works well:

```python
url = "http://olympus.realpython.org/profiles/aphrodite"
html = scrape_page(url)
title = parse_html(html, "title")
print(title)
```

Output:

```
Profile: Aphrodite
```

---

#### URL with "Bad" HTML

However, if we test with a different URL, something has gone wrong:

```python
url = "http://olympus.realpython.org/profiles/poseidon"
html = scrape_page(url)
title = parse_html(html, "title")
print(title)
```

Output:

```
<head>
<title >Profile: Poseidon
```

There's a glitch in the HTML where the website developer left an extra
space in the `<title >` tag.

This isn't an error when a browser renders the HTML, but it broke our 
naive parser.

In the next lesson, we'll look at a way to improve this using regular
expressions.

---
