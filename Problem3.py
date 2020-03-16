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

class test_Problem2(unittest.TestCase):


if __name__ == "__main__":