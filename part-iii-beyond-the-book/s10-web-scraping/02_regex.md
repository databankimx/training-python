## Using Regular Expressions to Improve HTML Parsing

We saw in the last lesson that small errors in the HTML will render our
naive parsing function incapable of performing its task, because we
limited our search to one exactly correct HTML tag.

We can improve this by using regular expressions instead of a static
search string.

---

### Improve Title Parser

We can create a more flexible search term using a regular expression. In
this case, we're leveraging the regular expression term `.*`, which
reads zero or more of any character, but we're augmenting it with the 
`?` term to make it non-greedy.

The non-greedy term `.*?` still matches any amount of any character,
but only until/unless it encounters the next matching pattern.

```python
import re

def parse_html_tag(html: str, tag_to_find: str) -> str:
    """Read content of teh specified HTML tag"""
    pattern = f"<.*?{tag_to_find}.*?>.*?<.*?/{tag_to_find}.*?>.*?"
    matches = re.search(pattern, html, re.IGNORECASE)
    if not matches:
        return f"'{tag_to_find}' not found"
    return re.sub("<.*?>", "", matches.group())
```

We can test this with our formerly "bad" URL:

```python
url = "http://olympus.realpython.org/profiles/poseidon"
html = scrape_page(url)
title = parse_html(html, "title")
print(title)
```

Output:

```
Profile: Poseidon
```

---
