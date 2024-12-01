def part_one():
    f = open("input.txt", "r").read().splitlines()
    return sum([ord(c) - 38 if c.isupper() else ord(c) - 96 for c in ["".join(set(r[:len(r)//2]).intersection(r[len(r)//2:])) for r in f]])


def part_two():
    f = open("input.txt", "r").read().splitlines()
    return sum([ord(c)-38 if c.isupper() else ord(c)-96 for c in ["".join(set(f[i]).intersection(set(f[i+1]).intersection(set(f[i+2])))) for i in range(0, len(f), 3)]])


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
