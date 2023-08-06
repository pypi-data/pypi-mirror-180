import pytest
import numpy as np
from src.autodiffpypi.forward_mode import Forward
from src.autodiffpypi.reverse_mode import Reverse
from src.autodiffpypi.base_derivatives import *
from src.autodiffpypi.reverse_mode import *
from src.autodiffpypi.forward_mode import *


def test_compare_forward_reverse():
    def multi_function():
        x = 2
        y = 4

        def f1(x, y): return x ** 2 + y
        def f2(x, y): return log(y) - x / y

        der_x_rev = np.round(Reverse([f1, f2], 2).derivative([x,y], 0), 2)
        der_y_rev = np.round(Reverse([f1, f2], 2).derivative([x,y], 1), 2)

        der_x = np.round(Forward([f1, f2], 2).derivative([x,y], 0), 2)
        der_y = np.round(Forward([f1, f2], 2).derivative([x,y], 1), 2)

        jrev = np.round(Reverse([f1, f2], 2).jacobian([x, y]), 2)
        jfor = np.round(Forward([f1, f2], 2).jacobian([x, y]), 2)

        assert(der_x.all() == der_x_rev.all())
        assert(der_y.all() == der_y_rev.all())
        assert(jrev.all() == jfor.all())

    def complex_function():
        x = np.sin(0.5)
        y = 138202
        z = 4.01
        f = lambda x, y, z: log(y - z) ** 2 + sigmoid(z) - 3 * x
        
        jrev = np.round(Reverse(f, 3).jacobian([x, y, z]), 2)
        jfor = np.round(Forward(f, 3).jacobian([x, y, z]), 2)

        assert(jrev.all() == jfor.all())

    multi_function()
    complex_function()

test_compare_forward_reverse()