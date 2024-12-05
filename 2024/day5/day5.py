def part_one():
    f = open("test.txt", "r").read().split("\n\n")
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
    fixed = []  
       
    for row in rows:
        # KAHN'S ALGORTHM
        # https://en.wikipedia.org/wiki/Topological_sorting
        deps_c = deps.copy()
        s = set([node for node in row if node not in deps_c or all(dep not in row for dep in deps_c[node])])
        l = []
        while s:
            print(f"set: {s}")
            print(f"list: {l}")

            n = s.pop()
            l.append(n)
            
            for m in list(deps_c.keys()):
                if n in deps_c[m]:
                    deps_c[m].remove(n)
                if not deps_c[m]:
                    s.add(m)

        fixed.append(l)
    
    return sum([r[len(r)//2] for r in fixed]) 


if __name__ == "__main__":
    s, rs, od = part_one()
    print(f"Solution to part one {s}")
    print(f"Solution to part two {part_two(rs, od)}")
