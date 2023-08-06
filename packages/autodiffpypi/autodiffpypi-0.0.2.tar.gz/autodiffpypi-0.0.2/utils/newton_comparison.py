import numpy as np
from src import AutoDiffPy as adp
from src.AutoDiffPy.forward_mode import Forward
from applications.newtons import newton


# Finite diff
f = lambda x: x - np.exp(-2.0 * np.sin(4.0 * x) * np.sin(4.0 * x))
J = lambda x, eps: (
    f(x + eps) - f(x)
) / eps  # Finite-Difference approximation of J


def fd_newton(f, J, x_k, tol=1.0e-8, max_it=100, eps=1.0e-8):
    root = None
    for k in range(max_it):
        dx_k = -f(x_k) / J(x_k, eps)
        if abs(dx_k) < tol:
            root = x_k + dx_k
            print(f"Found root {root:e} at iteration {k+1}")
            print(f(root))
            break
        print(f"Iteration {k+1}: Delta x = {dx_k:e}")
        x_k += dx_k
    return root


fd_new = fd_newton(f, J, 100, max_it=10000)

# AD newton

init_guess = 100
f = lambda x : x - adp.exp(-2.0 * adp.sin(4.0 * x) * adp.sin(4.0 * x))
AD_new = newton.newton(f, init_guess, 100000)

print(f"Finite diff: {fd_new}")
print(f"AD: {AD_new}")
print("True: 2.473481e-01")