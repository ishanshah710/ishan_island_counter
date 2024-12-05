import sys

from island_count_strategies.bfs import bfs_mark_island
from utils import read_grid_and_validate

def count_islands(grid):
    """
    Counts the number of islands in the grid using BFS.

    Args:
        grid (list[list[int]]): A 2D grid representing land (1) and water (0).

    Returns:
        int: The number of distinct islands.
    """
    
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0
    visited = set()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col) not in visited:  
                island_count += 1
                bfs_mark_island(grid, row, col, rows, cols, visited)

    return island_count


def main(file_path):
    try:
        grid = read_grid_and_validate(file_path)
        result = count_islands(grid)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_file>", file=sys.stderr)
        sys.exit(1)

    input_file_path = sys.argv[1]
    main(input_file_path)