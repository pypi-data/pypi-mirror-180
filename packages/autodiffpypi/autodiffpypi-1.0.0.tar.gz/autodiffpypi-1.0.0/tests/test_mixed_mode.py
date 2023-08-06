import pytest
from src.autodiffpypi.mixed_mode import Mixed_Mode
from src.autodiffpypi.base_derivatives import *

def test_mixed_mode():
    """
    Test suite for the Mixed_Mode class, including 
    `evaluate`, `derivative`, and `jacobian`.
    """

    def test_init():
        x = 2
        f = 8 * x
        with pytest.raises(ValueError):
            Mixed_Mode(f, 1)
            Mixed_Mode([f, f], 1)
        with pytest.raises(TypeError):
            f = lambda x: x**2
            Mixed_Mode(f, "1")
        with pytest.raises(TypeError):
            f = lambda x: x**2
            Mixed_Mode(f, 1.0)
        
    def test_forward():
        x = 2
        f = lambda x: 2 * x + x**3 - log(x)
        assert(Mixed_Mode(f, 1, 1).jacobian(x) == [2 + 3 * 2**2 - 1 / 2])

    def test_reverse():
        x = 2
        y = 3
        f1 = lambda x, y: x ** 2 + y
        f2 = lambda x, y: y**2 - x**2
        f3 = lambda x : x + 1
        test = Mixed_Mode([f1, f2, f3], 2, 50001).jacobian([x, y])
        assert(test[0][0] == 4.)
        assert(test[0][1] == 1.)
        assert(test[1][0] == -4.)
        assert(test[1][1] == 6.)
        assert(test[2][0] == 1.)
        assert(test[2][1] == 0.)
        
    test_init()
    test_forward()
    test_reverse()

if __name__ == '__main__':
    test_mixed_mode()
    print("Good job! All tests passed.")
