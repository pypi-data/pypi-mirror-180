import pytest
import math
import numpy as np

from cyanDiff.ad_types import DualNumber, Function, DiffObject, VectorFunction
from cyanDiff.reverse_mode import Node


class Test_DualNumber:
    
    def test_init(self):
        x = DualNumber(2, 1.0)
        y = DualNumber(2)
        z = DualNumber(3.1, 4)

        assert x.real == pytest.approx(2)
        assert x.dual == pytest.approx(1.0)
        assert y.real == pytest.approx(2)
        assert y.dual == pytest.approx(1.0)
        assert z.real == pytest.approx(3.1)
        assert z.dual == pytest.approx(4.0)

    def test_add(self):
        x = DualNumber(2, 1.0)
        y = DualNumber(2)
        z = DualNumber(3.1, 4)
        t_1 = x + x + 1
        t_2 = x + y + z
        assert t_1.real == pytest.approx(5.0)
        assert t_1.dual == pytest.approx(2.0)
        assert t_2.real == pytest.approx(7.1)
        assert t_2.dual == pytest.approx(6.0)

        with pytest.raises(TypeError):
            x + "12"

    def test_radd(self):
        x = DualNumber(2, 1.0)
        y = DualNumber(2)
        t_1 = 1 + x + y
        assert t_1.real == pytest.approx(5.0)
        assert t_1.dual == pytest.approx(2.0)

        t_2 = 10 + x + y
        assert t_2.real == pytest.approx(14.0)
        assert t_2.dual == pytest.approx(2.0)

        with pytest.raises(TypeError):
            "12" + x

    def test_sub(self):
        x = DualNumber(2, 1.0)
        t_1 = x - 1
        assert t_1.real == pytest.approx(1.0)
        assert t_1.dual == pytest.approx(1.0)

        t_2 = x - 1 - x
        assert t_2.real == pytest.approx(-1.0)
        assert t_2.dual == pytest.approx(0)
        assert x.real == pytest.approx(2.0)

        with pytest.raises(TypeError):
            x - "12"

    def test_rsub(self):
        x = DualNumber(2, 1.0)
        t_1 = x - 2
        assert t_1.real == pytest.approx(0)
        assert t_1.dual == pytest.approx(1.0)

        t_2 = 1 - x
        assert t_2.real == pytest.approx(-1.0)
        assert t_2.dual == pytest.approx(-1.0)

        with pytest.raises(TypeError):
            "12" - x

    def test_mul(self):
        x = DualNumber(2, 1.0)
        t_1 = x * 2 * 4
        assert t_1.real == pytest.approx(16.0)
        assert t_1.dual == pytest.approx(8.0)

        t_2 = x * x
        assert t_2.real == pytest.approx(4.0)
        assert t_2.dual == pytest.approx(4.0)

        with pytest.raises(TypeError):
            x * "12"

    def test_rmul(self):
        x = DualNumber(2, 1.0)
        t_1 = 18 * x
        assert t_1.real == pytest.approx(36.0)
        assert t_1.dual == pytest.approx(18)

        t_2 = 3 * x * x
        assert t_2.real == pytest.approx(12.0)
        assert t_2.dual == pytest.approx(12)

        with pytest.raises(TypeError):
            "12" * x

    def test_truediv(self):
        x = DualNumber(2, 1.0)
        t_1 = x / 2
        assert t_1.real == pytest.approx(1.0)
        assert t_1.dual == pytest.approx(0.5)

        t_2 = x / x
        assert t_2.real == pytest.approx(1.0)
        assert t_2.dual == pytest.approx(0)

        with pytest.raises(TypeError):
            x / "12"

    def test_rtruediv(self):
        x = DualNumber(2, 1.0)
        t_1 = 4 / x
        assert t_1.real == pytest.approx(2.0)
        assert t_1.dual == pytest.approx(-1.0)

        with pytest.raises(TypeError):
            "12" / x

    def test_pow(self):
        x = DualNumber(2, 1.0)
        y = DualNumber(0)
        t_1 = x ** 2
        t_3 = x * x
        assert t_1.real == pytest.approx(4.0)
        assert t_1.dual == pytest.approx(4.0)
        assert t_1.real == pytest.approx(t_3.real)

        t_2 = x ** 0.5
        t_4 = math.sqrt(x.real)
        assert t_2.real == pytest.approx(1.4142135623730951)
        assert t_2.dual == pytest.approx(0.3535533905932738)
        assert t_2.real == pytest.approx(t_4.real)
        assert (y ** 2).dual == pytest.approx(0)

        with pytest.raises(TypeError):
            x ** "12"

    def test_rpow(self):
        x = DualNumber(2, 1.0)
        t_1 = 4 ** x
        assert t_1.real == pytest.approx(16.0)
        assert t_1.dual == pytest.approx(22.18070977791825)

        with pytest.raises(TypeError):
            "12" ** x

    def test_neg(self):
        x = DualNumber(2, 1.0)
        t_1 = -x
        assert t_1.real == pytest.approx(-2.0)
        assert t_1.dual == pytest.approx(-1.0)

    def test_reflexivity(self):
        x = DualNumber(2, 1.0)
        y = DualNumber(2)

        t_1 = x + y
        t_2 = y + x
        assert t_1.real == pytest.approx(t_2.real)
        assert t_1.dual == pytest.approx(t_2.dual)

        t_3 = x * y
        t_4 = y * x
        assert t_3.real == pytest.approx(t_4.real)
        assert t_3.dual == pytest.approx(t_4.dual)

