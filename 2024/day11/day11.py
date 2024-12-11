def part_one():
    f = open("input.txt", "r").read().split(" ")
    f = [int(n) for n in f]
    c = 25
    while c > 0:
        c -= 1
        tmp = []
        for n in f:
            if n == 0:
                tmp.append(1)
            elif len(str(n)) % 2 == 0:
                n1, n2 = int(str(n)[len(str(n))//2:]), int(str(n)[:len(str(n))//2])
                tmp.append(n1)
                tmp.append(n2)
            else:
                tmp.append(n * 2024)
        f = tmp

    return len(f)


def part_two():
    f = open("input.txt", "r").read().split(" ")
    f = [int(n) for n in f]
    
    memo = {}

    def sim(n, i):
        if (n, i) in memo:
            return memo[(n, i)]
        if i == 0:
            return 1
        if n == 0:
            res = sim(1, i-1)
            memo[(1, i-1)] = res
            return res
        elif len(str(n)) % 2 == 0:
            n1, n2 = int(str(n)[len(str(n))//2:]), int(str(n)[:len(str(n))//2])
            res = sim(n1, i-1) + sim(n2, i-1)
            memo[(n, i)] = res
            return res
        else:
            res = sim(n*2024, i-1)
            memo[(n, i)] = res
            return res
    
    return sum([sim(n, 75) for n in f])


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
