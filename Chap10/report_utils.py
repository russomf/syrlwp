# report_utils.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Compute the 4-parameters logistic function at Xs given the parameters
def fourPL(Xs, A, B, C, D):
    return [ D+(A-D)/(1 + math.pow((X/C),B) ) for X in Xs ]

# Fit all plate data to 4PLs
def fit_4PLs(df, Xs, guess, bounds):
    # For each row, copy data into a List, fit and accumulate fitted params
    param_sets = []
    for col in df.columns:
        # Fit the data to the 4PL
        params, _ = curve_fit(fourPL, Xs, df[col], p0=guess, bounds=bounds)
        param_sets.append( params )

    return param_sets

# Plot data in columns 1-10 in each row
def plot_fits(df, Xs, param_sets=None):

    # Dimensions of subplot layout
    nrows = 2
    ncols = 4

    # Create a panel of plots for measured data scatter plots and fit
    fig, axs = plt.subplots(nrows, ncols, figsize=(6, 6))

    # Generate a list of log(conc) to be used for plotting all 4PL fits
    plot_concs = np.linspace(Xs[0], Xs[-1], 100)

    # For all rows of wells, create scatter plot
    for r in range(nrows):                          # For all rows
        for c in range(ncols):                      # For all columns
            col = r*ncols+c                         # DataFrame column
            ax  = axs[r][c]                         # Ref to axis
            Ys  = df[col]                           # Measured data
            params = param_sets[col]                # Parameter set
            ax.set_title(f'Sample {col+1}')         # Add title
            ax.scatter(Xs, Ys, marker='+')          # Scatter and line plots
            ax.plot(plot_concs, fourPL(plot_concs, *params))

    fig.tight_layout()                              # Update and return figure
    return fig

# Plot one set of data
def plot_fit(Ys, Xs, title, params):
    # Create a figure for measured data scatter plots and fit
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    
    # Generate a list of log(conc) to be used for plotting all 4PL fits
    plot_concs = np.linspace(Xs[0], Xs[-1], 100)
    
    ax.set_title(title)                     # Add title
    ax.scatter(Xs, Ys, marker='+')          # Scatter and line plots
    ax.plot(plot_concs, fourPL(plot_concs, *params))
    
    fig.tight_layout()                      # Update and return figure
    return fig

# Compute a list of lists of average values and plot plate as a heatmap
def plot_heatmap(df, title):
    # Create a 1 x 1 panel for heatmap
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Create a heatmap. Plot transposed DataFrame.
    heatmap = ax.pcolormesh(df.T)

    # Turn off axes, set title to barcode, add colorbar
    ax.axis('off')
    ax.set_title(title)
    fig.colorbar(heatmap)

    # Label wells with value
    for r in range( 8 ):
        for c in range( 10 ):
            ax.text(c+0.5, r+0.5, f'{df.iloc[c][r]:.2f}', horizontalalignment='center', verticalalignment='center')

    # Label rows
    for r in range(8):
        lbl = chr(r+65)
        ax.text(-0.25, 7-r+0.5, lbl, horizontalalignment='center', verticalalignment='center')

    # Label columns
    for c in range(10):
        lbl = str(c+1)
        ax.text(c+0.5, -0.25, lbl, horizontalalignment='center', verticalalignment='center')

    # Return final figure
    return fig
