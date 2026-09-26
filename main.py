import matplotlib.pyplot as plt

# ==========================================
# 1. ORIGINAL CUBE
# ==========================================

x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# Connections between cube vertices
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


# ==========================================
# 2. TRANSLATION
# ==========================================

Tx = 2
Ty = 1
Tz = 1

x_translated = [value + Tx for value in x]
y_translated = [value + Ty for value in y]
z_translated = [value + Tz for value in z]


# ==========================================
# 3. SCALING
# ==========================================

Sx = 2
Sy = 2
Sz = 2

x_scaled = [value * Sx for value in x]
y_scaled = [value * Sy for value in y]
z_scaled = [value * Sz for value in z]


# ==========================================
# 4. CREATE 3D VIEW
# ==========================================

fig = plt.figure(figsize=(10, 7))

ax = fig.add_subplot(111, projection="3d")


# ==========================================
# 5. DRAW ORIGINAL CUBE
# ==========================================

for start, end in edges:

    ax.plot(
        [x[start], x[end]],
        [y[start], y[end]],
        [z[start], z[end]],
        linewidth=2
    )


# ==========================================
# 6. DRAW TRANSLATED CUBE
# ==========================================

for start, end in edges:

    ax.plot(
        [x_translated[start], x_translated[end]],
        [y_translated[start], y_translated[end]],
        [z_translated[start], z_translated[end]],
        linewidth=2
    )


# ==========================================
# 7. DRAW SCALED CUBE
# ==========================================

for start, end in edges:

    ax.plot(
        [x_scaled[start], x_scaled[end]],
        [y_scaled[start], y_scaled[end]],
        [z_scaled[start], z_scaled[end]],
        linewidth=2
    )


# ==========================================
# 8. AXIS LABELS
# ==========================================

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")


# ==========================================
# 9. TITLE
# ==========================================

ax.set_title("Solid Modelling Transformation Simulator")


# ==========================================
# 10. DISPLAY
# ==========================================

plt.show()