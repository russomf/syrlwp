# ttest.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Perform Two-sample T-tests

# 1. Import modules
import pandas as pd
import scipy.stats as stats

# 2. Read experimental data into DataFrame
df      = pd.read_csv('data_ttest.csv')

# 3. Compute normalized percent inhibition for three columns
mpos    = df['pos'].mean()
mneg    = df['neg'].mean()
pi_neg  = 100.0 * (1.0 - (mpos - df['neg'])/(mpos - mneg))
pi_smp1 = 100.0 * (1.0 - (mpos - df['samp1'])/(mpos - mneg))
pi_smp2 = 100.0 * (1.0 - (mpos - df['samp2'])/(mpos - mneg))

# 4. Check the variance of samp1 and negative control groups and print ratio.
# If ratio is in [0.25, 4] assume equal variances.
ratio1  = pi_smp1.var()/pi_neg.var()
print(f'ratio1: {ratio1}')
eq_var1 = False
if 0.25 < ratio1 < 4: eq_var1 = True

# 5. Two-sample T-test using SciPy stats submodule.
# Compare samp1 with negative control. 
# Null hypothesis: two population means are equal.
rslt1   = stats.ttest_ind(a=pi_smp1, b=pi_neg, equal_var=eq_var1)
print(f'pvalue for samp1: {rslt1.pvalue}')

# 6. Repeat analysis with sample 2.
# If ratio is in [0.25, 4] assume equal variances.
ratio2  = pi_smp2.var()/pi_neg.var()
print(f'ratio2: {ratio2}')
eq_var2 = False
if 0.25 < ratio2 < 4: eq_var2 = True

# Two-sample T-test using SciPy stats submodule.
# Null hypothesis: two population means are equal.
rslt2 = stats.ttest_ind(a=pi_smp2, b=pi_neg, equal_var=eq_var2)
print(f'pvalue for samp2: {rslt2.pvalue}')
