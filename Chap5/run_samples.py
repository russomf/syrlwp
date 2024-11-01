# run_samples.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

def run_samples(*samples, **params):
    print(f'Run samples {samples} with parameters {params}')

# Test run_samples
run_samples( 'sample1', 'sample2', 'sample3', temp=125, vol=20)
run_samples( 'cmpd1', 'cmpd2', solvent='DMSO', duration=100)
run_samples()
