import pytest
from main import count_islands


def test_zero_island():
    assert count_islands([]) == 0


def test_one_island():
    grid = [[1]]
    assert count_islands(grid) == 1


def test_no_island():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert count_islands(grid) == 0


def test_multiple_islands():
    grid = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    assert count_islands(grid) == 4


def test_single_large_island():
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    assert count_islands(grid) == 1


def test_complex_islands():
    grid = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 0]
    ]
    assert count_islands(grid) == 2
