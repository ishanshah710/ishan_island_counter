import sys
from collections import deque


DIRECTIONS = [
    (-1, 0), (1, 0), (0, -1), (0, 1),  
    (-1, -1), (-1, 1), (1, -1), (1, 1) 
]


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
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1]
        ]
        result = count_islands(grid)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

main()