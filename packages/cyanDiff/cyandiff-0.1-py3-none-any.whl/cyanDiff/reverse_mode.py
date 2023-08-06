#!/usr/bin/env python3
"""This module implements reverse mode autodifferentiation (AD).

Reverse mode AD is implemented by means of a computational graph which is a representation of 
a more complex mathematical expression in terms of smaller operations and individual components, 
the nodes of the graph. The nodes of this graph are implemented in the class :class:`Node`, and 
the operators in each node are implemented in the class :class:`Operator`. In the computational 
graph, we store the calculated partial derivatives of nodes with respect to their parent in the 
forward pass of reverse mode, which can then be used to calculated the partial derivatives of the 
function with respect to the variables of the function by application of the chain rule. This then 
allows for the calculation of the derivative for single variate or jacobian matrix of a function 
at a particular point. 

Users, however, only handle the DiffObject class implemented in the :class:`ad_types` module. This
class makes use of the the :class:`Node` object defined here in order to perform reverse mode AD. 
Users can then calculate the derivative or jacobian matrix using :class:`DiffObject.diff_at()` (for 
single variate) and :class:`DiffObject.jacobian_at()` (for multi variate) while setting the `reverse_mode`
argument set to true.

Users can also visualize the reverse mode computational graph, with either a text-based visualization 
of the graph structure, or using a graphical visulization. Though these are handled with methods in
:class:`DiffObject`, the implementation of these methods is handled in the :class:`Node` defined here.
"""

from __future__ import annotations
from enum import Enum
from typing import Dict, Union, Set
import numpy as np
import copy
import networkx as nx
import matplotlib.pyplot as plt

class Operator(Enum):
    """Implements the operators stored in the nodes (see :class:`Node`) of the computational graph
    
    Enumeration type used to store all the operators that are allowed in reverse mode AD.
    """
    VAR = 1    # represents an independent variable
    ADD = 2    # [1] + [2]
    SUB = 3    # [1] - [2]
    MUL = 4    # [1] * [2]
    DIV = 5    # [1] / [2]
    POW = 6    # [1] ^ [2]
    NEG = 7    # - [1]
    SIN = 8    # sin( [1] )
    COS = 9    # cos( [1] )
    TAN = 10   # tan( [1] )
    EXP = 11   # exp( [1] )
    LOG = 12   # log( [1] )
    SINH = 13  # sinh( [1] )
    COSH = 14  # cosh( [1] )
    TANH = 15  # tanh( [1] )
    LOGI = 16  # logistic( [1] )
    SQRT = 17  # sqrt( [1] )
    ASIN = 18  # arcsin( [1] )
    ACOS = 19  # arccos( [1] )
    ATAN = 20  # arctan( [1] )
    ASINH = 21 # arcsinh( [1] )
    ATANH = 22 # arctanh( [1] )
    ACOSH = 23 # arccosh( [1] )
    

    def format_str(self):
        return f"[{str(self).split('.')[1]}]"
    
