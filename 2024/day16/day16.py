from heapq import heappop, heappush


def part_one():
    m = open("input.txt", "r").read().splitlines()
    w, h = len(m), len(m[0])
    
    for y, row in enumerate(m):
        for x, char in enumerate(row):
            if char == 'S':
                s = x,y
            if char == 'E':
                e = x,y
    
    open_set = []
    heappush(open_set, (0, s, (1, 0)))
    g_score = {s: 0}

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while open_set:
        current_cost, current, current_dir = heappop(open_set)

        if current == e:
            return current_cost

        x, y = current
        for i, (dx, dy) in enumerate(dirs):
            nx, ny = (x + dx, y + dy)

            if not (0 <= nx < w and 0 <= ny < h):
                continue

            if m[ny][nx] == '#':
                continue

            new_cost = 1
            if current_dir != (dx, dy):
                new_cost += 1000

            tentative_g_score = current_cost + new_cost

            if (nx, ny) not in g_score or tentative_g_score < g_score[(nx, ny)]:
                g_score[(nx, ny)] = tentative_g_score
                heappush(open_set, (tentative_g_score, (nx, ny), (dx, dy)))


def part_two():
    pass


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
