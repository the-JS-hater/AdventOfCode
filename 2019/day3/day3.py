def part_one():
    f = open("input.txt", "r")
    wire1 = f.readline().split(",")
    wire2 = f.readline().split(",")
    
    def cable_set(cable):
        new_set = set()
        curr_x = 0
        curr_y = 0
        for instruction in cable:
            length = int(instruction[1:])
            match instruction[0]:
                case 'U':
                    path = {(curr_x, curr_y + i) for i in range(length + 1)}
                    curr_y += length
                case 'D':
                    path = {(curr_x, curr_y - i) for i in range(length + 1)}
                    curr_y -= length
                case 'L':
                    path = {(curr_x - i, curr_y) for i in range(length + 1)}
                    curr_x -= length
                case 'R':
                    path = {(curr_x + i, curr_y) for i in range(length + 1)}
                    curr_x += length
            
            new_set.update(path)
        return new_set
    
    set1 = cable_set(wire1)
    set2 = cable_set(wire2)


    intersections = cable_set(wire1).intersection(cable_set(wire2)).remove((0, 0))
    shortest_dist = float('inf')
    for cross_section in intersections:
        dist = abs(cross_section[0]) + abs(cross_section[1])
        shortest_dist = min(dist, shortest_dist)

    return shortest_dist


def part_two():
    pass


if __name__ == "__main__":
    print(f"Solution to part one is: {part_one()}")
