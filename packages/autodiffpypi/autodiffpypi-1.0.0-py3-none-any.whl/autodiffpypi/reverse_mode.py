#!/usr/bin/env python3
# File       : reverse_mode.py
# Description: Computes Reverse-mode AD

import numpy as np
from inspect import signature
from src.autodiffpypi.base_derivatives import *
from src.structures.graph import Node

class Reverse():

    def __init__(self, function_list, num_of_inputs):
        """ Initialize Reverse mode class

        Params:
            self: Reverse
            function_list: array, function
            num_of_inputs: int, number of inputs
        """
        self.function_list = np.array(function_list) if isinstance(function_list, list) else np.array([function_list])
        self.num_of_inputs = num_of_inputs
    
    def build_nodes(self, inputs):
        """ Helper function to build nodes from inputs
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
        # type checking
        if len(inputs) != self.num_of_inputs:
            raise IndexError

        # build nodes out of input variables        
        return [Node(var) for var in inputs]

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
        node_list = self.build_nodes(inputs)

        # Multiple functions
        if len(self.function_list) > 1:
            res = []
            for func in self.function_list:
                fun_params = len(signature(func).parameters)
                if len(node_list) > fun_params:
                    # Address edge case where not all functions take the same number of inputs
                    res.append(np.array([func(*node_list[0:fun_params]).value]))
                else:
                    res.append(np.array([func(*node_list).value]))
            return np.array(res)

        # evaluate all functions at those variables
        return [func(*node_list).value for func in self.function_list]

    def derivative(self, inputs, index = None):
        """ Compute derivative with respect to input at specified index.
        If not index is specified and the function is only of one variable,
        it will return the derivative with respect to that variable.

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

        # type checking
        if isinstance(inputs, (float, int)):
            inputs = [inputs]
        if len(inputs) != self.num_of_inputs:
            raise ValueError("Number of input variables must match function definition")
        if index is not None and not isinstance(index, int):
            raise TypeError("Index must be an int")

        # default to derivative of first variable if no index provided
        if len(inputs) == 1 or index is None:
            index = 0

        if len(self.function_list) > 1:
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
        node_list = self.build_nodes(inputs)

        # build jacobian matrix
        jac = [[func(*node_list).get_gradients()[node] for node in node_list] for  func in self.function_list]
        return np.array(jac)