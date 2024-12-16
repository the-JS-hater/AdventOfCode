from re import findall


WIDTH = 101
HEIGHT = 103
ITERATIONS = 100

def part_one():
    f = open("input.txt", "r").read().splitlines()
    robots = []

    for l in f:
        robots.append([int(n) for n in findall(r"-?[0-9]+", l)])
    
    t_l = 0
    b_l = 0
    t_r = 0
    b_r = 0

    for x, y, dx, dy in robots:
        x = (x + dx * ITERATIONS) % WIDTH
        y = (y + dy * ITERATIONS) % HEIGHT
        
        if x == WIDTH // 2 or y == HEIGHT // 2:
            continue 
        
        match [x < WIDTH // 2, y < HEIGHT // 2]:
            case [True, True]:
                t_l += 1
                continue
            case [True, False]:
                b_l += 1
                continue
            case [False, True]:
                t_r += 1
                continue
            case [False, False]:
                b_r += 1
                continue

    return t_l * b_l * t_r * b_r


def part_two():
    f = open("input.txt", "r").read().splitlines()
    robots = []

    for l in f:
        robots.append([int(n) for n in findall(r"-?[0-9]+", l)])
    
    
    # i=6752 to see the tree :)
    i = 0
    while True:
        i += 1
        t_l = 0
        b_l = 0
        t_r = 0
        b_r = 0
        map = [[" " for i in range(WIDTH)] for j in range(HEIGHT)]

        for x, y, dx, dy in robots:
            x = (x + dx * i) % WIDTH
            y = (y + dy * i) % HEIGHT
            map[y][x] = "x"   
            if x == WIDTH // 2 or y == HEIGHT // 2:
                continue 
            
            match [x < WIDTH // 2, y < HEIGHT // 2]:
                case [True, True]:
                    t_l += 1
                    continue
                case [True, False]:
                    b_l += 1
                    continue
                case [False, True]:
                    t_r += 1
                    continue
                case [False, False]:
                    b_r += 1
                    continue

        n = t_l * b_l * t_r * b_r
        if n < 200000000:
            printable_map = "".join(["".join(row) + "\n" for row in map])
            print(f"i={i}\n {printable_map}\n")
            input()


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
