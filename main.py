import matplotlib.pyplot as plt

# --------------------------------
# 1. ORIGINAL CUBE
# --------------------------------

x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# Connections between cube vertices
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


# --------------------------------
# 2. TRANSLATION
# --------------------------------

Tx = 2
Ty = 1
Tz = 1

x_new = [value + Tx for value in x]
y_new = [value + Ty for value in y]
z_new = [value + Tz for value in z]


# --------------------------------
# 3. CREATE 3D VIEW
# --------------------------------

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")


# --------------------------------
# 4. DRAW ORIGINAL CUBE
# --------------------------------

for start, end in edges:
    ax.plot(
        [x[start], x[end]],
        [y[start], y[end]],
        [z[start], z[end]],
        linewidth=2
    )


# --------------------------------
# 5. DRAW TRANSLATED CUBE
# --------------------------------

for start, end in edges:
    ax.plot(
        [x_new[start], x_new[end]],
        [y_new[start], y_new[end]],
        [z_new[start], z_new[end]],
        linewidth=2
    )


# --------------------------------
# 6. LABEL AXES
# --------------------------------

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

ax.set_title("3D Solid Modelling - Translation")


# --------------------------------
# 7. SHOW RESULT
# --------------------------------

plt.show()