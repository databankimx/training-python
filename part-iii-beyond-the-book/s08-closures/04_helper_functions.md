## Nesting Helper Functions

Sometimes a nested function just provides a helper function to do some work
that needs to occur under certain contexts.

One goal when developing APIs is to provide the most flexibility possible.

---

### Example Scenario

Let's imagine a scenario where we have a function that reads a CSV file and
reports on its data.

A developer calling this function might have an already open file object, or
they might instead just have the path to the file. It would be convenient if
the function could accept either one and then open the file if it receives
only the path.

> See [hotspots.csv](./data/hotspots.csv) for the data file we will process.  
> See [helper_functions.py](./04_helper_functions.py) for the full code for
> this example.

The function signature might look like this:

```python
import io

def process_hotspots(file: str | io.TextIOWrapper) -> None:
    """Read CSV and report on WiFi hotspots in NYC"""
    ...
```

How can we ensure that we can handle both possible inputs?

---

### Nesting the Functional Code

First, we can create an inner function that contains the code for parsing the
CSV file. This function will only accept a file object.

```python
import csv
from collections import Counter

def process_hotspots(file: str | io.TextIOWrapper) -> None:

# -- SNIP --

    def most_common_provider(file_obj: io.TextIOWrapper) -> None:
        """Helper function for counts from the CSV"""
        hotspots = []
        with file_obj as csv_file:
            content = csv.DictReader(csv_file)
            for row in content:
                hotspots.append(row["Provider"])

        counter = Counter(hotspots)
        print(
            f"There are {len(hotspots)} Wi-Fi hotspots in NYC.\n"
            f"{counter.most_common(1)[0][0]} has the most with "
            f"{counter.most_common(1)[0][1]}."
        )
```

This inner function parses the CSV file and makes a list of the WiFi hotspots
in New York City. It them reports on the provider of the most hotspots.

---

### Resolving Path vs. File and Calling the Inner Function

We still have an outer function that takes in either a path or a file
object, so we need to resolve that.

Let's add a little logic to the outer function to ensure that we always have
a file object before calling the inner function.

```python

def process_hotspots(file: str | io.TextIOWrapper) -> None:

# -- SNIP --

    if isinstance(file, str):
        with open(file, encoding="utf-8") as file_obj:
            most_common_provider(file_obj)
    else:
        most_common_provider(file)
```

Here, either path calls the inner function, but when the input value is a
string (path only), we open the file, so either path passes a file object.

---

### Testing

Putting it all together, we have this overall function:

<details>
<summary>Helper Function Example</summary>

```python
import os
import sys
import csv
import io
from collections import Counter

def process_hotspots(file: str | io.TextIOWrapper) -> None:
    """Read CSV and report on WiFi hotspots in NYC"""

    def most_common_provider(file_obj: io.TextIOWrapper) -> None:
        """Helper function for counts from the CSV"""
        hotspots = []
        with file_obj as csv_file:
            content = csv.DictReader(csv_file)
            for row in content:
                hotspots.append(row["Provider"])

        counter = Counter(hotspots)
        print(
            f"There are {len(hotspots)} Wi-Fi hotspots in NYC.\n"
            f"{counter.most_common(1)[0][0]} has the most with "
            f"{counter.most_common(1)[0][1]}."
        )

    if isinstance(file, str):
        # Got a string-based filepath
        with open(file, encoding="utf-8") as file_obj:
            most_common_provider(file_obj)
    else:
        # Got a file object
        most_common_provider(file)
```

</details>

---

#### Testing with a File Object

In our calling code, we can open a file and pass the file object.

```python
file_path = os.path.join(os.path.dirname(sys.argv[0]), "data", "hotspots.csv")
with open(file_path, encoding="utf-8") as file_obj:
    process_hotspots(file_obj)
```

Output:

```
There are 3319 Wi-Fi hotspots in NYC.
LinkNYC - Citybridge has the most with 1868.
```

---

#### Testing with a Path

Alternately, we can pass just the path to the file.

```python
file_path = os.path.join(os.path.dirname(sys.argv[0]), "data", "hotspots.csv")
process_hotspots(file_path)
```

Output:

```
There are 3319 Wi-Fi hotspots in NYC.
LinkNYC - Citybridge has the most with 1868.
```

---
