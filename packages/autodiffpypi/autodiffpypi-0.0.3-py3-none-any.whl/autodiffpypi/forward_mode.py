#!/usr/bin/env python3
# File       : reverse_mode.py
# Description: Computes Forward-mode AD

import numpy as np
from inspect import signature
from src.autodiffpypi.base_derivatives import *
from src.autodiffpypi.dual_number import *

class Forward():
    def __init__(self, function_list, num_of_inputs):
        """ Initialize Forward mode class

        Params:
            self: Forward
            function_list: array, function
            num_of_inputs: int
        """
        if isinstance(function_list, list):
            if len(function_list) == 0:
                raise ValueError("Input to Forward class should be a function or a non-empty list of functions")
            for elt in function_list:
                if not callable(elt):
                    raise ValueError("Input to Forward class should be a function or a non-empty list of functions")
            self.function_list = np.array(function_list)
        elif callable(function_list):
            self.function_list = np.array([function_list])
        else:
            raise ValueError("Input to Forward class should be a function or a non-empty list of functions")
        if not isinstance(num_of_inputs, int):
            raise TypeError("Input to Forward class num_of_inputs should be an int")
        
        self.num_of_inputs = num_of_inputs


    def evaluate(self, inputs):
        """ Evaluate the given functions
        Params:
            self: Forward
            inputs: list of (int/float) / np.array of (int/float) / int / float

        Returns:
            value: int / float or np.array of ints / floats

        Example:
        >>> x = 2
        >>> f1 = lambda x: x ** 2
        >>> Forward(f1, 1).evaluate(x)
        4
        """
        # Type checking
        if isinstance(inputs, int) or isinstance(inputs, float):
            inputs = [inputs]
        elif isinstance(inputs, np.ndarray):
            inputs = np.ndarray.tolist(inputs)
        elif not isinstance(inputs, list) and not isinstance(inputs, np.ndarray):
            raise TypeError("input into evaluate must be int/float/list/np array of ints/floats")

        # Check if the number of inputs match
        if len(inputs) != self.num_of_inputs:
            raise ValueError("Number of input variables must match function definition")

        # Convert to dual numbers
        duals = [DualNumber(input) for input in inputs]

        # Multiple functions
        if len(self.function_list) > 1:
            res = []
            for fun in self.function_list:
                fun_params = len(signature(fun).parameters)
                if len(duals) > fun_params:
                    # Address edge case where not all functions take the same number of inputs
                    res.append(np.array([fun(*duals[0:fun_params]).real]))
                else:
                    res.append(np.array([fun(*duals).real]))
            return np.array(res)
        # Single function
        else:
            return self.function_list[0](*duals).real


    def derivative(self, inputs, index = None):
        """ Compute derivative
        Params:
            self: Forward
            inputs: list of (int/float) / np.array of (int/float) / int / float
            index: int, Optional

        Returns:
            derivative: np.array of floats / float

        Example:
        >>> x = 1
        >>> f1 = lambda x: x ** 2
        >>> Forward(f1, 1).derivative(x)
        2
        """
        # Type checking
        if isinstance(inputs, int) or isinstance(inputs, float):
            inputs = [inputs]
        elif isinstance(inputs, np.ndarray):
            inputs = np.ndarray.tolist(inputs)
        elif not isinstance(inputs, list) and not isinstance(inputs, np.ndarray):
            raise TypeError("input into derivative must be int/float/list/np array of ints/floats")

        # Check if the number of inputs match
        if len(inputs) != self.num_of_inputs:
            raise ValueError("Number of input variables must match function definition")

        # Check that index is an int or None
        if index is not None and not isinstance(index, int):
            raise TypeError("Index must be an int")

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
            self: Forward
            inputs: list of (int/float) / numpy array of (int/float) / int / float

        Returns:
            jacobian: np.array

        Example:
        >>> x = DualNumber(2,1)
        >>> f = lambda x : x ** 2
        >>> Forward(f, 1).jacobian()
        [4.0]
        """
        # Type checking
        if isinstance(inputs, int) or isinstance(inputs, float):
            inputs = [inputs]
        elif isinstance(inputs, np.ndarray):
            inputs = np.ndarray.tolist(inputs)
        elif not isinstance(inputs, list) and not isinstance(inputs, np.ndarray):
            raise TypeError("input into Jacobian must be int/float/list/np array of ints/floats")

        # Check if the number of inputs match
        if len(inputs) != self.num_of_inputs:
            raise ValueError("Number of input variables must match function definition")

        duals_list = []
        # Convert to dual
        for ind in range(len(inputs)):
            lst = [DualNumber(x, 0.0) for x in inputs]
            lst[ind].dual = 1.0
            duals_list.append(lst)
        
        # Per function, we want to have a numpy list
        res = []
        for fun in self.function_list:
            arr = []
            for duals in duals_list:
                fun_params = len(signature(fun).parameters)
                if len(duals) > fun_params:
                    arr.append(fun(*duals[0:fun_params]).dual)
                else:
                    arr.append(fun(*duals).dual)
            res.append(np.array(arr))
        return np.array(res)
