import sys
from collections import deque


DIRECTIONS = [
    (-1, 0), (1, 0), (0, -1), (0, 1),  
    (-1, -1), (-1, 1), (1, -1), (1, 1) 
]

def validate_grid(grid):
    if not grid or not all(isinstance(row, list) for row in grid):
        raise ValueError("Grid elements must be list.")
    row_length = len(grid[0])
    
    if not all(len(row) == row_length for row in grid):
        raise ValueError("All grid rows must have the same length.")
    
    if not all(cell in (0, 1) for row in grid for cell in row):
        raise ValueError("Grid can only contain 0s and 1s.")


def read_grid_and_validate(file_path):
    try:
        with open(file_path, "r") as file:
            grid = [
                list(map(int, line.strip().split())) for line in file
            ]
        validate_grid(grid)
        return grid
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except ValueError:
        print("Invalid file data: Ensure file only has 0s and 1s.")
        sys.exit(1)


def bfs(grid, start_row, start_col, rows, cols, visited):
    queue = deque([(start_row, start_col)])
    visited.add((start_row, start_col))

    while queue:
        current_row, current_col = queue.popleft()
        for dr, dc in DIRECTIONS:
            neighbor_row, neighbor_col = current_row + dr, current_col + dc
            if (
                0 <= neighbor_row < rows
                and 0 <= neighbor_col < cols
                and grid[neighbor_row][neighbor_col] == 1
                and (neighbor_row, neighbor_col) not in visited
            ):
                visited.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col))


def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0
    visited = set()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col) not in visited:  
                island_count += 1
                bfs(grid, row, col, rows, cols, visited)

    return island_count


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_file>", file=sys.stderr)
            sys.exit(1)

        input_file_path = sys.argv[1]
        grid = read_grid_and_validate(input_file_path)
        result = count_islands(grid)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

main()