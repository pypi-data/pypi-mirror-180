import numpy as np
import pytest

from cyanDiff.ad_overloads import (sin, cos, tan, sinh, cosh, tanh, exp, log, 
    logistic, sqrt, arcsin, arccos, arctan, arcsinh, arccosh, arctanh, logbase)
from cyanDiff.ad_types import DualNumber, Function, Node, DiffObject


class Test_overloads:
    def test_sin(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            sin(x0)

        t1 = sin(x1)
        t2 = sin(x2)
        t3 = sin(x3)
        t4 = sin(x4)
        t5 = sin(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.sin(2.0))
        assert t2.real == pytest.approx(np.sin(3.0))
        assert t2.dual == pytest.approx(np.cos(3.0))
        assert t3({x3: 10}) == pytest.approx(np.sin(10.0))
        assert t4({x4: 10}) == pytest.approx(np.sin(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.sin(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.sin(10.0))

    def test_cos(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            cos(x0)

        t1 = cos(x1)
        t2 = cos(x2)
        t3 = cos(x3)
        t4 = cos(x4)
        t5 = cos(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.cos(2.0))
        assert t2.real == pytest.approx(np.cos(3.0))
        assert t2.dual == pytest.approx(-np.sin(3.0))
        assert t3({x3: 10}) == pytest.approx(np.cos(10.0))
        assert t4({x4: 10}) == pytest.approx(np.cos(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.cos(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.cos(10.0))

    def test_tan(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            tan(x0)

        t1 = tan(x1)
        t2 = tan(x2)
        t3 = tan(x3)
        t4 = tan(x4)
        t5 = tan(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.tan(2.0))
        assert t2.real == pytest.approx(np.tan(3.0))
        assert t2.dual == pytest.approx(1 / np.cos(3.0) ** 2)
        assert t3({x3: 10}) == pytest.approx(np.tan(10.0))
        assert t4({x4: 10}) == pytest.approx(np.tan(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.tan(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.tan(10.0))

    def test_sinh(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            sinh(x0)

        t1 = sinh(x1)
        t2 = sinh(x2)
        t3 = sinh(x3)
        t4 = sinh(x4)
        t5 = sinh(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.sinh(2.0))
        assert t2.real == pytest.approx(np.sinh(3.0))
        assert t2.dual == pytest.approx(np.cosh(3.0))
        assert t3({x3: 10}) == pytest.approx(np.sinh(10.0))
        assert t4({x4: 10}) == pytest.approx(np.sinh(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.sinh(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.sinh(10.0))

    def test_cosh(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            cosh(x0)

        t1 = cosh(x1)
        t2 = cosh(x2)
        t3 = cosh(x3)
        t4 = cosh(x4)
        t5 = cosh(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.cosh(2.0))
        assert t2.real == pytest.approx(np.cosh(3.0))
        assert t2.dual == pytest.approx(np.sinh(3.0))
        assert t3({x3: 10}) == pytest.approx(np.cosh(10.0))
        assert t4({x4: 10}) == pytest.approx(np.cosh(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.cosh(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.cosh(10.0))

    def test_tanh(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            tanh(x0)

        t1 = tanh(x1)
        t2 = tanh(x2)
        t3 = tanh(x3)
        t4 = tanh(x4)
        t5 = tanh(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.tanh(2.0))
        assert t2.real == pytest.approx(np.tanh(3.0))
        assert t2.dual == pytest.approx(1 / np.cosh(3.0) ** 2)
        assert t3({x3: 10}) == pytest.approx(np.tanh(10.0))
        assert t4({x4: 10}) == pytest.approx(np.tanh(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.tanh(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.tanh(10.0))

    def test_exp(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            exp(x0)

        t1 = exp(x1)
        t2 = exp(x2)
        t3 = exp(x3)
        t4 = exp(x4)
        t5 = exp(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.exp(2.0))
        assert t2.real == pytest.approx(np.exp(3.0))
        assert t2.dual == pytest.approx(np.exp(3.0))
        assert t3({x3: 10}) == pytest.approx(np.exp(10.0))
        assert t4({x4: 10}) == pytest.approx(np.exp(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.exp(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.exp(10.0))

    def test_log(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            log(x0)

        t1 = log(x1)
        t2 = log(x2)
        t3 = log(x3)
        t4 = log(x4)
        t5 = log(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.log(2.0))
        assert t2.real == pytest.approx(np.log(3.0))
        assert t2.dual == pytest.approx(1 / 3.0)
        assert t3({x3: 10}) == pytest.approx(np.log(10.0))
        assert t4({x4: 10}) == pytest.approx(np.log(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.log(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.log(10.0))

    def test_logistic(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            logistic(x0)

        t1 = logistic(x1)
        t2 = logistic(x2)
        t3 = logistic(x3)
        t4 = logistic(x4)
        t5 = logistic(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(1 / (1 + np.exp(-2.0)))
        assert t2.real == pytest.approx(1 / (1 + np.exp(-3.0)))
        assert t2.dual == pytest.approx(np.exp(3.0) / (1 + np.exp(3.0)) ** 2)
        assert t3({x3: 10}) == pytest.approx(1 / (1 + np.exp(-10.0)))
        assert t4({x4: 10}) == pytest.approx(1 / (1 + np.exp(-10.0)))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(1 / (1 + np.exp(-10.0)))
        assert t5(10, reverse_mode=True) == pytest.approx(1 / (1 + np.exp(-10.0)))

    def test_sqrt(self):
        x0 = "hello"
        x1 = 9
        x2 = DualNumber(4)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            sqrt(x0)

        t1 = sqrt(x1)
        t2 = sqrt(x2)
        t3 = sqrt(x3)
        t4 = sqrt(x4)
        t5 = sqrt(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(3.0)
        assert t2.real == pytest.approx(2.0)
        assert t2.dual == pytest.approx(0.25)
        assert t3({x3: 16}) == pytest.approx(4.0)
        assert t4({x4: 16}) == pytest.approx(4.0)
        t5.set_var_order(x5)
        assert t5(16) == pytest.approx(4.0)
        assert t5(16, reverse_mode=True) == pytest.approx(4.0)

    def test_arcsin(self):
        x0 = "hello"
        x1 = 0.5
        x2 = DualNumber(0.6)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            arcsin(x0)

        t1 = arcsin(x1)
        t2 = arcsin(x2)
        t3 = arcsin(x3)
        t4 = arcsin(x4)
        t5 = arcsin(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.arcsin(0.5))
        assert t2.real == pytest.approx(np.arcsin(0.6))
        assert t2.dual == pytest.approx(1 / np.sqrt(0.64))
        assert t3({x3: 0.8}) == pytest.approx(np.arcsin(0.8))
        assert t4({x4: 0.8}) == pytest.approx(np.arcsin(0.8))
        t5.set_var_order(x5)
        assert t5(0.8) == pytest.approx(np.arcsin(0.8))
        assert t5(0.8, reverse_mode=True) == pytest.approx(np.arcsin(0.8))

    def test_arccos(self):
        x0 = "hello"
        x1 = 0.5
        x2 = DualNumber(0.6)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            arccos(x0)

        t1 = arccos(x1)
        t2 = arccos(x2)
        t3 = arccos(x3)
        t4 = arccos(x4)
        t5 = arccos(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.arccos(0.5))
        assert t2.real == pytest.approx(np.arccos(0.6))
        assert t2.dual == pytest.approx(-1 / np.sqrt(0.64))
        assert t3({x3: 0.8}) == pytest.approx(np.arccos(0.8))
        assert t4({x4: 0.8}) == pytest.approx(np.arccos(0.8))
        t5.set_var_order(x5)
        assert t5(0.8) == pytest.approx(np.arccos(0.8))
        assert t5(0.8, reverse_mode=True) == pytest.approx(np.arccos(0.8))

    def test_arctan(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            arctan(x0)

        t1 = arctan(x1)
        t2 = arctan(x2)
        t3 = arctan(x3)
        t4 = arctan(x4)
        t5 = arctan(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.arctan(2.0))
        assert t2.real == pytest.approx(np.arctan(3.0))
        assert t2.dual == pytest.approx(1 / 10.0)
        assert t3({x3: 10}) == pytest.approx(np.arctan(10.0))
        assert t4({x4: 10}) == pytest.approx(np.arctan(10.0))
        t5.set_var_order(x5)
        assert t5(10) == pytest.approx(np.arctan(10.0))
        assert t5(10, reverse_mode=True) == pytest.approx(np.arctan(10.0))

    def test_arcsinh(self):
        x0 = "hello"
        x1 = 0.5
        x2 = DualNumber(0.6)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            arcsinh(x0)

        t1 = arcsinh(x1)
        t2 = arcsinh(x2)
        t3 = arcsinh(x3)
        t4 = arcsinh(x4)
        t5 = arcsinh(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.arcsinh(0.5))
        assert t2.real == pytest.approx(np.arcsinh(0.6))
        assert t2.dual == pytest.approx(1 / np.sqrt(1.36))
        assert t3({x3: 0.8}) == pytest.approx(np.arcsinh(0.8))
        assert t4({x4: 0.8}) == pytest.approx(np.arcsinh(0.8))
        t5.set_var_order(x5)
        assert t5(0.8) == pytest.approx(np.arcsinh(0.8))
        assert t5(0.8, reverse_mode=True) == pytest.approx(np.arcsinh(0.8))

    def test_arccosh(self):
        x0 = "hello"
        x1 = 2
        x2 = DualNumber(3)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            arccosh(x0)

        t1 = arccosh(x1)
        t2 = arccosh(x2)
        t3 = arccosh(x3)
        t4 = arccosh(x4)
        t5 = arccosh(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.arccosh(2))
        assert t2.real == pytest.approx(np.arccosh(3))
        assert t2.dual == pytest.approx(1 / np.sqrt(8))
        assert t3({x3: 8}) == pytest.approx(np.arccosh(8.0))
        assert t4({x4: 8}) == pytest.approx(np.arccosh(8.0))
        t5.set_var_order(x5)
        assert t5(8) == pytest.approx(np.arccosh(8.0))
        assert t5(8, reverse_mode=True) == pytest.approx(np.arccosh(8.0))

    def test_arctanh(self):
        x0 = "hello"
        x1 = 0.5
        x2 = DualNumber(0.6)
        x3 = Node()
        x4 = Function()
        x5 = DiffObject()

        with pytest.raises(TypeError):
            arctanh(x0)

        t1 = arctanh(x1)
        t2 = arctanh(x2)
        t3 = arctanh(x3)
        t4 = arctanh(x4)
        t5 = arctanh(x5)

        assert isinstance(t2, DualNumber)
        assert isinstance(t3, Node)
        assert isinstance(t4, Function)
        assert isinstance(t5, DiffObject)

        assert t1 == pytest.approx(np.arctanh(0.5))
        assert t2.real == pytest.approx(np.arctanh(0.6))
        assert t2.dual == pytest.approx(1 / 0.64)
        assert t3({x3: 0.8}) == pytest.approx(np.arctanh(0.8))
        assert t4({x4: 0.8}) == pytest.approx(np.arctanh(0.8))
        t5.set_var_order(x5)
        assert t5(0.8) == pytest.approx(np.arctanh(0.8))
        assert t5(0.8, reverse_mode=True) == pytest.approx(np.arctanh(0.8))

    def test_logbase(self):
        x0 = "hello"
        x1 = 144
        x2 = Node()
        x3 = Function()
        x4 = DiffObject()

        with pytest.raises(TypeError):
            logbase(1, x0)

        t1 = logbase(12, x1)
        t2 = logbase(x2, x2 ** 2 + 2 * x2)
        t3 = logbase(x3, x3 ** 3 + 3 * x3)
        t4 = logbase(x4, x4 ** 4 + 4 * x4)

        assert t1 == pytest.approx(2.0)
        assert isinstance(t2, Node)
        assert isinstance(t3, Function)
        assert isinstance(t4, DiffObject)

        assert t2({x2: 3}) == pytest.approx(2.46497352072)
        assert t2.diff_at({x2: 3}) == pytest.approx(-0.262444276184)
        assert t3({x3: 5}) == pytest.approx(3.07041507127)
        assert t3.diff_at({x3: 5}) == pytest.approx(-0.0353789087923)
        t4.set_var_order(x4)
        assert t4(7) == pytest.approx(4.0059583084)
        assert t4(7, reverse_mode=True) == pytest.approx(4.0059583084)
        assert t4.diff_at(7) == pytest.approx(-0.0029762379156)
        assert t4.diff_at(7, reverse_mode=True) == pytest.approx(-0.0029762379156)

    def test_composition(self):
        x1 = DualNumber(1, 1.0)
        x2 = Function()
        x3 = DualNumber(3.1, 5.3)

        t1 = exp(x3**2 - x3)
        assert t1.real == pytest.approx(np.exp(3.1**2 - 3.1))
        assert t1.dual == pytest.approx(5.3 * (2*3.1 - 1) * np.exp(3.1**2 - 3.1))

        t2 = log(exp(x3))
        assert t2.real == pytest.approx(x3.real)
        assert t2.dual == pytest.approx(x3.dual)

        x5 = x1 + x3

        t3 = exp(sin(x5**2 * log(x5)))
        assert t3.real == pytest.approx(np.exp(np.sin(4.1**2 * np.log(4.1))))
        assert t3.dual == pytest.approx(6.3 * np.exp(np.sin(4.1**2 * np.log(4.1))) * np.cos(4.1**2 * np.log(4.1)) * (2*4.1 * np.log(4.1) + 4.1))

        t4 = tan(log(-sin(exp(x3**0.5))))
        assert t4.real == pytest.approx(np.tan(np.log(-np.sin(np.exp(np.sqrt(3.1))))))
        assert t4.dual == pytest.approx(5.3 / (np.cos(np.log(-np.sin(np.exp(np.sqrt(3.1)))))**2) * 1/(np.sin(np.exp(np.sqrt(3.1)))) * np.cos(np.exp(np.sqrt(3.1))) * np.exp(np.sqrt(3.1)) * 1/(2 * np.sqrt(3.1)))

        t5 = exp(x3)/((1 + sin(x3))**0.5)
        assert t5.real == pytest.approx(np.exp(3.1)/((1 + np.sin(3.1))**0.5))
        assert t5.dual == pytest.approx(5.3 * ((1 + np.sin(3.1))**0.5 * np.exp(3.1) - np.exp(3.1) * 0.5 * (1 + np.sin(3.1))**-0.5 * np.cos(3.1))/(1 + np.sin(3.1)))

        t6 = x3 ** x3
        assert t6.real == pytest.approx(3.1**3.1)
        assert t6.dual == pytest.approx(5.3*(3.1**3.1 * (np.log(3.1) + 1)))

        t7 = x2 ** x2
        assert t7({x2: 3.0}) == pytest.approx(27.0)