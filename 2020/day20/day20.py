from math import sqrt
from itertools import pairwise


def part_one():
    f_lines = open("testInput.txt", "r").readlines()
    image_str_array = "".join(f_lines).strip().replace("Tile", "").replace(" ", "").split("\n\n")
    
    processed_array = [[img.split(":\n")[0], img.split(":\n")[1].split("\n")]
                         for img in image_str_array]
    
    image_side_length = int(sqrt(len(processed_array)))
    
    solution = [[None for _ in range(image_side_length)] for _ in range(image_side_length)]
    
    solved_grid = solve(image_side_length, solution, processed_array)
    
    if solved_grid:
        corner_ids = [
            int(solved_grid[0][0][0]),  
            int(solved_grid[0][-1][0]),  
            int(solved_grid[-1][0][0]),  
            int(solved_grid[-1][-1][0]),  
        ]
        return corner_ids, eval('*'.join(map(str, corner_ids)))
    return None


def solve(n, solution, remaining):
    if complete(n, solution):
        if validate(solution):
            return solution
        return None

    row, col = find_next_empty(n, solution)
    if row is None or col is None:
        return None

    for i, (tile_id, tile_matrix) in enumerate(remaining):
        for orientation in generate_orientations(tile_matrix):
            solution[row][col] = [tile_id, orientation]
            
            result = solve(
                n,
                solution,
                remaining[:i] + remaining[i+1:]  
            )
            if result:  
                return result
        solution[row][col] = None

    return None  


def validate(solution):
    for row in solution:
        for left, right in pairwise(row):
            left_matrix = left[1]  
            right_matrix = right[1]
            
            left_column = [r[-1] for r in left_matrix]  
            right_column = [r[0] for r in right_matrix]
            
            if left_column != right_column:
                return False

    for upper, lower in pairwise(solution):
        for i in range(min(len(upper), len(lower))):  
            upper_matrix = upper[i][1]  
            lower_matrix = lower[i][1]
            
            upper_row = upper_matrix[-1]  
            lower_row = lower_matrix[0]  
            
            if upper_row != lower_row:
                return False

    return True


def complete(n, solution):
    return all(all(cell is not None for cell in row) for row in solution)


def rotate(matrix):
    return ["".join(row) for row in zip(*matrix[::-1])]


def flip(matrix):
    return [row[::-1] for row in matrix]


def generate_orientations(matrix):
    orientations = []
    rotated = matrix
    for _ in range(4):  
        orientations.append(rotated)
        orientations.append(flip(rotated))  
        rotated = rotate(rotated)
    return orientations


def find_next_empty(n, solution):
    for i, row in enumerate(solution):
        for j, cell in enumerate(row):
            if cell is None:
                return i, j
    return None, None  


def part_two():
    pass


if __name__ == "__main__":
    corners, product = part_one()
    print(f"Corners: {corners}")
    print(f"Solution to part one (product of corners): {product}")
