import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.ion() # enables interactive mode for ploting. No plt.show() is needed!


directory = "./"+"band_structure.dat"

count =0
arr1 = []
arr2 = []
with open(directory) as fp:
	for line in fp:

		if (count % 3 == 1):
			arr1.append([float(x) for x in line.split()])
		if (count % 3 == 2):
			arr2.append([float(x) for x in line.split()])

		count += 1 
data1 = np.transpose(arr1)
data2 = np.transpose(arr2)

fig = plt.figure()
ax = fig.gca()
for i in range(0,data1.shape[0]):
	ax.plot(data1[i,:], linestyle="solid", linewidth=2, marker="")
for i in range(0,data2.shape[0]):
	ax.plot(data2[i,:], linestyle="solid", linewidth=2, marker="")

input("Press Enter to exit...")