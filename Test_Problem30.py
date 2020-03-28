import unittest
from Problem30 import Problem30


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(Problem30.digitFifthpower(), 443839)


if __name__ == '__main__':
    unittest.main()