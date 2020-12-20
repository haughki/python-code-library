import unittest
""" https://www.hackerrank.com/challenges/cut-the-sticks/problem """



def cut_the_sticks(arr):
    sticks = arr
    # don't really need to do this in reverse: at first, I thought it was a way to slice bits off the
    # end of the array as I looped, but turns out, don't even need to do that. Not taking time to re-write.
    sticks.sort(reverse=True)
    number_of_sticks = []
    i = len(sticks) - 1

    while i > -1:
        number_of_sticks.append(i + 1)
        last_value = sticks[i]
        i -= 1
        while i > -1 and sticks[i] == last_value:
            i -= 1

    #print(number_of_sticks)
    return number_of_sticks


    # total_to_subtract = 0
    # for s in reversed(sticks):
    #     # print(s)
    #     # print(sticks[i])
    #     number_of_sticks.append(i + 1)
    #     last_value = s
    #     new_sub = last_value
    #     total_to_subtract = total_to_subtract + new_sub
    #     while sticks[i] == last_value:
    #         i -= 1
    #     i -= 1



class TestPageCount(unittest.TestCase):

    def test1(self):
        self.assertEqual(cut_the_sticks([5, 4, 2, 4, 2, 8]), [6, 4, 2, 1])

    def test2(self):
        self.assertEqual(cut_the_sticks([5]), [1])



if __name__ == '__main__':
    unittest.main()
