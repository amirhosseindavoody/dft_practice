import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns

###################################
# plot band structure
###################################


filename = "./16_zgnr/band_structure_spin_up.dat"

count =0
nk = 0
arr = []
with open(filename) as fp:
	for line in fp:
		if (count % 11 == 0):
			arr.append([])
			nk += 1
		else:
			arr[nk-1] += [float(x) for x in line.split()]
		count += 1 

data_up = np.transpose(arr)

# filename = "./16_zgnr/band_structure_spin_down.dat"

# count =0
# nk = 0
# arr = []
# with open(filename) as fp:
# 	for line in fp:
# 		if (count % 6 == 0):
# 			arr.append([])
# 			nk += 1
# 		else:
# 			arr[nk-1] += [float(x) for x in line.split()]
# 		count += 1 

# data_down = np.transpose(arr)

sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 1.5})
plt.ion()
fig = plt.figure()
ax = fig.gca()
for i in range(0,data_up.shape[0]):
	ax.plot(data_up[i,:],color="red")
	# ax.plot(data_down[i,:],color = "blue")


####################################
# plot atom positions
####################################

# plt.ion() # enables interactive mode for ploting. No plt.show() is needed!
# fig = plt.figure()
# ax = fig.gca()

# filename = "./16_zgnr/ionmov.pos"
# data = np.loadtxt(filename)
# for i in range(1,17):
# 	ax.plot(data[i,2],data[i,1], linestyle="none", linewidth=2, marker="o", markerfacecolor="none", markeredgecolor="blue")

# filename = "./16_zgnr/atom.pos"
# data = np.loadtxt(filename)
# for i in range(1,17):
# 	ax.plot(data[i,0],data[i,1], linestyle="none", linewidth=2, marker="o", markerfacecolor="none", markeredgecolor="red")

# ax.axis('equal')

input("Press Enter to exit...")