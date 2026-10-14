"""Real-Time Interaction"""

import time
import mechanicalsoup

def load_multiple_times(dice_url: str, num_loads: int) -> None:
    """Using the browser object, reload a page several times"""
    browser = mechanicalsoup.Browser()
    for i in range(num_loads):
        page = browser.get(dice_url)
        tag = page.soup.select("#result")[0]
        print(f"The result of your dice roll is: {tag.text}")

        if i < num_loads - 1:
            print("Pausing for 1 second...")
            time.sleep(1)

def main() -> None:
    """Main function"""
    dice_url = "http://olympus.realpython.org/dice"
    load_multiple_times(dice_url, 5)

if __name__ == "__main__":
    main()
