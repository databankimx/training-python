## Scraping Images

In addition to the data we've scraped, each of the profile pages has
one or more images on it. Although not necessarily always a part of web 
scraping, sometimes it can be useful to capture the images on pages we
scrape.

---

### Image Download Function

Let's add a function to download images from URLs.

For this, I'll use a utility module we've used in previous examples:

<details>
<summary>relative_paths.py</summary>
<br>

```python
"""A module to expose a simple method to interact with files via relative path"""

from os import path

ROOT_DIR = None

def get_path(file_name: str, folder: str | None=None, parent_levels: int | None=0, debug: bool | None=False) -> str:
    """
    Find the relative path to a specified file

    Parameters:  
    * **file_name**: The name of the file
    * **folder**: The folder the file is stored in (optional - default: None)
    * **parent_levels**: The number of levels above the current directory (optional - default: 0)
    * **debug**: If True, print debug information (optional - default: False)

    **Returns**:  
    The file's relative path
    """
    initialize(debug)
    for _ in range(parent_levels):
        file_name = path.join("..", file_name)
    file_path = path.join(ROOT_DIR, file_name) if folder == None else path.join(ROOT_DIR, folder, file_name)
    if debug:
        print(f"Set file path: {file_path}")
    return file_path

def initialize(debug: bool | None=False) -> None:
    """
    Store the root directory

    Parameters:  
    * **debug**: If True, print debug information (optional - default: False)
    """
    global ROOT_DIR
    if ROOT_DIR != None: return
    ROOT_DIR = path.dirname(__file__)
    if debug:
        print(f"Set root directory: {ROOT_DIR}")
```

</details>
<br>

```python
import requests
from pathlib import Path
from relative_paths import get_path

def download_image(url: str) -> None:
    """Store an image file"""
    image = requests.get(url).content
    filename = url.split("/")[-1]
    filepath = Path(get_path(filename, "images"))
    filepath.write_bytes(image)
```

---

### Scrape Images Function

Now, we can add a function to find all the images on the page

```python
def scrape_images(url: str, soup: BeautifulSoup) -> None:
    """Extract all images from the page"""
    print(" - Images:")
    base_url = "http://" + url.split("/")[2]
    for img in soup.find_all("img"):
        source = img["src"]
        print("   -", source)
        download_image(base_url + source)
```

---

### Pulling It All Together

Finally, we'll modify our scraping routine to include the image grabs:

```python
def scrape_page(url: str, data: list[str]) -> None:
    """Extract data from a single profile page"""

    # -- SNIP --

    scrape_images(url, soup)
    print()
```

Output:

```
PROFILE: APHRODITE
URL: http://olympus.realpython.org/profiles/aphrodite
 - Name:            Aphrodite
 - Hometown:        Mount Olympus
 - Favorite Animal: Dove
 - Favorite Color:  Red
 - Images:
   - /static/aphrodite.gif

PROFILE: POSEIDON
URL: http://olympus.realpython.org/profiles/poseidon
 - Name:            Poseidon
 - Hometown:        Sea
 - Favorite Animal: Dolphin
 - Favorite Color:  Blue
 - Images:
   - /static/poseidon.jpg

PROFILE: DIONYSUS
URL: http://olympus.realpython.org/profiles/dionysus
 - Name:            Dionysus
 - Hometown:        Mount Olympus
 - Favorite Animal: Leopard
 - Favorite Color:  Wine
 - Images:
   - /static/dionysus.jpg
   - /static/grapes.png
```

Additionally, the four captured images can now be found in the
[images](./images/) directory.

---
