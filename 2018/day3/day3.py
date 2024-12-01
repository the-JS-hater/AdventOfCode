def part_one():
    f = open("test.txt", "r").read().splitlines()
    sets = []
    for line in f:
        data = line.split("@ ")[1].split(": ")
        coord, area = data
        coord = list(map(int, coord.split(",")))
        area = list(map(int, area.split("x")))
            
        sets += {(coord[0] + x, coord[1] + y) for x in range(area[0]) for y in range(area[1])}
    
    print(sets)
    sum = 0
    for i, set1 in enumerate(sets):
        for set2 in sets[i + 1:]:
            sum += len(set1.intersection(set2))

    return sum
    

def part_two():
    pass


if __name__ == "__main__":
    print(f"Solution to part one: {part_one()}")
