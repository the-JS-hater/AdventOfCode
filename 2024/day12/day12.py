from collections import deque


def part_one():
    m = open("input.txt").read().splitlines()
    h = len(m)
    w = len(m[0])
    visited = set()
    
    def calc_area(id, coord):
        area = set()
        to_visit = deque([coord])
        while True:
            if not to_visit:
                break
            x, y = to_visit.popleft()
            if m[y][x] == id:
                area.add((x,y))
                visited.add((x,y))
            else:
                continue
            
            neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
            for x, y in neighbors:
                if not (0 <= x < w) or not (0 <= y < h):
                    continue
                if (x, y) in visited or (x,y) in to_visit:
                    continue
                to_visit.append((x,y))
        
        perim = 0
        for x, y in area:
            neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
            
            for neighbor in neighbors:
                 if neighbor not in area:
                     perim += 1

        return len(area) * perim

    cost = 0
    for y, r in enumerate(m):
        for x, id in enumerate(m[y]):
            if (x, y) in visited:
                continue
            else:
                cost += calc_area(id, (x,y))

    return cost


def part_two():
    m = open("test.txt").read().splitlines()
    h = len(m)
    w = len(m[0])
    visited = set()
    
    def calc_area(id, coord):
        area = set()
        to_visit = deque([coord])
        while True:
            if not to_visit:
                break
            x, y = to_visit.popleft()
            if m[y][x] == id:
                area.add((x,y))
                visited.add((x,y))
            else:
                continue
            
            neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
            for x, y in neighbors:
                if not (0 <= x < w) or not (0 <= y < h):
                    continue
                if (x, y) in visited or (x,y) in to_visit:
                    continue
                to_visit.append((x,y))
        

        # TODO: if i can simply detect the nr. of corners,
        # nr. of coreners == nr. of sides
        sides = 0
        for x, y in area:
            neighbors = [(x-1,y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1)]
            n_corners = sum([neighbor in area for neighbor in neighbors])

        return len(area) * sides

    cost = 0
    for y, r in enumerate(m):
        for x, id in enumerate(m[y]):
            if (x, y) in visited:
                continue
            else:
                cost += calc_area(id, (x,y))

    return cost


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
