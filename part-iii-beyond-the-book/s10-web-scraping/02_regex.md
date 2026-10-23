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
    """Read content of the specified HTML tag"""
    pattern = f"<.*?{tag_to_find}.*?>.*?<.*?/{tag_to_find}.*?>.*?"
    match = re.search(pattern, html, re.IGNORECASE)
    if not match:
        return f"'{tag_to_find}' not found"
    return re.sub("<.*?>", "", match.group())
```

> Note: this function uses `scrape_page()` from the previous lesson, which returns
> the HTML for a URL.

We can test this with our formerly "bad" URL:

```python
url = "http://olympus.realpython.org/profiles/poseidon"
html = scrape_page(url)
title = parse_html_tag(html, "title")
print(title)
```

Output:

```
Profile: Poseidon
```

The pattern has a limit: `.` doesn't match a newline by default, so it only finds a
tag that sits on one line. A tag split across lines won't match, so check a page's
HTML before relying on this approach.

> Note: the code file turns off Sonar warnings on two lines (the `re.sub()` return
> and the list of page URLs). Those comments stay in the code file.

---
