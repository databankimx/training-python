"""Inner Functions as Helpers"""

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

def main() -> None:
    """Run the program"""
    file_path = os.path.join(os.path.dirname(sys.argv[0]), "data", "hotspots.csv")

    # We can now call our outer function with a string path...
    print("\nCall with path...")
    process_hotspots(file_path)

    # ... or with a file object
    print("\nCall with file...")
    with open(file_path, encoding="utf-8") as file_obj:
        process_hotspots(file_obj)

if __name__ == "__main__":
    main()
