from math import sqrt


def part_one():
    f_lines = open("testInput.txt", "r").readlines()
    
    image_str_array = "".join(f_lines).strip().replace("Tile", "").replace(" ", "").split("\n\n")
    
    processed_array = [[img.split(":\n")[0], img.split(":\n")[1].split("\n")]
                         for img in image_str_array]
    
    image_side_length = int(sqrt(len(processed_array)))
    
    # validate(), complete(), solve()
    pass


def solve(n, solution):
    # for each image not in solution, for each rotation
        # try to place it into the solution
    # n bounds the matrix
    pass


def validate(solution):
    # match last, first column side to side
    # match last, first row bottom to top
    pass


def complete(n, solution):
    # check that solution is a n x n matrix
    # ... or maybe just that it has n * n nr. of elems
    pass


def part_two():
    pass


if __name__ == "__main__":
    print(f"solution to part one: {part_one()}")
