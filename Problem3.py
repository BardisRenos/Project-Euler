# Largest prime factor
# Problem 3
class Problem3:
    def largestPrimeFactor(self, num, extremum = False):
        list_of_facotrs = []

        for i in range(3, num+1, 2):
            if(num<i):
                break
            while num%i == 0:
                print(i, num)
                list_of_facotrs.append(i)
                num /= i
        
        return list_of_facotrs[-1]

#Unit testing 
import unittest

class test_Problem3(unittest.TestCase):

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