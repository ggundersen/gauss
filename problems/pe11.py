"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2012-12

In the 20*20 grid below, four numbers along a diagonal line have been marked in
red.

[See ../static/txt/pe11_grid.txt]

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
What is the greatest product of four adjacent numbers in any direction (up,
down, left, right, or diagonally) in the 20*20 grid?

Solution:
----------------------------------------------------------------------------"""

import os


def get_grid():

    path = os.path.normpath(os.path.dirname(__file__) + '../../txt/pe11_grid.txt')
    f = open(path,'r')
    grid_master = f.read().split(' ')
    grid_master = map(int, grid_master)
    grid = [grid_master[i:i+20] for i in range(0, len(grid_master), 20)]
    f.close()
    return grid


def get_h_max(grid):

    h = []
    for row in grid:
        for col in range(len(grid)-3):
            h.append(row[col]*row[col+1]*row[col+2]*row[col+3])
    return max(h)


def get_v_max(grid):

    v = []
    for col in range(len(grid)):
        for row in range(len(grid)-3):
            v.append(grid[row][col]*grid[row+1][col]*grid[row+2][col]*grid[row+3][col])
    return max(v)


def get_r_max(grid):

    r = []
    for row in range(len(grid)-3):
        for col in range(len(grid)-3):
            r.append(grid[row][col]*grid[row+1][col+1]*grid[row+2][col+2]*grid[row+3][col+3])
    return max(r)


def get_l_max(grid):

    l = []
    for row in range(3,len(grid)):
        for col in range(len(grid)-3):
            l.append(grid[row][col]*grid[row-1][col+1]*grid[row-2][col+2]*grid[row-3][col+3])
    return max(l)


def main():

    grid = get_grid()
    return max(get_h_max(grid), get_h_max(grid), get_r_max(grid), get_l_max(grid))