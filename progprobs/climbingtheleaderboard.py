import unittest
from bisect import bisect_left

from aacommon.stdiocapture import StdInFromString, StdOutCapture

"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard
"""


def climb_board(grid_string):
    stdinfromstring = StdInFromString(grid_string)
    n = int(input().strip())

    # an "array map" of scores and ranks -- two arrays with corresponding indexes.  We want the scores array in
    # ascending order so that we can use binary search (bisect in python) accordingly.  Hence all the machinations
    # to get things efficiently in that order.  Note that we have to walk the list to convert to int the string scores
    # from the input to int anyhow.
    str_scores = input().strip().split(' ')
    num_scores = len(str_scores)
    scores = [None] * num_scores
    scores[num_scores - 1] = int(str_scores[0])
    ranks = [None] * num_scores
    ranks[num_scores - 1] = 1
    reversei = num_scores - 2
    
    for i in range(1, num_scores):
        score = int(str_scores[i])
        if score == scores[reversei + 1]:
            ranks[reversei] = ranks[reversei + 1]
        else:
            ranks[reversei] = ranks[reversei + 1] + 1
        scores[reversei] = score
        reversei -= 1

    m = int(input().strip())
    alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
    stdinfromstring.close()

    for ascore in alice:
        pos = bisect_left(scores, ascore)
        if pos >= len(scores):
            print(1)  # first!
        elif ascore == scores[pos]:
            print(ranks[pos])
        else:
            print(ranks[pos] + 1)


class TestClimbBoard(unittest.TestCase):
    def setUp(self):
        self._stdoutcapture = StdOutCapture()

    def tearDown(self):
        self._stdoutcapture.close()

    def test_one_change(self):
        climb_board("""7
100 100 50 40 40 20 10
4
5 25 40 50 120""")
        self.assertEquals("""6
4
3
2
1""", self._stdoutcapture.value().strip('\n'))


if __name__ == '__main__':
    unittest.main()
