"""Using Bit Flags"""

from enum import IntFlag

class ProductLicenses(IntFlag):
    """Defines names for product licenses as bit-flags"""
    unlicensed         = 0b0000_0000
    word_processing    = 0b0000_0001
    spreadsheets       = 0b0000_0010
    presentations      = 0b0000_0100
    email_client       = 0b0000_1000
    notebook           = 0b0001_0000
    collaboration      = 0b0010_0000
    project_management = 0b0100_0000
    publishing         = 0b1000_0000

def main() -> None:
    """Displays names of the product licenses that are enabled"""
    licenses = 11
    for l in ProductLicenses:
        if not licenses & l:
            continue
        print(l.name)

if __name__ == "__main__":
    main()
