"""Trigonometric Functions"""

import numpy as np

def show_radians(lst: list[int]) -> None:
    """Convert a list of degrees to radians"""
    print("Degrees to Radians:")
    r_arr = np.radians(lst)
    for d, r in zip(lst, r_arr):
        print(f"{d:>3}° = {r / np.pi:.2f}πᶜ")
    print()

def show_hypotenuse(base: int|float, perp: int|float) -> None:
    """Calculate hypotenuse from the leg lengths"""
    hyp = np.hypot(base, perp)
    print(f"For legs {base} and {perp}, hypotenuse = {hyp}\n")

def print_out(txt: str, lbl: str, lst: list[int], arr: np.ndarray) -> None:
    """Print out the results"""
    print(f"{txt.title()}:")
    for d, r in zip(lst, arr):
        if round(d) == 0:
            d = 0.0
        if round(r) == 0:
            r = 0.0
        if r > 1000000:
            r = np.inf
        if isinstance(d, int):
            print(f"{lbl}({d:>3}) = {r:>5.2f}")
        else:
            print(f"{lbl}({d:>5.2f}) = {r:>5.2f}")
    print()

def do_trig(lst: list[int]) -> None:
    """Perform trigonometric functions"""
    rad = np.radians(lst)
    s = np.sin(rad)
    print_out("sine", "sin", lst, s)
    c = np.cos(rad)
    print_out("cosine", "cos", lst, c)
    t = np.tan(rad)
    print_out("tangent", "tan", lst, t)
    a_s = np.arcsin(s)
    print_out("arcsine", "arcsin", s, a_s)
    a_c = np.arccos(c)
    print_out("arccosine", "arccos", c, a_c)
    a_t = np.arctan(t)
    print_out("arctangent", "arctan", c, a_t)

def main() -> None:
    """Run the program"""
    circle_degrees = [45, 90, 135, 180, 225, 270, 315, 360]
    show_radians(circle_degrees)
    base, perp = 3.0, 4.0
    show_hypotenuse(base, perp)
    do_trig(circle_degrees)

if __name__ == "__main__":
    main()
