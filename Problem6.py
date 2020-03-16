# Sum square difference
# Problem 6

class Problem6:
    def sumSquareDifference(self, num):
        sum_of_squares = 0
        square_of_sum = 0
        for i in range(1, num+1):
            sum_of_squares += i**2
            square_of_sum += i
        square_of_sum = square_of_sum**2

        return square_of_sum-sum_of_squares

import unittest
class test_Problem1(unittest.TestCase):
    def test_result(self):
        A = Problem6()
        self.assertEqual(A.sumSquareDifference(100), 25164150)

if __name__ == "__main__":
    unittest.main()