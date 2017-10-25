import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

###################################
# plot band structure
###################################

a_cc = 1.42		#Angstrom

N = 8

x0 = a_cc*np.sqrt(3.0)/2.0;
y0 = a_cc*1.5

x = np.zeros((2*N+2))
y = np.zeros((2*N+2))

x[0:N:2] = 0;
x[1:N:2] = -x0;
x[N:2*N:2] = -x0;
x[N+1:2*N:2] = 0;

y[0:N] = (np.arange(0,N))*y0;
y[N:2*N] = (np.arange(0,N))*y0+0.5*a_cc;

x[2*N] = x[0]
y[2*N] = -a_cc
x[2*N+1] = x[2*N-1]
y[2*N+1] = np.max(y[0:2*N])+a_cc

for i in range(0,2*N+2):
	print("%1.5f  %1.5f  0.00" % (x[i],y[i]))


plt.ion() # enables interactive mode for ploting. No plt.show() is needed!
fig = plt.figure()
ax = fig.gca()

for i in range(0,2*N+2):
	ax.plot(x[i],y[i], linestyle="none", linewidth=2, marker="o", markerfacecolor="none", markeredgecolor="blue")

ax.axis('equal')

input("Press Enter to exit...")