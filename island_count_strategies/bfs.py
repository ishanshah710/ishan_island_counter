from collections import deque

from constants import DIRECTIONS

def is_valid_cell(row, col, ROWS, COLS):
    return 0 <= row < ROWS and 0 <= col < COLS

def bfs_mark_island(
        grid, start_row, start_col, rows, cols, visited
):
    """
    Performs Breadth-First Search to mark all connected lands as visited.

    Args:
        grid (list[list[int]]): A 2D grid representing land (1) and water (0). 
        start_row (int): Starting row for BFS.
        start_col (int): Starting column for BFS.
        rows (int): row length
        cols (int): column length
        visited (Set): contains (row, col) pair that are visited
    """
    
    queue = deque([(start_row, start_col)])
    visited.add((start_row, start_col))

    while queue:
        current_row, current_col = queue.popleft()
        for dr, dc in DIRECTIONS:
            neighbor_row, neighbor_col = current_row + dr, current_col + dc
            if (
                is_valid_cell(neighbor_row, neighbor_col, rows, cols)
                and grid[neighbor_row][neighbor_col] == 1
                and (neighbor_row, neighbor_col) not in visited
            ):
                visited.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col))
