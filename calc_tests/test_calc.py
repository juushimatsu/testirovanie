import unittest

from main import calculate

class TestCalc(unittest.TestCase):
    
    def test_addition(self): # +
        self.assertEqual(calculate("2+2"), 4)
    def test_multiplication(self): # *
        self.assertEqual(calculate("5*2"), 10)
    def test_subtraction(self): # -
        self.assertEqual(calculate("9-4"), 5)
    def test_division(self): # /
        self.assertEqual(calculate("30/15"), 2)

    def test_multitest(self):
        self.assertEqual(calculate("3+1-3"), 1)

    # bad result

    def test_addition(self): # +
        self.assertEqual(calculate("2+2"), 10)
    def test_multiplication(self): # *
        self.assertEqual(calculate("5*2"), 40)
    def test_subtraction(self): # -
        self.assertEqual(calculate("9-4"), 30)
    def test_division(self): # /
        self.assertEqual(calculate("30/15"), 42)

class TestCalcZero(unittest.TestCase):
    def test_zeromultiplication(self): # *
        self.assertEqual(calculate("10*0"), 0)
    def test_zerodivision(self): # /
        with self.assertRaises(ZeroDivisionError):calculate("10/0")

if __name__ == "__main__":
    unittest.main()