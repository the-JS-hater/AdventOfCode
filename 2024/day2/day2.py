from itertools import pairwise


def part_one():
    def increasing(nums):
        return all([-4 < a - b < 0 for a,b in pairwise(nums)])
    def decreasing(nums):
        return all([0 < a - b < 4 for a,b in pairwise(nums)])

    f = open("input.txt", "r").read().splitlines()
    f = [list(map(int , (l.rstrip().split(" ")))) for l in f]
    return sum(increasing(l) or decreasing(l) for l in f)


def part_two():
    def increasing(nums):
        return all([-4 < a - b < 0 for a,b in pairwise(nums)])
    def decreasing(nums):
        return all([0 < a - b < 4 for a,b in pairwise(nums)])

    f = open("input.txt", "r").read().splitlines()
    f = [list(map(int , (l.rstrip().split(" ")))) for l in f]
   
    return sum(1 for l in f if any(increasing(l[:i] + l[i+1:]) or decreasing(l[:i] + l[i+1:]) for i in range(len(l))))


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
