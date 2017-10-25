import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns

###################################
# plot band structure
###################################


filename = "./28_agnr/band_structure.dat"

count =0
nk = 0
arr = []
with open(filename) as fp:
	for line in fp:
		if (count % 10 == 0):
			arr.append([])
			nk += 1
		else:
			arr[nk-1] += [float(x) for x in line.split()]
		count += 1 

data = np.transpose(arr)

# sns.set_style("darkgrid")
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
plt.ion() # enables interactive mode for ploting. No plt.show() is needed!
fig = plt.figure()
ax = fig.gca()
for i in range(0,data.shape[0]):
	ax.plot(data[i,:])

# for i in range(0,data.shape[0]):
# 	sns.lmplot(np.arange(0,data.shape[1]),data[i,:])


####################################
# plot atom positions
####################################

# plt.ion() # enables interactive mode for ploting. No plt.show() is needed!
# fig = plt.figure()
# ax = fig.gca()

# # # filename = "./28_agnr/ionmov.pos"
# # # data = np.loadtxt(filename)
# # # for i in range(0,data.shape[0]):
# # # 	ax.plot(data[i,0],data[i,1], linestyle="none", linewidth=2, marker="o", markerfacecolor="none", markeredgecolor="blue")

# filename = "./16_agnr_hydrogen_terminated/atom.pos"
# data = np.loadtxt(filename)
# data = data * 0.5291772108
# for i in range(0,data.shape[0]):
# 	ax.plot(data[i,0],data[i,1], linestyle="none", linewidth=2, marker="o", markerfacecolor="none", markeredgecolor="blue")

# ax.axis('equal')

# # filename = "./28_agnr/optcell.pos"
# # data = np.loadtxt(filename)
# # for i in range(0,data.shape[0]):
# # 	ax.plot(data[i,0],data[i,1], linestyle="none", linewidth=2, marker="o", markerfacecolor="none", markeredgecolor="red")

input("Press Enter to exit...")