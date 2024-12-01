def part_one():
    p = {'X': 1, 'Y': 2, 'Z': 3}
    a = {'X': 3, 'Y': 6, 'Z': 0}
    b = {'X': 0, 'Y': 3, 'Z': 6}
    c = {'X': 6, 'Y': 0, 'Z': 3}
    f = open("input.txt", "r").read().splitlines()
    sum = 0
    for line in f:
        opp, me = line.split(" ")
        if opp == 'A':
            sum += p[me] + a[me]
        if opp == 'B':
            sum += p[me] + b[me]
        if opp == 'C':
            sum += p[me] + c[me]
        
    return sum



def part_two():
    p = {'X': 1, 'Y': 2, 'Z': 3}
    a = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
    b = {'X': 'X', 'Y': 'Y', 'Z': 'Z'}
    c = {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
    f = open("input.txt", "r").read().splitlines()
    
    sum = 0
    for line in f:
        opp, me = line.split(" ")
        if opp == 'A':
            if me == 'X':
                sum += 0 + p[a[me]]
            if me == 'Y':
                sum += 3 + p[a[me]]
            if me == 'Z':
                sum += 6 + p[a[me]]
        if opp == 'B':
            if me == 'X':
                sum += 0 + p[b[me]]
            if me == 'Y':
                sum += 3 + p[b[me]]
            if me == 'Z':
                sum += 6 + p[b[me]]
        if opp == 'C':
            if me == 'X':
                sum += 0 + p[c[me]]
            if me == 'Y':
                sum += 3 + p[c[me]]
            if me == 'Z':
                sum += 6 + p[c[me]]
        
    return sum


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
