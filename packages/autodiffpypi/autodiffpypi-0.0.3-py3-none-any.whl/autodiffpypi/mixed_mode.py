#!/usr/bin/env python3
# File       : mixed_mode.py
# Description: Computes Mixed-mode AD

from src.autodiffpypi.base_derivatives import *
from src.autodiffpypi.forward_mode import Forward
from src.autodiffpypi.reverse_mode import Reverse


class Mixed_Mode(Forward, Reverse):

    def __init__(self, function_list, num_of_inputs, threshold = 50000):
        """ Initialize Mixed mode class
        Params:
            self: Mixed_Mode
            function_list: array, function: ()
            num_inputs: number of inputs
            threshold: number of inputs at which reverse mode is used instead of forward mode
        """
        self.function_list = function_list
        self.num_of_inputs = num_of_inputs
        self.threshold = threshold

        # fewer inputs --> use forward mode
        if(num_of_inputs < threshold):
            Forward.__init__(self, function_list, num_of_inputs)

        # more inputs --> use reverse mode
        else:
            Reverse.__init__(self, function_list, num_of_inputs) 