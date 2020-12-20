import math
import unittest

""" https://www.hackerrank.com/challenges/drawing-book/problem """
# def page_count(n, p):
#     midpoint = n//2
#     #print(midpoint)
#
#     if n % 2 == 0:
#         if p > midpoint:
#             return math.ceil((n - p) / 2)
#         else:
#             return p // 2
#     else:
#         if p > midpoint:
#             return (n - p) // 2
#         else:
#             return p // 2


# best solution from discussion comments
def page_count(n, p):
    midpoint = n // 2
    target_from_front = p // 2
    target_from_back = midpoint - target_from_front
    return min(target_from_front, target_from_back)

class TestPageCount(unittest.TestCase):

    def test1(self):
        self.assertEqual(page_count(9, 6), 1)

    def test2(self):
        self.assertEqual(page_count(9, 4), 2)

    def test3(self):
        self.assertEqual(page_count(9, 5), 2)

    def test4(self):
        self.assertEqual(page_count(9, 3), 1)

    def test5(self):
        self.assertEqual(page_count(9, 2), 1)

    def test6(self):
        self.assertEqual(page_count(9, 9), 0)

    def test7(self):
        self.assertEqual(page_count(9, 1), 0)

    def test8(self):
        self.assertEqual(page_count(10, 7), 2)

    def test9(self):
        self.assertEqual(page_count(10, 5), 2)

    def test10(self):
        self.assertEqual(page_count(10, 4), 2)

    def test11(self):
        self.assertEqual(page_count(8, 4), 2)

    def test12(self):
        self.assertEqual(page_count(8, 5), 2)

    def test13(self):
        self.assertEqual(page_count(7, 3), 1)

if __name__ == '__main__':
    unittest.main()
    # print(page_count(9, 5))
