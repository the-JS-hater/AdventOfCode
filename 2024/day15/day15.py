def part_one():
    
    map, instructions = open("input.txt").read().split("\n\n") 
    map = map.splitlines()
    instructions = "".join(instructions.replace("\n", ""))
    h = len(map)
    w = len(map[0])

    def find_robot():
        for y, row in enumerate(map):
            for x, val in enumerate(row):
                if val == "@":
                    return x,y
    
    def collision(x, y):
        if not (0<=x<w):
            return True
        if not (0<=y<h):
            return True
        if map[y][x] == "#":
            return True

        return False
    
    def is_box(x, y):
        if not (0<=x<w):
            return False 
        if not (0<=y<h):
            return False 
        if map[y][x] == "O":
            return True


    pos = find_robot()
    for instruction in instructions:
        match instruction:
            case '<':
                dx, dy = -1, 0
            case 'v':
                dx, dy = 0, 1
            case '>':
                dx, dy = 1, 0
            case '^':
                dx, dy = 0, -1

        nx, ny = x + dx, y + dy
        
        if collision(nx, ny):
            continue
        if is_box(nx, ny):
            #move row/col
            pass
        
        pos = nx, ny



def part_two():
    pass


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
