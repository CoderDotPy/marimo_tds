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
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return

@app.cell
def _():
    # Create a slider to select the number of points
    n_points = mo.ui.slider(10, 100, value=50, label="Number of points")
    n_points  # Display the slider
    return

@app.cell
def _():
    # Generate random data based on the slider value
    # This cell automatically re-executes when n_points.value changes
    x = np.random.rand(n_points.value)
    y = np.random.rand(n_points.value)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.7)
    plt.title(f"Scatter plot with {n_points.value} points")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.gca()  # Return the current axes to display the plot
    return

@app.cell
def _():
    # Dynamic markdown output based on the slider value
    mo.md(f"""
    # Dynamic Output
    
    The current number of points selected is **{n_points.value}**.
    """)
    return

if __name__ == "__main__":
    app.run()

