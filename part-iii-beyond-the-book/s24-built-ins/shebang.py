#! python3

# That line starting the script tells the system to use the python3
# interpreter, even if the default is a different version

import sys


def version_example() -> None:
    """Print the version of the Python that runs the script"""
    print(f"Running Python {sys.version_info.major}.{sys.version_info.minor}")
    print()


def main() -> None:
    """Run the shebang example"""
    version_example()


if __name__ == "__main__":
    main()
