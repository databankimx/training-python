"""Lesson 4.2"""

def noob_loop_list(lst: list[int]) -> None:
    """Print items and indices in a list looping on index"""
    print("Looping list on index:")
    # pylint: disable=consider-using-enumerate
    for i in range(len(lst)):
        item = lst[i]
        print(f"Index: {i}, Item: {item}")
    print()

def loop_list(lst: list[int]) -> None:
    """Print items and indices in a list using a for-loop"""
    print("Looping list on enumerate:")
    for i, item in enumerate(lst):
        print(f"Index: {i}, Item: {item}")
    print()

def noob_loop_two_lists(lst_1: list[int], lst_2: list[str]) -> None:
    """Print items from two lists, looping on index"""
    print("Looping two lists on index:")
    # pylint: disable=consider-using-enumerate
    for i in range(len(lst_1)):
        item_1 = lst_1[i]
        item_2 = lst_2[i]
        print(f"Index: {i}, Item 1: {item_1}, Item 2: {item_2}")
    print()

def loop_two_lists(lst_1: list[int], lst_2: list[str]) -> None:
    """Print items from two lists using a for-loop"""
    print("Looping two lists on enumerate/zip:")
    for i, (item_1, item_2) in enumerate(zip(lst_1, lst_2)):
        print(f"Index: {i}, Item 1: {item_1}, Item 2: {item_2}")
    print()

def noob_loop_dict(dic: dict[int, str]) -> None:
    """Print keys and values in a dictionary looping on index"""
    print("Looping dictionary on index:")
    for i in range(len(dic)):
        key = list(dic.keys())[i]
        value = dic[key]
        print(f"Index: {i}, Key: {key}, Value: {value}")
    print()

def loop_dict(dic: dict[int, str]) -> None:
    """Print keys and values in a dictionary using a for-loop"""
    print("Looping dictionary on enumerate:")
    for i, (key, value) in enumerate(dic.items()):
        print(f"Index: {i}, Key: {key}, Value: {value}")
    print()

def main() -> None:
    """Main function to demonstrate loops"""
    nums = [1, 42, 73]
    letters = ["S", "W", "M"]
    noob_loop_list(nums)
    loop_list(nums)
    noob_loop_two_lists(nums, letters)
    loop_two_lists(nums, letters)
    nums_letters = {nums[i]: letters[i] for i in range(len(nums))}
    noob_loop_dict(nums_letters)
    loop_dict(nums_letters)

if __name__ == "__main__":
    main()
