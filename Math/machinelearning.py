import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# Paramaters for blood imagiong (Red blood cell count (RBC), White blood cell count (WBC) and Platelet count (PLT))
healthyhumans = np.array([
#    h1     h2   h3
    (3.5, 3.2, 3.6, 3.1,3.2,3.2,3.4,3.5,3.5,3.6,3.7,3.8,3.9), # x
    (5.5, 5.23, 5.0 ), # y
    (8.3, 8.1, 8.3 ), # z
  ])

# Sick bastards
sickbastards = np.array([
    (1.1, 1.8, 1.7),
    (3.4, 3.6, 3.1),
    (7.0, 7.1, 7.6),
    ])

# Unknown idiots
unknownidiots = np.array([
    (3.4, 2.9, 1.1),
    (5.3, 3.0, 4.98),
    (8.6, 9.0, 7.4),
        ])

# Define the 3D point coordinates (x, y, z)
ks = []
for i in range(3):
    k = np.mean(healthyhumans[i, :])
    ks.append(k)

healthyavg = np.array(ks)


ks = []
for i in range(3):
    k = np.mean(sickbastards[i, :])
    ks.append(k)

bastardavg = np.array(ks)




# Create a figure and set it to 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Helathy average vetors, we will use this to calucllate the shortest distance, determening if they are closer to the follwing vectors,
# which calucalte the distance to sick poeple to detemine the probability if the unknownidiot is Healthy or Sick
vh0 = unknownidiots[:, 0] - healthyavg
vh1 = unknownidiots[:, 1] - healthyavg
vh2 = unknownidiots[:, 2] - healthyavg

# Here are the aformentioned vectors for sick people
vs0 = unknownidiots[:, 0] - bastardavg
vs1 = unknownidiots[:, 1] - bastardavg
vs2 = unknownidiots[:, 2] - bastardavg



# print(healthyavg, unknownidiots[0], V1 )
ax.quiver(*healthyavg, *vh0)

ax.quiver(*healthyavg, *vh1)

ax.quiver(*healthyavg, *vh2)


# showing the sick vectors so we can see them obv

ax.quiver(*bastardavg, *vs0)

ax.quiver(*bastardavg, *vs1)

ax.quiver(*bastardavg, *vs2)


# Now we use linear algebra in numpy to calucalte the maginute, the smalles (or the shortest distance) from a point will be classed as that point so we can determine,
# the probability of each unknownidiot beaing eaither healthyhuman or sickbastard

magvs0 = np.linalg.norm(vs0)
magvs1 = np.linalg.norm(vs0)
magvs2 = np.linalg.norm(vs0)
print(magvs0, magvs1, magvs2)


magvh0 = np.linalg.norm(vh0)
magvh1 = np.linalg.norm(vh0)
magvh2 = np.linalg.norm(vh0)
print(magvh0, magvh1, magvh2)


# Plot the point on the 3D axis
ax.scatter(*healthyhumans, c='g', marker='o')

ax.scatter(*sickbastards, c='r', marker='o')

ax.scatter(*unknownidiots, c='b', marker='o')

ax.scatter(*healthyavg, c='g', marker='x')

ax.scatter(*bastardavg, c='r', marker='x')


# Set axis labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Show the plot
plt.show()

while True:
    x = int(input("Enter x variable: "))
    y = int(input("Enter y variable: "))
    z = int(input("Enter z variable: "))

    vector = np.array([
    x, y, z
    ])

    magh = np.linalg.norm(vector - healthyavg)

    mags = np.linalg.norm(vector - bastardavg)

    if magh < mags:
        print("R.I.P (bastad)")

    else:
        print("Go home (human)")

