import matplotlib.pyplot as plt
import numpy as np

# Define two vectors
v1 = np.array([2, 3])
v2 = np.array([4, -1])

# Compute the difference vector
diff = v2 - v1

# Create a plot
fig, ax = plt.subplots()

# Draw the vectors
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='v1')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v2')
ax.quiver(v1[0], v1[1], diff[0], diff[1], angles='xy', scale_units='xy', scale=1, color='green', label='diff')

# Set the plot limits
lim = np.max(np.abs([v1, v2, diff])) + 1
ax.set_xlim((-lim, lim))
ax.set_ylim((-lim, lim))

# Move the origin to (0, 0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Add the legend and grid
ax.legend()
ax.grid()

# Show the plot
plt.show()

