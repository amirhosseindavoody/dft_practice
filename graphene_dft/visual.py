import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.ion() # enables interactive mode for ploting. No plt.show() is needed!


directory = "/home/amirhossein/Desktop/graphene_dft/"+"graphene_band_structure.dat"

count =0
arr = []
with open(directory) as fp:
	for line in fp:
		count += 1 
		if (count > 2) and (count % 2 == 1):
			arr.append([float(x) for x in line.split()])

data = np.transpose(arr)

# data = np.loadtxt(directory+"graphene_band_structure.dat", skiprows=0)
# wave_vec = data[:,0]
# energy = np.transpose(data[:,1:])


fig = plt.figure()
ax = fig.gca()
for i in range(0,data.shape[0]):
	ax.plot(data[i,:], linestyle="solid", linewidth=2, marker="")

# Nu = int(energy.shape[0]/2)
# bands = Nu+np.arange(-3,3)
# fig = plt.figure()
# ax = fig.gca()
# for i in bands:
# 	ax.plot(wave_vec,energy[i,:], linestyle="solid", linewidth=2, marker="")

# fig.tight_layout()
# ax.set_ylim([-1, 1])

# fig = plt.figure()
# ax = fig.gca()
# energy = np.loadtxt(directory+"cnt1.pi.dat", skiprows=0)
# for i in range(1,energy.shape[1]):
# 	ax.plot(energy[:,0],energy[:,i], linestyle="solid", linewidth=2, marker="")

# fig = plt.figure()
# ax = fig.gca()
# energy = np.loadtxt(directory+"cnt1.vq.dat", skiprows=0)
# for i in range(1,energy.shape[1]):
# 	ax.plot(energy[:,0],energy[:,i], linestyle="solid", linewidth=2, marker="")

# plt.yscale('log')


# fig = plt.figure()
# ax = fig.gca()

# directory = "/home/amirhossein/research/test/"

# psi = np.loadtxt(directory+"cnt1.electron_psi.dat", skiprows=0)
# for i in range(1,psi.shape[1]):
# 	ax.cla();
# 	ax.plot(psi[:,0],psi[:,i], linestyle="solid", linewidth=2, marker="")
# 	# input()

input("Press Enter to exit...")