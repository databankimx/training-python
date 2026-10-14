"""Using the `urllib` library"""

from urllib.request import urlopen

def scrape_page(url: str) -> str:
    """Returns the HTML content of a web page"""
    with urlopen(url) as page:
        page_bytes = page.read()
        return page_bytes.decode("utf-8")

def parse_html(html: str, tag_to_find: str) -> str:
    """Locate specified HTML tag and returns its content"""
    tag_to_find = tag_to_find.lower()
    start_index = html.lower().find(f"<{tag_to_find}>") \
        + len(tag_to_find) + 2
    end_index = html.lower().find(f"</{tag_to_find}>")
    return html[start_index:end_index]

def main() -> None:
    """Read web pages and print the titles"""
    pages = [
        "http://olympus.realpython.org/profiles/aphrodite",
        "http://olympus.realpython.org/profiles/poseidon"
    ]

    for page in pages:
        html = scrape_page(page)
        title = parse_html(html, "title")
        print(title)

if __name__ == "__main__":
    main()
