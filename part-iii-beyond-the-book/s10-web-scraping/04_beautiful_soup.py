"""Using the `BeautifulSoup` HTML Parser"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_with_soup(url: str) -> BeautifulSoup:
    """Returns soup object"""
    with urlopen(url) as page:
        html = page.read().decode("utf-8")
        return BeautifulSoup(html, "html.parser")

def main() -> None:
    """Read web page and print the HTML"""
    url = "http://olympus.realpython.org/profiles"
    soup = scrape_with_soup(url)
    print(soup.prettify())

if __name__ == "__main__":
    main()
