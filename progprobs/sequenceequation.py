import unittest
""" https://www.hackerrank.com/challenges/permutation-equation/problem """


# This was a tricky one, and I spent a while looking at the example I had written down before I saw that I could
# calculate a meaningful value from i, so that I could do only one pass. The trick for this one was actually
# drawing on the paper lines that represented what my eyes were doing with the problem set I was working on.
def permutation_equation(p):
    y = [None] * len(p)
    i = 0
    for value in p:
        # print(i)
        # print(p[i] - 1)
        # print(p[(p[i] - 1)] - 1)

        # for each i, calculate p[p[i]]. The result of this is the _index_ of the y array,
        # where the value at that index is i
        y[p[p[i] - 1] - 1] = i + 1  # minus/plus one's are all to handle 0 offset.

        i += 1

    # print(y)
    return y

class TestPageCount(unittest.TestCase):

    def test1(self):
        self.assertEqual(permutation_equation([2, 4, 1, 3]), [4, 3, 2, 1])

    def test2(self):
        self.assertEqual(permutation_equation([5, 2, 1, 3, 4]), [4, 2, 5, 1, 3])



if __name__ == '__main__':
    unittest.main()
