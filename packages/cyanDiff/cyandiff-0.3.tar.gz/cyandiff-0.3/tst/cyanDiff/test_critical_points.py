import pytest
import numpy as np

from cyanDiff.ad_overloads import sin, cos, tan, exp, log
from cyanDiff.ad_types import DualNumber, Function
from cyanDiff.critical_points import CriticalPoints
from cyanDiff.ad_helpers import make_vars

class Test_critical_points:
    def test_scalar_critical(self):
        x = make_vars(1)
        f1 = x**2 + 1
        f1.set_var_order(x)
        cp = CriticalPoints()
        d1 = cp.scalar_critical(f1, -2, 3, incr=0.01, tol=1e-10)
        assert d1['local mins'] == [(0.0, 1.0)]
        assert d1['local maxes'] == [] 

        y = make_vars(1)
        f2 = (y - 1)**2 * (y - 4)**3
        f2.set_var_order(y)
        d2 = cp.scalar_critical(f2, -5, 5, incr=1e-4, tol=1e-10)
        assert d2['local mins'] == [(2.2, -8.39808)]
        assert d2['local maxes'] == [(1.0, -0.0)]

        with pytest.raises(ValueError):
            cp.scalar_critical(f2, -5, 5, incr=1e-11, tol=1e-10)

        with pytest.raises(ValueError):
            cp.scalar_critical(f2, 5, -5, incr=1e-4, tol=1e-10)

        with pytest.raises(ValueError):
            cp.scalar_critical(f2, -5, 5, incr=1e-4, tol=-1)