def part_one():
    f = open("input.txt", "r").read().splitlines()
    def solveable(val, nums):
        if len(nums) == 1:
            return nums[0] == val
        return solveable(val, [nums[0] + nums[1]] + nums[2:]) or solveable(val, [nums[0] * nums[1]] + nums[2:])
    
    return sum([int(l.split(": ")[0]) for l in f if solveable(int(l.split(": ")[0]), list(map(int, l.split(": ")[1].split(" "))))])


def part_two():
    f = open("input.txt", "r").read().splitlines()
    def solveable(val, nums):
        if len(nums) == 1:
            return nums[0] == val
        return solveable(val, [nums[0] + nums[1]] + nums[2:]) or \
                solveable(val, [nums[0] * nums[1]] + nums[2:]) or \
                solveable(val, [int(str(nums[0]) + str(nums[1]))] + nums[2:]) 
    
    return sum([int(l.split(": ")[0]) for l in f if solveable(int(l.split(": ")[0]), list(map(int, l.split(": ")[1].split(" "))))])


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
