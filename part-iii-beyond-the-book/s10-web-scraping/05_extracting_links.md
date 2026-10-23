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
    return [link["href"] for link in soup.find_all("a")]
```

Here, we are using the `.find_all()` method to locate all `<a>` tags in
the HTML (`<a>` or "anchor" is the HTML tag for a hyperlink).

The function uses `scrape_with_soup()` from the previous lesson.

Then, from each one, we're extracting the `href` attribute, which 
contains the link URL. Note that `link["href"]` raises a `KeyError` if an `<a>`
tag has no `href`. `link.get("href")` returns `None` instead.

> Note: the code file turns off a Sonar warning on the base URL. That comment stays
> in the code file.

The links on this page are relative (such as `/profiles/aphrodite`), so the code
builds each full URL by joining the base URL with the last part of the link. That
works for this site, but `urllib.parse.urljoin(base_url, href)` is the sturdier
choice, because it handles relative and absolute links correctly.

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
