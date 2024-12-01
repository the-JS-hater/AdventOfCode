def part_one():
    return sum(map(int, open("input.txt", "r").readlines()))


def part_two():
    f = list(map(int, open("input.txt", "r").readlines()))
    known = {0}
    freq = 0
    i = 0
    while True:
        freq += f[i % len(f)]
        if freq in known:
            return freq

        known.add(freq)
        i += 1


if __name__ == "__main__":
    print(f"Solution to part one: {part_one()}")
    print(f"Solution to part two: {part_two()}")
