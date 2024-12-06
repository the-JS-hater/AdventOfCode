def part_one():
    f = open("input.txt", "r").read()
    f = f.splitlines()
    w = len(f[0])
    h = len(f)
    visited = set()
    dir = [0, -1]  
    pos = find_start(f)

    visited.add((pos[0], pos[1]))  

    while True:
        if pos[0] + dir[0] < 0 or pos[0] + dir[0] >= w or pos[1] + dir[1] < 0 or pos[1] + dir[1] >= h:
            return len(visited)

        c_m = [pos[0] + dir[0], pos[1] + dir[1]]

        if f[c_m[1]][c_m[0]] == '#':
            dir = rotate(dir)  
            continue  

        pos = c_m
        visited.add((pos[0], pos[1]))  


def part_two():
    #TODO:
    pass


def find_start(m):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == '^':
                return [x, y]


def rotate(dir):
    match dir:
        case [1, 0]: 
            return [0, 1]
        case [0, 1]:    
            return [-1, 0]
        case [-1, 0]: 
            return [0, -1]
        case [0, -1]: 
            return [1, 0]


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
