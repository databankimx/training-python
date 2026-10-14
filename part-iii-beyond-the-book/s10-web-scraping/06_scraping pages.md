## Scraping the Linked Pages

In the last example, we identified all of the URL paths that link to the individual profile pages.

The next step is to add code to scrape each of those pages and extract the data for a scrape report.

---

### The Functions

We'll need two functions for this task:

#### Content-Parsing Function:

This is similar to our previous version, except that we don't need to
look for tag indicators (since `BeautifulSoup` has removed the HTML for
us).

```python
def parse_text_content(text: str, search: str) -> str:
    """Read information from the text"""
    start = text.lower().find(search.lower()) + len(search)
    end = text[start:].find("\n") + start
    return text[start:end].strip(" \r\n\t")
```

---

#### Page Scraping Function:

This will perform all of the scraping tasks on the page

```python
def scrape_page(url: str, data: list[str]) -> None:
    """Extract data from a single profile page"""
    soup = scrape_with_soup(url)
    print(soup.title.string.upper())
    print("URL: {url}")
    text = soup.get_text()
    for datum in data:
        item = parse_text_content(text, f"{datum}:")
        print(f" - {datum}:{' ' * (15 - len(datum))} {item}")
    print()
```

---

### Testing

Let's test the program:

```python
base_url = "http://olympus.realpython.org/profiles"
links = get_links(base_url)
data = ["Name", "Hometown", "Favorite Animal", "Favorite Color"]
for link in links:
    url = base_url + "/" + link.split("/")[-1]
    scrape_page(url, data)
```

Output:

```
PROFILE: APHRODITE
URL: http://olympus.realpython.org/profiles/aphrodite
 - Name:            Aphrodite
 - Hometown:        Mount Olympus
 - Favorite Animal: Dove
 - Favorite Color:  Red

PROFILE: POSEIDON
URL: http://olympus.realpython.org/profiles/poseidon
 - Name:            Poseidon
 - Hometown:        Sea
 - Favorite Animal: Dolphin
 - Favorite Color:  Blue

PROFILE: DIONYSUS
URL: http://olympus.realpython.org/profiles/dionysus
 - Name:            Dionysus
 - Hometown:        Mount Olympus
 - Favorite Animal: Leopard
 - Favorite Color:  Wine
```

---
