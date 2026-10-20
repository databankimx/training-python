"""Module to test city functions"""

# pylint: disable = no-name-in-module
from city_functions import city_country_population

def main() -> None:
    """Main process"""
    done = False
    while not done:
        obj = {"city": "", "country": "", "population": None}
        for key in obj:
            datum = None
            if key != "population":
                while not datum:
                    datum = input(f"Please enter a {key}: ")
                if datum.lower()[0] == "q":
                    done = True
                    break
                obj[key] = datum
            else:
                datum = input(f"Please enter a {key}: ")
                if not datum:
                    obj[key] = None
                else:
                    if datum.lower() == "q" or datum.lower() == "quit":
                        done = True
                        break
                    try:
                        obj[key] = int(datum)
                    except ValueError:
                        print(f"{datum} is not a number. Passing 'None' for population.")
                        obj[key] = None
        if not done:
            print(city_country_population(obj["city"], obj["country"], obj["population"]))

if __name__ == "__main__":
    main()
