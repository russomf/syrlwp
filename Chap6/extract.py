# extract.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import re
p_data = re.compile(r'([A-H]\d{1,2}):\s*(-?\d+\.\d+(?:E-?\d+)?|FAIL)')

def extract_data(plate_file):
    matches = []                            # Assume no matches
    with open(plate_file, 'r') as fp:       # Open data file
        content = fp.read()                 # Read all content into on string
        matches = p_data.findall(content)   # Find all matches and overwrite
    return matches                          # Return all matches

if __name__ == '__main__':
    print( extract_data('plate.txt') )
