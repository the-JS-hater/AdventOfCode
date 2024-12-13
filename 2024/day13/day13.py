import numpy as np
from re import findall

def part_one():
    f = open("input.txt", "r").read().split("\n\n")
    tot = 0
    
    for eq in f:
        a1, b1, a2, b2, a_res, b_res = [int(n) for n in findall(r"[0-9]+", eq)]
        eq = np.array([[a1, a2], [b1, b2]])
        res = np.array([a_res, b_res])
        res = np.linalg.solve(eq, res)
        
        if all([np.isclose(a, np.round(a)) for a in list(res)]):
            tot += res[0] * 3 + res[1]
    
    return int(tot)


def part_two():
    f = open("input.txt", "r").read().split("\n\n")
    tot = 0
    
    for eq in f:
        a1, b1, a2, b2, a_res, b_res = [int(n) for n in findall(r"[0-9]+", eq)]
        eq = np.array([[a1, a2], [b1, b2]])
        res = np.array([a_res + 10000000000000, b_res + 10000000000000])
        res = np.linalg.solve(eq, res)

        if all([abs(a - round(a)) < 1e-3 for a in res]):
            tot += res[0] * 3 + res[1]
    
    return int(tot)


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
