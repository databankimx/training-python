"""Web scraping with `MechanicalSoup`"""

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

def main() -> None:
    """Retrieve the profiles page HTML after logging in"""
    url = "http://olympus.realpython.org/login"
    username = "zeus"
    password = "ThunderDude"
    html = log_in(url, username, password)
    print(html)

if __name__ == "__main__":
    main()
