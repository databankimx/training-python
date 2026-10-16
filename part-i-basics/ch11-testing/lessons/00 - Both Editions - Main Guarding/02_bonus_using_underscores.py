"""Using underscores in names"""

# pylint: disable=wildcard-import, unused-wildcard-import
from underscore_module import * #NOSONAR
import underscore_module

class MyClass: #pylint: disable=too-few-public-methods
    """Demonstrates name mangling"""

    def __init__(self):
        self.__name = "value" #pylint: disable=unused-private-member #NOSONAR

def main() -> None:
    """Main function"""
    print("Leading underscore with import *:")
    print(f"  visible_name defined: {'visible_name' in globals()}")
    print(f"  _hidden_name defined: {'_hidden_name' in globals()}")

    print("Leading underscore with import module:")
    print(f"  underscore_module._hidden_name = {underscore_module._hidden_name}") #pylint: disable=protected-access #NOSONAR

    print("Trailing underscore:")
    class_ = "a value that can't use the reserved word"
    print(f"  class_ = {class_}")

    print("Single underscore:")
    count = 0
    for _ in range(3):
        count += 1
    print(f"  loop ran {count} times")
    var1, _, _, var2, _ = ["important", "meh", "meh", "important", "meh"]
    print(f"  var1 = {var1}, var2 = {var2}")

    print("Double leading underscore (name mangling):")
    thing = MyClass()
    print(f"  thing._MyClass__name = {thing._MyClass__name}") #pylint: disable=protected-access #NOSONAR
    print(f"  hasattr(thing, '__name'): {hasattr(thing, '__name')}")

    print("Dunder names:")
    print(f"  __name__ = {__name__}")

if __name__ == "__main__":
    main()
