# Summation of Primes
# Problem 10th
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


class Problem10:
    @staticmethod
    def summationOfPrime(num):
        if(type(num) is str):
            return  False
        if(num<1):
            return False
        primeNum = 2
        sum = 0
        while primeNum<num:
            if(Problem10.isPrime(primeNum)):
                sum += primeNum
            primeNum += 1

        return sum
    @staticmethod
    def isPrime(n):
        # if n < 2: return "Neither prime, nor composite"
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

import unittest
class test_Problem10(unittest.TestCase):
    def test_result(self):
        self.assertEqual(Problem10.summationOfPrime(2000000), 142913828922)
    
    def test_value(self):
        self.assertFalse(Problem10.summationOfPrime("20"))

    def test_negative_values(self):
        self.assertFalse(Problem10.summationOfPrime(0))

if __name__ == "__main__":
    unittest.main()