class Node:
    """Implements the nodes of the computational graph in reverse mode AD.

    Each :class:`Node` represents a node in a computational graph. The node represents a mathematical 
    expression comprised of a binary or unary operator with the corresponding number of operands, 
    which can be of type :class:`Node` or numeric types (:class:`int` or :class:`float`). Some nodes
    represent the variables, and thus have no parents. The :class:`Node` objects also store the 
    associated partials with respect to their parents, which are calculated when we perform the forward 
    pass of reverse mode AD. Since the values are stored, when the reverse pass is performed, the 
    sensitivities can then be accumulated using the already calculated values.

    Using math operators, :class:`Node` objects can be combined together in various way. All such node 
    operations are also compatible with :class:`int' and :class:`float` objects.

    :param parent1: First parent node, or a constant value
    :type parent1: :class:`Node`, :class:`int`, :class:`float`  
    """
    valid_types = (int, float) # types that can be combined by math operators with nodes
    next_node_id = 0           # tracks node id to be handed out next
    next_img_id = 0            # tracks next image file numbering for comp graph image 

    def __init__(self, p1=None, p2=None, op=Operator.VAR):
        self.parent1 = p1
        self.parent2 = p2
        self.parent1_partial : float = None # computed during _f_eval
        self.parent2_partial : float = None # computed during _f_eval

        self.operator : Operator = op
        self.value : float = None           # computed during _f_eval
        self.sensitivity : float = None     # computed during _r_eval
        
        self.children : list[Node] = []
        self.vars : Set[Node] = set()
        if p1 is not None and isinstance(p1, Node):
            self.vars = self.vars.union(p1.vars)
        if p2 is not None and isinstance(p2, Node):
            self.vars = self.vars.union(p2.vars)

        self.node_id = self.next_node_id
        self.incr_node_id()
        self.graph_img_node : GraphImgNode = None
        self.graph_depth : int = None

    @classmethod
    def incr_node_id(cls):
        """Increments universal id counter to ensure unique ids for nodes"""
        cls.next_node_id += 1

    @classmethod
    def incr_img_id(cls):
        """Increments file numbering for autogenerated computational graph images"""
        cls.next_img_id += 1

    def _f_eval(self, value_assignment : Dict[Node, Union[int, float]]):
        """Private method for performing forward pass evaluation.
        
        Calculates the partial derivative of each node in the computational graph with respect to its
        parents given a particular assignment of values to the variables of the function (a dictionary 
        :class:`value_assignment`). Each partial derivative is stored to the :class:`parent1_partial` 
        and :class:`parent2_partial` attributes of the node object respectively. Also calculate the value
        of the function at the value assignment, and store in :class:`self.value`

        :param value_assignment: dictionary with variables as keys and assigned value (:class:`int` or 
        :class:`float`) to those variables as the values in the dict.
        :type value_assignment: :class:`dict`
        :returns: :class:`self.value`, the value of the function at the given point
        :rtype: :class:`int` or :class:`float`
        """
        if self.value is not None:
            return self.value

        # evaluate the first parent
        if self.parent1 is None:
            f = None
        elif isinstance(self.parent1, self.valid_types):
            f = self.parent1
        elif isinstance(self.parent1, Node):
            f = self.parent1._f_eval(value_assignment)

        # evaluate the second parent
        if self.parent2 is None:
            g = None
        elif isinstance(self.parent2, self.valid_types):
            g = self.parent2
        elif isinstance(self.parent2, Node):
            g = self.parent2._f_eval(value_assignment)

        # based on operator of node, evaluate values and partials wrt to parents
        if self.operator == Operator.VAR:
            for k in value_assignment.keys():
                if k.node_id == self.node_id:
                    self.value = value_assignment[k]
                    return self.value
            raise KeyError("Missing variable in value assignment")
        elif self.operator == Operator.ADD:
            self.value = f + g
            self.parent1_partial = 1
            self.parent2_partial = 1
        elif self.operator == Operator.SUB:
            self.value = f - g
            self.parent1_partial = 1
            self.parent2_partial = -1
        elif self.operator == Operator.MUL:
            self.value = f * g
            self.parent1_partial = g
            self.parent2_partial = f
        elif self.operator == Operator.DIV:
            self.value = f / g
            self.parent1_partial = 1 / g
            self.parent2_partial = (-f) * (g ** -2)
        elif self.operator == Operator.POW:
            self.value = f ** g
            self.parent1_partial = g * (f ** (g - 1))
            self.parent2_partial = (f ** g) * np.log(f)
        elif self.operator == Operator.NEG:
            self.value = -f
            self.parent1_partial = -1
        elif self.operator == Operator.SIN:
            self.value = np.sin(f)
            self.parent1_partial = np.cos(f)
        elif self.operator == Operator.COS:
            self.value = np.cos(f)
            self.parent1_partial = -np.sin(f)
        elif self.operator == Operator.TAN:
            self.value = np.tan(f)
            self.parent1_partial = 1 / (np.cos(f) ** 2)
        elif self.operator == Operator.EXP:
            self.value = np.exp(f)
            self.parent1_partial = np.exp(f)
        elif self.operator == Operator.LOG:
            self.value = np.log(f)
            self.parent1_partial = 1 / f
        elif self.operator == Operator.SINH:
            self.value = np.sinh(f)
            self.parent1_partial = np.cosh(f)
        elif self.operator == Operator.COSH:
            self.value = np.cosh(f)
            self.parent1_partial = np.sinh(f)
        elif self.operator == Operator.TANH:
            self.value = np.tanh(f)
            self.parent1_partial = 1 / (np.cosh(f) ** 2)
        elif self.operator == Operator.LOGI:
            self.value = 1 / (1 + np.exp(-f))
            self.parent1_partial = np.exp(f) / ((np.exp(f) + 1) ** 2) 
        elif self.operator == Operator.SQRT:
            self.value = np.sqrt(f)
            self.parent1_partial = 1 / (2 * np.sqrt(f))
        elif self.operator == Operator.ASIN:
            self.value = np.arcsin(f)
            self.parent1_partial = 1 / np.sqrt(1 - f ** 2)
        elif self.operator == Operator.ACOS:
            self.value = np.arccos(f)
            self.parent1_partial = -1 / np.sqrt(1 - f ** 2)
        elif self.operator == Operator.ATAN:
            self.value = np.arctan(f)
            self.parent1_partial = 1 / (1 + f ** 2)
        elif self.operator == Operator.ASINH:
            self.value = np.arcsinh(f)
            self.parent1_partial = 1 / np.sqrt(1 + f ** 2)
        elif self.operator == Operator.ATANH:
            self.value = np.arctanh(f)
            self.parent1_partial = 1 / (1 - f ** 2)
        elif self.operator == Operator.ACOSH:
            self.value = np.arccosh(f)
            self.parent1_partial = -1 / np.sqrt(f ** 2 - 1)
        else:
            raise TypeError("ERROR: unsupported operator")

        return self.value

    def _r_eval(self, root):
        """Calculate the partial of an output node in the graph wrt to another.
        
        Finds the numerical value of the partial, i.e. the sensitivity, of :class:`self` 
        node wrt to :class:`root` node. If sensitivity has already been calculated and 
        stored as :class:`self.sensitivity`, just return that value.

        :param root: output node of the graph
        :type root: :class:`Node`
        :returns: sensitivity of root node wrt to another node
        :rtype: :class:`int` or :class:`float`
        """
        # return stored value if it exists
        if self.sensitivity is not None:
            return self.sensitivity

        # recursively apply chain rule to get sensitivity
        if self is root:
            self.sensitivity = 1
        else:
            self.sensitivity = 0
            for c in self.children:
                c_sens = c._r_eval(root)

                if c.parent1 is self:
                    c_partial = c.parent1_partial
                elif c.parent2 is self:
                    c_partial = c.parent2_partial
                else:
                    raise LookupError("Incorrect node link in graph")

                self.sensitivity += c_sens * c_partial

        return self.sensitivity

    def _clear(self):
        """Cleans out all cached values that resulted from lazy evaluation."""
        self.value = None
        self.sensitivity = None
        self.graph_img_node = None
        self.graph_depth = None

        if isinstance(self.parent1, Node):
            self.parent1._clear()

        if isinstance(self.parent2, Node):
            self.parent2._clear()

    def __call__(self, value_assignment):
        """Calculate value of function at a point.
        
        :param value_assignment: dictionary with variables as keys and assigned value (:class:`int` or 
        :class:`float`) to those variables as the values in the dict.
        :type value_assignment: :class:`dict`
        :returns: value of function represented by node at a particular point
        :rtype: :class:`int` or :class:`float`
        """
        self._clear()
        return self._f_eval(value_assignment)

    def _diff_wrt_at(self, var_id : int, value_assignment):
        # WARNING: assumes that self._clear() has already been called, or that
        # already-cached values are correct from a prior call to _f_eval
        self._f_eval(value_assignment)
        retval = 0
        for var in self.vars:
            if var.node_id == var_id:
                retval += var._r_eval(self)

        return retval

    def diff_at(self, value_assignment):
        """Calculates the derivative of single variate function at particular point.

        :param value_assignment: dictionary with variables as keys and assigned value (:class:`int` or 
        :class:`float`) to those variables as the values in the dict.
        :type value_assignment: :class:`dict`
        :returns: value of function represented by node at a particular point
        :rtype: :class:`int` or :class:`float`
        """
        self._clear()
        var_ids = set()
        for var in self.vars:
            var_ids.add(var.node_id)

        if len(var_ids) != 1:
            raise TypeError("diff_at can only be used for functions of a single variable (R1 -> Rn)")

        return self._diff_wrt_at(list(var_ids)[0], value_assignment)

    def jacobian_at(self, variable_order : list[Node], value_assignment):
        """Calculates the derivative of single variate function at particular point.

        :param variable_order: list of variables specifying order of partials in the outputted jacobian
        :type variable_order: :class:`list` of :class:`Node`
        :param value_assignment: dictionary with variables as keys and assigned value (:class:`int` or 
        :class:`float`) to those variables as the values in the dict.
        :type value_assignment: :class:`dict`
        :returns: value of function represented by node at a particular point
        :rtype: :class:`int` or :class:`float`
        """
        self._clear()
        retval = np.zeros(len(variable_order))
        for idx, var in enumerate(variable_order):
            retval[idx] = self._diff_wrt_at(var.node_id, value_assignment)
            
        return retval

    def __add__(self, other):
        """Makes a new node that represents the addition of two parent nodes"""
        if not isinstance(other, (*self.valid_types, Node)):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=self_c, p2=other_c, op=Operator.ADD)
        self_c.children.append(retval)
        if isinstance(other_c, Node):
            other_c.children.append(retval)
        return retval

    def __radd__(self, other):
        """Reversed addition of nodes for when first operand is not a node"""
        if not isinstance(other, self.valid_types):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=other_c, p2=self_c, op=Operator.ADD)
        self_c.children.append(retval)
        return retval

    def __sub__(self, other):
        """Makes a new node that represents the subtraction of two parent nodes"""
        if not isinstance(other, (*self.valid_types, Node)):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=self_c, p2=other_c, op=Operator.SUB)
        self_c.children.append(retval)
        if isinstance(other_c, Node):
            other_c.children.append(retval)
        return retval

    def __rsub__(self, other):
        """Reversed subtraction of nodes for when first operand is not a node"""
        if not isinstance(other, self.valid_types):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=other_c, p2=self_c, op=Operator.SUB)
        self_c.children.append(retval)
        return retval

    def __mul__(self, other):
        """Makes a new node that represents the multiplication of two parent nodes"""
        if not isinstance(other, (*self.valid_types, Node)):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=self_c, p2=other_c, op=Operator.MUL)
        self_c.children.append(retval)
        if isinstance(other_c, Node):
            other_c.children.append(retval)
        return retval

    def __rmul__(self, other):
        """Reversed multiplication of nodes for when first operand is not a node"""
        if not isinstance(other, self.valid_types):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=other_c, p2=self_c, op=Operator.MUL)
        self_c.children.append(retval)
        return retval

    def __truediv__(self, other):
        """Makes a new node that represents the division of two parent nodes"""
        if not isinstance(other, (*self.valid_types, Node)):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=self_c, p2=other_c, op=Operator.DIV)
        self_c.children.append(retval)
        if isinstance(other_c, Node):
            other_c.children.append(retval)
        return retval

    def __rtruediv__(self, other):
        """Reversed division of nodes for when first operand is not a node"""
        if not isinstance(other, self.valid_types):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=other_c, p2=self_c, op=Operator.DIV)
        self_c.children.append(retval)
        return retval

    def __pow__(self, other):
        """Makes a new node that represents the exponentiation of one parent node by a second"""
        if not isinstance(other, (*self.valid_types, Node)):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=self_c, p2=other_c, op=Operator.POW)
        self_c.children.append(retval)
        if isinstance(other_c, Node):
            other_c.children.append(retval)
        return retval

    def __rpow__(self, other):
        """Reversed exponentiation of nodes for when first operand is not a node"""
        if not isinstance(other, self.valid_types):
            raise TypeError(f"Invalid type: {type(other)}")

        self_c, other_c = safe_copy_nodes(self, other)

        retval = Node(p1=other_c, p2=self_c, op=Operator.POW)
        self_c.children.append(retval)
        return retval

    def __neg__(self):
        """Makes a new node that represents the negation of a parent node"""
        self_c = safe_copy_nodes(self)

        retval = Node(p1=self_c, op=Operator.NEG)
        self_c.children.append(retval)
        return retval

    def __str__(self):
        """Formats node for printing, giving its operator and value info"""
        if self.value is None:
            val_str = "no_val"
        else:
            val_str = "{0:.3f}".format(self.value)

        return f'{self.operator.format_str()} ({val_str})\n'

    def _get_graphImgNode(self):
        """Return a :class:`GraphImgNode` representing this node to be used in image representation of graph
        
        :returns: image representation version of :class:`self` node
        :rtype: :class:`GraphImgNode`
        """
        if self.graph_img_node is None:
            self.graph_img_node = GraphImgNode(str(self))

        return self.graph_img_node

    def _string_viz(self, indent=0):
        """Returns string representation of a computational graph.
        
        :returns: a string that represents the hierarchy of nodes and their parents in a comp graph rooted 
        at :class:`self` node
        :rtype: :class:`string`
        """
        value = ""
        value += f"\u25c6 {str(self)}"
        offset = 10 * " " * indent

        # represent the first parent
        if self.parent1 is None:
            p1_str = "---\n"
        elif isinstance(self.parent1, Node):
            p1_str = self.parent1._string_viz(indent + 1)
        elif isinstance(self.parent1, self.valid_types):
            p1_str = "(const) {0:.3f}\n".format(self.parent1)
        else:
            raise TypeError("Graph error -- data corrupted?")

        # represent the second parent
        if self.parent2 is None:
            p2_str = "---\n"
        elif isinstance(self.parent2, Node):
            p2_str = self.parent2._string_viz(indent + 1)
        elif isinstance(self.parent2, self.valid_types):
            p2_str = "(const) {0:.3f}\n".format(self.parent2)
        else:
            raise TypeError("Graph error -- data corrupted?")

        # for non-variable nodes with parent(s), represent that hierarchical relationship
        if self.operator != Operator.VAR:
            if self.parent1 is not None:
                value += offset + '\u2514parent1: ' + p1_str
            if self.parent2 is not None:
                value += offset + '\u2514parent2: ' + p2_str
        return value

    def text_graph_viz(self):
        """Visualizes graph with text but with no whitespace to organize it"""
        return self._string_viz().strip()

    def _calc_graph_depth(self):
        """Private method to \calculate the depth of graph from output node :class:`self`
        
        Note that just the output node itself is depth 1.

        :returns: depth of graph
        :rtype: :class:`int`
        """
        p1_depth = 0
        p2_depth = 0
        
        if isinstance(self.parent1, Node):
            p1_depth = self.parent1._calc_graph_depth()
        if isinstance(self.parent2, Node):
            p2_depth = self.parent2._calc_graph_depth()

        return 1 + max(p1_depth, p2_depth)

    def get_graph_depth(self):
        """Get stored grab depth value from output node :class:`self` if it exists, otherwise calculate it
        
        :returns: depth of graph
        :rtype: :class:`int`
        """
        if self.graph_depth is None:
            self.graph_depth = self._calc_graph_depth()

        return self.graph_depth

    def _make_graph(self, graph=None, x=0, y=0, level=0, added_nodes=set()):
        """Generate a graph of type :class:`networkx.digraph.DiGraph` from the node itself.

        Recursively generate a directed graph from the node. The graph generated
        is a visualization of a binary tree. The function recursively gets called,
        and it appends a representation of the subgraph starting at the `self`
        node to the parameter `graph`, if it exists. 

        :param graph: the graph object that is being built up. If one exists, the
        existing node's and its edges (connected to its parents) will be added
        to this graph. Otherwise a blank graph is initialized.
        :type graph: :class:`networkx.digraph.DiGraph`
        :param x: the x-coordinate of the root node of the subgraph currently being built
        :type x: :class:`int`
        :param y: the y-coordinate of the root node of the subgraph currently being built
        :type y: :class:`int`
        :param level: the level of the `self` node within the binary tree being built
        :type level: :class:`int`
        :param added_nodes: a set of existing nodes within the binary tree. This prevents
        repeated addition of the same node into the graph object that is being created
        :type added_nodes: :class:`set`
        :returns: generated graph object
        :rtype: :class:`networkx.digraph.DiGraph`
        """
        DG = nx.DiGraph() if graph is None else graph

        parent = self._get_graphImgNode()

        # if `self` nodes doesn't exist in the graph, create and add it
        if parent not in added_nodes:
            added_nodes.add(parent)
            new_pos = (x, y)
            DG.add_node(parent, pos=new_pos)

        # create and add node for self's parent1 node, if it exists
        if isinstance(self.parent1, Node):
            child1 = self.parent1._get_graphImgNode()
            if child1 not in added_nodes:
                added_nodes.add(child1)
                # calculate the position of the new child node, relative to the root `self`
                new_pos = (x - 2 ** (level - 1), y - 1)
                DG.add_node(child1, pos=new_pos)
            DG.add_edge(child1, parent)
            self.parent1._make_graph(graph=DG, x=(x - 2 ** (level - 1)), y=y - 1, level=level - 1, added_nodes=added_nodes)
        elif isinstance(self.parent1, self.valid_types):
            p1_str = "(const) {0:.3f}\n".format(self.parent1)
            new_node = GraphImgNode(p1_str)
            if new_node not in added_nodes:
                added_nodes.add(new_node)
                new_pos = (x - 2 ** (level - 1), y - 1)
                DG.add_node(new_node, pos=new_pos)
            DG.add_edge(new_node, parent)

        # create and add node for self's parent2 node, if it exists
        if isinstance(self.parent2, Node):
            child2 = self.parent2._get_graphImgNode()
            if child2 not in added_nodes:
                added_nodes.add(child2)
                # calculate the position of the new child node, relative to the root `self`
                new_pos = (x + 2 ** (level - 1), y - 1)
                DG.add_node(child2, pos=new_pos)
            DG.add_edge(child2, parent)
            self.parent2._make_graph(graph=DG, x=(x + 2 ** (level - 1)), y=y - 1, level=level - 1, added_nodes=added_nodes)
        elif isinstance(self.parent2, self.valid_types):
            p2_str = "(const) {0:.3f}\n".format(self.parent2)
            new_node = GraphImgNode(p2_str)
            if new_node not in added_nodes:
                added_nodes.add(new_node)
                new_pos = (x + 2 ** (level - 1), y - 1)
                DG.add_node(new_node, pos=new_pos)
            DG.add_edge(new_node, parent)

        return DG

    def graph_image(self):
        depth = self.get_graph_depth()
        comp_graph = self._make_graph(level=depth + 1)
        plt.figure(figsize=(2 ** (depth) + 6.9, depth * 2 + 2))
        plt.axis("off")
        pos=nx.get_node_attributes(comp_graph,'pos')
        nx.draw_networkx(comp_graph, pos, with_labels=True, font_size=14, node_size=1800)
        plt.savefig(f"graph{self.next_img_id}.png")
        print(f"Computational graph image saved as: graph{self.next_img_id}.png")
        self.incr_img_id()


def safe_copy_nodes(*nodes):
    """Make a copy of a node
    
    If the node is a variable, make a full copy and register itself as an independent variable. Otherwise,
    just give a reference to itself.

    :returns: copy of node
    "rtype: :class:`Node` 
    """
    def safe_copy(a_node):
        if isinstance(a_node, Node):
            if a_node.operator == Operator.VAR:
                out = copy.deepcopy(a_node)
                out.vars.add(out)
            else:
                out = a_node
        else:
            out = a_node
        
        return out

    if len(nodes) == 1:
        return safe_copy(nodes[0])
    else:
        return list(map(safe_copy, nodes))

class GraphImgNode:
    """Equivalent of :class:`Node` for visualizing the computational graph
    
    :param str: string representation of node
    :type str: :class:`str`
    :param id: id number for each node representation
    :type id: :class:`int`
    """
    next_var_id = 0 # tracks id number to give unique ids to each node representation

    def __init__(self, str):
        """Initialize instance of class with params as indicated"""
        self.str = str
        self.id = self.next_var_id
        self.incr_var_id()

    @classmethod
    def incr_var_id(cls):
        """Increments the unique id tracker"""
        cls.next_var_id += 1

    def __str__(self):
        """Returns the string representation of the node"""
        return self.str