from matplotlib.figure import projections
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import panda as pd

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

unknownage = np.array([
    (6, 5), # Time spent sleeping 
    (1, 5), # Time spent studying
    (4, 5), # Avg grade
    ])


ks15 = []
 
for i in range(3):
    k15 = np.mean(age15[i, :])
    ks15.append(k15) 
 
avg15 = np.array(ks15)

print(avg15) 

ks16 = []
for i in range(3):
    k16 = np.mean(age16[i, :])
    ks16.append(k16)

avg16 = np.array(ks16)

print(avg16)

ks17 = []
for i in range(3):
    k17 = np.mean(age17[i, :]) 
    ks17.append(k17)

avg17 = np.array(ks17)

print(avg17)

ks18 = []
for i in range(3):
    k18 = np.mean(age18[i, :])
    ks18.append(k18)

avg18 = np.array(ks18)
print(avg18)

allavg = (avg15 + avg16 + avg17 + avg18) / 4
print(allavg)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# This is here to display each data point

ax.scatter(*age15, c='b', marker='o')
ax.scatter(*age16, c='g', marker='o')
ax.scatter(*age17, c='r', marker='o')
ax.scatter(*age18, c='y', marker='o')

ax.scatter(*unknownage, c='m', marker='s')

# Vector
v15 = allavg - avg15
print(f"VEC 15{v15}")
v16 = allavg - avg16
print(v16)
v17 = allavg - avg17
print(v17)
v18 = allavg - avg18
print(v18)


vun15 = unknownage[:, 0] - avg15
vun16 = unknownage[:, 0] - avg16
vun17 = unknownage[:, 0] - avg17
vun18 = unknownage[:, 0] - avg18
# Magnitudes
mag15 = np.linalg.norm(vun15)
mag16 = np.linalg.norm(vun16)
mag17 = np.linalg.norm(vun17)
mag18 = np.linalg.norm(vun18)
print(f"Vector magnitudes for collum #1: {mag15, mag16, mag17, mag18}")

min_mag_idx = np.argmin([mag15, mag16, mag17, mag18])

# Determine which age group the unknown data most likely belongs to based on the index of the smallest magnitude
if min_mag_idx == 0:
    print("The unknown data most likely belongs to age group 15")
elif min_mag_idx == 1:
    print("The unknown data most likely belongs to age group 16")
elif min_mag_idx == 2:
    print("The unknown data most likely belongs to age group 17")
else:
    print("The unknown data most likely belongs to age group 18")



vug15 = unknownage[:, 1] - avg15
vug16 = unknownage[:, 1] - avg16
vug17 = unknownage[:, 1] - avg17
vug18 = unknownage[:, 1] - avg18
# Magnitudes for other thingy

mug15 = np.linalg.norm(vug15)
mug16 = np.linalg.norm(vug16)
mug17 = np.linalg.norm(vug17)
mug18 = np.linalg.norm(vug18)
print(f"The magnitudes for collum #2: {mug15, mug16, mug17, mug18}]")





# Make vector to the unknow points
avg_color = 'c'

# Plot the vector
#ax.quiver(*avg15, *v15, length=1, color=avg_color)
#ax.quiver(*avg16, *v16, length=1, color=avg_color)
#ax.quiver(*avg17, *v17, length=1, color=avg_color)
#ax.quiver(*avg18, *v18, length=1, color=avg_color)

# Plot vectors from the averages to the unknown data
ax.quiver(*avg15, *vun15, length=1, color=avg_color, arrow_length_ratio=0.1)
ax.quiver(*avg16, *vun16, length=1, color=avg_color, arrow_length_ratio=0.1)  
ax.quiver(*avg17, *vun17, length=1, color=avg_color, arrow_length_ratio=0.1) 
ax.quiver(*avg18, *vun18, length=1, color=avg_color, arrow_length_ratio=0.1)  


# This is here to show the averages of each age group

ax.scatter(avg15[0], avg15[1], avg15[2], c='b', marker='x')
ax.scatter(avg16[0], avg16[1], avg16[2], c='g', marker='x')
