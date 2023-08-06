#!/usr/bin/env python3
# File       : newton.py
# Description: Computes Roots with an AD computed Jacobian
# from src import AutoDiffPy as adp
import src.autodiffpypi as adp
import numpy as np


def newton(function, init_guesses, max_iterations=200, tol=1.0e-8):
    """ Newton's Method

    Args:
        function (lambda function) : the function we are looking for roots for
        x_k (int/float): the initial guess
        max_iterations (int, optional): Number of iterations of Newton's. Defaults to 200.
        tol (_type_, optional): Accuracy level representated by tolerance. Defaults to 1.0e-8.

    Returns:
        Float: Newton's approximation of the root based on the initial guess and iterations.

    Example:
        >>> function = lambda x : x - adp.exp(-2.0 * adp.sin(4.0 * x) * adp.sin(4.0 * x))
        >>> init_guess = [0.1]
        >>> print(newton(function, init_guess, 10000))
        [.2473481]      
    """
    # If guess is 0 it will not converge
    if 0 in init_guesses:
        raise TypeError("Guess cannot be of value 0")

    num_vars = len(init_guesses)

    # Check for dimension match
    if (isinstance(function, list)):
        if (len(function) != num_vars):
            raise ValueError("Dimensions must match for Newtons")
    
    fwd = adp.Forward(function, num_vars)
    flag = False
    x_k = init_guesses

    for k in range(max_iterations):
        # Compute function at current guess
        fun = fwd.evaluate(x_k)

        # Run function through forward mode
        Jacobian = fwd.jacobian(x_k)
        fun = -fun

        # Calculate derivative
        if num_vars == 1:
            der_xk = (fun / Jacobian)[0]
        else: 
            der_xk = np.linalg.solve(Jacobian, fun).tolist()
            # Return to list form
            der_xk = [x[0] for x in der_xk]
        
        # Add derivative
        x_k = [x_k[i] + der_xk[i] for i in range(num_vars)]

        # Check if below tolerance
        tol_check = max([abs(x) for x in der_xk])
        if tol_check < tol:
            print(f"Root approximated at {[var for var in x_k]} from iteration {k+1}")
            flag = True
            break
    
    if not flag:
        print(f"No root found after {max_iterations} iterations.")
    
    return x_k
