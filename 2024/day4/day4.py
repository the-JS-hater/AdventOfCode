from re import findall


def part_one():
    f = open("input.txt", "r").read().splitlines();
    vs = sum([len(findall(r"XMAS", l)) for l in f])
    vs += sum([len(findall(r"SAMX", l)) for l in f])
    hs = sum([len(findall(r"XMAS", l)) for l in ["".join(l) for l in zip(*f)]])
    hs += sum([len(findall(r"SAMX", l)) for l in ["".join(l) for l in zip(*f)]])
    
    ds = ["".join(f[r][c] for r, c in zip(range(row_start, len(f)), range(col_start, len(f[0]))))
    for row_start, col_start in [(0, col) for col in range(len(f[0]))] + [(row, 0) for row in range(1, len(f))]
    ]

    ds += ["".join(f[r][c] for r, c in zip(range(row_start, len(f)), range(col_start, -1, -1)))
    for row_start, col_start in [(0, col) for col in range(len(f[0]) - 1, -1, -1)] + [(row, len(f[0]) - 1) for row in range(1, len(f))]
    ]   

    ds = sum([len(findall(r"SAMX", d)) for d in ds]) + sum([len(findall(r"XMAS", d)) for d in ds])
    
    return vs + hs + ds


def part_two():
    f = open("input.txt", "r").read().splitlines()
    return sum(
    1
    for y in range(1, len(f) - 1)
    for x in range(1, len(f[y]) - 1)
    if f[y][x] == 'A' 
        and ((f[y-1][x-1] == 'M' and f[y+1][x+1] == 'S') or 
             (f[y-1][x-1] == 'S' and f[y+1][x+1] == 'M')) and 
        ((f[y-1][x+1] == 'M' and f[y+1][x-1] == 'S') or 
         (f[y-1][x+1] == 'S' and f[y+1][x-1] == 'M'))
    )


if __name__ == "__main__":
    print(f"Slution to part one: {part_one()}")
    print(f"Slution to part two: {part_two()}")
