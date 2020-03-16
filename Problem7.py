# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

class Problem7:
    def is_prime_num(self, num):
        if (num <= 1):
            return False
        if (num%2 == 0):
            return False
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True

    def nb_num(self, num):
        number = 1
        i = 1
        while number != num:
            i += 2
            if (self.is_prime_num(i)):
                number += 1
        return i


import unittest
class test_Problem7(unittest.TestCase):
    
    def test_result(self):
        A = Problem7()
        self.assertEqual(A.nb_num(10001), 104743)

if __name__ == "__main__":
    unittest.main()