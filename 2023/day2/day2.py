from re import findall


MAX_R = 12
MAX_G = 13
MAX_B = 14


def part_one():
    f = open("input.txt", "r").read().splitlines()
    idx_sum = 0
    for l in f:
        id = int(findall("Game [0-9]+:", l)[0][5:-1])
        rs = max([int(ns.replace(" red", "")) for ns in findall("[0-9]+ red", l)])
        if rs > MAX_R:
            continue
        gs = max([int(ns.replace(" green", "")) for ns in findall("[0-9]+ green", l)])
        if gs > MAX_G:
            continue
        bs = max([int(ns.replace(" blue", "")) for ns in findall("[0-9]+ blue", l)])
        if bs > MAX_B:
            continue
        
        idx_sum += id
    
    return idx_sum
        
        
def part_two():
    f = open("input.txt", "r").read().splitlines()
    return sum ([
        max([int(ns.replace(" red", "")) for ns in findall("[0-9]+ red", l)]) * 
            max([int(ns.replace(" green", "")) for ns in findall("[0-9]+ green", l)]) * 
            max([int(ns.replace(" blue", "")) for ns in findall("[0-9]+ blue", l)]) \
            for l in f])


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
