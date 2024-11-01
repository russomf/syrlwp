# plateconv2.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import sys
from pathlib import Path

# Convert row-column pair to an A01-style well label
def rowCol2Label(row, col):
    # Validate parameter values
    if row < 1: raise ValueError('row value must be > 1')
    if col < 1: raise ValueError('col value must be > 1')
    
    row = chr(row+64)           # Convert row to letter
    col = str(col).zfill(2)     # Convert col to string and left-pad with 0's
    return f'{row}{col}'        # Format as well label and return string

# Convert an A01-style well label to a row-column pair of integers
def label2RowCol(lbl):
    lbl = lbl.strip().upper()   # Remove spaces and uppercase

    # Validate parameter values
    if len(lbl) < 2: raise ValueError('label must be at least 2 characters')

    row = ord(lbl[0])-64        # Get char code for first char and subtract 64
    col = int(lbl[1:])          # Convert remaining chars to an int
    return row, col             # Return pair as tuple

# Test utilities
if __name__ == '__main__':
    # Test plate well translation functions
    try:
        row = input("Enter a well row: ") 
        col = input("Enter a well column: ") 
        row, col = int(row), int(col)
        lbl = rowCol2Label(row, col)
        print(f'Well at ({row},{col}) has label {lbl}\n')

        lbl = input("Enter well label: ")
        row, col = label2RowCol(lbl)
        print(f'Well with label {lbl} is at ({row},{col})')
    except Exception as e:
        print(e)
        info = sys.exc_info()[-1]
        lineno = info.tb_lineno
        fpath  = info.tb_frame.f_code.co_filename
        fname  = Path(fpath).name
        print(f'(see line {lineno} in {fname})')
