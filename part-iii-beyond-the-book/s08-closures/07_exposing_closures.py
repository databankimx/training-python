"""Exposing Closures"""

def make_point(x: int, y: int) -> callable:
    """Generates a point with access to its coordinate values"""
    def point():
        """Defines a point"""
        print(f"Point({x}, {y})")

    def get_x() -> int:
        """Getter function for x"""
        return x

    def get_y() -> int:
        """Getter function for y"""
        return y

    point.get_x = get_x
    point.get_y = get_y

    def set_x(val: int) -> None:
        """Setter function for x"""
        nonlocal x
        x = val

    def set_y(val: int) -> None:
        """Setter function for y"""
        nonlocal y
        y = val

    point.set_x = set_x
    point.set_y = set_y

    return point

def main() -> None:
    """Main function"""
    point = make_point(1, 2)
    point()
    print(f"x = {point.get_x()}")
    print(f"y = {point.get_y()}\n")
    point.set_x(42)
    point.set_y(7)
    point()
    print(f"x = {point.get_x()}")
    print(f"y = {point.get_y()}")

if __name__ == "__main__":
    main()
