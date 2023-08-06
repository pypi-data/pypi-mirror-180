#!/usr/bin/env python3
# File       : find_threshold.py
# Description: Computes Reverse AD

import time
from src.autodiffpypi.base_derivatives import *
from src.autodiffpypi.forward_mode import Forward
from src.autodiffpypi.reverse_mode import Reverse

def find_threshold():
    """
    Returns the amount of nodes at which Reverse mode is faster than Forward mode
    """

    # example function
    def f1(*args):
        val = sum([val for val in args])
        return val * val

    # example arguements
    x, y, a, b, c, d, e, f = 9.23462362, 7.34534562345, 7.1346265427, 24564373456234564357345724572457, \
        3524285839092.20934562494512345, 83794562.89124235, 1234892552346.572894762, 3
    args = [x, y, a, b, c, d, e, f]


    while (True): 
        rev_mode = Reverse(f1, len(args))
        for_mode = Forward(f1, len(args))

        # reverse mode
        start_rev = time.time()
        rev_res = rev_mode.jacobian(*args)
        end_rev = time.time()
        rev_time = (end_rev - start_rev)
        
        # forward mode
        start_for = time.time()
        for_res = for_mode.jacobian(*args)
        end_for = time.time()
        for_time = end_for - start_for

        # check time, see if reverse mode outperforms forward mode
        if rev_time > for_time:
            args.extend(args)
        else:
            print(len(args))
            break
    
if __name__ == '__main__':
    find_threshold()