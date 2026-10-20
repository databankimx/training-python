## Extracting Hyperlinks Using `BeautifulSoup`

The `BeautifulSoup` object exposes a ton of methods for accessing
specific HTML controls.

The `.find_all("tag_name")` method, for example, returns a list of all
matching tags in the HTML.

---

### Getting the Link URLs

Let's add a function that extracts and returns all hyperlink URLs from 
the target page.

```python
def get_links(url: str) -> list[str]:
    """Obtain the links to the profile pages"""
    soup = scrape_with_soup(url)
    return [l["href"] for l in soup.find_all("a")]
```

Here, we are using the `.find_all()` method to locate all `<a>` tags in
the HTML (`<a>` or "anchor" is the HTML tag for a hyperlink).

Then, from each one, we're extracting the `href` attribute, which 
contains the link URL.

We can test thus:

```python
base_url = "http://olympus.realpython.org/profiles"
links = get_links(base_url)
for link in links:
    url = base_url + "/" + link.split("/")[-1]
    print(url)
```

Output:

```
http://olympus.realpython.org/profiles/aphrodite
http://olympus.realpython.org/profiles/poseidon
http://olympus.realpython.org/profiles/dionysus
```

---
