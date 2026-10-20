## Real-Time Interaction

Sometimes, you'll need to perform a task on a page in response to 
another result.

Although not part of our scraping process, let's look at how we can
interact in real time with a page.

---

### Rolling Dice

The Real Python sample site includes a dice rolling page. We'll create
a function that rolls the die on this page several times.

```python
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
```

We can test it like this:

```python
dice_url = "http://olympus.realpython.org/dice"
load_multiple_times(dice_url, 5)
```

Output:

```
The result of your dice roll is: 2
Pausing for 1 second...
The result of your dice roll is: 1
Pausing for 1 second...
The result of your dice roll is: 1
Pausing for 1 second...
The result of your dice roll is: 6
Pausing for 1 second...
The result of your dice roll is: 2
```

---
