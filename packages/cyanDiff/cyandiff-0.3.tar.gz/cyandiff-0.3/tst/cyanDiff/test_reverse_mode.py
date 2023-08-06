import pytest
import copy
import networkx as nx
import numpy as np

from cyanDiff.ad_types import DualNumber, Function, DiffObject, VectorFunction
from cyanDiff.reverse_mode import Node, Operator, safe_copy_nodes, GraphImgNode

class Test_Operators:
    
    def test_format_str(self):
        op = Operator.ASIN
        assert op.format_str() == "[ASIN]"

class Test_Node:

    def test_init(self):
        parent1 = Node()
        parent2 = Node()
        child = Node(p1=parent1, p2=parent2, op=Operator.ADD)
        assert child.node_id != parent1.node_id
        assert child.node_id != parent2.node_id
        assert child.parent1 == parent1
        assert child.parent2 == parent2

    def test_f_eval(self):
        ops = list(Operator)
        x = Node()
        y = Node() 
        zs = list(map(lambda op : Node(p1=safe_copy_nodes(x), p2=safe_copy_nodes(y), op=op), ops[1:22]))
        value_assignment = {x: 0.5, y: 2}
        partial_vals = [(2.5, 1, 1), 
                        (-1.5, 1, -1), 
                        (1, 2, 0.5), 
                        (1/4, 1/2, -1/8),
                        (1/4, 1, np.log(0.5) * (0.5 ** 2)), 
                        (-0.5, -1, None), 
                        (np.sin(0.5), np.cos(0.5), None),
                        (np.cos(0.5), -np.sin(0.5), None), 
                        (np.tan(0.5), np.cos(0.5) ** (-2), None),
                        (np.exp(0.5), np.exp(0.5), None), 
                        (np.log(0.5), 1/0.5, None), 
                        (np.sinh(0.5), np.cosh(0.5), None),
                        (np.cosh(0.5), np.sinh(0.5), None),
                        (np.tanh(0.5), np.cosh(0.5) ** (-2), None),
                        (1 / (1 + np.exp(-0.5)), np.exp(0.5) / ((np.exp(0.5) + 1) ** 2), None),
                        (np.sqrt(0.5), 1 / (2 * np.sqrt(0.5)), None),
                        (np.arcsin(0.5), 1 / np.sqrt(1 - 0.5 ** 2), None),
                        (np.arccos(0.5), -1 / np.sqrt(1 - 0.5 ** 2), None),
                        (np.arctan(0.5), 1 / (1 + 0.5 ** 2), None),
                        (np.arcsinh(0.5), 1 / np.sqrt(1 + 0.5 ** 2), None),
                        (np.arctanh(0.5), 1 / (1 - 0.5 ** 2), None)]

        for z, fval_and_pvals in zip(zs, partial_vals):
            func_val, partial1, partial2 = fval_and_pvals
            z._f_eval(value_assignment)
            assert z.value == pytest.approx(func_val)
            assert z.parent1_partial == pytest.approx(partial1)
            assert z.parent2_partial == pytest.approx(partial2)
        
        # separately test VAR due to unique structure
        assert safe_copy_nodes(x)._f_eval(value_assignment) == pytest.approx(0.5)

        # separately test ACOSH due to function domain restriction
        val_ass_acosh = {x: 69}
        z_acosh = Node(p1=safe_copy_nodes(x), op=Operator.ACOSH)
        z_acosh._f_eval(val_ass_acosh)
        assert z_acosh.value == pytest.approx(np.arccosh(69))
        assert z_acosh.parent1_partial == pytest.approx(-1 / np.sqrt(69 ** 2 - 1))
        assert z_acosh.parent2_partial == None

        z_const = Node(p1=2.0, p2=3, op=Operator.ADD)
        assert z_const._f_eval({}) == pytest.approx(5)

        z_with_value = Node()
        z_with_value.value = 2
        assert z_with_value._f_eval({}) == pytest.approx(2)

        with pytest.raises(KeyError):
            safe_copy_nodes(x)._f_eval({y: 2})

        with pytest.raises(TypeError):
            bad_op_node = Node(p1=safe_copy_nodes(x), op=55)
            bad_op_node._f_eval({x: 3})

    def test_r_eval(self):
        x = Node()
        y = Node()
        z = Node(p1=x, p2=y, op=Operator.ADD)

        x.children = [z]
        y.children = [z]

        z.parent1_partial = 1
        z.parent2_partial = 1

        assert x._r_eval(z) == 1

        bad_node = Node()
        bad_node.children = [x]
        with pytest.raises(LookupError):
            bad_node._r_eval(z)

    def test_clear(self):
        x = Node()
        y = Node()
        z = Node(p1=x, p2=y, op=Operator.ADD)

        x.children = [z]
        y.children = [z]

        z._clear()

    def test_call(self):
        x = Node()
        y = Node(p1=x, op=Operator.SIN)
        assert y({x: 3}) == pytest.approx(np.sin(3))
    
    def test_diff_wrt_at(self):
        x = Node()
        y = Node()
        x.vars = [x]
        y.vars = [y]
        z = Node(p1=x, p2=y, op=Operator.SUB)

        x.children = [z]
        y.children = [z]
        
        assert z._diff_wrt_at(x.node_id, {x: 2, y: 3}) == 1 

    def test_diff_at(self):
        x = Node()
        y = Node()
        z1 = x + y
        with pytest.raises(TypeError):
            z1.diff_at({x: 1, y: 1})
        
        z2 = safe_copy_nodes(x) * 2
        assert z2.diff_at({x: 1}) == pytest.approx(2)

    def test_jacobian_at(self):
        x = Node()
        y = Node()
        z1 = x * y
        assert z1.jacobian_at([x, y], {x: 2, y: 5}) == pytest.approx(np.array([5, 2]))

    def test_add(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            x + "node"
        z1 = x + y
        z2 = x + 3
        assert z1({x: 5, y: 3.5}) == pytest.approx(8.5)
        assert z2({x: 3}) == pytest.approx(6) 
    
    def test_radd(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            "node" + x
        z1 = 3 + x
        assert z1({x: 5}) == pytest.approx(8)

    def test_sub(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            x - "node"
        z1 = x - y
        z2 = x - 7.5
        assert z1({x: 5, y: 3.5}) == pytest.approx(1.5)
        assert z2({x: 10}) == pytest.approx(2.5) 

    def test_rsub(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            [5] - x
        z1 = 3 - x
        assert z1({x: 5}) == pytest.approx(-2)

    def test_mul(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            x * "CS107"
        z1 = x * y
        z2 = x * 1.5
        assert z1({x: 5, y: 0.5}) == pytest.approx(2.5)
        assert z2({x: 10}) == pytest.approx(15) 
    
    def test_rmul(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            {"hi": 6} * x
        z1 = 3 * x
        assert z1({x: 5}) == pytest.approx(15)

    def test_truediv(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            x / "CS107"
        z1 = x / y
        z2 = x / 3
        assert z1({x: 6, y: 3}) == pytest.approx(2)
        assert z2({x: 8}) == pytest.approx(8/3)

    def test_rtruediv(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            "name" / x
        z1 = 10 / x
        assert z1({x: 5}) == pytest.approx(2)

    def test_pow(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            x ** "CS107"
        z1 = x ** y
        z2 = x ** 4
        assert z1({x: 6, y: 2}) == pytest.approx(36)
        assert z2({x: 5}) == pytest.approx(625)

    def test_rpow(self):
        x = Node()
        y = Node()
        with pytest.raises(TypeError):
            "name" ** x
        z1 = 10 ** x
        assert z1({x: 3}) == pytest.approx(1000)

    def test_neg(self):
        x = Node()
        y = -x
        assert y({x: 2}) == pytest.approx(-2)

    def test_str(self):
        x = Node(op=Operator.SIN)
        assert str(x) == "[SIN] (no_val)\n"
        x.value = 1.7291
        assert str(x) == "[SIN] (1.729)\n"

    def test_string_viz(self):
        x = Node()
        y = Node()
        z = x ** 2 + 3 * y
        assert z._string_viz() == ("◆ [ADD] (no_val)\n" + "└parent1: ◆ [POW] (no_val)\n" + 10 * " " +
                                  "└parent1: ◆ [VAR] (no_val)\n" + 10 * " " + "└parent2: (const) 2.000\n" +
                                  "└parent2: ◆ [MUL] (no_val)\n" + 10 * " " + "└parent1: (const) 3.000\n" +
                                  10 * " " + "└parent2: ◆ [VAR] (no_val)\n")

        bad1 = Node(p1="node", p2=3, op=Operator.SUB)
        with pytest.raises(TypeError):
            bad1._string_viz()
        bad2 = Node(p1=3, p2="node", op=Operator.SUB)
        with pytest.raises(TypeError):
            bad2._string_viz()

    def test_text_graph_viz(self):
        x = Node()
        y = Node()
        z = x - y
        assert z.text_graph_viz() == "◆ [SUB] (no_val)\n└parent1: ◆ [VAR] (no_val)\n└parent2: ◆ [VAR] (no_val)"

    def test_get_graph_depth(self):
        x = Node()
        y = Node()
        z = ((x ** 3) - y) * 5
        assert z.get_graph_depth() == pytest.approx(4)

    def test_graph_image(self):
        x = Node()
        y = Node()
        z = (3 * x) / y - x ** 5
        try:
            z.graph_image()
        except:
            assert False

    def test_safe_copy_nodes(self):
        x = Node()
        x_copy = safe_copy_nodes(x)
        assert x is not x_copy
        y = Node(op=Operator.ADD)
        y_copy = safe_copy_nodes(y)
        assert y is y_copy

class Test_GraphImgNode:

    def test_init(self):
        x = GraphImgNode("x")
        y = GraphImgNode("y")
        assert x.id != y.id

    def test_str(self):
        x = GraphImgNode("x")
        assert str(x) == "x"