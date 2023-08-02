from home_work import Calculator
import pytest


# ○ pytest.
class TestCalculator:
    @pytest.fixture(scope='class')
    def calc(self):
        return Calculator()

    def test_add(self, calc):
        assert calc.add(1, 2) == 3

    def test_sub(self, calc):
        assert calc.sub(1, 2) == -1

    def test_mul(self, calc):
        assert calc.mul(1, 2) == 2

    def test_div(self, calc):
        assert calc.div(1, 2) == 0.5

    def test_div_zero(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.div(1, 0)

    def test_wrong_type(self, calc):
        with pytest.raises(TypeError):
            calc.add('4', '4')
