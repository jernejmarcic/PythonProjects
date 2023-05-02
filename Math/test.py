from matplotlib.figure import projections
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

age15 = np.array([
    (6, 7, 7), # Time spent sleeping 
    (2, 3, 3), # Time spent studying
    (6, 7, 5), # Avg grade
])  

age16 = np.array([
    (7, 6, 6, 7, 6, 8, 7), # Time spent sleeping
    (4, 4, 1, 2, 1, 2, 6), # Time spent studying
    (5, 6, 6, 4, 6, 5, 7), # Avg grade
])  

age17 = np.array([
    (7, 8), # Time spent sleeping
    (3, 0.5), # Time spent studying
    (7, 6.7), # Avg grade
])  

age18 = np.array([
    (7, 7), # Time spent sleeping
    (4, 4), # Time spent 
    (6, 6), # Avg grade
])  

ks15 = []
for i in range(3):
    k15 = np.mean(age15[i, :])
    ks15.append(k15) 
avg15 = np.array(ks15)

ks16 = []
for i in range(3):
    k16 = np.mean(age16[i, :])
    ks16.append(k16)
avg16 = np.array(ks16)

ks17 = []
for i in range(3):
    k17 = np.mean(age17[i, :]) 
    ks17.append(k17)
avg17 = np.array(ks17)

ks18 = []
for i in range(3):
    k18 = np.mean(age18[i, :])
    ks18.append(k18)
avg18 = np.array(ks18)

allavg = (avg15 + avg16 + avg17 + avg18) / 4

avg = np.array([6, 3, 6])  # replace with the actual values of the average for all ages


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot data points for each age group
ax.scatter(*age15, c='b', marker='o')
ax.scatter(*age16, c='g', marker='o')
ax.scatter(*age17, c='r', marker='o')
ax.scatter(*age18, c='y', marker='o')

# Plot the average of each age group
ax.scatter(avg15[0], avg15[1], avg15[2], c='b', marker='x')
ax.scatter(avg16[0], avg16[1], avg16[2], c='g', marker='x')
ax.scatter(avg17[0], avg17[1], avg17[2], c='r', marker='x')
ax.scatter(avg18[0], avg18[1], avg18[2], c='y', marker='x')

# Plot a black diamond to represent the average of all averages
ax.scatter(*allavg, c='k', marker='D')

# Plot vectors from each age average to the overall average
avg_vecs = np.array([allavg - avg for avg in [avg15, avg16, avg17, avg18]])
for avg_vec, avg_color in zip(avg_vecs, ['b', 'g', 'r', 'y']):
    ax.quiver(*avg, *avg_vec, length=1, color=avg_color)

# Calculate the distance from each age average

