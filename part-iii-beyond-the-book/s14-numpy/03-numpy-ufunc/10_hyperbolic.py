"""Hyperbolic Functions"""

import numpy as np

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
            print(f"{lbl}({d:>6.2f}) = {r:>5.2f}")
    print()

def do_trig_h(lst: list[int]) -> None:
    """Perform hyperbolic functions"""
    rad = np.radians(lst)
    s = np.sin(rad)
    print_out("hyperbolic sine", "sinh", lst, s)
    c = np.cosh(rad)
    print_out("hyperbolic cosine", "cosh", lst, c)
    t = np.tanh(rad)
    print_out("hyperbolic tangent", "tanh", lst, t)
    a_s = np.arcsinh(s)
    print_out("hyperbolic arcsine", "arcsinh", s, a_s)
    a_c = np.arccosh(c)
    print_out("hyperbolic arccosine", "arccosh", c, a_c)
    a_t = np.arctanh(t)
    print_out("hyperbolic arctangent", "arctanh", c, a_t)

def main() -> None:
    """Main function"""
    circle_degrees = [45, 90, 135, 180, 225, 270, 315, 360]
    do_trig_h(circle_degrees)

if __name__ == "__main__":
    main()
