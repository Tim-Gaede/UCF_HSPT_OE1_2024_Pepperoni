from math import asin, ceil, sqrt
from random import randint

NAME = "pepperoni"
test_case = 1
MAX = 1000
RANDOM_CASES = 5

def solve_case(r: int, x: int, y: int, p: int) -> float:
    theta = asin(p / sqrt(x**2 + y**2))
    return r**2 * theta

def make_case(r: int, x: int, y: int, p: int) -> None:
    global test_case

    base_name = f"{NAME}{test_case:03d}"
    test_case += 1
    
    print(f"{base_name}: {r} {x} {y} {p}")

    assert r > 0 and x > 0 and y > 0 and p > 0 
    assert r < MAX and x < MAX and y < MAX and p < MAX
    assert p < r # pepperoni is smaller than the pizza
    assert x**2 + y**2 < (r - p)**2 # fits inside the pizza
    assert x**2 + y**2 > p**2 # doesn't touch the center
    
    ans = solve_case(r, x, y, p) 
    print(f"-> {ans:.15f}")

    with open(f"{base_name}.in", "w") as input, open(f"{base_name}.out", "w") as output:
        input.write(f"{r} {x} {y} {p}\n")
        output.write(f"{ans:.15f}\n")

make_case(10, 1, 6, 2) # not actually sample case 1
make_case(5, 2, 3, 1) # sample case 2
make_case(3, 1, 1, 1)
make_case(MAX-1, 1, 1, 1)
make_case(MAX-1, MAX-3, 1, 1)
make_case(MAX-1, 1, MAX-3, 1)
make_case(MAX-1, 499, 1, 499)
make_case(MAX-1, 1, 499, 499)

for _ in range(RANDOM_CASES):
    r = randint(3, MAX-1)

    while True:
        x = randint(1, r-2)
        y = randint(1, r-2)

        if x**2 + y**2 < (r-1)**2:
            break

    d = sqrt(x**2 + y**2)
    cap = min(ceil(d-1), ceil(r-d-1))
    p = randint(1, cap)
    
    make_case(r, x, y, p)
