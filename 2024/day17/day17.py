REGS = "ABC"


def part_one():
    regs = {reg: 0 for reg in REGS}
    combo = {4: 'A', 5: 'B', 6: 'C'}
    program = []

    r,p = open("test.txt", "r").read().split("\n\n")
    r = r.splitlines()
    p = p.replace("Program: ", "")
    
    def run(program):
        out = ""
        for l in r:
            l = l.replace("Register ", "")
            reg, val = l.split(": ")
            regs[reg] = int(val)
        pc = 0
        while pc < len(program):
            opcode = program[pc]
            operand = program[pc+1]
            match opcode:
                case 0:
                    numerator = regs['A']
                    denominator = operand
                    if operand in combo:
                        denominator = regs[combo[operand]]
                    regs['A'] = numerator // denominator
                case 1:
                    regs['B'] = regs['B'] ^ operand
                case 2:
                    if operand in combo:
                        operand = regs[combo[operand]]
                    regs['B'] = operand % 8
                case 3:
                    if regs['A']:
                        pc = operand
                        continue
                case 4:
                    regs['B'] = regs['B'] ^ regs['C']
                case 5:
                    if operand in combo:
                        operand = regs[combo[operand]]
                    if not out:
                        out = f"{operand % 8}"
                    else:
                        out += f",{operand % 8}"
                case 6:
                    numerator = regs['A']
                    denominator = operand
                    if operand in combo:
                        denominator = regs[combo[operand]]
                    regs['B'] = int(numerator / denominator)
                case 7:
                    numerator = regs['A']
                    denominator = operand
                    if operand in combo:
                        denominator = regs[combo[operand]]
                    regs['C'] = int(numerator / denominator)

            pc += 2
        return out
    
    program = [int(val) for val in p.split(',')]
    initial_out = run(program)
    return initial_out


def part_two():
    pass


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
