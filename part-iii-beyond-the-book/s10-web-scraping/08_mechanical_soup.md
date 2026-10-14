## Interaction With `MechanicalSoup`

Sometimes your scraping bot will have to navigate some interactive
process (like a login page) before you can access the material you want 
to gather.

For this, an HTML parser is insufficient. You require a browser object
that can interact with the HTML page in a manner that you have 
automated in advance.

The `MechanicalSoup` library provides exactly that functionality.

To install it, make sure you're in an active virtual environment and
run the following command:

```
python -m pip install mechanicalsoup
```

---

### Logging In with a Browser Object

The Real Python sample site includes a login page that requires a 
username and password to be entered. Following a successful login, the
browser automatically routed to the profiles page, which we've already
figured out how to parse.

Let's use `MechanicalSoup` to create a login function to complete our
bot's functionality.

```python
import mechanicalsoup

def log_in(url: str, un: str, pw: str) -> str:
    """Log in to a website and return the HTML from the landing page"""
    browser = mechanicalsoup.Browser()
    login_page = browser.get(url)
    login_html = login_page.soup
    login_form = login_html.select("form")[0]
    login_form.select("input[name='user']")[0]["value"] = un
    login_form.select("input[name='pwd']")[0]["value"] = pw
    profiles_page = browser.submit(login_form, login_page.url)
    return profiles_page.soup
```

We can test our ability to log in and verify that we receive the HTML
for the profiles page.

```python
url = "http://olympus.realpython.org/login"
username = "zeus"
password = "ThunderDude"
html = log_in(url, username, password)
print(html)
```

Output:

```html
<html>
<head>
<title>All Profiles</title>
</head>
<body bgcolor="yellow">
<center>
<br/><br/>
<h1>All Profiles:</h1>
<br/><br/>
<h2>
<a href="/profiles/aphrodite">Aphrodite</a>
<br/><br/>
<a href="/profiles/poseidon">Poseidon</a>
<br/><br/>
<a href="/profiles/dionysus">Dionysus</a>
</h2>
</center>
</body>
</html>
```

---