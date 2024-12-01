def part_one():
    f = open("input.txt", "r").readlines()
    l1 = sorted([int(string.split("   ")[0]) for string in f])
    l2 = sorted([int(string.split("   ")[1]) for string in f])

    return sum([abs(a - b) for a,b in zip(l1, l2)])


def part_two():
    f = open("input.txt", "r").readlines()
    l1 = [int(string.split("   ")[0]) for string in f]
    l2 = [int(string.split("   ")[1]) for string in f]
    
    return sum([l1.count(x) * x for x in l2])


if __name__ == "__main__":
    print(f"sollution to part one: {part_one()}")
    print(f"sollution to part two: {part_two()}")
