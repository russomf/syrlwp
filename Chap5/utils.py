# utils.py
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
