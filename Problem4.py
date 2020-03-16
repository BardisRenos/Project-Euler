#Largest palindrome product
#Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


class Problem4:
    def is_palindrome(self, num):

        if str(num) == str(num)[::-1]:
            return True
        return False

    def largestPalindromeProduct(self):
        result = 0
        for i in range(100,1000):
            for j in range(100, 1000):
                if self.is_palindrome(i*j):
                    if(i*j > result):
                        result = i*j
        return result

#Unit testing 
import unittest

class test_Problem2(unittest.TestCase):
    def test_result(self):
        A = Problem4()
        #I compare the correct result with our algorithm
        self.assertEqual(A.largestPalindromeProduct(), 906609)

if __name__ == "__main__":
    unittest.main()