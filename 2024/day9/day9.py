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
    # TODO
    pass


if __name__ == "__main__":
    print(f"Solution to part one {part_one()}")
    print(f"Solution to part two {part_two()}")
