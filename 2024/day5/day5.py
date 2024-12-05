from functools import cmp_to_key


def part_one():
    f = open("input.txt", "r").read().split("\n\n")
    od = {}
    for p in f[0].splitlines():
        p = list(map(int, p.split('|')))
        if p[1] not in od:
            od[p[1]] = [p[0]]
        else:
            od[p[1]].append(p[0])
    
    sum = 0
    rs = [] # collect input for part 2
    for l in f[1].splitlines():
        l = list(map(int, l.split(",")))
        seen = set()
        flag = True
        for e in l:
            if e in od:
                r = set(l).intersection(od[e])
                if not r.issubset(seen):
                    flag = False 
                    break
            
            seen.add(e)

        if flag:
            sum += l[len(l)//2]

        if not flag: # collect input for part 2
            rs.append(l)
    
    return sum, rs, od


def part_two(rows, deps):
    def cmp(a, b):
        if b in deps and a in deps[b]:
            return 1
        elif a in deps and b in deps[a]:
            return -1
        else: 
            return 0

    return sum([sorted(row, key=cmp_to_key(cmp))[len(row)//2] for row in rows])


if __name__ == "__main__":
    s, rs, od = part_one()
    print(f"Solution to part one {s}")
    print(f"Solution to part two {part_two(rs, od)}")
