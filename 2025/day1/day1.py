def part_one(input):
    solution = 50
    zs = 0
    for l in input:
        dir, dist = (l[0], int(l[1:]))
        if dir == "L":
            solution = (solution - dist) % 100
        else:
            solution = (solution + dist) % 100
        if not solution: zs += 1
    print(f"sollution to part one: {zs}")

def part_two(input):
    solution = 50
    zs = 0
    for l in input:
        dir, dist = l[0], int(l[1:])
        if dir == "L":
            dist = -dist
        full_revs = abs(dist) // 100
        zs += full_revs
        leftover = abs(dist) % 100
        if leftover:
            if dist < 0:  
                if solution - leftover < 0:
                    zs += 1
            else:         
                if solution + leftover >= 100:
                    zs += 1
        solution = (solution + dist) % 100
    print(f"solution to part two: {zs}")


if __name__ == "__main__":
    l = open("input.txt", "r").readlines()
    part_one(l)
    part_two(l)
