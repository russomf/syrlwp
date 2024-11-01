# experiment.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import sys
from bs4 import BeautifulSoup

# Makes a function that tests for measurement tags with a cutoff
def well_with_cutoff(cutoff):
    def fxn(tag):       # Inner function defined to test measurement cutoff
        return tag.name == 'well' and float(tag.measurement.string) > cutoff
    return fxn

# Given a well element, extract and return desired information.
def get_well_data(well):
    cmpds = [el['id'] for el in well('compound')]           # Implied find_all()
    test  = well.measurement['test']                        # Test name
    value = float(well.measurement.string)                  # Measured value
    return {'compounds':cmpds, 'test':test, 'value':value}  # Return dictionary

# Test
if __name__ == '__main__':
    fname = sys.argv[1]                                     # Expect file name
    with open(fname, 'r') as file:                          # Open file
        bs = BeautifulSoup(file, 'xml')                     # Parse as XML

    wells = bs(well_with_cutoff(50))                        # Get all well elements
    data  = [get_well_data(well) for well in wells]         # Get data from wells
    print(data)                                             # Print data
