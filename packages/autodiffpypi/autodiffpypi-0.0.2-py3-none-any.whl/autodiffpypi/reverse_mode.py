#!/usr/bin/env python3
# File       : reverse_mode.py
# Description: Computes Reverse-mode AD

import numpy as np
from src.autodiffpypi.base_derivatives import *
from src.structures.graph import Node

class Reverse():

    # def __init__(self, fn, nodes):
    def __init__(self, fn, num_inputs):
        """ Initialize Reverse mode class

        Params:
            self: Reverse
            fn: array, function: () -> Node
            num_inputs: number of inputs
        """
        self.fn = np.array(fn) if isinstance(fn, list) else np.array([fn])
        self.num_inputs = num_inputs
    
    def build_nodes(self, inputs):
        """ Helper function to build node variables
        Params:
            self: Reverse
            inputs: List of integers

        Returns:
            value: List of nodes

        >>> x = 2
        >>> y = 5
        >>> def f1(x, y):
        >>>     return x ** y
        >>> def f2(x, y):
        >>>     return x + y
        >>> reverse_ex = Reverse([f1, f2], 2)
        >>> value = reverse_ex.build_nodes()
        >>> print(value)
        [Node(2), Node(5)]
        """
        if len(inputs) != self.num_inputs:
            raise IndexError

        # build nodes out of input variables
        node_list = []
        for var in inputs:
            node_list.append(Node(var))
        
        return node_list

    def evaluate(self, inputs):
        """ Evaluate input functions
        Params:
            self: Reverse
            inputs: List of integers

        Returns:
            value: List of integers

        Example:
        >>> x = 2
        >>> y = 5
        >>> def f1(x, y):
        >>>     return x ** y
        >>> def f2(x, y):
        >>>     return x + y
        >>> reverse_ex = Reverse([f1, f2], 1)
        >>> value = reverse_ex.evaluate([x, y])
        >>> print(value)
        [32, 7]
        """
        # build nodes out of input variables
        node_list = self.build_nodes(inputs)

        # evaluate all functions at those variables
        res_arr = []
        for func in self.fn:
            res_arr.append(func(*node_list).value)

        return res_arr

    def derivative(self, inputs, index = None):
        """ Compute derivative
        Params:
            self: Reverse
            inputs: List of integers
            index: Integer

        Returns:
            derivative: List of integers

        Example:
        >>> x = 2
        >>> y = 5
        >>> def f1(x, y):
        >>>     return x ** y
        >>> def f2(x, y):
        >>>     return x + y
        >>> reverse_ex = Reverse([f1, f2], 1)
        >>> value = reverse_ex.derivative([x, y], 1)
        >>> print(value)
        [32log(2), 1]
        """
        if isinstance(inputs, (float, int)):
            inputs = [inputs]

        if len(inputs) != self.num_inputs:
            raise ValueError("Number of input variables must match function definition")

        if index is not None and not isinstance(index, int):
            raise TypeError("Index must be an int")

        # default to derivative of x if no index provided
        if len(inputs) == 1 or index is None:
            index = 0

        # return specified column(s) of jacobian
        if len(self.fn) > 1:
            lst = self.jacobian(inputs)[:, index]
            return np.array([[elt] for elt in lst])
        else:
            return self.jacobian(inputs)[0][index]


    def jacobian(self, inputs):
        """ Compute jacobian matrix of derivatives
        Params:
            self: Reverse

        Returns:
            jacobian: List of ints

        Example:
        >>> x = 2
        >>> y = 3
        >>> def f1(x, y):
        >>>     return x ** y
        >>> def f2(x, y):
        >>>     return x + y
        >>> reverse_ex = Reverse([f1, f2], 1)
        >>> value = reverse_ex.jacobian([x, y])
        >>> print(value)
        [ [12, 8log(2)], [1, 1] ]
        """
        # build nodes out of input variables
        node_list = self.build_nodes(inputs)

        m  = []
        for func in self.fn:
            m.append([func(*node_list).get_gradients()[node] for node in node_list])
        return np.array(m)
