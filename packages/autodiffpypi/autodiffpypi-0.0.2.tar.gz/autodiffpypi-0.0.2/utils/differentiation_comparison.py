import numpy as np
import time
import sympy as sym
# from skfdiff import Model, Simulation


from src import AutoDiffPy as adp
from src.AutoDiffPy.forward_mode import Forward


x = sym.symbols('x')  # define the symbolic variable
sym.init_printing(use_unicode=True)  # for pretty terminal printing

f = x - sym.exp(-2 * sym.sin(4 * x)**2)  # our function f(x)
start_sym = time.time()
J = sym.diff(f, x)  # compute the derivative w/r/t x
end_sym = time.time()
sym_time1 = (end_sym - start_sym)

f = lambda x : x - adp.exp(-2 * adp.sin(4 * x)**2)  # our function f(x)
fwd = Forward(f, 1)
start_ad = time.time()
x = 5
J = fwd.jacobian(x)  # compute the derivative w/r/t x
end_ad = time.time()
ad_time1 = (end_ad - start_ad)

print(f"Sym time: {sym_time1}")
print(f"AD time: {ad_time1}")

x = sym.symbols('x')  # define the symbolic variable
y = sym.symbols('y')
sym.init_printing(use_unicode=True)  # for pretty terminal printing

f = x - sym.exp(-2 * sym.sin(4 * x)**2) * sym.log(y)  # our function f(x)
start_sym = time.time()
J = sym.diff(f, x, y)  # compute the derivative w/r/t x
end_sym = time.time()
sym_time2 = (end_sym - start_sym)

f = lambda x, y : x - adp.exp(-2 * adp.sin(4 * x)**2) * adp.log(y)  # our function f(x)
fwd = Forward(f, 2)
start_ad = time.time()
x = 5
y = 10
J = fwd.jacobian(x, y)  # compute the derivative w/r/t x
end_ad = time.time()
ad_time2 = (end_ad - start_ad)

x = sym.symbols('x')  # define the symbolic variable
y = sym.symbols('y')
z = sym.symbols('z')

f = x - sym.exp(-2 * sym.sin(4 * x)**2) * sym.log(y)** sym.cos(z)  # our function f(x)
start_sym = time.time()
J = sym.diff(f, x, y, z)  # compute the derivative w/r/t x
end_sym = time.time()
sym_time3 = (end_sym - start_sym)

f = lambda x, y, z : x - adp.exp(-2 * adp.sin(4 * x)**2) * adp.log(y)** adp.cos(z)  # our function f(x)
fwd = Forward(f, 3)
start_ad = time.time()
x = 5
y = 10
z = 3
J = fwd.jacobian(x, y, z)  # compute the derivative w/r/t x
end_ad = time.time()
ad_time3 = (end_ad - start_ad)



import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
SymDiff = [sym_time1, sym_time2, sym_time3]
ADDiff = [ad_time1, ad_time2, ad_time3]
 
# Set position of bar on X axis
br1 = np.arange(len(SymDiff))
br2 = [x + barWidth for x in br1]
 
# Make the plot
plt.bar(br1, SymDiff, color ='r', width = barWidth,
        edgecolor ='grey', label ='Symbolic')
plt.bar(br2, ADDiff, color ='g', width = barWidth,
        edgecolor ='grey', label ='AutoDiffPy')
 
# Adding Xticks
plt.xlabel('Number of Inputs', fontweight ='bold', fontsize = 15)
plt.ylabel('Time in Seconds', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(SymDiff))],
        ['1', '2', '3'])
plt.title('Computation Time For Computing Jacobian of Function', fontweight ='bold', fontsize = 20)
plt.legend(fontsize=20)
plt.show()



# f = lambda x: x - np.exp(-2.0 * np.sin(4.0 * x) * np.sin(4.0 * x))
# J = lambda x, eps: (
#     f(x + eps) - f(x)
# ) / eps  # Finite-Difference approximation of J