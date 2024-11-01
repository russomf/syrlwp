# fit_MM.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from scipy.optimize import curve_fit

# Michaelis-Menten kinetics
def MM(Xs, Km, Vmax):
    return [(Vmax*X)/(Km + X) for X in Xs]

# Experimental data from initial velocity experiments
S0 = [0.05, 0.10, 0.25, 0.50, 1.00,  2.50,  5.00,  8.00, 20.00, 30.00] # [mM]
v0 = [3.0,   6.0, 17.0, 31.0, 48.0, 101.0, 121.0, 139.0, 152.0, 181.0] # µM/min

# Initial guess and estimated bounds
guess  = [10, 100]              # Lit values KM = 2.5 mM and Vmax = 0.19 mM min−1
bounds = [[0,0],[20,1000]]      # Parameter bounds

# Fit and print results
params, _ = curve_fit(MM, S0, v0, p0=guess, bounds=bounds)
print(f'Km={params[0]:0.3f} mM, Vmax={params[1]*0.001:0.3f} mM/min' )
