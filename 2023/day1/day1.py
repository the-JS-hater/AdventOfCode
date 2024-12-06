from re import findall


def part_one():
    f = open("input.txt", "r").read().splitlines()
    return sum([int(r[0] + r[-1]) for r in [[n for n in l if n.isnumeric()] for l in f]])


def part_two():
    f = open("input.txt", "r").read().splitlines()
    nss = []
    for l in f:
        ns = findall(r'[0-9]|one|two|three|four|five|six|seven|eight|nine', l)
        ns = [n if n != 'zero' else '0' for n in ns]
        ns = [n if n != 'one' else '1' for n in ns]
        ns = [n if n != 'two' else '2' for n in ns]
        ns = [n if n != 'three' else '3' for n in ns]
        ns = [n if n != 'four' else '4' for n in ns]
        ns = [n if n != 'five' else '5' for n in ns]
        ns = [n if n != 'six' else '6' for n in ns]
        ns = [n if n != 'seven' else '7' for n in ns]
        ns = [n if n != 'eight' else '8' for n in ns]
        ns = [n if n != 'nine' else '9' for n in ns]
        nss.append(ns)

    return sum([int(r[0] + r[-1]) for r in nss])



if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
