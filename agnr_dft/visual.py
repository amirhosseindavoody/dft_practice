import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.ion() # enables interactive mode for ploting. No plt.show() is needed!

filename = "band.dat"

count =0
nk = 0
arr = []
with open(filename) as fp:
	for line in fp:
		if (count % 6 == 0):
			arr.append([])
			nk += 1
		else:
			arr[nk-1] += [float(x) for x in line.split()]
		count += 1 

data = np.transpose(arr)

fig = plt.figure()
ax = fig.gca()
for i in range(0,data.shape[0]):
	ax.plot(data[i,:], linestyle="solid", linewidth=2, marker="")

input("Press Enter to exit...")