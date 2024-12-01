from collections import Counter


def part_one():
    twos = 0
    threes = 0
    f = open("input.txt", "r").readlines()
    for string in f:
        vals = Counter(string).values()
        twos += 2 in vals
        threes += 3 in vals
    return twos * threes



def part_two():
    f = open("input.txt", "r").read().splitlines()
    for i, string in enumerate(f):
        for second in f[i + 1:]:
            diffs = 0
            idx = None
            for j in range(len(string)):
                if string[j] != second[j]:
                    diffs += 1
                    idx = j
            if diffs == 1:
                return string[:idx] + string[idx + 1:]


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
