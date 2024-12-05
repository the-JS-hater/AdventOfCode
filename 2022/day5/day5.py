def part_one():
    f = open("input.txt", "r").read().split("\n\n")
    print(list(zip(*f[0].splitlines())))
    
    stacks = [[] for i in range(9)]
    for stack_i in range(9):
        pass



def part_two():
    pass


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
