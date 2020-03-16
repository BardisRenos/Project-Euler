# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

class Problem3:
    def largestPrimeFactor(self, num, extremum = False):
        list_of_facotrs = []
        if(type(num) is str):
            return False
        if(num<3):
            return False
        else:
            for i in range(3, num+1, 2):
                if(self.is_prime_num(i)):
                    while num%i == 0:
                        list_of_facotrs.append(i)
                        num /= i
        return list_of_facotrs[-1]

    def is_prime_num(self, num):
        if (num <= 1):
            return False
        if (num%2 == 0):
            return False
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True

#Unit testing 
import unittest

class test_Problem2(unittest.TestCase):

    def test_check_type_number(self):
        A = Problem3()
        #Test of the given value type
        self.assertFalse(A.largestPrimeFactor("600851475143"))

    def test_check_number(self):
        A = Problem3()
        #Test of the given value
        self.assertFalse(A.largestPrimeFactor(2))
    
    def test_compare_result(self):
        A = Problem3()
        #Test the final result
        self.assertEqual(A.largestPrimeFactor(600851475143), 6857)


if __name__ == "__main__":
    unittest.main()
