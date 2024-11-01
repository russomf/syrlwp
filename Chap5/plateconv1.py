# plateconv1.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

# Convert row-column pair to an A01-style well label
def rowCol2Label(row, col):
    row = chr(row+64)           # Convert row to letter
    col = str(col).zfill(2)     # Convert col to string and left-pad with 0's
    return f'{row}{col}'        # Format as well label and return string

# Convert an A01-style well label to a row-column pair of integers
def label2RowCol(lbl):
    lbl = lbl.strip().upper()   # Remove spaces and uppercase
    row = ord(lbl[0])-64        # Get char code for first char and subtract 64
    col = int(lbl[1:])          # Convert remaining chars to an int
    return row, col             # Return pair as tuple

# Test plate well translation functions
# row = input("Enter a well row: ") 
# col = input("Enter a well column: ") 
# row, col = int(row), int(col)
# lbl = rowCol2Label(row, col)
# print(f'Well at ({row},{col}) has label {lbl}')

# lbl = input("Enter well label: ")
# row, col = label2RowCol(lbl)
# print(f'Well with label {lbl} is at ({row},{col})')

# Test utilities
# if __name__ == '__main__':
    # assert well2RowCol('A01')   == (1, 1)
    # assert well2RowCol('b3')    == (2, 3)
    # assert well2RowCol('P20')   == (16, 20)
    # assert well2RowCol('  k4 ') == (11, 4)
    # print(well2RowCol('A01'))
    # print(well2RowCol('b3'))
    # print(well2RowCol('P20'))
    # print(well2RowCol('  k4 '))
