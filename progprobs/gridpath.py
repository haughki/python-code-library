import unittest

""" Given the following grid, check if path exists. 
There are only left, right, up, and down links and no diagonal links exists.  """
numRows = 0
numCols = 0


def find_start(grid, path):
    print("rows: ", numRows)
    print("cols: ", numCols)

    for row in range(numRows):
        for col in range(numCols):
            print(row, col, sep=',', end=' - ')
            print(grid[row][col])
            if grid[row][col] == path[0]:
                return row, col


row = 0
col = 1


def can_go_to(start_pos, dest, grid):
    r = start_pos[row]
    c = start_pos[col]

    up = start_pos[row] - 1
    if up > -1:
        if grid[up][c] == dest:
            return up, c

    down = start_pos[row] + 1
    if down < numRows:
        if grid[down][c] == dest:
            return down, c

    left = start_pos[col] - 1
    if left > -1:
        if grid[r][left] == dest:
            return r, left

    right = start_pos[col] + 1
    if right < numCols:
        if grid[r][right] == dest:
            return r, right

    return None


def print_grid(grid):
    print("   ", end="")
    for col in range(len(grid[0])):
        print(col, end=" ")
    for row in range(len(grid)):
        print()
        print(row, end="  ")
        for col in range(len(grid[0])):
            print(grid[row][col], end=" ")
    print()
            
            
def path_exists(grid, path):
    print_grid(grid)
    curr_pos = find_start(grid, path)
    print("Start: " + str(path[0]) + " @ " + str(curr_pos))
    for e in path[1:]:
        print(curr_pos, e, sep=' --> ')
        curr_pos = can_go_to(curr_pos, e, grid)
        if curr_pos is None:
            return False

    return True


def set_nrows_ncols(grid):
    global numRows
    global numCols
    numRows = len(grid)
    numCols = len(grid[0])


class TestGridPath(unittest.TestCase):
    def test_happy(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        set_nrows_ncols(grid)
        path = [3, 6, 5]

        self.assertEqual(True, path_exists(grid, path))
        print()

    def test_sad(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        set_nrows_ncols(grid)
        path = [3, 6, 2]

        self.assertEqual(False, path_exists(grid, path))
        print()

    def test_longer(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        set_nrows_ncols(grid)
        path = [5, 2, 3, 2, 1, 4]

        self.assertEqual(True, path_exists(grid, path))
        print()

    def test_diff_grid(self):
        grid = [
            [8, 2, 9, 7],
            [1, 5, 3, 6],
            [4, 12, 22, 16],
        ]
        set_nrows_ncols(grid)
        path = [5, 1, 4, 12, 22, 3, 9]

        self.assertEqual(True, path_exists(grid, path))
        print()


if __name__ == '__main__':
    unittest.main()
