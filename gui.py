import tkinter as tk
from tkinter import messagebox

from transformations import translation_matrix


# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title("Solid Modelling Transformation Simulator")

window.geometry("500x500")


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    window,
    text="Solid Modelling Transformation Simulator",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)


# ==========================================
# TRANSFORMATION TYPE
# ==========================================

transformation_label = tk.Label(
    window,
    text="Transformation: Translation",
    font=("Arial", 13)
)

transformation_label.pack(pady=10)


# ==========================================
# X INPUT
# ==========================================

x_label = tk.Label(
    window,
    text="X Translation:"
)

x_label.pack()

x_entry = tk.Entry(window)

x_entry.pack(pady=5)


# ==========================================
# Y INPUT
# ==========================================

y_label = tk.Label(
    window,
    text="Y Translation:"
)

y_label.pack()

y_entry = tk.Entry(window)

y_entry.pack(pady=5)


# ==========================================
# Z INPUT
# ==========================================

z_label = tk.Label(
    window,
    text="Z Translation:"
)

z_label.pack()

z_entry = tk.Entry(window)

z_entry.pack(pady=5)


# ==========================================
# APPLY FUNCTION
# ==========================================

def apply_translation():

    try:

        tx = float(x_entry.get())
        ty = float(y_entry.get())
        tz = float(z_entry.get())

        matrix = translation_matrix(
            tx,
            ty,
            tz
        )

        print("Translation Matrix:")
        print(matrix)

        messagebox.showinfo(
            "Transformation Applied",
            f"Translation applied:\n\n"
            f"X = {tx}\n"
            f"Y = {ty}\n"
            f"Z = {tz}"
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers."
        )


# ==========================================
# APPLY BUTTON
# ==========================================

apply_button = tk.Button(
    window,
    text="APPLY TRANSFORMATION",
    command=apply_translation,
    width=25,
    height=2
)

apply_button.pack(pady=20)


# ==========================================
# RESET FUNCTION
# ==========================================

def reset():

    x_entry.delete(0, tk.END)
    y_entry.delete(0, tk.END)
    z_entry.delete(0, tk.END)


# ==========================================
# RESET BUTTON
# ==========================================

reset_button = tk.Button(
    window,
    text="RESET",
    command=reset,
    width=15
)

reset_button.pack()


# ==========================================
# START APPLICATION
# ==========================================

window.mainloop()