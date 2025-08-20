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
    # Import dependencies shared across cells
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt

@app.cell
def _(mo):
    # Cell 2: Create a slider widget
    # Provides the variable `n_points` for later cells
    n_points = mo.ui.slider(10, 100, value=50, label="Number of points")
    n_points  # Display slider
    return n_points

@app.cell
def _(np, plt, n_points):
    # Cell 3: Generate data and plot
    # Depends on:
    #   - `n_points` (from Cell 2: user input)
    #   - `np` and `plt` (from Cell 1: imports)
    x = np.random.rand(n_points.value)
    y = np.random.rand(n_points.value)

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.7)
    plt.title(f"Scatter plot with {n_points.value} points")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.gca()  # Return current axes so plot displays
    return x, y

@app.cell
def _(mo, n_points):
    # Cell 4: Dynamic Markdown output
    # Depends on:
    #   - `n_points` (from Cell 2: user input)
    #   - `mo` (from Cell 1: import)
    mo.md(f"""
    # Dynamic Output
    
    The current number of points selected is **{n_points.value}**.
    """)
    return

if __name__ == "__main__":
    app.run()
