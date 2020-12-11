import unittest

from aacommon.stdiocapture import StdInFromString, StdOutCapture

"""
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies?h_r=next-challenge&h_v=zen
"""


def beautiful_days(ijk):
    stdinfromstring = StdInFromString(ijk)
    i, j, k = [int(temp) for temp in input().strip().split(' ')]
    stdinfromstring.close()

    num_beautiful = 0
    for n in range(i, j + 1):
        nrev = reverse(n)
        if abs(n - nrev) % k == 0:
            num_beautiful += 1
    
    print(num_beautiful)


def reverse(num):
    # modulus 10 to get the last digit, divide 10 to chop the last digit
    rev = 0
    while num != 0:
        dig = num % 10
        rev = dig + rev * 10  # the trick: this just works; keep multiplying the result by 10 and adding the latest digit
        num //= 10  # // is floor division in python
    return rev


class TestBeautiful(unittest.TestCase):
    def setUp(self):
        self._stdoutcapture = StdOutCapture()

    def tearDown(self):
        self._stdoutcapture.close()

    def test_first_case(self):
        beautiful_days("20 23 6")
        self.assertEquals("2", self._stdoutcapture.value().strip('\n'))

    def test_rand_case(self):
        beautiful_days("1 9 1")
        self.assertEquals("9", self._stdoutcapture.value().strip('\n'))

if __name__ == '__main__':
    unittest.main()
