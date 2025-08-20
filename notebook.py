# /// script
# [tool.marimo.runtime]
# auto_instantiate = false
# ///

import marimo

__generated_with = "ai"
app = marimo.App(width="medium")

@app.cell
def _():
    # Email: 22f3000814@ds.study.iitm.ac.in
    # Cell 1: Imports
    # Provides: mo, np, plt
    # Used by: Cell 2 (mo), Cell 3 (np, plt), Cell 4 (mo)
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt

@app.cell
def _(mo):
    # Cell 2: Slider widget
    # Provides: n_points
    # Used by: Cell 3 (to generate random data), Cell 4 (to show dynamic markdown)
    n_points = mo.ui.slider(10, 100, value=50, label="Number of points")
    n_points  # Display the slider
    return n_points

@app.cell
def _(np, plt, n_points):
    # Cell 3: Data generation and plotting
    # Depends on: n_points (Cell 2), np (Cell 1), plt (Cell 1)
    # Provides: x, y
    # Used by: (could be reused in future cells for analysis)
    x = np.random.rand(n_points.value)
    y = np.random.rand(n_points.value)

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.7)
    plt.title(f"Scatter plot with {n_points.value} points")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.gca()  # Return the current axes to display the plot
    return x, y

@app.cell
def _(mo, n_points):
    # Cell 4: Dynamic Markdown output
    # Depends on: mo (Cell 1), n_points (Cell 2)
    # Provides: a markdown block describing current slider state
    mo.md(f"""
    # Dynamic Output
    
    The current number of points selected is **{n_points.value}**.
    """)
    return

if __name__ == "__main__":
    app.run()
