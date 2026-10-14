"""Final Web Scraping Bot"""

import json
from pathlib import Path
from urllib.request import urlopen
from relative_paths import get_path
from utility_functions import pause
from mechanicalsoup import Browser
import requests
from bs4 import BeautifulSoup

class WebScraper():
    """Simple web scraping bot"""

    def __init__(self, config_loc: str="data",
                 config_file: str="secrets.json") -> None:
        """Initialize"""
        settings = json.loads(
            Path(get_path(config_file, config_loc)).read_text(encoding="utf-8"))
        self.base_url = settings["base_url"]
        self.username = settings["un"]
        self.password = settings["pw"]
        self.debug = settings["debug"]
        self.img_folder = settings["img_folder"]
        self.data = settings["data"]
        if self.debug:
            self.debug_message("Initialized Web Scraper.\n")

    def debug_message(self, message: str) -> None:
        """Print a debug message"""
        print(message)
        pause()
        print()

    def full_url(self, url: str) -> str:
        """Make sure the URL starts with the base URL"""
        return (url if url.startswith(self.base_url)
                else self.base_url + url)

    def log_in(self, url: str="/login") -> str:
        """Log into the main page and return the result URL"""
        browser = Browser()
        login_page = browser.get(self.full_url(url))
        login_html = login_page.soup
        login_form = login_html.select("form")[0]
        un = login_form.select("input[name='user']")[0]
        un["value"] = self.username
        pw = login_form.select("input[name='pwd']")[0]
        pw["value"] = self.password
        result_page = browser.submit(login_form, login_page.url)
        if self.debug:
            self.debug_message(
                f"Logged in and found links page: {result_page.url}\n")
        return result_page.url

    def scrape_with_soup(self, url: str) -> BeautifulSoup:
        """Returns soup object"""
        page = urlopen(url)
        html = page.read().decode("utf-8")
        return BeautifulSoup(html, "html.parser")

    def get_links(self, url: str) -> list[str]:
        """Obtain the links to the profile pages"""
        soup = self.scrape_with_soup(self.full_url(url))
        links = [l["href"] for l in soup.find_all("a")]
        if self.debug:
            self.debug_message(f"Obtained links: {links}\n")
        return links

    def parse_text_content(self, text: str, search: str) -> str:
        """Read information from the text"""
        start = text.lower().find(search.lower()) + len(search)
        end = text[start:].find("\n") + start
        return text[start:end].strip(" \r\n\t")

    def download_image(self, url: str) -> None:
        """Store an image file"""
        image = requests.get(self.full_url(url), timeout=10).content
        filename = url.split("/")[-1]
        filepath = Path(get_path(filename, self.img_folder))
        filepath.write_bytes(image)
        if self.debug:
            self.debug_message(f"Stored image: {filename}\n")

    def scrape_images(self, soup: BeautifulSoup) -> None:
        """Extract all images from the page"""
        print(" - Images:")
        for img in soup.find_all("img"):
            source = img["src"]
            print("   -", source)
            self.download_image(source)

    def get_data(self, url: str) -> None:
        """Find and print out the data for the specified profile page"""
        soup = self.scrape_with_soup(self.full_url(url))
        print(soup.title.string.upper())
        text = soup.get_text()
        span = max([len(d) for d in self.data])
        for datum in self.data:
            item = self.parse_text_content(text, f"{datum}:")
            print(f" - {datum}:{' ' * (span - len(datum))} {item}")
        self.scrape_images(soup)
        print()

    def scrape(self) -> None:
        """Perform full scraping process"""
        links_url = self.log_in()
        links = self.get_links(links_url)
        for link in links:
            self.get_data(link)
