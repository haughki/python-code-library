import unittest

""" https://www.hackerrank.com/challenges/counting-valleys/problem """


# def counting_valleys(steps, path):
#     elevation = 0
#     valleys = 0
#     for step in path:
#         # print(step)
#         if step == "D":
#             elevation -= 1
#             if elevation == -1:
#                 valleys += 1
#         else:
#             elevation += 1
#
#     return valleys

# Same logic, just compacted
def counting_valleys(steps, path):
    valleys = elevation = 0
    for step in path:
        elevation += -1 if step == "D" else 1
        valleys += 1 if step == "D" and elevation == -1 else 0
    return valleys




class TestPageCount(unittest.TestCase):

    def test1(self):
        self.assertEqual(counting_valleys(2, "DU"), 1)

    def test2(self):
        self.assertEqual(counting_valleys(2, "UD"), 0)

    def test3(self):
        self.assertEqual(counting_valleys(4, "UDDU"), 1)

    def test4(self):
        self.assertEqual(counting_valleys(4, "UDDU"), 1)

    def test5(self):
        self.assertEqual(counting_valleys(6, "UDDUDUDU"), 3)



if __name__ == '__main__':
    unittest.main()
    # print(page_count(9, 5))
