# Multiples of 3 and 5
# Problem 1

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