import matplotlib.pyplot as plt # Python brings the plotting tools from the matplotlib.plt is just a short name we give to matplotlib plotting module.

# Create a 3D plotting area
fig = plt.figure() #creates a figure or window.(Give me a blank drawing sheet) 
ax = fig.add_subplot(111, projection="3d") #creates 3d coordinate system.

# Coordinates of the 8 cube vertices
x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# Connections between vertices
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Draw each edge
for start, end in edges: # take each pair of points one by one.
    ax.plot( # draw a line between them.
        [x[start], x[end]],
        [y[start], y[end]],
        [z[start], z[end]]
    )

# Axis labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Title
ax.set_title("3D Solid Model")

# Display
plt.show()