def part_one():
    f = open("input.txt", "r").read().replace("\n", "")
    f = list(map(int, f))
    idx_l = []
    flag = False
    
    i = 0
    for n in f:
        if flag:
            idx_l += [-1] * n
        else:
            idx_l += [i] * n
            i += 1
        flag = not flag

    r_i = -1
    l_i = 0
    
    while l_i < len(idx_l) and abs(r_i) <= len(idx_l) and l_i < len(idx_l) + r_i:
        if idx_l[l_i] != -1:
            l_i += 1
            continue
        
        while idx_l[r_i] == -1:
            r_i -= 1
        
        idx_l[l_i] = idx_l[r_i]
        idx_l[r_i] = -1
        l_i += 1
        r_i -= 1
    
    return sum([i * n for i,n in enumerate(idx_l) if n != -1])


def part_two():
    f = open("test.txt", "r").read().replace("\n", "")
    f = list(map(int, f))
    idx_l = []
    free_l = []
    
    flag = False
    i = 0
    for n in f:
        if flag:
            free_l.append(n)
        else:
            idx_l.append((i, n))
            i += 1
        flag = not flag

    print(idx_l)
    print(free_l)
    
    dumb = []
    org_l = idx_l.copy()
    offset_dic = {i: 1 for i in range(len(free_l))}
    tmp_idxs = idx_l[::-1][:-1]
    for i, size in tmp_idxs:
        for j, space in enumerate(free_l):
            if space < size:
                continue

            free_l[j] -= size
            org_i = org_l.index((i, size))
            dumb.append((org_i - 1, size))
            #free_l[org_i - 1] += size
            tmp_idxs.remove((i, size))
            idx_l.remove((i, size))
            idx_l.insert(j + offset_dic[j], (i, size))
            offset_dic[j] += 1
            break
    
    for i, size in dumb:
        free_l[i] += size

    print(idx_l)
    print(free_l)


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
