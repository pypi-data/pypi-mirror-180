#!/usr/bin/env python3
# File       : base_derivatives.py
# Description: Holds the base derivatives of functions

import numpy as np
from src.autodiffpypi.dual_number import DualNumber
from src.structures.graph import Node

_supported_types = (float, int)


# Trig functions - sin, cos, tan
def sin(input):
    """sin implementation - supports evaluation and derivative

    Args:
        input (DualNumber/Node/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/Node/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative sin(x) = cos(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (cos(x))
    """
    if isinstance(input, DualNumber):
        real = np.sin(input.real)
        dual = np.cos(input.real) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.sin(input.value), [(input, np.cos(input.value))])
    elif isinstance(input, _supported_types):
        return np.sin(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def cos(input):
    """cos implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative cos(input) = -sin(input), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (-sin(input))
    """
    if isinstance(input, DualNumber):
        real = np.cos(input.real)
        dual = -np.sin(input.real) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.cos(input.value), [(input, -np.sin(input.value))])
    elif isinstance(input, _supported_types):
        return np.cos(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def tan(input):
    """tan implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative tan(x) = 1 / cos^2(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1/cos^2(x))
    """
    if isinstance(input, DualNumber):
        real = np.tan(input.real)
        dual = (1 / (np.cos(input.real)) ** 2) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.tan(input.value), [(input, 1 / (np.cos(input.value)) ** 2)])
    elif isinstance(input, _supported_types):
        return np.tan(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


# Inverse trig functions
def arcsin(input):
    """arcsin implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        ValueError: input must be in the range -1 <= input <= 1
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative arcsin(x) = 1/√1-x² where -1 <= x <= 1, or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1/√1-x² where -1 <= x <= 1)
    """
    if isinstance(input, DualNumber):
        if not (-1 <= input.real and input.real <= 1):
            raise ValueError(f"input must be in the range -1 <= input <= 1")
        real = np.arcsin(input.real)
        dual = (1 / np.sqrt(1 - input.real**2)) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        if not (-1 <= input.value and input.value <= 1):
            raise ValueError(f"input must be in the range -1 <= x <= 1")
        return Node(np.arcsin(input.value), [(input, 1 / np.sqrt(1 - input.value**2)) ])
    elif isinstance(input, _supported_types):
        if not (-1 <= input.real and input.real <= 1):
            raise ValueError(f"input must be in the range -1 <= x <= 1")
        return np.arcsin(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def arccos(input):
    """arccos implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        ValueError: input must be in the range -1 <= input <= 1
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative arcsos(x) = -1/√(1-x^2) where -1 < x < 1, or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (-1/√(1-x^2) where -1 < x < 1)
    """
    if isinstance(input, DualNumber):
        if not (-1 <= input.real and input.real <= 1):
            raise ValueError(f"input must be in the range -1 <= input <= 1")
        real = np.arccos(input.real)
        dual = (-1 / np.sqrt(1 - input.real**2)) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        if not (-1 <= input.value and input.value <= 1):
            raise ValueError(f"input must be in the range -1 <= input <= 1")
        return Node(np.arccos(input.value), [(input, -1 / np.sqrt(1 - input.value**2))])
    elif isinstance(input, _supported_types):
        if not (-1 <= input.real and input.real <= 1):
            raise ValueError(f"input must be in the range -1 <= input <= 1")
        return np.arccos(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def arctan(input):
    """arctan implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative arctan(x) = 1/(1+x^2), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1/(1+x^2))
    """
    if isinstance(input, DualNumber):
        real = np.arctan(input.real)
        dual = (1 / (1 + input.real**2)) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.arctan(input.value), [(input, 1 / (1 + input.value**2))])
    elif isinstance(input, _supported_types):
        return np.arctan(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def exp(input):
    """exp implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative exp(x) = exp(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (exp(x))
    """
    if isinstance(input, DualNumber):
        real = np.exp(input.real)
        dual = np.exp(input.real) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.exp(input.value), [(input, np.exp(input.value))])
    elif isinstance(input, _supported_types):
        return np.exp(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


# Hyperbolic functions
def sinh(input):
    """sinh implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative sinh(x) = cosh(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (cosh(x))
    """
    if isinstance(input, DualNumber):
        real = np.sinh(input.real)
        dual = np.cosh(input.real) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.sinh(input.value), [(input, np.cosh(input.value))])
    elif isinstance(input, _supported_types):
        return np.sinh(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def cosh(input):
    """cosh implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative cosh(x) = sinh(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (sinh(x))
    """
    if isinstance(input, DualNumber):
        real = np.cosh(input.real)
        dual = np.sinh(input.real) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.cosh(input.value), [(input, np.sinh(input.value))])
    elif isinstance(input, _supported_types):
        return np.cosh(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def tanh(input):
    """tanh implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative tanh(x) = 1 - tanh^2(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1 - tanh^2(x))
    """
    if isinstance(input, DualNumber):
        real = np.tanh(input.real)
        dual = (1 - (np.tanh(input.real))**2) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.tanh(input.value), [(input, 1 - (np.tanh(input.value))**2)])
    elif isinstance(input, _supported_types):
        return np.tanh(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def sqrt(input):
    """sqrt implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative sqrt(x) = 1 / 2*sqrt(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1 / 2*sqrt(x))
    """
    if isinstance(input, DualNumber):
        real = np.sqrt(input.real)
        dual = (1 / (2 * np.sqrt(input.real))) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.sqrt(input.value), [(input, 1 / (2 * np.sqrt(input.value)))])
    elif isinstance(input, _supported_types):
        return np.sqrt(input)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def pow(input, exp):
    """pow implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated
        exp (int): Exponent - must be a positive integer

    Raises:
        ValueError: a must be a positive integer
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative pow(x, exp) = exp * x**(exp-1), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (exp * x**(exp-1))
    """
    if not isinstance(exp, int) and exp > 0:
        raise ValueError(f"Exponent must be a positive integer")
    if isinstance(input, DualNumber):
        real = input.real ** exp
        dual = (exp * input.real**(exp-1)) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(input.value ** exp, [(input, exp * input.value**(exp-1))])
    elif isinstance(input, _supported_types):
        return input ** exp
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def log(input, base=np.e):
    """log implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated
        base (int/float, optional): base of the log. Defaults to np.e.

    Raises:
        ValueError: base provided base must be a positive integer/float
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative log(x, base) = 1 / (x * np.log(base)), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1 / (x * np.log(base))
    """
    # type checking for base
    if not (isinstance(base, _supported_types) and base > 0):
        raise ValueError(f"Provided base must be a positive integer/float")

    # derivative of log_a(x) = 1/x*ln(a)
    # default to base e (natural log) if no base provided
    if isinstance(input, DualNumber):
        real = np.log(input.real) / np.log(base)
        dual = (1 / (input.real * np.log(base))) * input.dual
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        return Node(np.log(input.value) / np.log(base), [(input, 1 / (input.value * np.log(base)))])
    elif isinstance(input, _supported_types):
        return np.log(input) / np.log(base)
    else:
        raise TypeError(f"Type error: `{type(input)}`")


def sigmoid(input):
    """sigmoid implementation - supports evaluation and derivative

    Args:
        input (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: input must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation sigmoid(x) = 1 / (1 + np.exp(-x))
        and derivative sigmoid(x) = (sigmoid(x) * (1 - sigmoid(x))), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (sigmoid(x) * (1 - sigmoid(x)))
    """
    if isinstance(input, DualNumber):
        real = 1 / (1 + np.exp(-input.real))
        dual = input.dual * real * (1-real)
        return DualNumber(real, dual)
    elif isinstance(input, Node):
        node_val = 1 / (1 + np.exp(-input.value))
        return Node(node_val, [ (input, node_val * (1 - node_val)) ])
    elif isinstance(input, _supported_types):
        return 1 / (1 + np.exp(-input))
    else:
        raise TypeError(f"Type error: `{type(input)}`")
