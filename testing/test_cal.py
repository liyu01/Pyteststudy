# -+- coding: utf-8 -*_ rom asyncio import sleep

import pytest

from pythoncode.calculator import Calculator


class Testcal:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("\n计算结束")

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [2, 3, 4], [10, 9, 19]], ids=['1', '2', '3'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    def test_add1(self):
        # calc = Calculator()
        result = self.calc.add(100, 100)
        assert result == 200

    def test_add2(self):
        # calc = Calculator()
        result = self.calc.add(0.1, 0.1)
        assert result == 0.2
