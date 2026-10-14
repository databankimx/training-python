"""Filtering HTML content using regular expressions"""

from urllib.request import urlopen
import re

def scrape_page(url: str) -> str:
    """Returns the HTML content of a web page"""
    with urlopen(url) as page:
        page_bytes = page.read()
        return page_bytes.decode("utf-8")

def parse_html_tag(html: str, tag_to_find: str) -> str:
    """Read content of teh specified HTML tag"""
    pattern = f"<.*?{tag_to_find}.*?>.*?<.*?/{tag_to_find}.*?>.*?"
    matches = re.search(pattern, html, re.IGNORECASE)
    if not matches:
        return f"'{tag_to_find}' not found"
    return re.sub("<.*?>", "", matches.group())

def main() -> None:
    """Read web pages and print the titles"""
    pages = [
        "http://olympus.realpython.org/profiles/aphrodite",
        "http://olympus.realpython.org/profiles/poseidon",
        "http://olympus.realpython.org/profiles/dionysus"
    ]

    for page in pages:
        html = scrape_page(page)
        title = parse_html_tag(html, "title")
        print(title)

if __name__ == "__main__":
    main()