class Test_Function:

    def test_init(self):
        func = lambda a : a + 69
        x = Function(func)
        assert x.evaluator == func

    def test_call(self):
        x = Function()
        f1 = x / 5.0 + 3
        assert f1({x: 3}) == pytest.approx(3.6)

        f2 = 2 ** x
        assert f2({x: 5}) == pytest.approx(32)
        
    def test_diff_at(self):
        x = Function()
        f1 = x ** 2 + 1
        assert f1.diff_at({x: 1}) == 2

        f2 = x ** 3 - 2.5 * x + 5
        assert f2.diff_at({x: 1}) == pytest.approx(0.5) 

        f3 = x ** x 
        assert f3.diff_at({x: 2}) == pytest.approx(6.77258872)

        y = Function()
        
        with pytest.raises(TypeError):
            f1.diff_at({x: 1, y: 2})

    def test_jacobian_at(self):
        x = Function()
        y = Function()
        f1 = x ** 3 + y
        assert f1.jacobian_at([x, y], {x: 5, y: 10}) == pytest.approx(np.array([75, 1]))

        z = Function()
        f2 = x / y + 2 ** z
        assert f2.jacobian_at([x, y, z], {x: 1, y: 2, z: 4}) == pytest.approx(np.array([0.5, -0.25, np.log(2) * 16]))

    def test_add(self):
        x = Function()
        y = Function()
        assert (x + y)({x: 1.0, y : 2.0}) == pytest.approx(3)

        with pytest.raises(TypeError):
            x + "y"

    def test_radd(self):
        x = 2
        y = Function()
        assert (x + y)({y : 1.0}) == pytest.approx(3)
        with pytest.raises(TypeError):
            "x" + y

    def test_sub(self):
        x = Function()
        y = Function()
        assert (x - y)({x: 2, y : 1.0}) == pytest.approx(1)

        with pytest.raises(TypeError):
            x - "y"

    def test_rsub(self):
        x = 3
        y = Function()
        assert (x - y)({y : 1.0}) == pytest.approx(2)
        with pytest.raises(TypeError):
            "69" - y

    def test_mul(self):
        x = Function()
        y = Function()
        assert (x * y)({x: 2.0, y : 1.0}) == pytest.approx(2)

        with pytest.raises(TypeError):
            x * "y"

    def test_rmul(self):
        x = 3
        y = Function()
        assert (x * y)({y : 2.0}) == pytest.approx(6)
        with pytest.raises(TypeError):
            "2" * y

    def test_truediv(self):
        x = Function()
        y = Function()
        assert (x / y)({x: 4, y : 2.0}) == pytest.approx(2)

        with pytest.raises(TypeError):
            x / "y"

    def test_rtruediv(self):
        x = 6
        y = Function()
        assert (x / y)({y : 2.0}) == pytest.approx(3)
        with pytest.raises(TypeError):
            [2] / y

    def test_pow(self):
        x = Function()
        y = Function()
        assert (x ** y)({x: 2, y : 2.0}) == pytest.approx(4)

        with pytest.raises(TypeError):
            x ** "y"
        
    def test_rpow(self):
        x = 3
        y = Function()
        assert (x ** y)({y : 2.0}) == pytest.approx(9)
        with pytest.raises(TypeError):
            {"a": 5} ** y

    def test_neg(self):
        x = Function()
        assert (-x)({x: 2}) == pytest.approx(-2)

