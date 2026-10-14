"""Scraping images"""

from urllib.request import urlopen
from pathlib import Path
from bs4 import BeautifulSoup
import requests
from relative_paths import get_path

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

def download_image(url: str) -> None:
    """Store an image file"""
    image = requests.get(url, timeout=10).content
    filename = url.split("/")[-1]
    filepath = Path(get_path(filename, "images"))
    filepath.write_bytes(image)

def scrape_images(url: str, soup: BeautifulSoup) -> None:
    """Extract all images from the page"""
    print(" - Images:")
    base_url = "http://" + url.split("/")[2]
    for img in soup.find_all("img"):
        source = img["src"]
        print("   -", source)
        download_image(base_url + source)

def scrape_page(url: str, data: list[str]) -> None:
    """Extract data from a single profile page"""
    soup = scrape_with_soup(url)
    print(soup.title.string.upper())
    print(f"URL: {url}")
    text = soup.get_text()
    for datum in data:
        item = parse_text_content(text, f"{datum}:")
        print(f" - {datum}:{' ' * (15 - len(datum))} {item}")
    scrape_images(url, soup)
    print()

def main() -> None:
    """Read web pages and scrape images"""
    base_url = "http://olympus.realpython.org/profiles"
    links = get_links(base_url)
    data = ["Name", "Hometown", "Favorite Animal", "Favorite Color"]
    for link in links:
        url = base_url + "/" + link.split("/")[-1]
        scrape_page(url, data)

if __name__ == "__main__":
    main()
