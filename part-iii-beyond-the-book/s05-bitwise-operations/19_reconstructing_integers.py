"""Module to reconstruct integers from a data stream"""

def reconstruct_integers(byte_arr: list[int], size: int=4) -> list[int]:
    """Construct integers from data stream"""
    assert len(byte_arr) % size == 0, "Invalid data!"

    num_units = len(byte_arr) // size

    integers = []

    for n in range(0, num_units * size, size):
        data = byte_arr[n:n+size]
        integers.append(reconstruct_integer(data, size))

    return integers

def reconstruct_integer(data: list[int], size: int=4) -> int:
    """Construct integer from data set"""
    assert len(data) == size, "Invalid data!"

    num = 0
    for i, n in enumerate(data):
        num += n << (i * 8)
    return num

def main() -> None:
    """Test the reconstruct_integers function"""
    byte_arr = [
        0b0000_0000, 0b0000_0000, 0b0000_0000, 0b0000_0000,
        0b1101_0010, 0b0000_0010, 0b1001_0110, 0b0100_1001,
        0b0001_0101, 0b1100_1101, 0b0101_1011, 0b0000_0111,
        0b1111_1111, 0b1111_1111, 0b1111_1111, 0b1111_1111
    ]
    values = reconstruct_integers(byte_arr)
    for value in values:
        out = f"{value:,}"
        print(f"{out:>13}")

if __name__ == "__main__":
    main()
