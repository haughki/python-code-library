import unittest

def acm_team(topic):
    members = topic

    max_topics = 0
    num_teams = 0
    member_to_int = {}
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            # print(topics[i], topics[j], sep=" -- ")
            i_ints = None
            j_ints = None
            if i in member_to_int:
                i_ints = member_to_int[i]
            else:
                i_ints = convert_to_ints(members[i])
                member_to_int[i] = i_ints

            if j in member_to_int:
                j_ints = member_to_int[j]
            else:
                j_ints = convert_to_ints(members[j])
                member_to_int[j] = j_ints

            print(i_ints)
            # print(j_ints)
            tot = 0

            for k in range(len(i_ints)):
                or_res = i_ints[k] | j_ints[k]
                c = bits_count[or_res]
                tot = tot + c

            if tot == max_topics:
                num_teams += 1
            elif tot > max_topics:
                max_topics = tot
                num_teams = 1
    return [max_topics, num_teams]



bits_count =[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4];
binary_to_decimal = {'0000': 0, '0001': 1, '0010': 2, '0011': 3, '0100': 4, '0101': 5, '0110': 6, '0111': 7, '1000': 8,
                     '1001': 9, '1010': 10, '1011': 11, '1100': 12, '1101': 13, '1110': 14, '1111': 15}

def convert_to_ints(binary_string):
    ints_list = []
    i = len(binary_string)
    while i > 0:
        string_chunk = ""
        j = 0
        if i > 3:
            j = i - 4
            string_chunk = binary_string[j:i]
        else:
            string_chunk = '0' * (4 - i) + binary_string[:i]

        # print(j, i, sep=":")
        ints_list.append(binary_to_decimal[string_chunk])
        # print(ints_list)
        i = j

    return ints_list






class TestPageCount(unittest.TestCase):

    # def testb1(self):
    #     self.assertEquals(convert_to_ints("00011100"), [12, 1])
    #
    # def testb2(self):
    #     self.assertEquals(convert_to_ints("11100"), [12, 1])

    def test1(self):
        self.assertEqual(acm_team(['10101', '11110', '00010']), [5, 1])

    def test2(self):
        self.assertEqual([3, 6], acm_team(['101', '111', '010', '000', '010']))




if __name__ == '__main__':
    unittest.main()

