"""Scraping Web Pages"""

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

def parse_text_content(text: str, search: str) -> str:
    """Read information from the text"""
    start = text.lower().find(search.lower()) + len(search)
    end = text[start:].find("\n") + start
    return text[start:end].strip(" \r\n\t")

def scrape_page(url: str, data: list[str]) -> None:
    """Extract data from a single profile page"""
    soup = scrape_with_soup(url)
    print(soup.title.string.upper())
    print(f"URL: {url}")
    text = soup.get_text()
    for datum in data:
        item = parse_text_content(text, f"{datum}:")
        print(f" - {datum}:{' ' * (15 - len(datum))} {item}")
    print()

def main() -> None:
    """Read web pages and scrape data"""
    base_url = "http://olympus.realpython.org/profiles"
    links = get_links(base_url)
    data = ["Name", "Hometown", "Favorite Animal", "Favorite Color"]
    for link in links:
        url = base_url + "/" + link.split("/")[-1]
        scrape_page(url, data)

if __name__ == "__main__":
    main()
