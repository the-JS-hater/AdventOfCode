def part_one():
    f = open("input.txt").read().splitlines()
    m = [[int(c) for c in l] for l in f]
    zeroes = [(x, y) for y in range(len(m)) for x in range(len(m[0])) if not m[y][x]]
    h = len(m)
    w = len(m[0])

    def dfs(prev, pos):
        x, y = pos
        if not (0 <= x < w) or not (0 <= y < h):
            return []
        current = m[y][x]
        if not (current == prev + 1):
            return []
        if current == 9:
            return [pos]
        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return dfs(current, (x+1, y)) + dfs(current, (x-1, y)) + dfs(current, (x, y+1)) + dfs(current, (x, y-1))
        
    tot = 0
    for x, y in zeroes:
        tot += len(set(dfs(0, (x+1, y)) + dfs(0, (x-1, y)) + dfs(0, (x, y+1)) + dfs(0, (x, y-1))))
    
    return tot


def part_two():
    f = open("input.txt").read().splitlines()
    m = [[int(c) for c in l] for l in f]
    zeroes = [(x, y) for y in range(len(m)) for x in range(len(m[0])) if not m[y][x]]
    h = len(m)
    w = len(m[0])

    def dfs(prev, pos):
        x, y = pos
        if not (0 <= x < w) or not (0 <= y < h):
            return False
        current = m[y][x]
        if not (current == prev + 1):
            return False
        if current == 9:
            return True
        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return sum([dfs(current, neighbor) for neighbor in neighbours])
        
    tot = 0
    for x, y in zeroes:
        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        tot += sum([dfs(0, neighbor) for neighbor in neighbours])   

    return tot


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
