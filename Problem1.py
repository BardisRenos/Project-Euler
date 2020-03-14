# Multiples of 3 and 5
# Problem 1

class Problem1:

    def multipleOf(self, num):
        listOfSum = []

        for i in range(1, num):
            if(i%3 == 0 or i%5 == 0):
                listOfSum.append(i)

        return sum(listOfSum)


#Unit testing 
import unittest
class


if __name__ == "__main__":
    A = Problem1()
    print(A.multipleOf(10))