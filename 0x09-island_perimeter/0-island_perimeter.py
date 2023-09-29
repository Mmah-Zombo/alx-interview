#!/usr/bin/python3
"""perimeter"""


def island_perimeter(grid):
    """calculates island perimeter"""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume all sides are land

                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for the top side
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the left side

    return perimeter
