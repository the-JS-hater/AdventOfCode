from copy import deepcopy


def part_one(m, pos, dir):
    w = len(m[0])
    h = len(m)
    visited = set()
    visited.add(tuple(pos))

    while True:
        c_m = [pos[0] + dir[0], pos[1] + dir[1]]
        if c_m[0] < 0 or c_m[0] >= w or c_m[1] < 0 or c_m[1] >= h:
            return len(visited)

        if m[c_m[1]][c_m[0]] == '#':
            dir = rotate(dir)  
            continue  
        
        pos = c_m

        visited.add(tuple(pos))  


def part_two(m, pos, dir):
    w = len(m[0])
    h = len(m)
    org_pos = deepcopy(pos)
    org_dir = deepcopy(dir)

    def walk(m, pos, dir):
        path = set()
        path.add((tuple(pos), tuple(dir)))
        while True:
            c_m = [pos[0] + dir[0], pos[1] + dir[1]]
            
            if c_m[0] < 0 or c_m[0] >= w or c_m[1] < 0 or c_m[1] >= h:
                return 0

            if m[c_m[1]][c_m[0]] == '#':
                dir = rotate(dir)  
                continue  
            
            pos = c_m
            if (tuple(pos), tuple(dir)) in path:
                return 1
            
            path.add((tuple(pos), tuple(dir)))  

    loops = []
    while True:
        if pos[0] + dir[0] < 0 or pos[0] + dir[0] >= w or pos[1] + dir[1] < 0 or pos[1] + dir[1] >= h:
            return len(set(loops))

        c_m = [pos[0] + dir[0], pos[1] + dir[1]]

        if m[c_m[1]][c_m[0]] == '#':
            dir = rotate(dir)  
            continue
        elif m[c_m[1]][c_m[0]] == '^':
            pos = c_m
            continue
        else:
            m_copy = deepcopy(m)
            m_copy[c_m[1]][c_m[0]] = '#'
            if walk(m_copy, org_pos, org_dir):
                loops.append(tuple(c_m))
            pos = c_m


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
    f = open("input.txt", "r").read()
    m = f.splitlines()
    m = list(map(list, m))
    dir = [0, -1]  
    pos = find_start(m)
    print(f"Solution to part one {part_one(m, pos, dir)}")
    print(f"Solution to part two {part_two(m, pos, dir)}")
