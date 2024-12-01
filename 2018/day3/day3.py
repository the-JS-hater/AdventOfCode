def part_one():
    f = open("test.txt", "r").read().splitlines()
    sets = []
    for line in f:
        data = line.split("@ ")[1].split(": ")
        coord, area = data
        coord = list(map(int, coord.split(",")))
        area = list(map(int, area.split("x")))
           
        sets += set({(coord[0] + x, coord[1] + y) for x in range(area[0]) for y in range(area[1])})
    
    print(sets)

    

def part_two():
    pass


if __name__ == "__main__":
    print(f"Solution to part one: {part_one()}")
