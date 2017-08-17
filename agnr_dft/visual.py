import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.ion() # enables interactive mode for ploting. No plt.show() is needed!


# directory = "./"+"spin_up_band.dat"
filename = "band.dat"

count =0
arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []
arr8 = []
with open(filename) as fp:
	for line in fp:

		if (count % 6 == 1):
			arr1.append([float(x) for x in line.split()])
		if (count % 6 == 2):
			arr2.append([float(x) for x in line.split()])
		if (count % 6 == 3):
			arr3.append([float(x) for x in line.split()])
		if (count % 6 == 4):
			arr4.append([float(x) for x in line.split()])
		if (count % 6 == 5):
			arr5.append([float(x) for x in line.split()])
		# if (count % 6 == 6):
		# 	arr6.append([float(x) for x in line.split()])
		# if (count % 9 == 7):
		# 	arr7.append([float(x) for x in line.split()])
		# if (count % 9 == 8):
		# 	arr8.append([float(x) for x in line.split()])

		count += 1 

data1 = np.transpose(arr1)
data2 = np.transpose(arr2)
data3 = np.transpose(arr3)
data4 = np.transpose(arr4)
data5 = np.transpose(arr5)
data6 = np.transpose(arr6)
data7 = np.transpose(arr7)
data8 = np.transpose(arr8)


fig = plt.figure()
ax = fig.gca()
for i in range(0,data1.shape[0]):
	ax.plot(data1[i,:], linestyle="solid", linewidth=2, marker="")
for i in range(0,data2.shape[0]):
	ax.plot(data2[i,:], linestyle="solid", linewidth=2, marker="")
for i in range(0,data3.shape[0]):
	ax.plot(data3[i,:], linestyle="solid", linewidth=2, marker="")
for i in range(0,data4.shape[0]):
	ax.plot(data4[i,:], linestyle="solid", linewidth=2, marker="")
for i in range(0,data5.shape[0]):
	ax.plot(data5[i,:], linestyle="solid", linewidth=2, marker="")
# for i in range(0,data6.shape[0]):
# 	ax.plot(data6[i,:], linestyle="solid", linewidth=2, marker="")
# for i in range(0,data7.shape[0]):
# 	ax.plot(data7[i,:], linestyle="solid", linewidth=2, marker="")
# for i in range(0,data8.shape[0]):
# 	ax.plot(data8[i,:], linestyle="solid", linewidth=2, marker="")


# directory = "./"+"spin_down_band.dat"

# count =0
# arr1 = []
# arr2 = []
# with open(directory) as fp:
# 	for line in fp:

# 		if (count % 3 == 1):
# 			arr1.append([float(x) for x in line.split()])
# 		if (count % 3 == 2):
# 			arr2.append([float(x) for x in line.split()])

# 		count += 1 
# data1 = np.transpose(arr1)
# data2 = np.transpose(arr2)

# # fig = plt.figure()
# # ax = fig.gca()
# for i in range(0,data1.shape[0]):
# 	ax.plot(data1[i,:], linestyle="solid", linewidth=2, marker="")
# for i in range(0,data2.shape[0]):
# 	ax.plot(data2[i,:], linestyle="solid", linewidth=2, marker="")

input("Press Enter to exit...")