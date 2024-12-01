def part_one():
    f = open("input.txt", "r")
    nums = [int(n) for n in f.readlines()]
    nums.sort()

    for a in nums:
        for b in nums:
            if a + b == 2020:
                return a * b
            if a + b > 2020:
                break


def part_two():
    f = open("input.txt", "r")
    nums = [int(n) for n in f.readlines()]
    nums.sort()

    for i, a in enumerate(nums):
        l = i + 1
        r = len(nums) - 1

        while l < r:
            b, c = nums[l], nums[r]
            total = a + b + c

            if total == 2020:
                return a*b*c
            if total > 2020:
                r -= 1
            else:
                l += 1


if __name__ == "__main__":
    print(f"solution to part one: {part_one()}")
    print(f"solution to part two: {part_two()}")
