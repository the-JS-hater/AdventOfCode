def part_one():
    f = open("input.txt", "r").read().split(" ")
    f = [int(n) for n in f]
    c = 25
    while c > 0:
        c -= 1
        tmp = []
        for i, n in enumerate(f):
            if n == 0:
                tmp.append(1)
            elif len(str(n)) % 2 == 0:
                n1, n2 = int(str(n)[len(str(n))//2:]), int(str(n)[:len(str(n))//2])
                tmp.append(n1)
                tmp.append(n2)
            else:
                tmp.append(n * 2024)
        f = tmp

    return len(f)


def part_two():
    f = open("input.txt", "r").read().split(" ")
    f = [int(n) for n in f]
    # TODO: trying to simulate 75 iterations is too slow
    
    pass


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
