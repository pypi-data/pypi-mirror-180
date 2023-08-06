import numpy as np
import pytest

from cyanDiff.ad_overloads import sin, cos, tan, exp, log
from cyanDiff.ad_types import Function, VectorFunction
from cyanDiff.newton_raphson import NewtonRaphson
from cyanDiff.ad_helpers import make_vars

class Test_NewtonRaphson:
    def test_scalar_solver(self):
        x = make_vars(1)
        f = x ** 2 - 4
        f.set_var_order(x)
        nr = NewtonRaphson()
        assert nr.scalar_solver(f, 1, 100) == pytest.approx(2, abs=1e-6)

        with pytest.raises(ZeroDivisionError):
            nr.scalar_solver(f, 0, 100)

        y = make_vars(1)
        g = 1 / cos(y) - 1
        g.set_var_order(y)
        assert nr.scalar_solver(g, 0.1, 100) == pytest.approx(0, abs=1e-6)

        z = make_vars(1)
        h = z ** z - 1
        h.set_var_order(z)
        assert nr.scalar_solver(h, 2, 100) == pytest.approx(1, abs=1e-6)
        
        w = make_vars(1)
        i = w ** 3 - 7
        i.set_var_order(w)
        assert nr.scalar_solver(i, 2, 100, print_results=True) == pytest.approx(7 ** (1 / 3), abs=1e-6)

    def test_multivariate_solver(self):
        x, y, z = make_vars(3)
        f = (x - 5)**2 + (y - 6)**2 + (z - 2)**2
        f.set_var_order(x, y, z)
        nr = NewtonRaphson()
        assert nr.multivariate_solver(f, (0, 0, 0), 100, print_results=True) == pytest.approx(np.array([5, 6, 2]), abs=1e-6)

        w, x, y = make_vars(3)
        f1 = (log(w)) ** 2 + (tan(y - 35)) ** 2
        f2 = 2 * (x - 6) + sin(x - 6)
        F = VectorFunction(f1, f2)
        F.set_var_order(w, x, y)
        x0 = (1.5, 0, 34.75)
        assert nr.multivariate_solver(F, x0, 1000) == pytest.approx(np.array([1, 6, 35]), abs=1e-6)

        w, x, y, z = make_vars(4)
        f1 = w**4 - 2
        f2 = exp((x - 1)**2) - 1
        f3 = y**2 
        f4 = z**2
        F = VectorFunction(f1, f2, f3, f4)
        F.set_var_order(w, x, y, z)
        x0 = (1, -2, 4, 7)
        assert nr.multivariate_solver(F, x0, 100) == pytest.approx(np.array([2 ** 0.25, 1, 0, 0]), abs=1e-6)





