import unittest

from aacommon.stdiocapture import StdInFromString, StdOutCapture

""" https://www.hackerrank.com/challenges/magic-square-forming """


def magic_square(grid_string):
    sysinfromstring = StdInFromString(grid_string)
    s = []
    for s_i in range(3):
        for s_temp in input().strip().split(' '):
            s.append(int(s_temp))

    sysinfromstring.close()

    known_squares = [[8, 1, 6, 3, 5, 7, 4, 9, 2],
                     [6, 1, 8, 7, 5, 3, 2, 9, 4],
                     [4, 9, 2, 3, 5, 7, 8, 1, 6],
                     [2, 9, 4, 7, 5, 3, 6, 1, 8],
                     [8, 3, 4, 1, 5, 9, 6, 7, 2],
                     [4, 3, 8, 9, 5, 1, 2, 7, 6],
                     [6, 7, 2, 1, 5, 9, 8, 3, 4],
                     [2, 7, 6, 9, 5, 1, 4, 3, 8]]
    
    least_cost = 1000  # arbitrary max cost
    for square in known_squares:
        curr_cost = 0
        for i in range(9):
            curr_cost += abs(square[i] - s[i])
            if curr_cost >= least_cost:
                break
        least_cost = min(least_cost, curr_cost)
    print(least_cost)


class TestMagicSquare(unittest.TestCase):
    def setUp(self):
        self._stdoutcapture = StdOutCapture()

    def tearDown(self):
        self._stdoutcapture.close()

    def test_one_change(self):
        magic_square("""4 9 2
3 5 7
8 1 5""")
        self.assertEquals("1", self._stdoutcapture.value().strip('\n'))

    def test_four_changes(self):
        magic_square("""4 8 2
4 5 7
6 1 6""")
        self.assertEquals("4", self._stdoutcapture.value().strip('\n'))

    def test_diff_pattern(self):
        magic_square("""8 7 1
1 2 9
6 3 4""")
        self.assertEquals("8", self._stdoutcapture.value().strip('\n'))


if __name__ == '__main__':
    unittest.main()
