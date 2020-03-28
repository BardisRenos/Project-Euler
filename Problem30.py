# Digit fifth powers
# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

class Problem30:
    @staticmethod
    def digitFifthpower():
        result = 0
        for i in range(2, 354295):
            if i == Problem30.returnNumber(i):
                result += i
        return result

    @staticmethod
    def returnNumber(num):
        sum = 0
        for i in str(num):
            sum += int(i) ** 5
        return sum


if __name__ == '__main__':
    print(Problem30.digitFifthpower())
