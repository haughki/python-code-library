import unittest

from aacommon.stdiocapture import StdOutCapture

"""
https://www.hackerrank.com/challenges/bon-appetit?h_r=internal-search
"""

def bonAppetit(n, k, b, ar):
    shared = 0
    for i in range(len(ar)):
        if i != k:
            shared += ar[i]

    half = shared / 2
    if half == b:
        return "Bon Appetit"
    else:
        return int(b - half)


# n, k = input().strip().split(' ')
# n, k = [int(n), int(k)]
# ar = list(map(int, input().strip().split(' ')))
# b = int(input().strip())

def getline1(line1):
    n, k = line1.strip().split(' ')
    return [int(n), int(k)]


def getline2(line2):
    return list(map(int, line2.strip().split(' ')))


def getline3(line3):
    return int(line3.strip())


class TestBonAppetit(unittest.TestCase):
    def setUp(self):
        self._stdoutcapture = StdOutCapture()

    def tearDown(self):
        self._stdoutcapture.close()

    def test_happy(self):
        line1 = "4 1"
        line2 = "3 10 2 9"
        line3 = "12"

        n, k = getline1(line1)
        ar = getline2(line2)
        b = getline3(line3)
        result = bonAppetit(n, k, b, ar)
        print(result)
        self.assertEquals(5, int(self._stdoutcapture.value().strip()))

    def test_bon(self):
        line1 = "4 1"
        line2 = "3 10 2 9"
        line3 = "7"

        n, k = getline1(line1)
        ar = getline2(line2)
        b = getline3(line3)
        result = bonAppetit(n, k, b, ar)
        print(result)
        self.assertEquals("Bon Appetit", self._stdoutcapture.value().strip())


if __name__ == '__main__':
    unittest.main()
