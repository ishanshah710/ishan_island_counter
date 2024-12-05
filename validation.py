"""validation.py file for different validations logics."""

def validate_grid(grid):
    if not grid or not all(isinstance(row, list) for row in grid):
        raise ValueError("Grid elements must be list.")
    row_length = len(grid[0])
    
    if not all(len(row) == row_length for row in grid):
        raise ValueError("All grid rows must have the same length.")
    
    if not all(cell in (0, 1) for row in grid for cell in row):
        raise ValueError("Grid can only contain 0s and 1s.")
