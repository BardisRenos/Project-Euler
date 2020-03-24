# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid, 
# and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

class Problem15:
    def latticePaths(self, num):
        if(type(num) is str):
            return False
        if(num<1):
            return False
        return (self.factorial(2*num) // (self.factorial(num)**2))

    def factorial(self, num):
        res = 2
        end = num
        if(num<=1):
            return False
        if(num == 2):
            return 2
        else:
            while res < end:
                num *= res
                res += 1
        return num


import unittest
class test_Problem15(unittest.TestCase):
    def test_result(self):
        A = Problem15()
        self.assertEqual(A.latticePaths(20), 137846528820)

    def test_value(self):
        A = Problem15()
        self.assertFalse(A.latticePaths("20"))

    def test_negative_values(self):
        A = Problem15()
        self.assertFalse(A.latticePaths(0)) 

if __name__ == "__main__":
    unittest.main()
