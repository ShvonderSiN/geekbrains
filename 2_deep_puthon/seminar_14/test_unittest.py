import unittest
from home_work import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_add(self):
        self.assertEquals(self.calc.add(1, 8), 9)

    def test_sub(self):
        self.assertEquals(self.calc.sub(1, 8), -7)

    def test_mul(self):
        self.assertEquals(self.calc.mul(1, 8), 8)

    def test_div(self):
        self.assertEquals(self.calc.div(1, 8), 0.125)

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(1, 0)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calc.add('4', '4')


if __name__ == "__main__":
    unittest.main()
