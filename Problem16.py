# Power digit sum
# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

class Problem16:
    @staticmethod
    def powerDigiSum(num):
        res = 0
        print(num)
        str_number = list(str(num)) 
        for i in str_number:
            res += int(i)

        return res

import unittest
class test_Problem16(unittest.TestCase):
    def test_result(self):
        self.assertEqual(Problem16.powerDigiSum(2**1000), 1366)

if __name__ == "__main__":
    unittest.main()
    