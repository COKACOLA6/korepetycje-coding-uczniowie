import numpy as np
import matplotlib.pyplot as plt

# Dimensions of the 3D grid
nx, ny, nz = 10, 10, 10

# Create a 3D boolean array of which voxels to draw
voxels = np.random.rand(nx, ny, nz) > 0.7  # About 30% will be visible

# Generate heat values for coloring
colors = np.empty(voxels.shape, dtype=object)
for x in range(nx):
    for y in range(ny):
        for z in range(nz):
            if voxels[x, y, z]:
                val = (x + y + z) / (nx + ny + nz)  # Normalize
                colors[x, y, z] = plt.cm.viridis(val)

# Plot the voxels
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')
plt.title('Voxel-style 3D Heatmap')
plt.show()
