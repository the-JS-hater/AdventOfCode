from itertools import combinations


def part_one():
    m = open("input.txt", "r").read().splitlines()
    h = len(m)
    w = len(m[0])

    freqs = {}
    
    for y in range(h):
        for x in range(w):
            if m[y][x] == '.':
                continue
            elif m[y][x] not in freqs:
                freqs[m[y][x]] = [(x,y)]
            else:
                freqs[m[y][x]].append((x, y))

    antinodes = set()
    for freq in freqs.values():
        for a, b in combinations(freq, 2):
            x1, y1 = a
            x2, y2 = b
            dx = x2 - x1
            dy = y2 - y1

            if 0 <= x1 - dx < w and 0 <= y1 - dy < h:
                antinodes.add((x1 - dx, y1 - dy))
            
            if 0 <= x2 + dx < w and 0 <= y2 + dy < h:
                antinodes.add((x2 + dx, y2 + dy))

    return len(antinodes)


def part_two():
    m = open("input.txt", "r").read().splitlines()
    h = len(m)
    w = len(m[0])

    freqs = {}
    for y in range(h):
        for x in range(w):
            if m[y][x] == '.':
                continue
            elif m[y][x] not in freqs:
                freqs[m[y][x]] = [(x,y)]
            else:
                freqs[m[y][x]].append((x, y))

    antinodes = set()
    for freq in freqs.values():
        for a, b in combinations(freq, 2):
            x1, y1 = a
            x2, y2 = b
            dx = x2 - x1
            dy = y2 - y1
            
            x, y = x1, y1
            while 0 <= x < w and 0 <= y < h:
                antinodes.add((x, y))
                x -= dx 
                y -= dy
            
            x, y = x2, y2
            while 0 <= x < w and 0 <= y < h:
                antinodes.add((x, y))
                x += dx
                y += dy

    return len(antinodes)


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
