def part_one():
    f = open("input.txt", "r").read().split("\n\n")
    od = {}
    for p in f[0].splitlines():
        p = list(map(int, p.split('|')))
        if p[1] not in od:
            od[p[1]] = [p[0]]
        else:
            od[p[1]].append(p[0])
    
    print(od)
    sum = 0
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
    
    return sum


def part_two():
    f = open("input.txt", "r").read().split("\n\n")
    od = {}
    for p in f[0].splitlines():
        p = list(map(int, p.split('|')))
        if p[1] not in od:
            od[p[1]] = [p[0]]
        else:
            od[p[1]].append(p[0])
    
    sum = 0
    for l in f[1].splitlines():
        l = list(map(int, l.split(",")))
        seen = set()
        for e in l:
            if e in od:
                r = set(l).intersection(od[e])
                if not r.issubset(seen):
                    #TODO
                    #fix rows
                    pass
            
            seen.add(e)
    
    return sum


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