class Test_DiffObject:

    def test_init(self):
        do = DiffObject()
        assert isinstance(do.function, Function)
        assert isinstance(do.node, Node)

    def test_set_var_order(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()

        do_x = DiffObject(function=x_func, node=x_node)
        do_y = DiffObject(function=y_func, node=y_node)
        do_xy = do_x + do_y
        do_xy.set_var_order(do_x, do_y)
        assert do_xy.var_order[0] == do_x
        assert do_xy.var_order[1] == do_y

        do_y2 = do_y - 2
        with pytest.raises(TypeError):
            do_y2.set_var_order(3)

    def test_call(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_2x = 2 * do_x
        with pytest.raises(TypeError):
            do_2x(6)
        do_2x.set_var_order(do_x)
        assert do_2x(2) == 4
        assert do_2x(5.0, reverse_mode=True) == pytest.approx(10)
        with pytest.raises(TypeError):
            do_2x(1, 1)

    def test_diff_at(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_xsq = do_x ** 2
        with pytest.raises(TypeError):
            do_xsq.diff_at(6)
        do_xsq.set_var_order(do_x)
        assert do_xsq.diff_at(4.0) == pytest.approx(8)
        assert do_xsq.diff_at(2.0, reverse_mode=True) == pytest.approx(4)
        y_func = Function()
        y_node = Node()
        do_y = DiffObject(node=y_node, function=y_func)
        do_xy = do_x / do_y
        do_xy.set_var_order(do_x, do_y)
        with pytest.raises(TypeError):
            do_xy.diff_at(3, 4)

    def test_jacobian_at(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do_xy = do_x ** 3 - do_y
        with pytest.raises(TypeError):
            do_xy.jacobian_at(2, 8, 5)
        do_xy.set_var_order(do_x, do_y)
        with pytest.raises(TypeError):
            do_xy.jacobian_at(2, 3, 5)
        assert do_xy.jacobian_at(2, 4) == pytest.approx(np.array([12, -1]))
        assert do_xy.jacobian_at(5, 2, reverse_mode=True) == pytest.approx(np.array([75, -1]))

    def test_add(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do_xy = do_x + do_y
        do_xy.set_var_order(do_x, do_y)
        assert do_xy.function({do_x.function: 1.0, do_y.function: 2}) == pytest.approx(3)
        assert do_xy.node({do_x.node: 3, do_y.node: 2.5}) == pytest.approx(5.5)
        do_x3 = do_x + 3
        do_x3.set_var_order(do_x)
        assert do_x3.function({do_x.function: 1.0}) == pytest.approx(4)
        assert do_x3.node({do_x.node: 2.0}) == pytest.approx(5)
        with pytest.raises(TypeError):
            do_xy + "5"
    
    def test_radd(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_3x = 3 + do_x
        do_3x.set_var_order(do_x)
        assert do_3x.function({do_x.function: 1.0}) == pytest.approx(4)
        assert do_3x.node({do_x.node: 2}) == pytest.approx(5)
        with pytest.raises(TypeError):
            "2" + do_x

    def test_sub(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do_xy = do_x - do_y
        do_xy.set_var_order(do_x, do_y)
        assert do_xy.function({do_x.function: 1.0, do_y.function: 2}) == pytest.approx(-1)
        assert do_xy.node({do_x.node: 3, do_y.node: 2.5}) == pytest.approx(0.5)
        do_x3 = do_x - 3
        do_x3.set_var_order(do_x)
        assert do_x3.function({do_x.function: 7.0}) == pytest.approx(4)
        assert do_x3.node({do_x.node: 15.0}) == pytest.approx(12)
        with pytest.raises(TypeError):
            do_x - [3]

    def test_rsub(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_3x = 3 - do_x
        do_3x.set_var_order(do_x)
        assert do_3x.function({do_x.function: 7.0}) == pytest.approx(-4)
        assert do_3x.node({do_x.node: 2}) == pytest.approx(1)
        with pytest.raises(TypeError):
            "2" - do_x

    def test_mul(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do_xy = do_x * do_y
        do_xy.set_var_order(do_x, do_y)
        assert do_xy.function({do_x.function: 3.0, do_y.function: 2}) == pytest.approx(6)
        assert do_xy.node({do_x.node: 3, do_y.node: 2.5}) == pytest.approx(7.5)
        do_x3 = do_x * 3
        do_x3.set_var_order(do_x)
        assert do_x3.function({do_x.function: 1.0}) == pytest.approx(3)
        assert do_x3.node({do_x.node: -2.0}) == pytest.approx(-6)
        with pytest.raises(TypeError):
            do_xy * "5"

    def test_rmul(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_3x = 5.0 * do_x
        do_3x.set_var_order(do_x)
        assert do_3x.function({do_x.function: 7.0}) == pytest.approx(35)
        assert do_3x.node({do_x.node: -2}) == pytest.approx(-10)
        with pytest.raises(TypeError):
            "2" * do_x

    def test_truediv(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do_xy = do_x / do_y
        do_xy.set_var_order(do_x, do_y)
        assert do_xy.function({do_x.function: 5.0, do_y.function: 2}) == pytest.approx(2.5)
        assert do_xy.node({do_x.node: -33, do_y.node: 3}) == pytest.approx(-11)
        do_x5 = do_x / 5
        do_x5.set_var_order(do_x)
        assert do_x5.function({do_x.function: 2}) == pytest.approx(0.4)
        assert do_x5.node({do_x.node: -15}) == pytest.approx(-3)
        with pytest.raises(TypeError):
            do_xy / (5, 2)

    def test_rtruediv(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_48x = 48 / do_x
        do_48x.set_var_order(do_x)
        assert do_48x.function({do_x.function: 6.0}) == pytest.approx(8)
        assert do_48x.node({do_x.node: -10}) == pytest.approx(-4.8)
        with pytest.raises(TypeError):
            "2" / do_x

    def test_pow(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do_xy = do_x ** do_y
        do_xy.set_var_order(do_x, do_y)
        assert do_xy.function({do_x.function: 5.0, do_y.function: 2}) == pytest.approx(25)
        assert do_xy.node({do_x.node: 3, do_y.node: 2}) == pytest.approx(9)
        do_x5 = do_x ** 5
        do_x5.set_var_order(do_x)
        assert do_x5.function({do_x.function: 2}) == pytest.approx(32)
        assert do_x5.node({do_x.node: 1}) == pytest.approx(1)
        with pytest.raises(TypeError):
            do_xy ** {"a": 2}

    def test_rpow(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_2x = 2 ** do_x
        do_2x.set_var_order(do_x)
        assert do_2x.function({do_x.function: 6.0}) == pytest.approx(64)
        assert do_2x.node({do_x.node: -2}) == pytest.approx(0.25)
        with pytest.raises(TypeError):
            "2" ** do_x
    
    def test_neg(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_negx = - do_x
        do_negx.set_var_order(do_x)
        assert do_negx.function({do_x.function: 6.0}) == pytest.approx(-6)
        assert do_negx.node({do_x.node: -2.5}) == pytest.approx(2.5)

    def test_str(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do_xy = do_x / do_y
        do_xy.set_var_order(do_x, do_y)
        assert str(do_xy) == "\u25c6 [DIV] (no_val)\n\u2514parent1: \u25c6 [VAR] (no_val)\n\u2514parent2: \u25c6 [VAR] (no_val)"

    def test_graph_image(self):
        do = DiffObject()
        try: 
            do.graph_image()
        except:
            assert False

class Test_VectorFunction:

    def test_init(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do1 = do_x + do_y
        do2 = do_x * do_y
        do1.set_var_order(do_x, do_y)
        do2.set_var_order(do_x, do_y)
        vf = VectorFunction(do1, do2)
        assert len(vf.diff_objects) == 2
        assert vf.diff_objects[0](1, 1) == do1(1, 1)
        assert vf.diff_objects[1](1, 1) == do2(1, 1)

    def test_set_var_order(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do1 = do_x + do_y
        do2 = do_x * do_y
        do1.set_var_order(do_x, do_y)
        do2.set_var_order(do_y, do_x)
        vf = VectorFunction(do1, do2)
        assert vf.diff_objects[0].var_order[0] == do_x and vf.diff_objects[0].var_order[1] == do_y
        assert vf.diff_objects[1].var_order[0] == do_y and vf.diff_objects[1].var_order[1] == do_x

    def test_call(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do1 = do_x ** 3 - do_y ** 2
        do2 = 1 + do_x * do_y
        do1.set_var_order(do_x, do_y)
        do2.set_var_order(do_x, do_y)
        vf = VectorFunction(do1, do2)
        assert vf(3, 2) == pytest.approx(np.array([23, 7]))

    def test_diff_at(self):
        x_func = Function()
        x_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do1 = do_x ** 2 - 5 * do_x
        do2 = 1 / (do_x ** 4)
        do1.set_var_order(do_x)
        do2.set_var_order(do_x)
        vf = VectorFunction(do1, do2)
        assert vf.diff_at(2) == pytest.approx(np.array([-1, - 1 / 8]))

    def test_jacobian_at(self):
        x_func = Function()
        y_func = Function()
        x_node = Node()
        y_node = Node()
        do_x = DiffObject(node=x_node, function=x_func)
        do_y = DiffObject(node=y_node, function=y_func)
        do1 = do_x * 5 - do_y * do_x
        do2 = 1 + do_x / do_y
        do1.set_var_order(do_x, do_y)
        do2.set_var_order(do_x, do_y)
        vf = VectorFunction(do1, do2)
        assert vf.jacobian_at(5, 3) == pytest.approx(np.array([[2, -5],[1 / 3, -5 / 9]]))

class Test_Helpers:
    def test_variadic_helper(self):
        x = DiffObject()
        y = DiffObject()
        z = DiffObject()
        f = x + y * z
        f.set_var_order(x, y, z)

        with pytest.raises(TypeError):
            f(1, 2, "3")

        with pytest.raises(TypeError):
            f(1, 2, np.array([1, 2, 3, 4]).reshape(2, 2))

        with pytest.raises(TypeError):
            f(np.array([1, 2, 3]).reshape(3, 1, 1))

        assert f(1, 2, 3) == 7
        assert f(1, [2, 3]) == 7
        assert f([1], [2], [3]) == 7
        assert f([1, 2, 3]) == 7
        assert f(1, np.array([2, 3]).reshape(-1, 2)) == 7
        assert f(np.array([1, 2, 3]).reshape(3, -1)) == 7
        assert f(np.array([1, 2]), 3) == 7