"""Utils.py file for helper and utility functions."""
import sys

from validation import validate_grid

def read_grid_and_validate(file_path):
    """
    Reads and validates grid from provided file path.
    """
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
