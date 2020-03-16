# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

class Problem1:

    def multipleOf(self, num):
        if(type(num) is str):
            return False
        if(num < 1):
            return False
        else:    
            listOfSum = []
            for i in range(1, num):
                if(i%3 == 0 or i%5 == 0):
                    listOfSum.append(i)

            return sum(listOfSum)

#Unit testing 
import unittest
class test_Problem1(unittest.TestCase):

    def test_values(self):
        #Test of the given value
        A = Problem1()
        self.assertFalse(A.multipleOf("10"))
    
    def test_zero_or_negative_value(self):
        #Test if the given value is zero or negative
        A = Problem1()
        self.assertFalse(A.multipleOf(0))

    def test_result(self):
        A = Problem1()
        self.assertEqual(A.multipleOf(10), 23)

if __name__ == "__main__":
    unittest.main()