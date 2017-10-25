import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

###################################
# plot band structure
###################################

a_cc = 1.42		#Angstrom

N = 14

x0 = 1.5
y0 = np.sqrt(3.0)/2.0;
x = np.zeros((2*N))
# x[1,]

print(x)

# x (2:2:N) = x0;
# x (N+1:2:2*N) = 1;
# x (N+2:2:2*N) = 1-x0;

# y (1:N) = ((1:N)-1)*y0;
# y (N+1:2*N) = ((1:N)-1)*y0;
# x = x*1.42;
# y = y*1.42;
# z = zeros(size(x))

input("Press Enter to exit...")