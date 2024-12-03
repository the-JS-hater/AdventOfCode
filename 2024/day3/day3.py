from re import findall


def part_one():
    f = open("input.txt", "r").read()
    return sum(int(mul[mul.find('(')+1:mul.find(',')])*int(mul[mul.find(',')+1:mul.find(')')]) for mul in findall(r'mul\([0-9]+,[0-9]+\)', f))


def part_two():
    f = open("input.txt", "r").read()
    matches = findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', f)

    sum = 0
    flag = True
    for mul in matches:
        if mul == "don't()":
            flag = False
            continue
        if mul == "do()":
            flag = True
            continue
        if not flag:
            continue

        op1 = mul[mul.find('(')+1:mul.find(',')]
        op2 = mul[mul.find(',')+1:mul.find(')')]
        sum += int(op1) * int(op2)

    return sum


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
