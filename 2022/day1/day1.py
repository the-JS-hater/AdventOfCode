def part_one():
    f = open("input.txt", "r").read().split("\n\n")
    return max([sum(map(int, line.rstrip().split("\n"))) for line in f])


def part_two():
    f = open("input.txt", "r").read().split("\n\n")
    return sum(sorted([sum(map(int, line.rstrip().split("\n"))) for line in f], reverse=True)[:3])


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
