def part_one():
    f  = open("input.txt", "r").read().splitlines()
    
    sum = 0
    for p in f:
        l1, h1, l2, h2 = map(int, p.replace(",", "-").split("-"))
        if l1 <= l2 and h2 <= h1:
            sum += 1
        elif l2 <= l1 and h1 <= h2:
            sum += 1

    return sum


def part_two():
    f  = open("input.txt", "r").read().splitlines()
    
    sum = 0
    for p in f:
        l1, h1, l2, h2 = map(int, p.replace(",", "-").split("-"))
        if l2 <= l1 <= h2:
            sum += 1
        elif l1 <= l2 <= h1:
            sum += 1
        elif l2 <= h1 <= h2:
            sum += 1
        elif l1 <= h2 <= h1:
            sum += 1
    
    return sum


if __name__ == "__main__":
    print(f"solution to part one: {part_one()}")
    print(f"solution to part two: {part_two()}")
