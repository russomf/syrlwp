# lh_ttest.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# T-test for comparing liquid handler syringe dispensed volume data

# 1. Import modules
import pandas as pd
import scipy.stats as stats

# 2. Set Parameters
ptarg   = .05       # Target p-value
syrg1   = 1         # First syringe to compare
syrg2   = 3         # Second syringe to compare
solvent = 'Water'   # Solvent to compare
evol    = 25.0      # Expected volume in µL

# 3. Read experimental data into DataFrame
# Filter data based on syringe number and solvent to compare
df      = pd.read_csv(r'lhdata_ttest.csv')
dfs1    = df[(df['Syringe'] == syrg1) & (df['Solvent'] == solvent)]
dfs2    = df[(df['Syringe'] == syrg2) & (df['Solvent'] == solvent)]

# 4. Compute general statistical measures
vol1    = dfs1['Measured']      # Columns of interest         
vol2    = dfs2['Measured']
var1    = vol1.var()            # Sample variance
var2    = vol2.var()
mean1   = vol1.mean()           # Means
mean2   = vol2.mean()
cv1     = vol1.std()/mean1*100  # Coefficients of variation
cv2     = vol2.std()/mean2*100
inacc1  = (mean1-evol)/evol*100 # Inaccuracy
inacc2  = (mean2-evol)/evol*100

# 5. Check equal variances
ratio   = var1/var2
eq_var  = False
if 0.25 < ratio < 4.0: eq_var = False

# 6. Perform t-test
rslt    = stats.ttest_ind(a=vol1, b=vol2, equal_var=eq_var)

# 7. Print results
print (f'Compare volume data for syringes {syrg1} and {syrg2} @{evol}µL for {solvent}')
print (f'syringe {syrg1}: mean={mean1:.2f}, CV={cv1:.2f}, inacc={inacc1:.2f}')
print (f'syringe {syrg2}: mean={mean2:.2f}, CV={cv2:.2f}, inacc={inacc2:.2f}')
print (f'p-value  : {rslt.pvalue}')
print (f't-stat   : {rslt.statistic}')

if rslt.pvalue >= ptarg:
    print (f'Syringe vols are NOT significantly different at p-value of {ptarg}')
else:
    print (f'Syringe vols are significantly different at p-value of {ptarg}')
