# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import utils

# Test plate well translation functions
row = input("Enter a well row: ") 
col = input("Enter a well column: ") 
row, col = int(row), int(col)
lbl = utils.rowCol2Label(row, col)
print(f'Well at ({row},{col}) has label {lbl}')

lbl = input("Enter well label: ")
row, col = utils.label2RowCol(lbl)
print(f'Well with label {lbl} is at ({row},{col})')
