"""Extracting Hyperlinks Using `BeautifulSoup`"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_with_soup(url: str) -> BeautifulSoup:
    """Returns soup object"""
    with urlopen(url) as page:
        html = page.read().decode("utf-8")
        return BeautifulSoup(html, "html.parser")

def get_links(url: str) -> list[str]:
    """Obtain the links to the profile pages"""
    soup = scrape_with_soup(url)
    return [l["href"] for l in soup.find_all("a")]

def main() -> None:
    """Read web page and get the hyperlinks"""
    base_url = "http://olympus.realpython.org/profiles"
    links = get_links(base_url)
    for link in links:
        url = base_url + "/" + link.split("/")[-1]
        print(url)

if __name__ == "__main__":
    main()
