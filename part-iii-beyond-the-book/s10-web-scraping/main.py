"""Final Web Scraping Program"""

from web_scraping_bot import WebScraper

def main() -> None:
    """Main function - Perform scraping"""
    bot = WebScraper()
    bot.scrape()

if __name__ == "__main__":
    main()
