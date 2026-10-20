"""Pandas Introduction"""

import pandas as pd

def check_version() -> None:
    """Check the installed version of Pandas"""
    print(f"Running Pandas version: {pd.__version__}\n")

def main() -> None:
    """Main function"""
    check_version()

if __name__ == "__main__":
    main()
