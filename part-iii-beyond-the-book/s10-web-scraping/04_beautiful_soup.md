## The `BeautifulSoup` HTML Parser

In our previous example, we were manually handling the content of very
simple HTML pages.

As we start scraping more complex websites (and trust me, anything worth
scraping is more complicated), it could become difficult to create
manual parsing functions for every conceivable HTML tag.

The `BeautifulSoup` library provides a pre-built HTML parser that loads
the content of an HTML page into easily consumable objects, saving us
the effort of creating all of that functionality.

`BeautifulSoup` is not in the Python Standard Library, so we'll have to
install in before we can use it. Make sure you're in an active virtual
environment, and then run this command in the terminal:

```
python -m pip install beautifulsoup4
```

---

### Getting the HTML Page Content

The process for obtaining the HTML content is nearly identical to the
manual method that we used previously. The one difference is that we'll 
pass the raw HTML text content to `BeautifulSoup` and return the parser
instead of the raw text.

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_with_soup(url: str) -> BeautifulSoup:
    """Returns soup object"""
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html, "html.parser")
```

Let's test this on the profiles page of the Real Python sample site:

```python
url = "http://olympus.realpython.org/profiles"
soup = scrape_with_soup(url)
print(soup.prettify())
```

Output:

<details>
<summary>Profiles Page HTML</summary>

```html
<html>
 <head>
  <title>
   All Profiles
  </title>
 </head>
 <body bgcolor="yellow">
  <center>
   <br/>
   <br/>
   <h1>
    All Profiles:
   </h1>
   <br/>
   <br/>
   <h2>
    <a href="/profiles/aphrodite">
     Aphrodite
    </a>
    <br/>
    <br/>
    <a href="/profiles/poseidon">
     Poseidon
    </a>
    <br/>
    <br/>
    <a href="/profiles/dionysus">
     Dionysus
    </a>
   </h2>
  </center>
 </body>
</html>
```

</details>

As you can see, the `BeautifulSoup` object returns the HTML as its
`repr()` and has a `prettify()` function to add indents.

---
