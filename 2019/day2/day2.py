def part_one(noun, verb):
    program = open("input.txt", "r").readline().replace(" ", "").split(",")
    program = list(map(int, program))
    pos_idx = 0
    
    program[1] = noun 
    program[2] = verb
    
    while program[pos_idx] != 99:
        match program[pos_idx]:
            case 1:
                addr1 = program[pos_idx + 1]
                addr2 = program[pos_idx + 2]
                addr3 = program[pos_idx + 3]
                program[addr3] = program[addr1] + program[addr2]
            case 2:
                addr1 = program[pos_idx + 1]
                addr2 = program[pos_idx + 2]
                addr3 = program[pos_idx + 3]
                program[addr3] = program[addr1] * program[addr2]
        
        pos_idx += 4
    return program[0]


def part_two():
    target = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            if part_one(noun, verb) == target:
                return 100 * noun + verb


if __name__ == "__main__":
    print(f"Solution to part one: {part_one(12, 2)}")
    print(f"Solution to part two: {part_two()}")
